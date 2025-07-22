def run(args, cli):
    print("Commandes disponibles :")
    print("  help   → Affiche cette aide")
    print("  ls     → Liste les fichiers disponibles")
    print("  cat    → Affiche le contenu d’un fichier")
    print("  edit   → Permet de modifier un fichier")
    print("  run    → Exécute un script (.cl)")
    print("  exit   → Quitte le jeu")

    if cli.state.total_money_earned >= 5:
        print("  upgrade → Améliore votre PC (débloqué à 5$)")
