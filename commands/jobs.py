import threading

HELP = (
    "Liste les scripts en cours d'exécution en arrière-plan."\
    "\nExemple : jobs"
)


def run(args, cli):
    if "tool_idle" not in cli.state.inventory:
        print("❌ Vous n'avez pas le module 'idle'. Achetez-le dans le shop.")
        return
    if not cli.background_tasks:
        print("Aucun script en arrière-plan.")
        return

    print("ID | Script en cours")
    for task_id, info in cli.background_tasks.items():
        status = "actif" if info["thread"].is_alive() else "terminé"
        print(f"  {task_id}  → {info['name']} ({status})")

