import random

def pick(msgs):
    return random.choice(msgs)


# -------- 7 PM --------

MSG_7PM_PRACTICED = [
    "Good. At least you did one thing worthwhile today.",
    "Bare minimum achieved. Don’t get comfortable.",
    "You showed up. Late, but you showed up.",
    "One problem done. Not impressive, but acceptable.",
    "You weren’t completely useless today. Progress.",
    "Something got solved. Finally.",
    "You did the job. Barely.",
    "Minimal effort detected. Still counts.",
    "At least today isn’t a total write-off.",
    "You practiced. Don’t stop now."
]

MSG_7PM_NOT_PRACTICED = [
    "You act like you’re trying. Your effort says otherwise.",
    "Still nothing? Impressive levels of avoidance.",
    "Another day, another excuse.",
    "Zero problems solved. Predictable.",
    "You had the whole day. You wasted it.",
    "Motivation isn’t missing — discipline is.",
    "If procrastination were a sport, you’d win.",
    "Thinking about coding doesn’t count.",
    "Nothing solved yet. Fix that.",
    "Today is slipping away. Again."
]


# -------- 10 PM --------

MSG_10PM_PRACTICED_AUTO = [
    "You worked today. Auto-commit cleaned the leftovers.",
    "Decent effort. System handled the rest.",
    "At least you left something worth committing.",
    "Work detected. Cleanup done.",
    "You did your part. Automation finished it.",
    "Not bad. Auto-commit wrapped it up.",
    "Progress made. Repository cleaned.",
    "Effort acknowledged. Mess handled.",
    "You weren’t perfect. Neither was the code. Fixed.",
    "Acceptable output. System approved."
]

MSG_10PM_PRACTICED_CLEAN = [
    "You already committed. No cleanup needed.",
    "Repository clean. Rare sight.",
    "You actually finished properly today.",
    "No loose ends. Good.",
    "Nothing to fix. Surprising.",
    "You closed your work. Nice.",
    "Clean repo. That’s how it should be.",
    "Nothing pending. Respectable.",
    "You handled it without help today.",
    "Automation bored. You did fine."
]

MSG_10PM_NOT_PRACTICED_AUTO = [
    "Auto-commit saved you, not your discipline.",
    "System committed something. You didn’t.",
    "Cleanup done. Effort still lacking.",
    "Automation worked harder than you.",
    "At least the bot showed up.",
    "Code committed. Motivation missing.",
    "System carried you today.",
    "Saved by automation. Again.",
    "Commit exists. Pride shouldn’t.",
    "This counts, but barely."
]

MSG_10PM_NOT_PRACTICED_CLEAN = [
    "You did nothing today. No excuses.",
    "Zero progress. Day wasted.",
    "Nothing solved. Nothing committed.",
    "This day goes in the trash.",
    "You showed up for nothing.",
    "No work. No results.",
    "Another empty day.",
    "Discipline skipped today.",
    "Nothing to show for today.",
    "Completely unproductive."
]

MSG_10PM_ERROR = [
    "Automation failed. Even the system is disappointed.",
    "Something broke. Check your setup.",
    "Bot failed. Investigate.",
    "Commit attempt failed. Fix it.",
    "System error. Not a good sign.",
    "Automation stumbled. You should care.",
    "Something went wrong. Look at logs.",
    "Failure detected. Handle it.",
    "Bot is unhappy. Debug required.",
    "Errors today. No excuses."
]
