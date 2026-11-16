#!/usr/bin/env python3
"""
Automated Daily Journal Generator for Obsidian.

Creates a new daily journal note based on a structured template
combining the 5-Minute Journal, Ivy Lee (Top 3 Priorities),
and Interstitial Journaling methods.
"""

from __future__ import annotations

import argparse
import datetime
import os
import subprocess
import sys
from pathlib import Path

# Paths relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_TEMPLATE_PATH = SCRIPT_DIR / "Templates" / "Daily_Journal_Template.md"
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "Daily_Journal"

FALLBACK_TEMPLATE = """---
date: "{{date}}"
day: "{{weekday}}"
type: daily-planner
tags:
  - journal/daily
  - planner
  - study-log
rating: 
mood: 
energy: 
sleep_hours: 
water_intake: 
workout_done: false
quran_read: false
study_hours_total: 0
hrs_cad: 0
hrs_dynamica: 0
hrs_comp_denken: 0
hrs_wiskunde: 0
hrs_chemie: 0
hrs_sgdm: 0
hrs_ethiek: 0
study_focus_score: 
---

# 📅 {{date}} — {{weekday}}

> *« What you do today can improve all your tomorrows. »*

[[{{yesterday}}|⬅️ {{yesterday}}]] • [[Daily_Journal/README_JOURNAL|📑 Index]] • [[{{tomorrow}}|{{tomorrow}} ➡️]]

---

> **`بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ`**
> *"In the name of Allah, the Most Gracious, the Most Merciful"*

---

## 📖 Quranic Verse & Spiritual Tadabbur (آية اليوم وتدبر)

> **« رَبِّ اشْرَحْ لِي صَدْرِي * وَيَسِّرْ لِي أَمْرِي »**
> *"My Lord, expand for me my chest [with assurance] and ease for me my task."*
> — *Surah Ta-Ha (20:25-26)*

- **📖 Daily Quran Wird (الورد اليومي):**
  - **Surah / Juz:** 
  - **Pages / Verses:** [ ] Read
  - **💡 Tadabbur & Reflection (تدبر وعبرة):** 
- **🤲 Daily Adhkar & Dua (الأذكار والدعاء):**
  - [ ] 🌅 Morning Adhkar (أذكار الصباح)
  - [ ] 🌇 Evening Adhkar (أذكار المساء)
  - [ ] 📿 Istighfar & Salawat
  - **Dua of the Day:** 

---

## 🌟 Daily Habit Tracker

### 🕌 Prayers & Worship (الصلوات المكتوبة والسنن)
| 🌅 Fajr | ☀️ Dhuhr | 🌤️ Asr | 🌇 Maghrib | 🌌 Isha | 📿 Sunnah / Tahajjud | 📖 Quran |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

### 🌿 Health, Focus & Life Habits
- **💧 Hydration:** `[ ] 1L`  `[ ] 2L`  `[ ] 3L`
- **😴 Sleep:** ____ hrs *(Bed: __:__ | Wake: __:__)*
- **📚 Reading & Skill Growth:** `[ ] 30+ mins` *(Book / Topic: ________)*
- **📵 Digital Discipline:** `[ ] No mindless scrolling`
- **🥗 Nutrition & Fasting:** `[ ] Clean eating` | Fasting today? `[ ] Yes`

---

## 🏋️‍♂️ Sport & Physical Activity (النشاط الرياضي)

- **Activity Type:** [ ] Gym / Strength  [ ] Running / Cardio  [ ] Mobility / Calisthenics  [ ] Rest / Recovery
- **Time & Duration:** `__:__` | `___ mins`
- **Intensity / Effort:** `[ ] Light (1-4)`  `[ ] Moderate (5-7)`  `[ ] Intense (8-10)`

### 📝 Workout Log
| Exercise / Movement | Sets x Reps | Weight / Distance | Notes & Form |
| :--- | :---: | :---: | :--- |
| 1. | | | |
| 2. | | | |
| 3. | | | |
| 4. | | | |

- **Post-Workout Recovery & Notes:** 

---

## 🎓 Groep T Daily Study Log (30-Day Catch-Up Sprint)
> 🏠 [[00_Groep_T_Command_Center|Command Center]] • [[01_30_Day_Catchup_Sprint_Plan|30-Day Sprint]] • [[02_Master_Course_Checklists|Master Checklists]] • [[03_Daily_Study_Hours_Tracker|Hours Dashboard]]
> *Update `hrs_*` & `study_hours_total` in Properties above so [[00_Study_Hours_Base.base]] tracks your daily & weekly totals!*

- **Target Today:** `6.5 – 8.0 hours` | **Actual Total:** `0h`
- [ ] **Morning Deep Work (3h):** 
- [ ] **Afternoon Practice / Oefensessie (2.5h):** 
- [ ] **Evening Active Recall / Kennisclips (1.5h):** 

---

## 🎯 Tasks & Execution (TaskNotes)

### 🥇 Most Important Tasks (The Rule of 3)
*If only these 3 are completed today, the day is an absolute win.*
- [ ] #task 🎯 **P1:** 
- [ ] #task 🎯 **P2:** 
- [ ] #task 🎯 **P3:** 

### 📋 Today's Agenda (TaskNotes Bases View)
![[TaskNotes/Views/agenda-default.base]]

### ⚡ Quick Capture & In-Progress Tasks
*TaskNotes syntax: `#task`, `@context`, `+project`, `📅{{date}}`, `!high`*
- [ ] #task 
- [ ] #task 

### ⏱️ Time-Blocking Schedule
- **06:00 - 08:00** | 🌅 Fajr, Quran Wird, Morning Routine & Daily Planning
- **08:00 - 12:00** | 🧠 Deep Work / Complex Engineering & High-Cognitive Focus
- **12:00 - 14:00** | ☀️ Dhuhr, Lunch & Recharge
- **14:00 - 17:00** | 💻 Engineering Implementation, Collaboration & Asr
- **17:00 - 19:00** | 🏋️ Workout / Sport Activity, Recovery & Maghrib
- **19:00 - 22:00** | 🌙 Dinner, Isha, Reading, Evening Review & Wind-down

---

## ⚡ Daytime Log & Fleeting Notes (Interstitial Journaling)
*Capture thoughts, meeting takeaways, engineering solutions, and ideas as they happen.*
- **{{time}}** — 

---

## 🌙 Evening Reflection & Muhasabah (المحاسبة والتقييم المسائي)

### 🙏 Gratitude (شكر النعم)
*What are 3 blessings I am genuinely grateful to Allah for today?*
1. 
2. 
3. 

### 🏆 Daily Wins & Highlights
*What went well today? What accomplishments am I proud of?*
- 

### 🔍 Lessons Learned & Self-Correction
*What friction or mistakes occurred, and what can I do better tomorrow?*
- 

### 🔋 Daily Check-in & Review
- **Overall Day Rating:** ⭐ ⭐ ⭐ ⭐ ⭐
- **Energy Level (1-10):** 
- **Focus & Mental Clarity (1-10):** 
- **Mood:** 
- **One-sentence summary of the day:** 
"""


