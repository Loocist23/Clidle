UNLOCK = 100.0
HELP = (
    "Synchronize a VM's money with the main machine."\
    "\nUsage: syncmoney [machine]"\
    "\nRun inside a VM without arguments or from main with the machine name."
)

import os
import json

def run(args, cli):
    if cli.state.total_money_earned < UNLOCK:
        print(f"❌ This command unlocks after earning {UNLOCK}$.")
        return

    if cli.remote_name is None:
        if not args:
            print("Usage: syncmoney <machine>")
            return
        name = args[0]
        machine = next((m for m in cli.state.machines if m["name"] == name), None)
        if not machine:
            print(f"❌ Unknown machine: {name}")
            return
        path = os.path.join(cli.home_path, f"remote_{name}", "save.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                m_state = json.load(f)
        except Exception:
            print(f"❌ Unable to load {name} state.")
            return
        amount = m_state.get("balance", 0.0)
        if amount <= 0:
            print(f"ℹ️ No money to sync from {name}.")
            return
        cli.state.balance += amount
        m_state["balance"] = 0.0
        machine["state"] = m_state
        with open(path, "w", encoding="utf-8") as f:
            json.dump(m_state, f, indent=2)
        cli.state.save()
        print(f"✅ Synced {amount:.2f}$ from {name} to main machine.")
    else:
        name = cli.remote_name
        if args:
            print("Ignoring machine argument inside VM.")
        main_path = os.path.join(os.path.dirname(cli.home_path), "save.json")
        try:
            with open(main_path, "r", encoding="utf-8") as f:
                main_data = json.load(f)
        except Exception:
            print("❌ Unable to load main machine state.")
            return
        amount = cli.state.balance
        if amount <= 0:
            print("ℹ️ No money to sync.")
            return
        main_data["balance"] += amount
        cli.state.balance = 0.0
        with open(main_path, "w", encoding="utf-8") as f:
            json.dump(main_data, f, indent=2)
        cli.state.save(path=os.path.join(cli.home_path, "save.json"))
        print(f"✅ Synced {amount:.2f}$ from {name} to main machine.")
