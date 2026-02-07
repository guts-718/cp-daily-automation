import subprocess
from git_utils import (
    has_pending_changes,
    get_next_commit_message
)


def _run_git_command(cmd: list[str]) -> bool:
    """
    Runs a git command.
    Returns True if successful, False otherwise.
    """
    result = subprocess.run(
        ["git"] + cmd,
        capture_output=True,
        text=True,
        shell=False
    )
    return result.returncode == 0


def run_auto_commit() -> str:
    """
    Attempts to auto-commit pending changes.

    Returns:
        "AUTO_COMMITTED"
        "NOTHING_TO_COMMIT"
        "ERROR"
    """
    if not has_pending_changes():
        return "NOTHING_TO_COMMIT"

    commit_message = get_next_commit_message()

    if not _run_git_command(["add", "."]):
        return "ERROR"

    if not _run_git_command(["commit", "-m", commit_message]):
        return "ERROR"

    if not _run_git_command(["push", "-u", "origin", "main"]):
        return "ERROR"

    return "AUTO_COMMITTED"


if __name__ == "__main__":
    status = run_auto_commit()
    print(status)
