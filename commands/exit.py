def run(args, cli):
    if cli.remote_machine:
        print("↩️ Déconnexion de la machine distante.")
        cli.remote_machine = None
    else:
        print("Au revoir.")
        cli.running = False
