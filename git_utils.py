import subprocess
import re
from datetime import datetime


COMMIT_PATTERN = re.compile(r"day(\d+)\s+commit-(\d+)")


def _run_git_command(cmd: list[str]) -> str:
    """Run a git command and return stdout as string."""
    result = subprocess.run(
        ["git"] + cmd,
        capture_output=True,
        text=True,
        shell=False
    )
    return result.stdout.strip()


def has_pending_changes() -> bool:
    """
    Returns True if there are untracked or modified files.
    """
    output = _run_git_command(["status", "--porcelain"])
    return bool(output)


def committed_today() -> bool:
    """
    Returns True if at least one commit exists today
    (manual or automated).
    """
    output = _run_git_command(
        ["log", "--since=today 00:00", "--oneline"]
    )
    return bool(output)


def get_last_commit_info() -> tuple[int, int]:
    """
    Returns (day_number, commit_number) from last commit message.

    If parsing fails or repo has no commits, returns (0, 0).
    """
    message = _run_git_command(
        ["log", "-1", "--pretty=format:%s"]
    )

    if not message:
        return 0, 0

    match = COMMIT_PATTERN.search(message)
    if not match:
        return 0, 0

    day = int(match.group(1))
    commit = int(match.group(2))
    return day, commit


def last_commit_was_today() -> bool:
    """
    Returns True if the most recent commit was made today.
    """
    date_str = _run_git_command(
        ["log", "-1", "--pretty=format:%cd", "--date=iso"]
    )

    if not date_str:
        return False

    last_commit_date = datetime.fromisoformat(date_str).date()
    return last_commit_date == datetime.now().date()


def get_next_commit_message() -> str:
    """
    Generates the next commit message in the format:
    dayX commit-Y
    """
    last_day, last_commit = get_last_commit_info()

    if last_day == 0:
        # First commit or unparsable history
        return "day1 commit-1"

    if last_commit_was_today():
        return f"day{last_day} commit-{last_commit + 1}"

    return f"day{last_day + 1} commit-1"
