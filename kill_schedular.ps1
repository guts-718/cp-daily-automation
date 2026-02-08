# CP Daily Automation Scheduler Teardown

$Task7PMName  = "CP Daily Roast (7pm)"
$Task10PMName = "CP Auto Commit & Verdict (10pm)"

Unregister-ScheduledTask -TaskName $Task7PMName -Confirm:$false -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $Task10PMName -Confirm:$false -ErrorAction SilentlyContinue

Write-Host "🗑️ CP Daily Automation scheduled tasks removed."