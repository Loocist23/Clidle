import random
import time
from ai_events import WORDS

HELP = (
    "Defend against an ongoing AI attack."\
    "\nType the displayed words fast enough to regain control."
)


def run(args, cli):
    state = cli.state
    if not state.under_attack:
        print("No AI attack detected.")
        return

    level = state.attack_level
    word_count = 3 + level
    time_limit = max(1.5, 5 - level)
    print(f"Type {word_count} words within {time_limit} seconds each:")

    for _ in range(word_count):
        word = random.choice(WORDS)
        start = time.time()
        typed = input(f"{word}> ").strip()
        duration = time.time() - start
        if typed != word or duration > time_limit:
            print("❌ Defense failed!")
            return

    print("✅ Attack repelled! Money production restored.")
    state.under_attack = False
    state.attack_level += 1
    state.next_attack_at *= 2
    state.save()
