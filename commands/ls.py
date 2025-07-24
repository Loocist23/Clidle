import os

IGNORE_LIST = [
    "save.json",
    # Ajoute ici d'autres fichiers ou dossiers à ignorer
]

def run(args, cli):
    files = os.listdir(cli.home_path)
    for f in files:
        if f in IGNORE_LIST:
            continue
        if not (os.path.isdir(os.path.join(cli.home_path, f)) and f.startswith("remote_")):
            print(f)
