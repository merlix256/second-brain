#!/usr/bin/env python3
"""
Groep T Study OS — All-in-One Obsidian Companion Web App & Analytics Server.

Reads and writes directly to your Obsidian vault (`Hunugs-vision`):
- Parses all #study-unit markdown notes under `Groep T/`
- Reads/writes study hours in `Daily_Journal/*.md` and `Groep T/Study_Logs/*.md`
- Syncs checkboxes to `Groep T/02_Master_Course_Checklists.md`
- Persists rich session telemetry in `Groep T/study_telemetry.json`
- Exports clean CSV snapshots (`Groep T/study_logs_export.csv`, `Groep T/study_units_export.csv`)
- Generates an in-vault analytics report (`Groep T/07_Study_Analytics_Snapshot.md`)
"""

from __future__ import annotations

import argparse
import csv
import datetime
import functools
import http.server
import io
import json
import mimetypes
import os
import re
import socketserver
import sys
import urllib.parse
import webbrowser
from pathlib import Path
from typing import Any

import daily_journal as dj

VAULT_ROOT = Path(__file__).resolve().parent
GROEP_T_DIR = VAULT_ROOT / "Groep T"
DAILY_JOURNAL_DIR = VAULT_ROOT / "Daily_Journal"
STUDY_LOGS_DIR = GROEP_T_DIR / "Study_Logs"
CHECKLIST_FILE = GROEP_T_DIR / "02_Master_Course_Checklists.md"
TELEMETRY_JSON = GROEP_T_DIR / "study_telemetry.json"
LOGS_CSV = GROEP_T_DIR / "study_logs_export.csv"
UNITS_CSV = GROEP_T_DIR / "study_units_export.csv"
SNAPSHOT_MD = GROEP_T_DIR / "07_Study_Analytics_Snapshot.md"
STATIC_DIR = VAULT_ROOT / "groep_t_app"

COURSES: list[dict[str, Any]] = [
    {
        "id": "cad",
        "name": "Ruimtelijk inzicht en CAD (T1AIB1)",
        "short": "Ruimtelijk Inzicht & CAD",
        "hrs_key": "hrs_cad",
        "ects": 3,
        "exam_date": "2026-12-12",
        "exam_label": "07–17 dec 2026 (Perm. Eval.)",
        "location": "Sessie 6 (Geen jan-examen)",
        "color": "#f43f5e",
        "index_file": "Groep T/Spatial_Insight_and_CAD_Vault/00 - MOC & Dashboards/Index.md",
    },
    {
        "id": "dynamica",
        "name": "Dynamica en energie (T1ADE1)",
        "short": "Dynamica & Energie",
        "hrs_key": "hrs_dynamica",
        "ects": 3,
        "exam_date": "2027-01-11",
        "exam_label": "ma 11.01.2027 08:30",
        "location": "DV1 - 02.54",
        "color": "#f97316",
        "index_file": "Groep T/Dynamica_en_Energie_/00_Meta/Index.md",
    },
    {
        "id": "comp_denken",
        "name": "Computationeel Denken (T1ACD1)",
        "short": "Computationeel Denken",
        "hrs_key": "hrs_comp_denken",
        "ects": 3,
        "exam_date": "2027-01-12",
        "exam_label": "di 12.01.2027 08:30",
        "location": "VHI - 02.25 (PC-klas)",
        "color": "#eab308",
        "index_file": "Groep T/Computationeel_Denken/Index.md",
    },
    {
        "id": "wiskunde",
        "name": "Wiskundige basistechnieken (T1AWB1)",
        "short": "Wiskunde",
        "hrs_key": "hrs_wiskunde",
        "ects": 6,
        "exam_date": "2027-01-16",
        "exam_label": "za 16.01.2027 08:30",
        "location": "GT - 03.13.01",
        "color": "#3b82f6",
        "index_file": "Groep T/Obsidian_Vault_Wiskundige_Basistechnieken/00 - MOC/Index.md",
    },
    {
        "id": "chemie",
        "name": "Chemie (T1ACH1)",
        "short": "Chemie",
        "hrs_key": "hrs_chemie",
        "ects": 6,
        "exam_date": "2027-01-19",
        "exam_label": "di 19.01.2027 12:30",
        "location": "DV1 - 02.54",
        "color": "#10b981",
        "index_file": "Groep T/Chemie/00 - Meta/Index.md",
    },
    {
        "id": "ethiek",
        "name": "Onderneming en ethiek (T1AOE1)",
        "short": "Onderneming & Ethiek",
        "hrs_key": "hrs_ethiek",
        "ects": 3,
        "exam_date": "2027-01-21",
        "exam_label": "do 21.01.2027 12:30",
        "location": "AV - 01.12",
        "color": "#a855f7",
        "index_file": "Groep T/Ethiek-/00_Overview/00_Course_Index.md",
    },
    {
        "id": "sgdm",
        "name": "SGDM (T1ASD1)",
        "short": "SGDM Materialen",
        "hrs_key": "hrs_sgdm",
        "ects": 6,
        "exam_date": "2027-01-29",
        "exam_label": "vr 29.01.2027 08:30",
        "location": "GRAU - 00.10",
        "color": "#06b6d4",
        "index_file": "Groep T/SGDM/00_Overview_Dashboard.md",
    },
]

