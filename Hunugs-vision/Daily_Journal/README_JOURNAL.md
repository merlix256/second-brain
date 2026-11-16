# 📓 Daily Journal Automation

This directory is set up with an automated daily journaling system tailored for Obsidian.

## 📂 Structure

- [`Daily_Journal/`](file:///home/merlix/Documents/Hunugs-vision/Daily_Journal) — Contains all your daily journal entries (`YYYY-MM-DD.md`).
- [`Templates/Daily_Journal_Template.md`](file:///home/merlix/Documents/Hunugs-vision/Templates/Daily_Journal_Template.md) — The master markdown template based on proven journaling methods.
- [`daily_journal.py`](file:///home/merlix/Documents/Hunugs-vision/daily_journal.py) — Python script to automatically generate daily journal pages.

---

## 🧠 The Daily Planner & Journaling Framework

The template is an integrated operating system for your day, combining spiritual grounding, physical performance, task execution, and mindful reflection:

1. **📖 Quranic Verse & Spiritual Tadabbur (آية وتدبر)**:
   - Starts with Bismillah and an inspiring Quranic verse.
   - Dedicated space for the daily Quran reading (Wird), reflection/tadabbur, and daily Adhkar (Morning/Evening).

2. **🌟 Habit Tracker**:
   - **Prayers & Worship:** Fajr, Dhuhr, Asr, Maghrib, Isha, Sunnah/Tahajjud, Quran.
   - **Health & Life Habits:** Hydration tracker (1L, 2L, 3L), Sleep hours & timing, 30+ mins reading/learning, screen discipline, nutrition/fasting.

3. **🏋️‍♂️ Sport & Physical Activity**:
   - Workout modality (Gym/Strength, Running/Cardio, Mobility/Calisthenics, Recovery).
   - Structured exercise log: Movement, Sets x Reps, Weight/Distance, Intensity rating (1-10), and post-workout recovery.

4. **🎯 TaskNotes Plugin & Task Execution**:
   - **Rule of 3 (Top Priorities):** Formatted with `#task` for automatic recognition by the TaskNotes plugin.
   - **Live Agenda Embed:** Embeds `![[TaskNotes/Views/agenda-default.base]]` to view and interact with your scheduled TaskNotes agenda directly inside the daily planner.
   - **Quick Capture:** Rapidly capture tasks using TaskNotes natural language syntax (`#task`, `@context`, `+project`, `📅date`, `!priority`).
   - **Time Blocking:** Structured guide for morning deep work, afternoon implementation, and evening wind-down.

5. **⚡ Interstitial Logging & Fleeting Notes**:
   - Frictionless timestamped capture (`HH:MM`) for meeting takeaways, engineering solutions, and spontaneous ideas.

6. **🌙 Evening Reflection & Muhasabah (المحاسبة والتقييم)**:
   - Gratitude / Shukr (3 items).
   - Daily wins, achievements, and lessons learned / continuous improvement.
   - Check-in metrics: Energy, mental clarity, mood, and overall day score.

---

## 🚀 How to Run the Python Script

### 1. Generate Today's Note Manually
```bash
python3 daily_journal.py
```
*(If today's file already exists, it will **not** overwrite it, preserving your notes).*

### 2. Plan for Tomorrow (Evening Prep)
```bash
python3 daily_journal.py --tomorrow
```

### 3. Generate a Note for a Specific Date
```bash
python3 daily_journal.py --date 2026-11-15
```

### 4. Overwrite / Force Refresh (Caution)
```bash
python3 daily_journal.py --force
```

---

## ⏰ Automatic Daily Scheduling (Cron)

To have Linux create your new journal page automatically every morning at 06:00 AM:

```bash
python3 daily_journal.py --install-cron
```

Or manually add it to your crontab (`crontab -e`):
```cron
0 6 * * * /usr/bin/python3 /home/merlix/Documents/Hunugs-vision/daily_journal.py >> /home/merlix/Documents/Hunugs-vision/.journal_cron.log 2>&1
```

---

## 💎 Obsidian Integration
The Obsidian core plugins have also been configured:
- Daily notes folder: `Daily_Journal`
- Template file: `Templates/Daily_Journal_Template`
- Bidirectional date links: Each note automatically links to `[[Yesterday]]` and `[[Tomorrow]]`.
