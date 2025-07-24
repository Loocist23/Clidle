import threading


def run(args, cli):
    if not cli.background_tasks:
        print("Aucun script en arrière-plan.")
        return

    print("ID | Script en cours")
    for task_id, info in cli.background_tasks.items():
        status = "actif" if info["thread"].is_alive() else "terminé"
        print(f"  {task_id}  → {info['name']} ({status})")

