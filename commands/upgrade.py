UPGRADES = [
    {
        "label": "CPU speed",
        "type": "power",
        "amount": 1,
        "cost": 5.00
    },
    {
        "label": "Code quality",
        "type": "gain",
        "amount": 0.01,
        "cost": 10.00
    }
]

HELP = (
    "Improve your machine's power or earnings."\
    "\nExample: upgrade"
)

def run(args, cli):
    state = cli.get_active_state()

    print("\n🔧 Available upgrades:\n")

    for i, upgrade in enumerate(UPGRADES, start=1):
        desc = ""
        if upgrade["type"] == "power":
            desc = f"+{upgrade['amount']} call/s"
        elif upgrade["type"] == "gain":
            desc = f"+{upgrade['amount']:.2f}$/call"

        print(f"{i}. {upgrade['label']} ({desc}) - {upgrade['cost']:.2f}$")

    print("\nEnter the number of the upgrade to buy (or 'q' to quit): ", end="")
    choice = input().strip().lower()

    if choice == "q":
        print("🔙 Back to the terminal.")
        return

    if not choice.isdigit():
        print("❌ Invalid input.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(UPGRADES):
        print("❌ Invalid number.")
        return

    upgrade = UPGRADES[index]

    if state.balance < upgrade["cost"]:
        print("❌ You don't have enough money!")
        return

    state.balance -= upgrade["cost"]

    if upgrade["type"] == "power":
        state.power += upgrade["amount"]
        print(f"✅ CPU speed increased! New speed: {state.power} call/s")
    elif upgrade["type"] == "gain":
        state.income_per_call += upgrade["amount"]
        print(f"✅ Code quality improved! New gain: {state.income_per_call:.2f}$/call")

    print(f"💸 Remaining money: {state.balance:.2f}$")

    state.save()
