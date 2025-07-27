import importlib

HELP = (
    "Display general help or help for a command."\
    "\nExample: help upgrade"
)


def run(args, cli):
    if args:
        cmd = args[0]
        try:
            module = importlib.import_module(f"commands.{cmd}")
        except ModuleNotFoundError:
            print(f"Unknown command: {cmd}")
            return

        doc = getattr(module, "HELP", None)
        if doc:
            print(doc)
        else:
            print(f"No help available for the command '{cmd}'.")
        return

    state = cli.state
    inventory = state.inventory

    print("Available commands:")

    # Basic commands
    print("  help   → Display this help")
    print("  ls     → List available files")
    print("  cat    → Show file contents")
    print("  edit   → Edit a file")
    print("  run    → Execute a .cl script")
    if "tool_idle" in inventory:
        print("  idle   → Run a script in the background")
        print("  jobs   → List background scripts")
        print("  stop   → Stop a script launched with 'idle'")
    else:
        print("  idle/jobs/stop → Buy the Idle module in the shop")
    print("  create → Create a new .cl script")
    print("  shop   → Open the shop to buy tools")
    print("  exit   → Quit the game")

    # Command unlocked by total money earned
    if state.total_money_earned >= 5:
        print("  upgrade → Upgrade your PC (unlocked at $5)")

    # Commands purchased from the shop
    if "tool_nmap" in inventory:
        print("  nmap   → Scan the local network (requires shop purchase)")

    if "tool_ssh" in inventory:
        print("  ssh    → Connect to a remote machine (via 'ssh name')")
