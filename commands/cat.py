import os

# Description utilisée par la commande "help".
HELP = (
    "Affiche le contenu d'un fichier."\
    "\nExemple : cat script.cl"
)

def run(args, cli):
    if not args:
        print("Utilisation : cat <nom_fichier>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                print("(fichier vide)")
            else:
                print(f"📄 {filename}:\n")
                print(content)
    else:
        print(f"❌ Fichier introuvable : {filename}")
