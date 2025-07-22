
import os
import time

TUTORIAL_FLAG = ".tutorial_done"

class ClidleTutorial:
    def __init__(self, fake_files):
        self.fake_files = fake_files

    def run(self):
        print("🎓 Bienvenue dans le tutoriel de Clidle !")
        print("Ce tutoriel va vous guider pour bien commencer. Commençons.")

        # Étape 1 : forcer help
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "help":
                print("✅ Bien joué ! Voici les commandes principales : help, ls, cat, edit, run, exit")
                break
            else:
                print("Tapez la commande 'help' pour continuer.")

        # Étape 2 : forcer ls
        print("\nEssayez maintenant 'ls' pour lister les fichiers.")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "ls":
                print("money.cl")
                break
            else:
                print("Tapez la commande 'ls' pour continuer.")

        # Étape 3 : forcer cat money.cl
        print("\nTrès bien ! Tapez maintenant 'cat money.cl' pour voir son contenu.")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "cat money.cl":
                print("(Le fichier est vide pour l'instant...)")
                break
            else:
                print("Tapez 'cat money.cl' pour continuer.")

        # Étape 4 : forcer edit money.cl avec makeMoney
        print("\nMaintenant, modifiez le fichier avec la commande 'edit money.cl'")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "edit money.cl":
                print("Entrez le contenu du fichier (terminez par une ligne vide) :")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)
                content = "\n".join(lines)
                if "makeMoney()" in content:
                    self.fake_files["money.cl"] = content
                    print("Fichier enregistré avec succès.")
                    break
                else:
                    print("⚠️ Vous devez inclure 'makeMoney()' dans le fichier.")
            else:
                print("Tapez 'edit money.cl' pour continuer.")

        # Explication de la puissance du PC
        print("\n🧠 Votre PC est actuellement capable d'appeler makeMoney() 10 fois/seconde,")
        print("et chaque appel vous rapporte 0.01$. Vous pourrez améliorer cela plus tard.")
        print("Maintenant, tapez 'run money.cl' pour lancer votre script.")

        # Étape 5 : forcer run money.cl
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "run money.cl":
                print("▶️ Script lancé (Ctrl+C pour arrêter le script).")
                try:
                    while True:
                        print("💰 +0.01$")
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("\n⏹️ Script stoppé.")
                    break
            else:
                print("Tapez 'run money.cl' pour continuer.")

        # Fin du tutoriel
        print("\n🎉 Bravo, vous avez terminé le tutoriel !")
        choice = input("Souhaitez-vous revoir ce tutoriel au prochain lancement ? (o/n) ").strip().lower()
        if choice == "n":
            with open(TUTORIAL_FLAG, "w") as f:
                f.write("done")
            print("Le tutoriel ne sera plus affiché.")
        else:
            print("Le tutoriel sera affiché à nouveau au prochain lancement.")
