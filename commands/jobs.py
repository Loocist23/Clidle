import threading

HELP = (
    "List scripts currently running in the background."\
    "\nExample: jobs"
)


def run(args, cli):
    if "tool_idle" not in cli.state.inventory:
        print("❌ You don't have the 'idle' module. Buy it in the shop.")
        return
    if not cli.background_tasks:
        print("No background scripts.")
        return

    print("ID | Running script")
    for task_id, info in cli.background_tasks.items():
        status = "active" if info["thread"].is_alive() else "finished"
        print(f"  {task_id}  → {info['name']} ({status})")

