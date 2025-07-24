HELP = (
    "Scanne le réseau local (si vous possédez l'outil)."\
    "\nExemple : nmap"
)

def run(args, cli):
    if "tool_nmap" not in cli.state.inventory:
        print("❌ Vous n'avez pas la commande 'nmap'. Achetez-la dans le shop.")
        return

    print("🔎 Scan réseau...\n")
    for machine in cli.state.machines:
        if machine["active"]:
            ports = ", ".join(str(p) for p in machine["ports"])
            print(f"- {machine['name']} ({machine['ip']}) : ports ouverts → {ports}")
