HELP = (
    "Quit the game or disconnect from the remote machine."\
    "\nExample: exit"
)

def run(args, cli):
    if cli.remote_name:
        print("↩️ Disconnecting from the remote machine.")
        cli.remote_name = None
    else:
        print("Goodbye.")
        cli.running = False
