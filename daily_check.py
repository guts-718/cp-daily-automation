import argparse
import os
import sys
import subprocess
import random
from logger import get_log_path
from messages import (
    pick,
    MSG_7PM_PRACTICED,
    MSG_7PM_NOT_PRACTICED,
    MSG_10PM_PRACTICED_AUTO,
    MSG_10PM_PRACTICED_CLEAN,
    MSG_10PM_NOT_PRACTICED_AUTO,
    MSG_10PM_NOT_PRACTICED_CLEAN,
    MSG_10PM_ERROR,
)


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
        send_message(pick(MSG_7PM_PRACTICED))
    else:
        send_message(pick(MSG_7PM_NOT_PRACTICED))


def run_10pm():
    practiced = committed_today()
    result, code = run_auto_commit()

    if result == "ERROR":
        send_message(pick(MSG_10PM_ERROR))
        sys.exit(EXIT_GIT_ERROR)
    elif practiced and result == "AUTO_COMMITTED":
        send_message(pick(MSG_10PM_PRACTICED_AUTO))
    elif practiced and result == "NOTHING_TO_COMMIT":
        send_message(pick(MSG_10PM_PRACTICED_CLEAN))
    elif not practiced and result == "AUTO_COMMITTED":
        send_message(pick(MSG_10PM_NOT_PRACTICED_AUTO))
    else:
        send_message(pick(MSG_10PM_NOT_PRACTICED_CLEAN))


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