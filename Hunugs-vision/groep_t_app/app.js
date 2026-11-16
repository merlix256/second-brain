/* Groep T Study OS Companion App — Client Logic */
"use strict";

let APP_STATE = null;
let CURRENT_DRAWER_PATH = null;

const MODES = {
  pomo25: { label: "25m Pomodoro", seconds: 25 * 60, stopwatch: false },
  pomo50: { label: "50m Deep Work", seconds: 50 * 60, stopwatch: false },
  pomo90: { label: "90m Exam Block", seconds: 90 * 60, stopwatch: false },
  stopwatch: { label: "Stopwatch", seconds: 0, stopwatch: true },
};

let timerState = loadTimerState();
let timerInterval = null;

function loadTimerState() {
  try {
    const saved = JSON.parse(localStorage.getItem("groep_t_timer") || "null");
    if (saved && MODES[saved.mode]) return saved;
  } catch (_) {}
  return { mode: "pomo25", remaining: 25 * 60, elapsed: 0, running: false, lastTick: null };
}

function saveTimerState() {
  localStorage.setItem("groep_t_timer", JSON.stringify(timerState));
}

function showToast(msg, isError = false) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.className = isError ? "toast error" : "toast";
  clearTimeout(el._t);
  el._t = setTimeout(() => el.classList.add("hidden"), 3200);
}

function escapeHtml(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function formatMMSS(totalSec) {
  const s = Math.max(0, Math.floor(totalSec));
  const hrs = Math.floor(s / 3600);
  const mins = Math.floor((s % 3600) / 60);
  const secs = s % 60;
  if (hrs > 0) return `${String(hrs).padStart(2, "0")}:${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  return `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
}

function playChime() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    [523.25, 659.25, 783.99].forEach((freq, idx) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.frequency.value = freq;
      osc.type = "sine";
      gain.gain.setValueAtTime(0.12, ctx.currentTime + idx * 0.14);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.14 + 0.45);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(ctx.currentTime + idx * 0.14);
      osc.stop(ctx.currentTime + idx * 0.14 + 0.46);
    });
  } catch (_) {}
}

/* ---------- API Calls ---------- */

async function fetchState() {
  const res = await fetch("/api/state");
  if (!res.ok) throw new Error("Failed to load vault state");
  APP_STATE = await res.json();
  renderAll();
}

async function apiPost(url, payload) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || "Request failed");
  if (data.state) {
    APP_STATE = data.state;
    renderAll();
  }
  return data;
}

/* ---------- Tooltip ---------- */

const tooltipEl = document.getElementById("chart-tooltip");
function showTooltip(evt, html) {
  tooltipEl.innerHTML = html;
  tooltipEl.classList.remove("hidden");
  const x = Math.min(window.innerWidth - 270, evt.clientX + 12);
  const y = Math.min(window.innerHeight - 120, evt.clientY + 12);
  tooltipEl.style.left = `${x}px`;
  tooltipEl.style.top = `${y}px`;
}
function hideTooltip() {
  tooltipEl.classList.add("hidden");
}

/* ---------- Render Pipeline ---------- */

function renderAll() {
  if (!APP_STATE) return;
  const s = APP_STATE.summary;
  const st = APP_STATE.streak;
  document.getElementById("header-meta").textContent =
    `Vault: ${APP_STATE.vault_name} • Sprint Day ${APP_STATE.sprint_day}/30 (${APP_STATE.today}) • ${s.done_units}/${s.total_units} Units (${s.completion_pct}%)`;

  renderKPIs();
  renderHeatmap();
  renderDailyBarChart();
  renderDonutAndFocus();
  renderCourseBars();
  populateLogFormSelectors();
  renderRecentSessions();
  renderUnitsTable();
  renderExamSimulatorAndLabs();
  renderDataExplorer();
}

function renderKPIs() {
  const s = APP_STATE.summary;
  const st = APP_STATE.streak;
  const firstExamDays = Math.min(...APP_STATE.courses.filter(c => c.id !== "cad").map(c => c.days_to_exam));
  const cadDays = APP_STATE.courses.find(c => c.id === "cad")?.days_to_exam ?? 0;

  const cards = [
    {
      label: "Total Studied Hours",
      value: `${s.total_hours_logged.toFixed(1)}h`,
      sub: `Today: ${s.today_hours.toFixed(1)}h / 6.0h target`,
      color: "#a855f7",
    },
    {
      label: "Consistency Streak",
      value: `${st.current} day${st.current === 1 ? "" : "s"}`,
      sub: `Longest: ${st.longest}d • Active days: ${st.active_days}`,
      color: "#10b981",
    },
    {
      label: "Modules Completed",
      value: `${s.done_units} / ${s.total_units}`,
      sub: `${s.completion_pct}% done • ~${s.est_hours_left.toFixed(0)}h remaining`,
      color: "#3b82f6",
    },
    {
      label: "Avg Focus Score",
      value: s.avg_focus !== null ? `${s.avg_focus} / 10` : "— / 10",
      sub: `Across ${APP_STATE.logs_daily.length} tracked journal days`,
      color: "#06b6d4",
    },
    {
      label: "Next Urgent Milestone",
      value: `${cadDays}d`,
      sub: `CAD Perm. Eval (Dec 7–17) • Jan Exams in ${firstExamDays}d`,
      color: "#f43f5e",
    },
  ];

  document.getElementById("kpi-grid").innerHTML = cards
    .map(
      (c) => `
      <div class="kpi-card" style="border-top: 3px solid ${c.color}">
        <div class="kpi-label">${escapeHtml(c.label)}</div>
        <div class="kpi-value">${escapeHtml(c.value)}</div>
        <div class="kpi-sub">${escapeHtml(c.sub)}</div>
      </div>`
    )
    .join("");
}

