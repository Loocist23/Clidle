import threading

HELP = (
    "Arrête un script lancé avec idle."\
    "\nExemple : stop 1"
)


def run(args, cli):
    if not args:
        print("Utilisation : stop <id>")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("ID invalide")
        return

    task = cli.background_tasks.get(task_id)
    if not task:
        print("Aucun script avec cet ID")
        return

    task["stop"].set()
    task["thread"].join(timeout=1)
    del cli.background_tasks[task_id]
    print(f"🛑 Script {task_id} arrêté")

