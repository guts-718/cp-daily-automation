# ============================
# CP Daily Automation Scheduler Setup
# ============================

# EDIT THESE PATHS BEFORE RUNNING (keep in sync with config.yaml)
$PythonExe = "C:\Users\rahul\AppData\Local\Programs\Python\Python311\python.exe"
$AutomationRepo = "C:\dev\cp_daily_automationr"
$TargetRepo = "C:\dev\cf"

$Task7PMName  = "CP Daily Roast (7pm)"
$Task10PMName = "CP Auto Commit & Verdict (10pm)"

New-Item -ItemType Directory -Force -Path "C:\temp" | Out-Null

$Action7PM = New-ScheduledTaskAction `
  -Execute "C:\Windows\System32\cmd.exe" `
  -Argument "/c `"$PythonExe `"$AutomationRepo\daily_check.py`" --mode=7pm > C:\temp\cp_bot.log 2>&1`"" `
  -WorkingDirectory $TargetRepo

$Action10PM = New-ScheduledTaskAction `
  -Execute "C:\Windows\System32\cmd.exe" `
  -Argument "/c `"$PythonExe `"$AutomationRepo\daily_check.py`" --mode=10pm > C:\temp\cp_bot.log 2>&1`"" `
  -WorkingDirectory $TargetRepo

$Trigger7PM  = New-ScheduledTaskTrigger -Daily -At 7pm
$Trigger10PM = New-ScheduledTaskTrigger -Daily -At 10pm

$Settings = New-ScheduledTaskSettingsSet `
  -AllowStartIfOnBatteries `
  -DontStopIfGoingOnBatteries `
  -StartWhenAvailable `
  -ExecutionTimeLimit (New-TimeSpan -Minutes 5)

Register-ScheduledTask -TaskName $Task7PMName -Action $Action7PM -Trigger $Trigger7PM -Settings $Settings -Force
Register-ScheduledTask -TaskName $Task10PMName -Action $Action10PM -Trigger $Trigger10PM -Settings $Settings -Force

Write-Host "✅ CP Daily Automation scheduled successfully."