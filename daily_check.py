import argparse

from git_utils import committed_today
from auto_commit import run_auto_commit
from telegram import send_message


def run_7pm_check():
    if committed_today():
        send_message(
            "Good. At least you did one thing worthwhile today — even if you wasted most of it."
        )
    else:
        send_message(
            "You act like you’re trying. Your effort so far says otherwise."
        )


def run_10pm_check():
    practiced_today = committed_today()
    auto_commit_result = run_auto_commit()

    if auto_commit_result == "ERROR":
        send_message(
            "Automation failed. Even the system is disappointed — check your repo or network."
        )
        return

    if practiced_today and auto_commit_result == "AUTO_COMMITTED":
        send_message(
            "You did some work today. Bare minimum achieved — auto-commit cleaned up the mess."
        )
    elif practiced_today and auto_commit_result == "NOTHING_TO_COMMIT":
        send_message(
            "Fine. You already committed today. Not impressive, but acceptable."
        )
    elif not practiced_today and auto_commit_result == "AUTO_COMMITTED":
        send_message(
            "Auto-commit saved you, not your discipline. Try actually solving a problem tomorrow."
        )
    else:
        send_message(
            "You did nothing today. No problems solved. No excuses."
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["7pm", "10pm"],
        required=True
    )
    args = parser.parse_args()

    if args.mode == "7pm":
        run_7pm_check()
    else:
        run_10pm_check()


if __name__ == "__main__":
    main()
