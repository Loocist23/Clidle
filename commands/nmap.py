HELP = (
    "Scan the local network (if you own the tool)."\
    "\nExample: nmap"
)

def run(args, cli):
    if "tool_nmap" not in cli.state.inventory:
        print("❌ You don't have the 'nmap' command. Buy it in the shop.")
        return

    print("🔎 Scanning network...\n")
    for machine in cli.state.machines:
        if machine["active"]:
            ports = ", ".join(str(p) for p in machine["ports"])
            print(f"- {machine['name']} ({machine['ip']}) : open ports → {ports}")