COURSE_BY_NAME = {c["name"]: c for c in COURSES}
COURSE_BY_HRS_KEY = {c["hrs_key"]: c for c in COURSES}
HRS_KEYS = [c["hrs_key"] for c in COURSES]


def split_frontmatter(text: str) -> tuple[list[str] | None, str]:
    """Split a markdown file into YAML frontmatter lines and body."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    lines = text.splitlines(keepends=True)
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            fm_lines = [l.rstrip("\r\n") for l in lines[1:idx]]
            body = "".join(lines[idx + 1 :])
            return fm_lines, body
    return None, text


def parse_simple_yaml(fm_lines: list[str] | None) -> dict[str, Any]:
    """Parse flat YAML frontmatter + simple string lists without external deps."""
    if not fm_lines:
        return {}
    data: dict[str, Any] = {}
    current_list_key: str | None = None
    for line in fm_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_list_key:
            item = stripped[2:].strip().strip('"').strip("'")
            if not isinstance(data.get(current_list_key), list):
                data[current_list_key] = []
            data[current_list_key].append(item)
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, raw_val = line.split(":", 1)
        key = key.strip()
        val = raw_val.strip()
        if not val:
            data[key] = ""
            current_list_key = key
            continue
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()] if inner else []
            continue
        low = val.lower()
        if low == "true":
            data[key] = True
        elif low == "false":
            data[key] = False
        elif low in ("null", "~"):
            data[key] = None
        else:
            unquoted = val.strip('"').strip("'")
            if re.fullmatch(r"-?\d+", unquoted):
                data[key] = int(unquoted)
            elif re.fullmatch(r"-?\d+\.\d+", unquoted):
                data[key] = float(unquoted)
            else:
                data[key] = unquoted
    return data


def format_yaml_scalar(val: Any) -> str:
    """Format a Python scalar cleanly for YAML frontmatter."""
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, int):
        return str(val)
    if isinstance(val, float):
        return str(int(val)) if val.is_integer() else str(round(val, 2))
    if val is None:
        return ""
    s = str(val)
    if s == "" or any(ch in s for ch in [":", "#", "[", "]", "{", "}"]):
        return f'"{s}"'
    return s


def update_frontmatter_keys(text: str, updates: dict[str, Any]) -> str:
    """Surgically update or insert scalar keys in YAML frontmatter while keeping layout intact."""
    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        new_fm = ["---"] + [f"{k}: {format_yaml_scalar(v)}" for k, v in updates.items()] + ["---", ""]
        return "\n".join(new_fm) + text

    seen = set()
    out_lines: list[str] = []
    for line in fm_lines:
        if ":" in line and not line.lstrip().startswith("-") and not line.lstrip().startswith("#"):
            key = line.split(":", 1)[0].strip()
            if key in updates:
                out_lines.append(f"{key}: {format_yaml_scalar(updates[key])}")
                seen.add(key)
                continue
        out_lines.append(line)

    for key, val in updates.items():
        if key not in seen:
            out_lines.append(f"{key}: {format_yaml_scalar(val)}")

    sep = "" if body.startswith("\n") or body.startswith("\r\n") else "\n"
    return "---\n" + "\n".join(out_lines) + "\n---" + sep + body


def to_float(val: Any, default: float = 0.0) -> float:
    if isinstance(val, bool) or val is None or val == "":
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def resolve_safe_vault_path(rel_path: str) -> Path:
    """Resolve a vault-relative path safely, preventing directory traversal."""
    candidate = (VAULT_ROOT / rel_path).resolve()
    if VAULT_ROOT not in candidate.parents and candidate != VAULT_ROOT:
        raise ValueError("Path escapes vault root")
    return candidate


def scan_study_units() -> list[dict[str, Any]]:
    """Load all #study-unit markdown notes in Groep T/."""
    units: list[dict[str, Any]] = []
    for path in sorted(GROEP_T_DIR.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        fm_lines, _ = split_frontmatter(text)
        meta = parse_simple_yaml(fm_lines)
        tags = meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        if "study-unit" not in tags:
            continue

        rel = path.relative_to(VAULT_ROOT).as_posix()
        completed = bool(meta.get("completed") is True or meta.get("status") == "done")
        status = "done" if completed else str(meta.get("status") or "todo")
        est_hours = to_float(meta.get("est_hours"), 1.5)
        course_name = str(meta.get("course") or "Unknown")
        course_info = COURSE_BY_NAME.get(course_name, {})

        units.append(
            {
                "path": rel,
                "name": path.stem,
                "course": course_name,
                "course_id": course_info.get("id", "other"),
                "course_short": course_info.get("short", course_name),
                "unit_type": str(meta.get("unit_type") or "theory"),
                "status": status,
                "completed": completed,
                "est_hours": round(est_hours, 2),
                "priority": str(meta.get("priority") or "medium"),
            }
        )
    return units


def parse_log_file(path: Path, source_type: str) -> dict[str, Any] | None:
    """Parse a Daily_Journal or Study_Logs note if it has study-log tag or study_hours_total."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    fm_lines, _ = split_frontmatter(text)
    meta = parse_simple_yaml(fm_lines)
    tags = meta.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    if "study-log" not in tags and "study_hours_total" not in meta:
        return None

    date_str = str(meta.get("date") or path.stem)
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        m = re.search(r"\d{4}-\d{2}-\d{2}", path.stem)
        if not m:
            return None
        date_str = m.group(0)

    hrs_by_course = {k: round(to_float(meta.get(k), 0.0), 2) for k in HRS_KEYS}
    subject_sum = round(sum(hrs_by_course.values()), 2)
    raw_total = round(to_float(meta.get("study_hours_total"), 0.0), 2)
    total_hours = raw_total if raw_total > 0 else subject_sum

    focus_val = to_float(meta.get("study_focus_score"), 0.0)
    focus_score = focus_val if focus_val > 0 else None
    pomodoros = int(to_float(meta.get("pomodoros_done"), 0.0))

    return {
        "date": date_str,
        "source": source_type,
        "path": path.relative_to(VAULT_ROOT).as_posix(),
        "total_hours": total_hours,
        "subject_sum": subject_sum,
        "hrs": hrs_by_course,
        "focus_score": focus_score,
        "pomodoros_done": pomodoros,
        "mood": meta.get("mood") or "",
        "sleep_hours": to_float(meta.get("sleep_hours"), 0.0) if meta.get("sleep_hours") not in (None, "") else None,
        "workout_done": bool(meta.get("workout_done") is True),
    }


def scan_study_logs() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Scan Daily_Journal and Study_Logs, returning raw entries and merged daily summaries."""
    raw_entries: list[dict[str, Any]] = []
    if DAILY_JOURNAL_DIR.exists():
        for p in sorted(DAILY_JOURNAL_DIR.glob("*.md")):
            parsed = parse_log_file(p, "Daily_Journal")
            if parsed:
                raw_entries.append(parsed)
    if STUDY_LOGS_DIR.exists():
        for p in sorted(STUDY_LOGS_DIR.glob("*.md")):
            if "template" in p.name.lower():
                continue
            parsed = parse_log_file(p, "Study_Logs")
            if parsed:
                raw_entries.append(parsed)

    # Merge per date without double-counting when one file is 0h or both have entries:
    # Preference rule: if Daily_Journal has > 0h, or Study_Logs has > 0h, take max per subject/total
    # unless user logged different subjects in each (sum only when sources don't overlap, or prefer non-zero).
    by_date: dict[str, dict[str, Any]] = {}
    for entry in raw_entries:
        d = entry["date"]
        if d not in by_date:
            by_date[d] = {
                "date": d,
                "total_hours": entry["total_hours"],
                "hrs": dict(entry["hrs"]),
                "focus_score": entry["focus_score"],
                "pomodoros_done": entry["pomodoros_done"],
                "sources": [entry["path"]],
                "entries": [entry],
            }
        else:
            existing = by_date[d]
            existing["sources"].append(entry["path"])
            existing["entries"].append(entry)
            # If existing had 0h and new has >0h (or vice versa), pick non-zero;
            # if both have >0h, keep highest per course to match the anti-double-counting guide.
            for k in HRS_KEYS:
                existing["hrs"][k] = round(max(existing["hrs"][k], entry["hrs"][k]), 2)
            existing["total_hours"] = round(max(existing["total_hours"], entry["total_hours"], sum(existing["hrs"].values())), 2)
            if entry["focus_score"] is not None:
                existing["focus_score"] = entry["focus_score"]
            existing["pomodoros_done"] = max(existing["pomodoros_done"], entry["pomodoros_done"])

    merged = sorted(by_date.values(), key=lambda x: x["date"])
    return raw_entries, merged


def load_telemetry() -> dict[str, Any]:
    """Load persistent JSON telemetry store."""
    if TELEMETRY_JSON.exists():
        try:
            data = json.loads(TELEMETRY_JSON.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("sessions", [])
                return data
        except json.JSONDecodeError:
            pass
    return {"version": 1, "updated_at": None, "sessions": []}


def save_telemetry(telemetry: dict[str, Any]) -> None:
    telemetry["updated_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    TELEMETRY_JSON.write_text(json.dumps(telemetry, indent=2, ensure_ascii=False), encoding="utf-8")


def export_csv_files(units: list[dict[str, Any]], merged_logs: list[dict[str, Any]]) -> None:
    """Write clean CSV exports of both study logs and study units into Groep T/."""
    with LOGS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "total_hours", *HRS_KEYS, "focus_score", "pomodoros_done", "sources"])
        for row in merged_logs:
            writer.writerow(
                [
                    row["date"],
                    row["total_hours"],
                    *[row["hrs"][k] for k in HRS_KEYS],
                    row["focus_score"] if row["focus_score"] is not None else "",
                    row["pomodoros_done"],
                    "; ".join(row["sources"]),
                ]
            )

    with UNITS_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["course", "unit_type", "name", "status", "completed", "est_hours", "priority", "path"])
        for u in units:
            writer.writerow(
                [u["course"], u["unit_type"], u["name"], u["status"], u["completed"], u["est_hours"], u["priority"], u["path"]]
            )


