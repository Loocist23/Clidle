import os
import json

HELP = (
    "Display the shop to buy tools and machines."\
    "\nExample: shop"
)

SHOP_ITEMS = [
    {
        "label": "Linux machine v1",
        "key": "vm_linux",
        "desc": "Adds a virtual machine configured with DHCP.",
        "cost": 25.00
    },
    {
        "label": "nmap command",
        "key": "tool_nmap",
        "desc": "Adds the 'nmap' command to scan machines.",
        "cost": 15.00
    },
    {
        "label": "ssh command",
        "key": "tool_ssh",
        "desc": "Allows connecting to a machine via 'ssh <name>'.",
        "cost": 10.00
    },
    {
        "label": "Idle module",
        "key": "tool_idle",
        "desc": "Allows using idle, jobs and stop to run scripts in the background.",
        "cost": 50.00,
        "unlock": 200.0
    }
]


def run(args, cli):
    state = cli.state

    print("\n🛍️ Shop:\n")
    available_items = [
        it for it in SHOP_ITEMS
        if it.get("unlock", 0) <= state.total_money_earned or it["key"] in state.inventory
    ]

    for i, item in enumerate(available_items, start=1):
        owned = "✅" if item["key"] in state.inventory else ""
        print(f"{i}. {item['label']} - {item['cost']:.2f}$ {owned}")
        print(f"   {item['desc']}")

    print("\nEnter the number of the item to buy (or 'q' to quit): ", end="")
    choice = input().strip().lower()

    if choice == "q":
        print("🔙 Back to the terminal.")
        return

    if not choice.isdigit():
        print("❌ Invalid input.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(available_items):
        print("❌ Invalid number.")
        return

    item = available_items[index]

    if item["key"] in state.inventory and item["key"] != "vm_linux":
        print("📦 You already own this item.")
        return

    if state.balance < item["cost"]:
        print("❌ Not enough money.")
        return

    # Purchase confirmed
    state.balance -= item["cost"]

    if item["key"] == "vm_linux":
        machine_name = input("🖥️ Give a name to the machine: ").strip()
        machine_ip = f"192.168.1.{len(state.machines) + 2}"
        machine_folder = os.path.join(cli.home_path, f"remote_{machine_name}")
        os.makedirs(machine_folder, exist_ok=True)

        # Default script
        script_path = os.path.join(machine_folder, "money.cl")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write("# Initial machine script\n")

        # Prepare the machine configuration
        machine_data = {
            "name": machine_name,
            "ip": machine_ip,
            "ports": [22],
            "active": True,
            "state": {
                "balance": 0.0,
                "power": 10,
                "income_per_call": 0.01,
                "total_money_earned": 0.0,
                "inventory": [],
                "machines": []
            },
            "scripts": []
        }

        # Initial save
        save_path = os.path.join(machine_folder, "save.json")
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(machine_data["state"], f, indent=2)

        # Add to the list only afterwards
        state.machines.append(machine_data)

        print(f"✅ Machine '{machine_name}' added to the network (IP: {machine_ip})")
    else:
        state.inventory.append(item["key"])
        print(f"✅ You purchased: {item['label']}!")
        if item["key"] == "tool_idle":
            print("The commands 'idle', 'jobs' and 'stop' are now available.")

    print(f"💸 Remaining balance: {state.balance:.2f}$")
    state.save()