def load_template(template_path: Path) -> str:
    """Load the markdown template file, or fall back to the default template."""
    if template_path.exists():
        return template_path.read_text(encoding="utf-8")
    return FALLBACK_TEMPLATE


def render_template(template_content: str, target_date: datetime.date) -> str:
    """Replace template tags with actual date and time values."""
    yesterday = target_date - datetime.timedelta(days=1)
    tomorrow = target_date + datetime.timedelta(days=1)
    now = datetime.datetime.now()

    replacements = {
        "{{date}}": target_date.strftime("%Y-%m-%d"),
        "{{title}}": target_date.strftime("%Y-%m-%d"),
        "{{weekday}}": target_date.strftime("%A"),
        "{{yesterday}}": yesterday.strftime("%Y-%m-%d"),
        "{{tomorrow}}": tomorrow.strftime("%Y-%m-%d"),
        "{{year}}": target_date.strftime("%Y"),
        "{{month}}": target_date.strftime("%m"),
        "{{day}}": target_date.strftime("%d"),
        "{{time}}": now.strftime("%H:%M"),
    }

    content = template_content
    for key, value in replacements.items():
        content = content.replace(key, value)
    return content


def create_daily_page(
    target_date: datetime.date,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    template_path: Path = DEFAULT_TEMPLATE_PATH,
    force: bool = False,
) -> Path | None:
    """Create a daily journal page for target_date. Returns the Path if created, None if already exists."""
    output_dir.mkdir(parents=True, exist_ok=True)
    file_name = f"{target_date.strftime('%Y-%m-%d')}.md"
    file_path = output_dir / file_name

    if file_path.exists() and not force:
        print(f"ℹ️  Daily page already exists: {file_path}")
        return None

    template_content = load_template(template_path)
    rendered = render_template(template_content, target_date)
    file_path.write_text(rendered, encoding="utf-8")
    print(f"✅ Created daily page: {file_path}")
    return file_path