def sync_checklist_checkbox(note_stem: str, completed: bool) -> bool:
    """Toggle matching `- [ ] [[Note Stem]]` checkbox inside 02_Master_Course_Checklists.md."""
    if not CHECKLIST_FILE.exists():
        return False
    text = CHECKLIST_FILE.read_text(encoding="utf-8")
    escaped = re.escape(note_stem)
    pattern = re.compile(rf"^(- \[)[ x](\] \[\[(?:[^\]|]*/)?{escaped}(?:\|[^\]]*)?\]\])", re.M)
    mark = "x" if completed else " "
    new_text, count = pattern.subn(rf"\g<1>{mark}\g<2>", text)
    if count > 0 and new_text != text:
        CHECKLIST_FILE.write_text(new_text, encoding="utf-8")
        return True
    return False


def ensure_log_file(target_date: str, target_target: str) -> Path:
    """Ensure Daily_Journal/YYYY-MM-DD.md or Groep T/Study_Logs/YYYY-MM-DD.md exists."""
    d_obj = datetime.date.fromisoformat(target_date)
    if target_target == "study_log":
        STUDY_LOGS_DIR.mkdir(parents=True, exist_ok=True)
        out = STUDY_LOGS_DIR / f"{target_date}.md"
        if not out.exists():
            tpl = STUDY_LOGS_DIR / "Study_Log_Template.md"
            content = tpl.read_text(encoding="utf-8") if tpl.exists() else "---\ndate: \"{{date}}\"\ntype: study-log\ntags:\n  - study-log\nstudy_hours_total: 0\n---\n\n# ⏱️ Study Log — {{date}}\n"
            out.write_text(dj.render_template(content, d_obj), encoding="utf-8")
        return out

    out = DAILY_JOURNAL_DIR / f"{target_date}.md"
    if not out.exists():
        dj.create_daily_page(d_obj)
    return out