/* Local timezone-safe ISO date helpers (avoids UTC midnight off-by-1 shifts) */
function parseLocalDate(iso) {
  const [y, m, d] = iso.split("-").map(Number);
  return new Date(y, m - 1, d);
}

function toLocalISO(dt) {
  const y = dt.getFullYear();
  const m = String(dt.getMonth() + 1).padStart(2, "0");
  const d = String(dt.getDate()).padStart(2, "0");
  return `${y}-${m}-${d}`;
}

function addDaysISO(iso, deltaDays) {
  const dt = parseLocalDate(iso);
  dt.setDate(dt.getDate() + deltaDays);
  return toLocalISO(dt);
}

function renderHeatmap() {
  const container = document.getElementById("heatmap-container");
  const logDates = APP_STATE.logs_daily.map((r) => r.date).sort();
  let startISO = "2026-10-01";
  if (logDates.length && logDates[0] < startISO) {
    startISO = `${logDates[0].slice(0, 7)}-01`;
  }
  let endISO = "2027-01-31";
  if (logDates.length && logDates[logDates.length - 1] > endISO) {
    endISO = logDates[logDates.length - 1];
  }

  const start = parseLocalDate(startISO);
  const end = parseLocalDate(endISO);
  const rangeLbl = document.getElementById("heatmap-range-label");
  if (rangeLbl) rangeLbl.textContent = `${startISO} → ${endISO}`;

  const logMap = new Map(APP_STATE.logs_daily.map((r) => [r.date, r]));
  const examMap = new Map(APP_STATE.courses.map((c) => [c.exam_date, c]));

  // Align first column to Monday (Mon=0 ... Sun=6)
  const startDayMon = (start.getDay() + 6) % 7;
  const cells = [];
  for (let i = 0; i < startDayMon; i++) cells.push(null);

  for (let d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
    cells.push(toLocalISO(d));
  }

  const weeks = Math.ceil(cells.length / 7);
  const cellSize = 18;
  const gap = 4;
  const leftPad = 34;
  const topPad = 24;
  const width = leftPad + weeks * (cellSize + gap) + 12;
  const height = topPad + 7 * (cellSize + gap) + 10;

  const dayLabels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  let svg = `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">`;

  dayLabels.forEach((lbl, idx) => {
    if (idx % 2 === 0) {
      svg += `<text x="0" y="${topPad + idx * (cellSize + gap) + 13}" fill="#8b9bb4" font-size="10.5">${lbl}</text>`;
    }
  });

  const shownMonths = new Set();
  const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  cells.forEach((iso, idx) => {
    if (!iso) return;
    const col = Math.floor(idx / 7);
    const row = idx % 7;
    const x = leftPad + col * (cellSize + gap);
    const y = topPad + row * (cellSize + gap);

    const dObj = parseLocalDate(iso);
    const ym = `${dObj.getFullYear()}-${dObj.getMonth()}`;
    if (dObj.getDate() <= 7 && !shownMonths.has(ym)) {
      shownMonths.add(ym);
      svg += `<text x="${x}" y="14" fill="#8b9bb4" font-size="11" font-weight="600">${monthNames[dObj.getMonth()]}</text>`;
    }

    const log = logMap.get(iso);
    const hrs = log ? log.total_hours : 0;
    let fill = "#1e293b";
    if (hrs >= 6) fill = "#4ade80";
    else if (hrs >= 4) fill = "#22c55e";
    else if (hrs >= 2) fill = "#15803d";
    else if (hrs > 0) fill = "#14532d";

    const isToday = iso === APP_STATE.today;
    const exam = examMap.get(iso);
    const stroke = exam ? "#f43f5e" : isToday ? "#a855f7" : "#253047";
    const sw = exam || isToday ? 2 : 1;

    svg += `<rect class="hm-cell" data-date="${iso}" x="${x}" y="${y}" width="${cellSize}" height="${cellSize}" rx="4" fill="${fill}" stroke="${stroke}" stroke-width="${sw}" style="cursor:pointer"/>`;
    if (exam) {
      svg += `<circle cx="${x + cellSize - 4}" cy="${y + 4}" r="2.6" fill="#f43f5e" pointer-events="none"/>`;
    }
  });

  svg += `</svg>`;
  container.innerHTML = svg;

  container.querySelectorAll(".hm-cell").forEach((el) => {
    el.addEventListener("mouseenter", (evt) => {
      const iso = el.getAttribute("data-date");
      const log = logMap.get(iso);
      const exam = examMap.get(iso);
      let html = `<strong>${iso}</strong><br/>`;
      html += log
        ? `Hours: <b>${log.total_hours.toFixed(2)}h</b>${log.focus_score ? ` • Focus: ${log.focus_score}/10` : ""}`
        : `Hours: <b>0.0h</b>`;
      if (exam) html += `<br/><span style="color:#fb7185">📝 ${escapeHtml(exam.short)} (${escapeHtml(exam.exam_label)})</span>`;
      showTooltip(evt, html);
    });
    el.addEventListener("mouseleave", hideTooltip);
    el.addEventListener("click", () => {
      const iso = el.getAttribute("data-date");
      document.getElementById("log-date").value = iso;
      document.querySelector('[data-tab="logger"]').click();
      showToast(`Selected ${iso} in Study Logger`);
    });
  });
}