def install_cron_job(hour: int = 6, minute: int = 0) -> bool:
    """Add a cron job to automatically run this script every morning."""
    python_bin = sys.executable
    script_path = SCRIPT_DIR / "daily_journal.py"
    cron_command = f"{minute:02d} {hour:02d} * * * {python_bin} {script_path} >> {SCRIPT_DIR}/.journal_cron.log 2>&1"

    # Get current crontab
    try:
        proc = subprocess.run(["crontab", "-l"], capture_output=True, text=True, check=False)
        current_cron = proc.stdout if proc.returncode == 0 else ""
    except Exception as e:
        print(f"❌ Failed to read current crontab: {e}")
        return False

    if str(script_path) in current_cron:
        print("ℹ️  Cron job for daily_journal.py is already installed.")
        return True

    new_cron = current_cron.strip()
    if new_cron:
        new_cron += "\n"
    new_cron += f"{cron_command}\n"

    try:
        subprocess.run(["crontab", "-"], input=new_cron, text=True, check=True)
        print(f"🎉 Successfully installed cron job to run daily at {hour:02d}:{minute:02d}!")
        print(f"Cron entry:\n  {cron_command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install cron job: {e}")
        return False


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Automated Daily Journal Page Creator for Obsidian."
    )
    parser.add_argument(
        "--date",
        type=str,
        help="Target date in YYYY-MM-DD format (default: today).",
    )
    parser.add_argument(
        "--tomorrow",
        action="store_true",
        help="Create journal page for tomorrow.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing note if it already exists.",
    )
    parser.add_argument(
        "--install-cron",
        action="store_true",
        help="Automatically configure Linux cron to run this script every day at 06:00 AM.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List existing journal entries.",
    )

    args = parser.parse_args()

    if args.install_cron:
        success = install_cron_job()
        return 0 if success else 1

    if args.list:
        if not DEFAULT_OUTPUT_DIR.exists():
            print("No daily journal entries found.")
            return 0
        entries = sorted(DEFAULT_OUTPUT_DIR.glob("*.md"))
        print(f"📓 Found {len(entries)} journal entries:")
        for entry in entries:
            print(f"  - {entry.name}")
        return 0

    if args.date:
        try:
            target_date = datetime.datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print(f"❌ Invalid date format: '{args.date}'. Expected YYYY-MM-DD.")
            return 1
    elif args.tomorrow:
        target_date = datetime.date.today() + datetime.timedelta(days=1)
    else:
        target_date = datetime.date.today()

    create_daily_page(target_date, force=args.force)
    return 0


if __name__ == "__main__":
    sys.exit(main())
