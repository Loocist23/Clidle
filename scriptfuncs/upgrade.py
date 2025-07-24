import os
import json

UPGRADES = [
    {
        "type": "power",
        "amount": 1,
        "cost": 5.00
    },
    {
        "type": "gain",
        "amount": 0.01,
        "cost": 10.00
    }
]

def run(cli, *args):
    """Achète automatiquement les améliorations si les fonds sont suffisants."""
    purchased = False
    for upgrade in UPGRADES:
        if cli.state.balance >= upgrade["cost"]:
            cli.state.balance -= upgrade["cost"]
            if upgrade["type"] == "power":
                cli.state.power += upgrade["amount"]
            elif upgrade["type"] == "gain":
                cli.state.income_per_call += upgrade["amount"]
            purchased = True
    if purchased:
        save_path = os.path.join(cli.home_path, "save.json")
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(cli.state.__dict__, f, indent=2)
        except Exception as e:
            print(f"⚠️ Erreur de sauvegarde dans {save_path} : {e}")