function renderDailyBarChart() {
  const mode = document.getElementById("chart-days-range").value || "auto";
  const container = document.getElementById("daily-bar-chart");
  const logMap = new Map(APP_STATE.logs_daily.map((r) => [r.date, r]));
  const logDates = APP_STATE.logs_daily.filter((r) => r.total_hours > 0).map((r) => r.date).sort();

  let startISO;
  let endISO = APP_STATE.today;
  if (logDates.length && logDates[logDates.length - 1] > endISO) {
    endISO = logDates[logDates.length - 1];
  }

  if (mode === "semester") {
    startISO = logDates.length && logDates[0] < "2026-10-01" ? logDates[0] : "2026-10-01";
    if ("2027-01-31" > endISO) endISO = "2027-01-31";
  } else if (mode === "auto") {
    const thirtyAgo = addDaysISO(endISO, -29);
    startISO = logDates.length && logDates[0] < thirtyAgo ? logDates[0] : thirtyAgo;
  } else {
    const n = parseInt(mode, 10) || 30;
    startISO = addDaysISO(endISO, -(n - 1));
  }

  const series = [];
  for (let d = parseLocalDate(startISO), endD = parseLocalDate(endISO); d <= endD; d.setDate(d.getDate() + 1)) {
    const iso = toLocalISO(d);
    series.push({ date: iso, row: logMap.get(iso) || null });
  }

  const maxH = Math.max(8, ...series.map((s) => (s.row ? s.row.total_hours : 0)));
  const W = 680;
  const H = 230;
  const padL = 34;
  const padB = 26;
  const padT = 14;
  const chartW = W - padL - 12;
  const chartH = H - padT - padB;
  const step = chartW / Math.max(1, series.length);
  const barW = Math.max(3, Math.min(24, step - 2));

  let svg = `<svg viewBox="0 0 ${W} ${H}" width="100%" height="${H}">`;

  // Horizontal grid + 6h Target line
  [0, 2, 4, 6, 8].forEach((val) => {
    if (val > maxH) return;
    const y = padT + chartH - (val / maxH) * chartH;
    const isTarget = val === 6;
    svg += `<line x1="${padL}" y1="${y}" x2="${W - 8}" y2="${y}" stroke="${isTarget ? "#4ade80" : "#253047"}" stroke-dasharray="${isTarget ? "5 4" : "2 3"}" stroke-width="${isTarget ? 1.5 : 1}"/>`;
    svg += `<text x="4" y="${y + 4}" fill="${isTarget ? "#4ade80" : "#8b9bb4"}" font-size="10">${val}h</text>`;
  });

  const labelStep = Math.max(1, Math.ceil(series.length / 7));
  series.forEach((item, idx) => {
    const x = padL + idx * step + Math.max(0, (step - barW) / 2);
    let yCursor = padT + chartH;

    if (item.row && item.row.total_hours > 0) {
      let stackedSum = 0;
      APP_STATE.courses.forEach((c) => {
        const val = item.row.hrs[c.hrs_key] || 0;
        if (val <= 0) return;
        stackedSum += val;
        const h = (val / maxH) * chartH;
        yCursor -= h;
        svg += `<rect class="bar-seg" data-date="${item.date}" data-total="${item.row.total_hours}" data-course="${escapeHtml(c.short)}" data-val="${val}" x="${x}" y="${yCursor}" width="${barW}" height="${h}" fill="${c.color}" rx="2"/>`;
      });
      if (item.row.total_hours > stackedSum + 0.01) {
        const diff = item.row.total_hours - stackedSum;
        const h = (diff / maxH) * chartH;
        yCursor -= h;
        svg += `<rect class="bar-seg" data-date="${item.date}" data-total="${item.row.total_hours}" data-course="Untagged Total" data-val="${diff.toFixed(2)}" x="${x}" y="${yCursor}" width="${barW}" height="${h}" fill="#64748b" rx="2"/>`;
      }
    } else {
      svg += `<rect x="${x}" y="${padT + chartH - 2}" width="${barW}" height="2" fill="#253047"/>`;
    }

    if (idx % labelStep === 0 || idx === series.length - 1) {
      const tx = Math.min(W - 34, x);
      svg += `<text x="${tx}" y="${H - 6}" fill="#8b9bb4" font-size="9.5">${item.date.slice(5)}</text>`;
    }
  });

  svg += `</svg>`;
  container.innerHTML = svg;

  container.querySelectorAll(".bar-seg").forEach((el) => {
    el.addEventListener("mouseenter", (evt) => {
      showTooltip(
        evt,
        `<strong>${el.dataset.date}</strong><br/>${el.dataset.course}: <b>${el.dataset.val}h</b><br/>Day Total: <b>${el.dataset.total}h</b>`
      );
    });
    el.addEventListener("mouseleave", hideTooltip);
  });
}