def append_session_to_markdown(
    file_path: Path,
    time_range: str,
    course_short: str,
    unit_name: str,
    duration_h: float,
    notes: str,
    new_total_hours: float | None = None,
) -> None:
    """Append a structured session bullet/row inside the Obsidian log note."""
    text = file_path.read_text(encoding="utf-8")
    safe_notes = (notes or "").replace("|", "/").replace("\n", " ").strip()
    unit_label = f"[[{unit_name}]]" if unit_name else "General study"

    if new_total_hours is not None:
        text = re.sub(
            r"(\*\*Actual Total:\*\*\s*`)[^`]*(`)",
            rf"\g<1>{new_total_hours:.2f}h\g<2>",
            text,
        )

    if "| Time Block" in text:
        row = f"| `{time_range}` | {course_short} | {unit_label} | `{duration_h:.2f}` | {safe_notes} |"
        # Replace an empty placeholder row if present, else append after table header separator
        empty_row_re = re.compile(r"^\|[ `]*\|[ ]*\|[ ]*\|[ ]*\|[ ]*\|$", re.M)
        if empty_row_re.search(text):
            text = empty_row_re.sub(row, text, count=1)
        else:
            sep_re = re.compile(r"(^\| :---.*\|$)", re.M)
            if sep_re.search(text):
                text = sep_re.sub(rf"\1\n{row}", text, count=1)
            else:
                text += f"\n{row}\n"
    elif "## 🎓 Groep T Daily Study Log" in text:
        bullet = f"- ✅ `{time_range}` **{course_short}** ({duration_h:.2f}h) — {unit_label}"
        if safe_notes:
            bullet += f" — *{safe_notes}*"
        marker = "- [ ] **Evening Active Recall"
        idx = text.find(marker)
        if idx != -1:
            line_end = text.find("\n", idx)
            if line_end != -1:
                text = text[: line_end + 1] + bullet + "\n" + text[line_end + 1 :]
            else:
                text += "\n" + bullet + "\n"
        else:
            text += "\n" + bullet + "\n"
    else:
        text += f"\n- `{time_range}` **{course_short}** ({duration_h:.2f}h): {unit_label} — {safe_notes}\n"

    file_path.write_text(text, encoding="utf-8")


