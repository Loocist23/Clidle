UPGRADES = [
    {
        "label": "Vitesse CPU",
        "type": "power",
        "amount": 1,
        "cost": 5.00
    },
    {
        "label": "Qualité du code",
        "type": "gain",
        "amount": 0.01,
        "cost": 10.00
    }
]

def run(args, cli):
    state = cli.get_active_state()

    print("\n🔧 Améliorations disponibles :\n")

    for i, upgrade in enumerate(UPGRADES, start=1):
        desc = ""
        if upgrade["type"] == "power":
            desc = f"+{upgrade['amount']} appel/s"
        elif upgrade["type"] == "gain":
            desc = f"+{upgrade['amount']:.2f}$/appel"

        print(f"{i}. {upgrade['label']} ({desc}) - {upgrade['cost']:.2f}$")

    print("\nTapez le numéro de l’amélioration à acheter (ou 'q' pour quitter) : ", end="")
    choice = input().strip().lower()

    if choice == "q":
        print("🔙 Retour au terminal.")
        return

    if not choice.isdigit():
        print("❌ Entrée invalide.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(UPGRADES):
        print("❌ Numéro invalide.")
        return

    upgrade = UPGRADES[index]

    if state.balance < upgrade["cost"]:
        print("❌ Vous n’avez pas assez d’argent !")
        return

    state.balance -= upgrade["cost"]

    if upgrade["type"] == "power":
        state.power += upgrade["amount"]
        print(f"✅ Vitesse CPU améliorée ! Nouvelle vitesse : {state.power} appel/s")
    elif upgrade["type"] == "gain":
        state.income_per_call += upgrade["amount"]
        print(f"✅ Qualité du code améliorée ! Nouveau gain : {state.income_per_call:.2f}$/appel")

    print(f"💸 Argent restant : {state.balance:.2f}$")

    state.save()