function renderDonutAndFocus() {
  const donutEl = document.getElementById("donut-chart");
  const legendEl = document.getElementById("donut-legend");
  const courses = APP_STATE.courses;
  const total = courses.reduce((acc, c) => acc + c.hours_logged, 0);

  const size = 154;
  const r = 56;
  const circ = 2 * Math.PI * r;
  let offset = 0;

  let svg = `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">`;
  svg += `<circle cx="77" cy="77" r="${r}" fill="none" stroke="#1e293b" stroke-width="20"/>`;
  if (total > 0) {
    courses.forEach((c) => {
      if (c.hours_logged <= 0) return;
      const len = (c.hours_logged / total) * circ;
      svg += `<circle cx="77" cy="77" r="${r}" fill="none" stroke="${c.color}" stroke-width="20" stroke-dasharray="${len} ${circ - len}" stroke-dashoffset="${-offset}" transform="rotate(-90 77 77)"/>`;
      offset += len;
    });
  }
  svg += `<text x="77" y="74" text-anchor="middle" fill="#e6edf7" font-size="18" font-weight="800">${total.toFixed(1)}h</text>`;
  svg += `<text x="77" y="92" text-anchor="middle" fill="#8b9bb4" font-size="10.5">Logged</text></svg>`;
  donutEl.innerHTML = svg;

  legendEl.innerHTML = courses
    .map((c) => {
      const pct = total > 0 ? ((c.hours_logged / total) * 100).toFixed(0) : 0;
      return `<div class="legend-row">
        <span class="legend-left"><span class="swatch" style="background:${c.color}"></span>${escapeHtml(c.short)}</span>
        <span><b>${c.hours_logged.toFixed(1)}h</b> (${pct}%)</span>
      </div>`;
    })
    .join("");

  // Focus Line Chart
  const focusEl = document.getElementById("focus-line-chart");
  const focusPts = APP_STATE.logs_daily.filter((r) => r.focus_score !== null && r.focus_score > 0).slice(-20);
  if (focusPts.length === 0) {
    focusEl.innerHTML = `<p class="muted">Log at least 1 study session with a Focus Score (1–10) to render the trend curve.</p>`;
    return;
  }
  const W = 520, H = 115, padL = 28, padR = 24, padT = 18, padB = 24;
  const cw = W - padL - padR, ch = H - padT - padB;
  const coords = focusPts.map((pt, i) => {
    const x = focusPts.length === 1 ? padL + cw / 2 : padL + (i / (focusPts.length - 1)) * cw;
    const y = padT + ch - ((pt.focus_score - 1) / 9) * ch;
    return { x, y, pt };
  });
  const pathD = coords.map((p, i) => `${i === 0 ? "M" : "L"} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(" ");
  let fSvg = `<svg viewBox="0 0 ${W} ${H}" width="100%" height="${H}">`;
  const midY = padT + ch - (4 / 9) * ch;
  fSvg += `<line x1="${padL}" y1="${padT}" x2="${W - padR}" y2="${padT}" stroke="#253047" stroke-dasharray="2 3"/>`;
  fSvg += `<line x1="${padL}" y1="${midY}" x2="${W - padR}" y2="${midY}" stroke="#253047" stroke-dasharray="2 3"/>`;
  fSvg += `<line x1="${padL}" y1="${padT + ch}" x2="${W - padR}" y2="${padT + ch}" stroke="#253047"/>`;
  fSvg += `<text x="2" y="${padT + 4}" fill="#8b9bb4" font-size="9.5">10</text>`;
  fSvg += `<text x="6" y="${midY + 3}" fill="#8b9bb4" font-size="9.5">5</text>`;
  fSvg += `<text x="6" y="${padT + ch}" fill="#8b9bb4" font-size="9.5">1</text>`;
  if (coords.length > 1) {
    fSvg += `<path d="${pathD}" fill="none" stroke="#06b6d4" stroke-width="2.5" stroke-linecap="round"/>`;
  }
  coords.forEach((c, idx) => {
    fSvg += `<circle class="focus-dot" data-date="${c.pt.date}" data-score="${c.pt.focus_score}" cx="${c.x}" cy="${c.y}" r="4.5" fill="#06b6d4" stroke="#0b0f17" stroke-width="1.5" style="cursor:pointer"/>`;
    fSvg += `<text x="${c.x}" y="${c.y - 8}" text-anchor="middle" fill="#67e8f9" font-size="9.5" font-weight="700">${c.pt.focus_score}</text>`;
    if (coords.length <= 8 || idx === 0 || idx === coords.length - 1 || idx % Math.ceil(coords.length / 5) === 0) {
      fSvg += `<text x="${c.x}" y="${H - 5}" text-anchor="middle" fill="#8b9bb4" font-size="9">${c.pt.date.slice(5)}</text>`;
    }
  });
  fSvg += `</svg>`;
  focusEl.innerHTML = fSvg;

  focusEl.querySelectorAll(".focus-dot").forEach((el) => {
    el.addEventListener("mouseenter", (evt) => {
      showTooltip(evt, `<strong>${el.dataset.date}</strong><br/>Focus Score: <b>${el.dataset.score}/10</b>`);
    });
    el.addEventListener("mouseleave", hideTooltip);
  });
}

function renderCourseBars() {
  document.getElementById("course-progress-bars").innerHTML = APP_STATE.courses
    .map((c) => {
      const displayPct = c.progress_pct !== undefined ? c.progress_pct : Math.max(c.pct, c.hours_pct || 0);
      return `
      <div class="cbar-row">
        <div class="cbar-title">
          <span class="swatch" style="background:${c.color}"></span>
          <span>${escapeHtml(c.short)}</span>
          <span class="ects-chip">${c.ects} ECTS</span>
        </div>
        <div class="cbar-track" title="Hours progress: ${c.hours_logged.toFixed(1)}h / ${c.est_hours_total}h (${c.hours_pct || 0}%) • Units completed: ${c.done_units}/${c.total_units} (${c.pct}%)">
          <div class="cbar-fill-hours" style="width:${c.hours_pct || 0}%; background:${c.color}"></div>
          <div class="cbar-fill" style="width:${c.pct}%; background:${c.color}"></div>
        </div>
        <div class="cbar-meta"><b>${displayPct}%</b> • ${c.hours_logged.toFixed(1)}h logged • ${c.done_units}/${c.total_units} units • ${c.est_hours_left.toFixed(1)}h left</div>
      </div>`;
    })
    .join("");
}

/* ---------- Tab 2: Timer & Logger ---------- */

function syncTimerUI() {
  const mode = MODES[timerState.mode];
  const displaySec = mode.stopwatch ? timerState.elapsed : timerState.remaining;
  const formatted = formatMMSS(displaySec);
  document.getElementById("timer-display").textContent = formatted;
  document.getElementById("mini-timer-display").textContent = formatted;
  document.getElementById("mini-timer-toggle").textContent = timerState.running ? "Pause" : "Start";
  document.getElementById("timer-dot").className = timerState.running ? "dot running" : "dot";
  document.getElementById("timer-status-text").textContent = timerState.running
    ? `${mode.label} • Focusing...`
    : `${mode.label} • Paused`;

  const ring = document.getElementById("timer-ring-fg");
  const totalCirc = 603.19;
  if (mode.stopwatch) {
    const modProgress = (timerState.elapsed % 3600) / 3600;
    ring.style.strokeDashoffset = String(totalCirc * (1 - modProgress));
  } else {
    const frac = mode.seconds > 0 ? timerState.remaining / mode.seconds : 0;
    ring.style.strokeDashoffset = String(totalCirc * (1 - frac));
  }
  document.querySelectorAll(".pill-btn").forEach((b) => {
    b.classList.toggle("active", b.dataset.mode === timerState.mode);
  });
}

function startTimer() {
  if (timerState.running) return;
  timerState.running = true;
  timerState.lastTick = Date.now();
  saveTimerState();
  syncTimerUI();
}

function pauseTimer() {
  timerState.running = false;
  timerState.lastTick = null;
  saveTimerState();
  syncTimerUI();
}

function resetTimer(newMode) {
  const m = newMode || timerState.mode;
  timerState = {
    mode: m,
    remaining: MODES[m].seconds,
    elapsed: 0,
    running: false,
    lastTick: null,
  };
  saveTimerState();
  syncTimerUI();
}

setInterval(() => {
  if (!timerState.running) return;
  const now = Date.now();
  const deltaSec = Math.max(1, Math.floor((now - (timerState.lastTick || now)) / 1000));
  timerState.lastTick = now;
  const mode = MODES[timerState.mode];

  if (mode.stopwatch) {
    timerState.elapsed += deltaSec;
  } else {
    timerState.remaining = Math.max(0, timerState.remaining - deltaSec);
    timerState.elapsed += deltaSec;
    if (timerState.remaining === 0) {
      timerState.running = false;
      playChime();
      showToast(`Focus block finished! Click "Copy Elapsed to Logger" to write it to Obsidian.`);
    }
  }
  saveTimerState();
  syncTimerUI();
}, 1000);

function populateLogFormSelectors() {
  const dateInput = document.getElementById("log-date");
  if (!dateInput.value) dateInput.value = APP_STATE.today;

  const courseSel = document.getElementById("log-course");
  const prevCourse = courseSel.value;
  courseSel.innerHTML = APP_STATE.courses
    .map((c) => `<option value="${c.id}">${escapeHtml(c.short)} (${c.ects} ECTS)</option>`)
    .join("");
  if (prevCourse) courseSel.value = prevCourse;

  refreshLogUnitOptions();
}

function refreshLogUnitOptions() {
  const courseId = document.getElementById("log-course").value;
  const unitSel = document.getElementById("log-unit");
  const prev = unitSel.value;
  const filtered = APP_STATE.units.filter((u) => !courseId || u.course_id === courseId);
  unitSel.innerHTML =
    `<option value="">— General Course Study —</option>` +
    filtered
      .map((u) => `<option value="${escapeHtml(u.path)}">${u.completed ? "✅ " : ""}${escapeHtml(u.name)} (${u.unit_type})</option>`)
      .join("");
  if (prev) unitSel.value = prev;
}

function renderRecentSessions() {
  const tbody = document.querySelector("#recent-sessions-table tbody");
  const rows = APP_STATE.sessions || [];
  if (!rows.length) {
    tbody.innerHTML = `<tr><td colspan="7" class="muted">No telemetry sessions logged yet from this app. Log your first session above!</td></tr>`;
    return;
  }
  tbody.innerHTML = rows
    .slice(0, 25)
    .map(
      (s) => `
      <tr>
        <td><code>${escapeHtml(s.date)}</code></td>
        <td>${escapeHtml(s.course_short)}</td>
        <td><b>${Number(s.hours).toFixed(2)}h</b></td>
        <td>${s.focus_score ? `${s.focus_score}/10` : "—"}</td>
        <td>${escapeHtml(s.unit_name || "General")}</td>
        <td>${escapeHtml(s.notes || "")}</td>
        <td><code>${escapeHtml(s.obsidian_file || "")}</code></td>
      </tr>`
    )
    .join("");
}

/* ---------- Tab 3: 270 Units ---------- */

function renderUnitsTable() {
  const courseSel = document.getElementById("unit-filter-course");
  if (courseSel.options.length <= 1) {
    courseSel.innerHTML =
      `<option value="">All Courses (7)</option>` +
      APP_STATE.courses.map((c) => `<option value="${c.id}">${escapeHtml(c.short)}</option>`).join("");
  }

  const q = document.getElementById("unit-search").value.trim().toLowerCase();
  const fCourse = courseSel.value;
  const fType = document.getElementById("unit-filter-type").value;
  const fStatus = document.getElementById("unit-filter-status").value;
  const fPrio = document.getElementById("unit-filter-priority").value;

  const filtered = APP_STATE.units.filter((u) => {
    if (fCourse && u.course_id !== fCourse) return false;
    if (fType && u.unit_type !== fType) return false;
    if (fStatus && u.status !== fStatus) return false;
    if (fPrio && u.priority !== fPrio) return false;
    if (q && !u.name.toLowerCase().includes(q) && !u.path.toLowerCase().includes(q) && !u.course.toLowerCase().includes(q)) return false;
    return true;
  });

  document.getElementById("units-count-label").textContent =
    `Showing ${filtered.length} of ${APP_STATE.units.length} study units (changes write directly to Markdown YAML & Master Checklists)`;

  const tbody = document.querySelector("#units-table tbody");
  tbody.innerHTML = filtered
    .map((u) => {
      const stCls = u.status === "done" ? "st-done" : u.status === "in-progress" ? "st-in-progress" : "st-todo";
      return `
      <tr>
        <td><input type="checkbox" class="unit-check" data-path="${escapeHtml(u.path)}" ${u.completed ? "checked" : ""} /></td>
        <td><span class="muted">${escapeHtml(u.course_short)}</span></td>
        <td><strong>${escapeHtml(u.name)}</strong></td>
        <td><code>${escapeHtml(u.unit_type)}</code></td>
        <td>
          <select class="select-sm unit-status-sel ${stCls}" data-path="${escapeHtml(u.path)}">
            <option value="todo" ${u.status === "todo" ? "selected" : ""}>🔴 todo</option>
            <option value="in-progress" ${u.status === "in-progress" ? "selected" : ""}>🟡 in-progress</option>
            <option value="done" ${u.status === "done" ? "selected" : ""}>🟢 done</option>
          </select>
        </td>
        <td>
          <select class="select-sm unit-prio-sel" data-path="${escapeHtml(u.path)}">
            <option value="high" ${u.priority === "high" ? "selected" : ""}>high</option>
            <option value="medium" ${u.priority === "medium" ? "selected" : ""}>medium</option>
            <option value="low" ${u.priority === "low" ? "selected" : ""}>low</option>
          </select>
        </td>
        <td>${u.est_hours}h</td>
        <td>
          <button class="btn btn-xs btn-secondary unit-open-btn" data-path="${escapeHtml(u.path)}" data-name="${escapeHtml(u.name)}">👁 View / Edit</button>
        </td>
      </tr>`;
    })
    .join("");

  tbody.querySelectorAll(".unit-check").forEach((chk) => {
    chk.addEventListener("change", async () => {
      try {
        await apiPost("/api/unit/update", { path: chk.dataset.path, completed: chk.checked });
        showToast(chk.checked ? "✅ Unit marked completed in Obsidian!" : "Reopened unit in Obsidian");
      } catch (e) {
        showToast(e.message, true);
      }
    });
  });

  tbody.querySelectorAll(".unit-status-sel").forEach((sel) => {
    sel.addEventListener("change", async () => {
      try {
        await apiPost("/api/unit/update", { path: sel.dataset.path, status: sel.value });
        showToast(`Status updated to ${sel.value}`);
      } catch (e) {
        showToast(e.message, true);
      }
    });
  });

  tbody.querySelectorAll(".unit-prio-sel").forEach((sel) => {
    sel.addEventListener("change", async () => {
      try {
        await apiPost("/api/unit/update", { path: sel.dataset.path, priority: sel.value });
        showToast(`Priority set to ${sel.value}`);
      } catch (e) {
        showToast(e.message, true);
      }
    });
  });

  tbody.querySelectorAll(".unit-open-btn").forEach((btn) => {
    btn.addEventListener("click", () => openNoteDrawer(btn.dataset.path, btn.dataset.name));
  });
}

/* ---------- Tab 4: Simulator & Labs ---------- */

function getSavedSimScores() {
  try {
    return JSON.parse(localStorage.getItem("groep_t_ects_sim") || "{}");
  } catch (_) {
    return {};
  }
}

function renderExamSimulatorAndLabs() {
  const scores = getSavedSimScores();
  const simEl = document.getElementById("ects-simulator-list");
  simEl.innerHTML = APP_STATE.courses
    .map((c) => {
      const val = scores[c.id] !== undefined ? scores[c.id] : 12;
      const pass = val >= 10;
      return `
      <div class="sim-row">
        <div>
          <strong>${escapeHtml(c.short)}</strong>
          <div class="muted">Progress: ${c.progress_pct ?? c.pct}% • Logged: ${c.hours_logged}h</div>
        </div>
        <span class="muted">${c.ects} ECTS</span>
        <input type="range" min="0" max="20" step="0.5" value="${val}" class="sim-slider" data-id="${c.id}" />
        <span class="sim-score" style="color:${pass ? "#34d399" : "#fb7185"}">${val}/20</span>
      </div>`;
    })
    .join("");

  const updateEctsBadge = () => {
    const curScores = getSavedSimScores();
    let passedEcts = 0;
    APP_STATE.courses.forEach((c) => {
      const s = curScores[c.id] !== undefined ? curScores[c.id] : 12;
      if (s >= 10) passedEcts += c.ects;
    });
    const pct = ((passedEcts / 30) * 100).toFixed(0);
    const badge = document.getElementById("ects-sim-badge");
    badge.textContent = `${passedEcts} / 30 ECTS (${pct}%) ${passedEcts >= 27 ? "✅ 90%+ GOAL MET" : "⚠️ Below 90%"}`;
    badge.className = passedEcts >= 27 ? "ects-badge" : "ects-badge warn";
  };

  simEl.querySelectorAll(".sim-slider").forEach((slider) => {
    slider.addEventListener("input", () => {
      const cur = getSavedSimScores();
      cur[slider.dataset.id] = parseFloat(slider.value);
      localStorage.setItem("groep_t_ects_sim", JSON.stringify(cur));
      const scoreEl = slider.parentElement.querySelector(".sim-score");
      const pass = parseFloat(slider.value) >= 10;
      scoreEl.textContent = `${slider.value}/20`;
      scoreEl.style.color = pass ? "#34d399" : "#fb7185";
      updateEctsBadge();
    });
  });
  updateEctsBadge();

  // Labs & Mandatory Evals
  const labs = APP_STATE.units.filter((u) => u.unit_type === "labo" || u.unit_type === "permanente-evaluatie");
  document.getElementById("labs-checklist-list").innerHTML = labs
    .map(
      (u) => `
      <div class="lab-item">
        <label class="checkbox-inline">
          <input type="checkbox" class="lab-check" data-path="${escapeHtml(u.path)}" ${u.completed ? "checked" : ""}/>
          <span><strong>${escapeHtml(u.name)}</strong> <span class="muted">(${escapeHtml(u.course_short)})</span></span>
        </label>
        <button class="btn btn-xs btn-ghost lab-open-btn" data-path="${escapeHtml(u.path)}" data-name="${escapeHtml(u.name)}">Open</button>
      </div>`
    )
    .join("");

  document.querySelectorAll(".lab-check").forEach((chk) => {
    chk.addEventListener("change", async () => {
      try {
        await apiPost("/api/unit/update", { path: chk.dataset.path, completed: chk.checked });
        showToast("Lab/Eval updated in Obsidian!");
      } catch (e) {
        showToast(e.message, true);
      }
    });
  });
  document.querySelectorAll(".lab-open-btn").forEach((btn) => {
    btn.addEventListener("click", () => openNoteDrawer(btn.dataset.path, btn.dataset.name));
  });

  // Exam Timeline
  document.getElementById("exam-timeline-cards").innerHTML = APP_STATE.courses
    .map(
      (c) => `
      <div class="exam-card" style="border-top-color:${c.color}">
        <h4>${escapeHtml(c.short)} (${c.ects} ECTS)</h4>
        <div class="muted">${escapeHtml(c.exam_label)} • ${escapeHtml(c.location)}</div>
        <div class="exam-days">${c.days_to_exam} days left</div>
        <div class="muted">Course readiness: <b>${c.pct}%</b> (${c.done_units}/${c.total_units} units)</div>
      </div>`
    )
    .join("");
}

/* ---------- Tab 5: Data Explorer ---------- */

function renderDataExplorer() {
  const f = APP_STATE.files;
  document.getElementById("data-file-paths").innerHTML = [
    `Telemetry JSON: <code>${escapeHtml(f.telemetry_json)}</code>`,
    `Study Logs CSV: <code>${escapeHtml(f.logs_csv)}</code>`,
    `Study Units CSV: <code>${escapeHtml(f.units_csv)}</code>`,
    `Obsidian Snapshot Note: <code>${escapeHtml(f.snapshot_md)}</code>`,
  ]
    .map((html) => `<span class="pill pill-purple">${html}</span>`)
    .join("");

  const tbody = document.querySelector("#daily-logs-table tbody");
  const rows = [...APP_STATE.logs_daily].reverse();
  tbody.innerHTML = rows
    .map(
      (r) => `
      <tr>
        <td><code>${escapeHtml(r.date)}</code></td>
        <td><b>${r.total_hours.toFixed(2)}h</b></td>
        <td>${r.hrs.hrs_cad || 0}</td>
        <td>${r.hrs.hrs_dynamica || 0}</td>
        <td>${r.hrs.hrs_comp_denken || 0}</td>
        <td>${r.hrs.hrs_wiskunde || 0}</td>
        <td>${r.hrs.hrs_chemie || 0}</td>
        <td>${r.hrs.hrs_ethiek || 0}</td>
        <td>${r.hrs.hrs_sgdm || 0}</td>
        <td>${r.focus_score ?? "—"}</td>
        <td><code>${escapeHtml(r.sources.join(", "))}</code></td>
      </tr>`
    )
    .join("");
}

/* ---------- Note Drawer ---------- */

async function openNoteDrawer(relPath, title) {
  CURRENT_DRAWER_PATH = relPath;
  document.getElementById("drawer-title").textContent = title;
  document.getElementById("drawer-path").textContent = relPath;
  document.getElementById("drawer-obsidian-link").href =
    `obsidian://open?vault=${encodeURIComponent(APP_STATE.vault_name)}&file=${encodeURIComponent(relPath.replace(/\.md$/, ""))}`;
  document.getElementById("drawer-content").textContent = "Loading note...";
  document.getElementById("note-drawer").classList.remove("hidden");

  try {
    const res = await fetch(`/api/unit/content?path=${encodeURIComponent(relPath)}`);
    const data = await res.json();
    document.getElementById("drawer-content").textContent = data.content || "";
  } catch (e) {
    document.getElementById("drawer-content").textContent = `Error: ${e.message}`;
  }
}

function closeDrawer() {
  document.getElementById("note-drawer").classList.add("hidden");
  CURRENT_DRAWER_PATH = null;
}

/* ---------- Event Wiring ---------- */

document.querySelectorAll(".tab").forEach((tabBtn) => {
  tabBtn.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach((b) => b.classList.remove("active"));
    document.querySelectorAll(".tab-panel").forEach((p) => p.classList.remove("active"));
    tabBtn.classList.add("active");
    document.getElementById(`tab-${tabBtn.dataset.tab}`).classList.add("active");
  });
});