def compute_streak(merged_logs: list[dict[str, Any]], today_str: str) -> dict[str, Any]:
    """Compute current and longest study streak (>0h/day)."""
    active_dates = {r["date"] for r in merged_logs if r["total_hours"] > 0}
    today = datetime.date.fromisoformat(today_str)

    # Current streak checks today, or yesterday if today hasn't been logged yet
    cur = 0
    cursor = today if today.isoformat() in active_dates else today - datetime.timedelta(days=1)
    while cursor.isoformat() in active_dates:
        cur += 1
        cursor -= datetime.timedelta(days=1)

    longest = 0
    if active_dates:
        sorted_d = sorted(datetime.date.fromisoformat(d) for d in active_dates)
        run = 1
        longest = 1
        for i in range(1, len(sorted_d)):
            if (sorted_d[i] - sorted_d[i - 1]).days == 1:
                run += 1
                longest = max(longest, run)
            else:
                run = 1
    return {"current": cur, "longest": longest, "active_days": len(active_dates)}


def build_state(today_str: str | None = None) -> dict[str, Any]:
    """Assemble the complete live state from Obsidian files + telemetry JSON."""
    today_str = today_str or datetime.date.today().isoformat()
    units = scan_study_units()
    raw_logs, merged_logs = scan_study_logs()
    telemetry = load_telemetry()

    # Keep CSV exports fresh whenever state is built? We export on writes and CLI --export;
    # let's check if CSVs don't exist yet and create them.
    if not LOGS_CSV.exists() or not UNITS_CSV.exists():
        export_csv_files(units, merged_logs)

    # Track logged hours per linked study unit from telemetry JSON
    unit_logged: dict[str, float] = {}
    for sess in telemetry.get("sessions", []):
        up = str(sess.get("unit_path") or "").strip()
        if up:
            unit_logged[up] = round(unit_logged.get(up, 0.0) + to_float(sess.get("hours"), 0.0), 2)

    for u in units:
        u["logged_hours"] = unit_logged.get(u["path"], 0.0)

    # Per-course summary
    course_stats: list[dict[str, Any]] = []
    for c in COURSES:
        c_units = [u for u in units if u["course"] == c["name"]]
        done_units = [u for u in c_units if u["completed"]]
        hours_est_total = round(sum(u["est_hours"] for u in c_units), 2)
        incomplete_est_hours = sum(u["est_hours"] for u in c_units if not u["completed"])
        hours_logged_on_done = sum(u["logged_hours"] for u in done_units)
        hours_logged = round(sum(r["hrs"].get(c["hrs_key"], 0.0) for r in merged_logs), 2)
        # Deduct logged hours on incomplete units + general unlinked course hours (never double-subtract done units)
        hours_logged_on_remaining = max(0.0, hours_logged - hours_logged_on_done)
        hours_est_left = round(max(0.0, incomplete_est_hours - hours_logged_on_remaining), 1)
        pct = round((len(done_units) / len(c_units) * 100) if c_units else 0.0, 1)
        hours_pct = round((min(1.0, hours_logged / hours_est_total) * 100) if hours_est_total else 0.0, 1)
        progress_pct = round(max(pct, hours_pct), 1)
        exam_d = datetime.date.fromisoformat(c["exam_date"])
        days_left = (exam_d - datetime.date.fromisoformat(today_str)).days

        course_stats.append(
            {
                **c,
                "total_units": len(c_units),
                "done_units": len(done_units),
                "remaining_units": len(c_units) - len(done_units),
                "pct": pct,
                "hours_pct": hours_pct,
                "progress_pct": progress_pct,
                "est_hours_total": hours_est_total,
                "est_hours_left": hours_est_left,
                "hours_logged": hours_logged,
                "days_to_exam": days_left,
            }
        )

    total_hours_logged = round(sum(r["total_hours"] for r in merged_logs), 2)
    today_row = next((r for r in merged_logs if r["date"] == today_str), None)
    today_hours = today_row["total_hours"] if today_row else 0.0
    focus_vals = [r["focus_score"] for r in merged_logs if r["focus_score"] is not None]
    avg_focus = round(sum(focus_vals) / len(focus_vals), 1) if focus_vals else None

    done_count = sum(1 for u in units if u["completed"])
    est_left_total = round(sum(c["est_hours_left"] for c in course_stats), 1)

    return {
        "vault_name": VAULT_ROOT.name,
        "today": today_str,
        "sprint_start": "2026-11-15",
        "sprint_day": max(1, (datetime.date.fromisoformat(today_str) - datetime.date(2026, 11, 15)).days + 1),
        "courses": course_stats,
        "units": units,
        "logs_daily": merged_logs,
        "logs_raw_count": len(raw_logs),
        "sessions": telemetry.get("sessions", [])[-100:][::-1],
        "streak": compute_streak(merged_logs, today_str),
        "summary": {
            "total_units": len(units),
            "done_units": done_count,
            "remaining_units": len(units) - done_count,
            "completion_pct": round((done_count / len(units) * 100) if units else 0.0, 1),
            "est_hours_left": est_left_total,
            "total_hours_logged": total_hours_logged,
            "today_hours": today_hours,
            "avg_focus": avg_focus,
        },
        "files": {
            "telemetry_json": TELEMETRY_JSON.relative_to(VAULT_ROOT).as_posix(),
            "logs_csv": LOGS_CSV.relative_to(VAULT_ROOT).as_posix(),
            "units_csv": UNITS_CSV.relative_to(VAULT_ROOT).as_posix(),
            "snapshot_md": SNAPSHOT_MD.relative_to(VAULT_ROOT).as_posix(),
        },
    }


