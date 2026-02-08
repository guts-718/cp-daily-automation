import argparse
import os
import sys
import subprocess

from git_utils import committed_today
from auto_commit import run_auto_commit
from telegram import send_message

EXIT_OK = 0
EXIT_CONFIG_ERROR = 1
EXIT_DEP_ERROR = 2
EXIT_GIT_ERROR = 3
EXIT_RUNTIME_ERROR = 4

def _check_git_repo():
    p = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
    return p.returncode == 0

def _check_deps():
    try:
        import requests  # noqa
        import dotenv    # noqa
        return True
    except Exception:
        return False

def _check_log_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
        test = os.path.join(path, "_write_test.tmp")
        with open(test, "w") as f:
            f.write("ok")
        os.remove(test)
        return True
    except Exception:
        return False

def run_health():
    ok = True

    if not _check_git_repo():
        print("[FAIL] Not inside a git repository")
        ok = False
    else:
        print("[OK] Git repository detected")

    if not _check_deps():
        print("[FAIL] Dependencies missing (requests / python-dotenv)")
        ok = False
    else:
        print("[OK] Dependencies installed")

    log_dir = os.getenv("CP_LOG_DIR", "C:\\temp")
    if not _check_log_dir(log_dir):
        print(f"[FAIL] Log directory not writable: {log_dir}")
        ok = False
    else:
        print(f"[OK] Log directory writable: {log_dir}")

    if ok:
        print("STATUS: READY")
        sys.exit(EXIT_OK)
    else:
        print("STATUS: BROKEN")
        sys.exit(EXIT_CONFIG_ERROR)

def run_7pm():
    if committed_today():
        send_message("Good. At least you did one thing worthwhile today — even if you wasted most of it.")
    else:
        send_message("You act like you’re trying. Your effort so far says otherwise.")

def run_10pm():
    practiced = committed_today()
    result, code = run_auto_commit()

    if result == "ERROR":
        send_message("Automation failed. Even the system is disappointed — check your repo or network.")
        sys.exit(EXIT_GIT_ERROR)

    if practiced and result == "AUTO_COMMITTED":
        send_message("You did some work today. Bare minimum achieved — auto-commit cleaned up the mess.")
    elif practiced and result == "NOTHING_TO_COMMIT":
        send_message("Fine. You already committed today. Not impressive, but acceptable.")
    elif not practiced and result == "AUTO_COMMITTED":
        send_message("Auto-commit saved you, not your discipline. Try actually solving a problem tomorrow.")
    else:
        send_message("You did nothing today. No problems solved. No excuses.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["7pm", "10pm", "health"], required=True)
    args = ap.parse_args()

    if args.mode == "health":
        run_health()
    elif args.mode == "7pm":
        run_7pm()
    else:
        run_10pm()

if __name__ == "__main__":
    try:
        main()
        sys.exit(EXIT_OK)
    except SystemExit:
        raise
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(EXIT_RUNTIME_ERROR)