document.getElementById("btn-refresh").addEventListener("click", async () => {
  await fetchState();
  showToast("Vault reloaded from Obsidian files");
});

document.getElementById("btn-snapshot").addEventListener("click", async () => {
  try {
    const res = await apiPost("/api/obsidian/snapshot", {});
    showToast(`✅ Wrote ${res.snapshot_file} into Obsidian!`);
  } catch (e) {
    showToast(e.message, true);
  }
});

document.getElementById("chart-days-range").addEventListener("change", renderDailyBarChart);
document.getElementById("log-course").addEventListener("change", refreshLogUnitOptions);

document.getElementById("log-session-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  try {
    const res = await apiPost("/api/log/session", {
      date: document.getElementById("log-date").value,
      target: document.getElementById("log-target").value,
      course_id: document.getElementById("log-course").value,
      hours: parseFloat(document.getElementById("log-hours").value),
      unit_path: document.getElementById("log-unit").value,
      focus_score: document.getElementById("log-focus").value,
      pomodoros: parseInt(document.getElementById("log-pomos").value || "0", 10),
      notes: document.getElementById("log-notes").value,
      mark_unit_done: document.getElementById("log-mark-done").checked,
    });
    document.getElementById("log-notes").value = "";
    document.getElementById("log-mark-done").checked = false;
    showToast(`✅ Saved to ${res.obsidian_file} + JSON/CSV!`);
  } catch (err) {
    showToast(err.message, true);
  }
});