def write_obsidian_snapshot(state: dict[str, Any]) -> Path:
    """Generate a live Markdown Analytics Snapshot note directly inside Groep T/."""
    s = state["summary"]
    st = state["streak"]
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def bar(pct: float, width: int = 16) -> str:
        filled = round((pct / 100.0) * width)
        return "█" * filled + "░" * (width - filled)

    lines = [
        "---",
        "title: Groep T Study Analytics Snapshot",
        f"generated_at: \"{now_str}\"",
        "tags:",
        "  - analytics",
        "  - snapshot",
        "  - groep-t",
        "---",
        "",
        "# 📈 Groep T — Study Analytics Snapshot",
        "",
        "> 🏠 **[[00_Groep_T_Command_Center|← Command Center]]** • **[[03_Daily_Study_Hours_Tracker|⏱️ Study Hours]]** • **[[02_Master_Course_Checklists|✅ Checklists]]**",
        f"> *Laatst gesynchroniseerd vanuit **Groep T Study OS Companion App** op `{now_str}` (Dag {state['sprint_day']} van de inhaalsprint).*",
        "",
        "## 🎯 Kernstatistieken",
        f"- **Totaal Gestudeerde Uren:** `{s['total_hours_logged']:.2f} h` (Vandaag: `{s['today_hours']:.2f} h`)",
        f"- **Studie-Streak:** `{st['current']} dag(en)` actief (Langste: `{st['longest']}d` | Actieve dagen: `{st['active_days']}`)",
        f"- **Modules Afgerond:** `{s['done_units']} / {s['total_units']}` (**{s['completion_pct']}%**)",
        f"- **Geschatte Resterende Studie-uren:** `{s['est_hours_left']:.1f} h`",
        f"- **Gemiddelde Focusscore:** `{s['avg_focus'] if s['avg_focus'] is not None else 'n.v.t.'} / 10`",
        "",
        "## 📚 Voortgang per Vak (30 ECTS)",
        "",
        "| Vak | ECTS | Dagen tot Eval | Modules Klaar | Progress | Resterend (u) | Gelogd (u) |",
        "| :--- | :-: | :-: | :-: | :--- | :-: | :-: |",
    ]
    for c in state["courses"]:
        prog = c.get("progress_pct", c["pct"])
        lines.append(
            f"| **{c['short']}** | {c['ects']} | {c['days_to_exam']}d | {c['done_units']} / {c['total_units']} | `{bar(prog)}` {prog}% | {c['est_hours_left']}h | {c['hours_logged']}h |"
        )

    lines.extend(["", "## 🗓️ Laatste 14 Studiedagen", "", r"| Datum | Totaal (u) | Doel ($\ge 6u$) | Focus |", "| :--- | :-: | :-: | :-: |"])
    recent = sorted(state["logs_daily"], key=lambda r: r["date"], reverse=True)[:14]
    if not recent:
        lines.append("| *Nog geen dagen gelogd* | `0.0h` | 🔴 `0h` | — |")
    else:
        for r in recent:
            h = r["total_hours"]
            badge = "✅ 6h+" if h >= 6 else ("🟡 4h+" if h >= 4 else ("🟠 <4h" if h > 0 else "🔴 0h"))
            foc = f"{r['focus_score']}/10" if r["focus_score"] is not None else "—"
            lines.append(f"| [[{r['date']}]] | `{h:.2f}h` | {badge} | {foc} |")

    lines.extend(
        [
            "",
            "---",
            "*Data-exports beschikbaar in `Groep T/study_telemetry.json`, `Groep T/study_logs_export.csv` en `Groep T/study_units_export.csv`.*",
        ]
    )
    SNAPSHOT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return SNAPSHOT_MD


class GroepTRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Serves static UI and JSON/CSV API endpoints backed directly by the Obsidian vault."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        # Clean concise stdout logging
        sys.stderr.write(f"[GroepT-App] {self.address_string()} - {format % args}\n")

    def _send_json(self, payload: Any, status: int = 200) -> None:
        raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def _read_json_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/state":
            try:
                self._send_json(build_state())
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=500)
            return

        if parsed.path == "/api/unit/content":
            qs = urllib.parse.parse_qs(parsed.query)
            rel_path = qs.get("path", [""])[0]
            try:
                target = resolve_safe_vault_path(rel_path)
                if not target.is_file():
                    self._send_json({"error": "File not found"}, status=404)
                    return
                self._send_json({"path": rel_path, "content": target.read_text(encoding="utf-8")})
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=400)
            return

        if parsed.path == "/api/export/csv":
            qs = urllib.parse.parse_qs(parsed.query)
            kind = qs.get("type", ["logs"])[0]
            state = build_state()
            export_csv_files(state["units"], state["logs_daily"])
            file_to_send = UNITS_CSV if kind == "units" else LOGS_CSV
            raw = file_to_send.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{file_to_send.name}"')
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
            return

        if parsed.path == "/api/export/json":
            telemetry = load_telemetry()
            raw = json.dumps(telemetry, indent=2, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="study_telemetry.json"')
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)
            return

        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        try:
            body = self._read_json_body()
        except Exception as exc:
            self._send_json({"error": f"Invalid JSON: {exc}"}, status=400)
            return

        if parsed.path == "/api/unit/update":
            try:
                rel_path = str(body["path"])
                target = resolve_safe_vault_path(rel_path)
                if not target.is_file():
                    self._send_json({"error": "Unit note not found"}, status=404)
                    return

                text = target.read_text(encoding="utf-8")
                updates: dict[str, Any] = {}
                if "completed" in body:
                    comp = bool(body["completed"])
                    updates["completed"] = comp
                    updates["status"] = "done" if comp else (body.get("status") or "todo")
                elif "status" in body:
                    st = str(body["status"])
                    updates["status"] = st
                    updates["completed"] = st == "done"

                if "priority" in body and body["priority"] in ("high", "medium", "low"):
                    updates["priority"] = body["priority"]
                if "est_hours" in body:
                    updates["est_hours"] = round(max(0.0, float(body["est_hours"])), 2)

                new_text = update_frontmatter_keys(text, updates)
                append_note = str(body.get("append_note") or "").strip()
                if append_note:
                    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    new_text = new_text.rstrip() + f"\n\n- 📝 **{stamp}:** {append_note}\n"

                target.write_text(new_text, encoding="utf-8")
                if "completed" in updates:
                    sync_checklist_checkbox(target.stem, bool(updates["completed"]))

                state = build_state()
                export_csv_files(state["units"], state["logs_daily"])
                self._send_json({"ok": True, "state": state})
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=400)
            return

        if parsed.path == "/api/log/session":
            try:
                date_str = str(body.get("date") or datetime.date.today().isoformat())
                datetime.date.fromisoformat(date_str)  # validate YYYY-MM-DD
                course_id = str(body["course_id"])
                course = next((c for c in COURSES if c["id"] == course_id), None)
                if not course:
                    self._send_json({"error": f"Unknown course_id: {course_id}"}, status=400)
                    return

                duration_h = round(float(body["hours"]), 2)
                if duration_h <= 0:
                    self._send_json({"error": "Duration must be > 0"}, status=400)
                    return

                target_kind = "study_log" if body.get("target") == "study_log" else "daily_journal"
                log_file = ensure_log_file(date_str, target_kind)
                text = log_file.read_text(encoding="utf-8")
                fm_lines, _ = split_frontmatter(text)
                meta = parse_simple_yaml(fm_lines)

                hrs_key = course["hrs_key"]
                current_course_hrs = to_float(meta.get(hrs_key), 0.0)
                new_course_hrs = round(current_course_hrs + duration_h, 2)

                # Recompute total cleanly across all 7 course properties
                new_total = 0.0
                for k in HRS_KEYS:
                    new_total += new_course_hrs if k == hrs_key else to_float(meta.get(k), 0.0)
                new_total = round(max(new_total, to_float(meta.get("study_hours_total"), 0.0) + duration_h), 2)

                updates: dict[str, Any] = {
                    hrs_key: new_course_hrs,
                    "study_hours_total": new_total,
                }
                if body.get("focus_score") not in (None, ""):
                    updates["study_focus_score"] = max(1, min(10, int(float(body["focus_score"]))))
                pomos = int(body.get("pomodoros") or 0)
                if pomos > 0:
                    updates["pomodoros_done"] = int(to_float(meta.get("pomodoros_done"), 0.0)) + pomos

                updated_text = update_frontmatter_keys(text, updates)
                log_file.write_text(updated_text, encoding="utf-8")

                unit_path = str(body.get("unit_path") or "").strip()
                unit_name = ""
                if unit_path:
                    u_file = resolve_safe_vault_path(unit_path)
                    if u_file.is_file():
                        unit_name = u_file.stem
                        u_raw = u_file.read_text(encoding="utf-8")
                        if body.get("mark_unit_done"):
                            u_txt = update_frontmatter_keys(u_raw, {"completed": True, "status": "done"})
                            u_file.write_text(u_txt, encoding="utf-8")
                            sync_checklist_checkbox(u_file.stem, True)
                        else:
                            u_fm, _ = split_frontmatter(u_raw)
                            u_meta = parse_simple_yaml(u_fm)
                            if not u_meta.get("completed") and u_meta.get("status") in (None, "", "todo"):
                                u_file.write_text(update_frontmatter_keys(u_raw, {"status": "in-progress"}), encoding="utf-8")

                now_time = datetime.datetime.now().strftime("%H:%M")
                time_range = str(body.get("time_range") or now_time)
                notes = str(body.get("notes") or "")
                append_session_to_markdown(log_file, time_range, course["short"], unit_name, duration_h, notes, new_total_hours=new_total)

                # Persist structured telemetry JSON
                telemetry = load_telemetry()
                telemetry["sessions"].append(
                    {
                        "id": f"{date_str}-{len(telemetry['sessions']) + 1}",
                        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
                        "date": date_str,
                        "course_id": course["id"],
                        "course": course["name"],
                        "course_short": course["short"],
                        "hours": duration_h,
                        "focus_score": updates.get("study_focus_score"),
                        "pomodoros": pomos,
                        "unit_path": unit_path,
                        "unit_name": unit_name,
                        "notes": notes,
                        "obsidian_file": log_file.relative_to(VAULT_ROOT).as_posix(),
                    }
                )
                save_telemetry(telemetry)

                state = build_state()
                export_csv_files(state["units"], state["logs_daily"])
                self._send_json({"ok": True, "obsidian_file": log_file.relative_to(VAULT_ROOT).as_posix(), "state": state})
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=400)
            return

        if parsed.path == "/api/obsidian/snapshot":
            try:
                state = build_state()
                export_csv_files(state["units"], state["logs_daily"])
                snap = write_obsidian_snapshot(state)
                self._send_json({"ok": True, "snapshot_file": snap.relative_to(VAULT_ROOT).as_posix(), "state": state})
            except Exception as exc:
                self._send_json({"error": str(exc)}, status=500)
            return

        self._send_json({"error": "Unknown endpoint"}, status=404)


class ReusableTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True


def main() -> int:
    parser = argparse.ArgumentParser(description="Groep T Study OS — All-in-One Obsidian Companion Web App")
    parser.add_argument("--host", default="127.0.0.1", help="Bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8765, help="Port to listen on (default: 8765)")
    parser.add_argument("--no-open", action="store_true", help="Do not automatically launch the browser")
    parser.add_argument("--export-only", action="store_true", help="Sync JSON, CSV & Obsidian Snapshot and exit")
    args = parser.parse_args()

    state = build_state()
    export_csv_files(state["units"], state["logs_daily"])
    if not TELEMETRY_JSON.exists():
        save_telemetry(load_telemetry())

    if args.export_only:
        snap = write_obsidian_snapshot(state)
        print(f"✅ Exported {LOGS_CSV.name}, {UNITS_CSV.name}, {TELEMETRY_JSON.name}, and {snap.name}")
        return 0

    with ReusableTCPServer((args.host, args.port), GroepTRequestHandler) as httpd:
        url = f"http://{args.host}:{args.port}"
        print(f"🚀 Groep T Study OS Companion running at {url}")
        print(f"📁 Vault: {VAULT_ROOT}")
        print(f"📊 Loaded {state['summary']['total_units']} study units & {len(state['logs_daily'])} logged days")
        print("Press Ctrl+C to stop.")
        if not args.no_open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Shutting down Groep T Study OS server.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
