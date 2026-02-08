# cp-daily-automation

A personal automation tool I built for myself to stay consistent with daily
competitive programming and DSA practice.

This project automatically checks my CP repository, commits unfinished work,
and sends blunt Telegram reminders to keep me accountable.

---

## Important Note

This tool is **not meant for everyone**.

- Messages are **hardcoded**
- Tone is intentionally **harsh and insulting**
- Assumes you practice **competitive programming daily**
- No customization layer as of now

If you don’t solve problems daily, this bot will just roast you every night.

---

##  What it does

- Detects whether you solved problems today (via Git commits)
- Sends **harsh telegram messages** at 7 PM
- Automatically commits & pushes work at 10 PM if you forgot
- Generates structured commit messages like:
  ```
  day27 commit-2 (this is how i have been doing for sometime, so decided to continue with it)
  ```
- Treats Git history as the single source of truth

---

##  How it works (high level)

- **Windows Task Scheduler** triggers scripts
- Scripts are **stateless**
- All decisions are derived from:
  - `git status`
  - `git log`

No databases and no background services. 

---

##  Schedule

| Time | Action |
|----|------|
| 7:00 PM | Motivation / roast based on whether you practiced |
| 10:00 PM | Auto-commit pending work + final summary |

---

##  Telegram Setup (Required)

This project **requires your own Telegram bot**.  
I do **not** provide one, and you should never reuse someone else’s bot token.

### Steps

1. Open Telegram and start **@BotFather**
2. Run:
   ```
   /start
   /newbot
   ```
3. Copy the **Bot Token** it gives you, its a large string like this: **82353123124:AAE7jsxxx**

4. Get your **Chat ID**
   - Open **@userinfobot**
   - Copy the `Id` it sends you, its like a sequence of around 10 digits.

5. Create a `.env` file in the project root, just like `.env.sample`:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   ```

---

## Setup

### 1. Clone repo
```bash
git clone https://github.com/guts-718/cp-daily-automation.git
cd cp-daily-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Test manually
```bash
python daily_check.py --mode=7pm
python daily_check.py --mode=10pm
```

If Telegram insults you, then it’s working.

---

## ⚠️ Warnings

- This tool uses `git add .` (so commit responsibly)
- Assumes `origin/main`
- Requires SSH auth for GitHub
- Will shame you when you slack

---

### Health Check
Run a one-shot validation to confirm everything is wired correctly:
```bash
python daily_check.py --mode=health
```

### Exit Codes
Scripts now return meaningful exit codes:
- 0: success
- 1: configuration error
- 2: dependency error
- 3: git error
- 4: runtime error

### Central Config
A single `config.yaml` documents all paths and schedules used by the system.
Keep `setup_scheduler.ps1` paths in sync with this file.

--- 

##  Why this exists

I built this because:
- I sometimes forget to commit
- I wanted honest accountability
- Gentle reminders don’t work on me

---

## 📌 License

MIT — do whatever you want, but don’t blame me if it hurts your feelings.
