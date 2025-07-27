import threading

HELP = (
    "Stop a script launched with idle."\
    "\nExample: stop 1"
)


def run(args, cli):
    if "tool_idle" not in cli.state.inventory:
        print("❌ You don't have the 'idle' module. Buy it in the shop.")
        return
    if not args:
        print("Usage: stop <id>")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("Invalid ID")
        return

    task = cli.background_tasks.get(task_id)
    if not task:
        print("No script with this ID")
        return

    task["stop"].set()
    task["thread"].join(timeout=1)
    del cli.background_tasks[task_id]
    print(f"🛑 Script {task_id} stopped")

