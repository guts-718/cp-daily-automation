# Scheduler Setup (Windows)

This project uses **Windows Task Scheduler**.
You do **not** need to keep any script running in the background.

## One‑Command Setup (Recommended)

1. Open **PowerShell as Administrator**
2. Allow script execution for this session:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
3. Run:
   ```powershell
   .\setup_scheduler.ps1
   ```

This will:
- Create a **7 PM motivation / roast task**
- Create a **10 PM auto‑commit + summary task**
- Log output to:
  ```
  C:\temp\cp_bot.log
  ```

## Removing the Scheduler

To stop everything:

```powershell
.\kill_scheduler.ps1
```

## Notes

- Tasks are wrapped using `cmd.exe` for maximum Windows reliability
- Python path **must match** the one used to install dependencies
- The scheduler runs scripts **inside your CP repo**, not this repo
