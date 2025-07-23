def run(args, cli):
    if cli.remote_name:
        print("↩️ Déconnexion de la machine distante.")
        cli.remote_name = None
    else:
        print("Au revoir.")
        cli.running = False
