import os
import json
from ai_events import trigger_ai_attack

def run(cli, *args):
    state = cli.state
    if state.under_attack:
        return

    state.balance += state.income_per_call
    state.total_money_earned += state.income_per_call

    if state.total_money_earned >= state.next_attack_at:
        trigger_ai_attack(cli)

    if cli.remote_name:
        # VM → home/remote_<name>/save.json
        save_path = os.path.join(cli.home_path, "save.json")
    else:
        # Main machine → home/save.json
        save_path = os.path.join(cli.home_path, "save.json")

    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(cli.state.__dict__, f, indent=2)
    except Exception as e:
        print(f"⚠️ Error saving to {save_path}: {e}")