// Timer controls
document.getElementById("btn-timer-start").addEventListener("click", startTimer);
document.getElementById("btn-timer-pause").addEventListener("click", pauseTimer);
document.getElementById("btn-timer-reset").addEventListener("click", () => resetTimer());
document.getElementById("mini-timer-toggle").addEventListener("click", () => {
  timerState.running ? pauseTimer() : startTimer();
});
document.querySelectorAll(".pill-btn").forEach((b) => {
  b.addEventListener("click", () => resetTimer(b.dataset.mode));
});
document.getElementById("btn-timer-send-to-log").addEventListener("click", () => {
  const hrs = Math.max(0.25, Math.round((timerState.elapsed / 3600) * 20) / 20);
  document.getElementById("log-hours").value = hrs.toFixed(2);
  showToast(`Copied ${hrs.toFixed(2)}h into session logger!`);
});

// Unit filters
["unit-search", "unit-filter-course", "unit-filter-type", "unit-filter-status", "unit-filter-priority"].forEach((id) => {
  document.getElementById(id).addEventListener("input", renderUnitsTable);
});

// Drawer
document.getElementById("drawer-close").addEventListener("click", closeDrawer);
document.getElementById("drawer-backdrop").addEventListener("click", closeDrawer);
document.getElementById("drawer-append-btn").addEventListener("click", async () => {
  const txt = document.getElementById("drawer-append-input").value.trim();
  if (!txt || !CURRENT_DRAWER_PATH) return;
  try {
    await apiPost("/api/unit/update", { path: CURRENT_DRAWER_PATH, append_note: txt });
    document.getElementById("drawer-append-input").value = "";
    await openNoteDrawer(CURRENT_DRAWER_PATH, document.getElementById("drawer-title").textContent);
    showToast("📝 Appended note directly to Obsidian file!");
  } catch (e) {
    showToast(e.message, true);
  }
});

// Init
syncTimerUI();
fetchState().catch((e) => showToast(e.message, true));
