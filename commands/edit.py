import os

def run(args, cli):
    if not args:
        print("Utilisation : edit <nom_fichier>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    print("Entrez le contenu du fichier (terminez par une ligne vide) :")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"{filename} modifié.")
