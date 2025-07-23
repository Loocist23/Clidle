import os
import json

def run(cli, *args):
    cli.state.balance += cli.state.income_per_call
    cli.state.total_money_earned += cli.state.income_per_call

    if cli.remote_name:
        # VM → home/remote_<nom>/save.json
        save_path = os.path.join(cli.home_path, "save.json")
    else:
        # Machine principale → home/save.json
        save_path = os.path.join(cli.home_path, "save.json")

    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(cli.state.__dict__, f, indent=2)
    except Exception as e:
        print(f"⚠️ Erreur de sauvegarde dans {save_path} : {e}")
