import os

HELP = (
    "Crée un nouveau script .cl."\
    "\nExemple : create monscript.cl"
)


def run(args, cli):
    if not args:
        print("Utilisation : create <nom_script.cl>")
        return

    filename = args[0]
    if not filename.endswith('.cl'):
        print("❌ Seuls les scripts .cl peuvent être créés")
        return

    path = os.path.join(cli.home_path, filename)
    if os.path.exists(path):
        print(f"⚠️ Le fichier {filename} existe déjà")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write('# Nouveau script Clidle\n')

    print(f"📄 Fichier {filename} créé")
