import os
import json

HELP = (
    "Affiche la boutique pour acheter outils et machines."\
    "\nExemple : shop"
)

SHOP_ITEMS = [
    {
        "label": "Machine Linux v1",
        "key": "vm_linux",
        "desc": "Ajoute une machine virtuelle configurée en DHCP.",
        "cost": 25.00
    },
    {
        "label": "Commande nmap",
        "key": "tool_nmap",
        "desc": "Ajoute la commande 'nmap' pour scanner les machines.",
        "cost": 15.00
    },
    {
        "label": "Commande ssh",
        "key": "tool_ssh",
        "desc": "Permet de se connecter à une machine via 'ssh <nom>'.",
        "cost": 10.00
    },
    {
        "label": "Module Idle",
        "key": "tool_idle",
        "desc": "Autorise l'usage d'idle, jobs et stop pour lancer des scripts en arrière-plan.",
        "cost": 50.00,
        "unlock": 200.0
    }
]


def run(args, cli):
    state = cli.state

    print("\n🛍️ Boutique :\n")
    available_items = [
        it for it in SHOP_ITEMS
        if it.get("unlock", 0) <= state.total_money_earned or it["key"] in state.inventory
    ]

    for i, item in enumerate(available_items, start=1):
        owned = "✅" if item["key"] in state.inventory else ""
        print(f"{i}. {item['label']} - {item['cost']:.2f}$ {owned}")
        print(f"   {item['desc']}")

    print("\nTapez le numéro de l'objet à acheter (ou 'q' pour quitter) : ", end="")
    choice = input().strip().lower()

    if choice == "q":
        print("🔙 Retour au terminal.")
        return

    if not choice.isdigit():
        print("❌ Entrée invalide.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(available_items):
        print("❌ Numéro invalide.")
        return

    item = available_items[index]

    if item["key"] in state.inventory and item["key"] != "vm_linux":
        print("📦 Vous possédez déjà cet objet.")
        return

    if state.balance < item["cost"]:
        print("❌ Pas assez d’argent.")
        return

    # Achat validé
    state.balance -= item["cost"]

    if item["key"] == "vm_linux":
        machine_name = input("🖥️ Donnez un nom à la machine : ").strip()
        machine_ip = f"192.168.1.{len(state.machines) + 2}"
        machine_folder = os.path.join(cli.home_path, f"remote_{machine_name}")
        os.makedirs(machine_folder, exist_ok=True)

        # Script par défaut
        script_path = os.path.join(machine_folder, "money.cl")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write("# Script initial de la machine\n")

        # Préparer la config de la machine
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

        # Sauvegarde initiale
        save_path = os.path.join(machine_folder, "save.json")
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(machine_data["state"], f, indent=2)

        # Ajout dans la liste seulement après
        state.machines.append(machine_data)

        print(f"✅ Machine '{machine_name}' ajoutée au réseau (IP : {machine_ip})")
    else:
        state.inventory.append(item["key"])
        print(f"✅ Vous avez acheté : {item['label']} !")
        if item["key"] == "tool_idle":
            print("Les commandes 'idle', 'jobs' et 'stop' sont maintenant disponibles.")

    print(f"💸 Solde restant : {state.balance:.2f}$")
    state.save()
