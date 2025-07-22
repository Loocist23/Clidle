import os
import json

def run(cli, *args):
    cli.state.balance += cli.state.income_per_call
    cli.state.total_money_earned += cli.state.income_per_call

    # Si on est sur une machine distante
    if cli.remote_name:
        # On sauvegarde dans le bon dossier de VM
        save_path = os.path.join(cli.remote_name, "save.json")
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(cli.state.__dict__, f, indent=2)
        except Exception as e:
            print(f"⚠️ Erreur de sauvegarde de la VM {cli.remote_name} : {e}")
    else:
        # Sinon on est sur la machine principale
        cli.state.save()
