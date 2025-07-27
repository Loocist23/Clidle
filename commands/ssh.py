from cli import ClidleCLI
import os
import json
from game_state import GameState

HELP = (
    "Connect to a remote machine via SSH."\
    "\nExample: ssh my_vm"
)

def run(args, cli):
    if "tool_ssh" not in cli.state.inventory:
        print("❌ You don't have the 'ssh' command. Buy it in the shop.")
        return

    if not args:
        print("Usage: ssh <machine_name>")
        return

    name = args[0]
    machine = next((m for m in cli.state.machines if m["name"] == name), None)

    if not machine:
        print(f"❌ Unknown machine: {name}")
        return

    print(f"\nConnecting to {name} ({machine['ip']})... Type 'exit' to return.\n")

    # Create a subshell with a virtual ClidleCLI
    session = ClidleCLI()
    session.running = True
    session.state = GameState.from_dict(machine["state"])

    session.home_path = os.path.join(cli.home_path, f"remote_{name}")
    os.makedirs(session.home_path, exist_ok=True)

    # Create a default script if missing
    money_path = os.path.join(session.home_path, "money.cl")
    if not os.path.exists(money_path):
        with open(money_path, "w", encoding="utf-8") as f:
            f.write("# Default script\nwhile True:\n    makeMoney()")
    
    session.remote_name = name

    session.run()

    # Reload main state in case the VM modified it (e.g., syncmoney)
    cli.state.load(path=cli.state_path)

    # Update the state in memory
    machine["state"] = session.state.__dict__.copy()

    # Save to the VM file
    save_path = os.path.join(session.home_path, "save.json")
    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(machine["state"], f, indent=2)
    except Exception as e:
        print(f"⚠️ Error saving VM {name}: {e}")

    # Global save (inventory, machine list, etc.)
    cli.state.save()

    print(f"🔙 Disconnected from {name}")
