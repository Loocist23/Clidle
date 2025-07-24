def run(args, cli):
    state = cli.state
    inventory = state.inventory

    print("Commandes disponibles :")

    # Commandes de base
    print("  help   → Affiche cette aide")
    print("  ls     → Liste les fichiers disponibles")
    print("  cat    → Affiche le contenu d’un fichier")
    print("  edit   → Permet de modifier un fichier")
    print("  run    → Exécute un script (.cl)")
    print("  idle   → Lance un script en tâche de fond")
    print("  jobs   → Liste les scripts en arrière-plan")
    print("  stop   → Arrête un script lancé avec 'idle'")
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
