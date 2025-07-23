from cli import ClidleCLI
import os
import json
from game_state import GameState

def run(args, cli):
    if "tool_ssh" not in cli.state.inventory:
        print("❌ Vous n'avez pas la commande 'ssh'. Achetez-la dans le shop.")
        return

    if not args:
        print("Utilisation : ssh <nom_de_machine>")
        return

    name = args[0]
    machine = next((m for m in cli.state.machines if m["name"] == name), None)

    if not machine:
        print(f"❌ Machine inconnue : {name}")
        return

    print(f"\nConnexion à {name} ({machine['ip']})... Tapez 'exit' pour revenir.\n")

    # Création d’un sous-shell avec un ClidleCLI virtuel
    session = ClidleCLI()
    session.running = True
    session.state = GameState.from_dict(machine["state"])

    session.home_path = os.path.join(cli.home_path, f"remote_{name}")
    os.makedirs(session.home_path, exist_ok=True)

    # Création d'un script par défaut si manquant
    money_path = os.path.join(session.home_path, "money.cl")
    if not os.path.exists(money_path):
        with open(money_path, "w", encoding="utf-8") as f:
            f.write("# Script par défaut\nwhile True:\n    makeMoney()")
    
    session.remote_name = name
    session.run()

    # MAJ du state en mémoire
    machine["state"] = session.state.__dict__.copy()

    # Sauvegarde dans le fichier de la VM
    save_path = os.path.join(session.home_path, "save.json")
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(machine["state"], f, indent=2)
    except Exception as e:
        print(f"⚠️ Erreur de sauvegarde de la VM {name} : {e}")

    # Sauvegarde globale (inventaire, liste des machines, etc.)
    cli.state.save()

    print(f"🔙 Déconnexion de {name}")
