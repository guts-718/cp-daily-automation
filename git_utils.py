import subprocess
import re
from datetime import datetime

COMMIT_PATTERN = re.compile(r"day(\d+)\s+commit-(\d+)")

def _run(cmd):
    p = subprocess.run(["git"] + cmd, capture_output=True, text=True)
    return p.stdout.strip(), p.returncode

def has_pending_changes() -> bool:
    out, _ = _run(["status", "--porcelain"])
    return bool(out)

def committed_today() -> bool:
    out, _ = _run(["log", "--since=today 00:00", "--oneline"])
    return bool(out)

def get_last_commit_info():
    msg, _ = _run(["log", "-1", "--pretty=format:%s"])
    if not msg:
        return 0, 0
    m = COMMIT_PATTERN.search(msg)
    if not m:
        return 0, 0
    return int(m.group(1)), int(m.group(2))

def last_commit_was_today() -> bool:
    date_str, _ = _run(["log", "-1", "--pretty=format:%cd", "--date=iso"])
    if not date_str:
        return False
    d = datetime.fromisoformat(date_str).date()
    return d == datetime.now().date()

def get_next_commit_message() -> str:
    day, num = get_last_commit_info()
    if day == 0:
        return "day1 commit-1"
    if last_commit_was_today():
        return f"day{day} commit-{num+1}"
    return f"day{day+1} commit-1"