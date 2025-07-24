import importlib

HELP = (
    "Affiche l'aide générale ou celle d'une commande."\
    "\nExemple : help upgrade"
)


def run(args, cli):
    if args:
        cmd = args[0]
        try:
            module = importlib.import_module(f"commands.{cmd}")
        except ModuleNotFoundError:
            print(f"Commande inconnue : {cmd}")
            return

        doc = getattr(module, "HELP", None)
        if doc:
            print(doc)
        else:
            print(f"Aucune aide disponible pour la commande '{cmd}'.")
        return

    state = cli.state
    inventory = state.inventory

    print("Commandes disponibles :")

    # Commandes de base
    print("  help   → Affiche cette aide")
    print("  ls     → Liste les fichiers disponibles")
    print("  cat    → Affiche le contenu d’un fichier")
    print("  edit   → Permet de modifier un fichier")
    print("  run    → Exécute un script (.cl)")
    if "tool_idle" in inventory:
        print("  idle   → Lance un script en tâche de fond")
        print("  jobs   → Liste les scripts en arrière-plan")
        print("  stop   → Arrête un script lancé avec 'idle'")
    else:
        print("  idle/jobs/stop → Achetez le module Idle dans le shop")
    print("  create → Crée un nouveau script .cl")
    print("  shop   → Ouvre la boutique pour acheter des outils")
    print("  exit   → Quitte le jeu")

    # Commande débloquée par total d'argent
    if state.total_money_earned >= 5:
        print("  upgrade → Améliore votre PC (débloqué à 5$)")

    # Commandes achetées dans le shop
    if "tool_nmap" in inventory:
        print("  nmap   → Scan du réseau local (nécessite achat dans le shop)")

    if "tool_ssh" in inventory:
        print("  ssh    → Connexion à une machine distante (via 'ssh nom')")
