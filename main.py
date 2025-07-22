import os
from cli import ClidleCLI
from tutorial import ClidleTutorial, TUTORIAL_FLAG

# Simulation d'un système de fichiers de jeu
fake_files = {
    "money.cl": ""
}

def main():
    if not os.path.exists(TUTORIAL_FLAG):
        tutoriel = ClidleTutorial(fake_files)
        tutoriel.run()

    print("\\n🖥️ Bienvenue dans Clidle. Tapez 'help' pour afficher les commandes.")
    cli = ClidleCLI()
    cli.fake_files = fake_files  # Injecte les fichiers du tutoriel
    cli.run()

if __name__ == "__main__":
    main()