
import os
import time

TUTORIAL_FLAG = os.path.join("home", ".tutorial_done")

class ClidleTutorial:
    def __init__(self, fake_files):
        self.fake_files = fake_files

    def run(self):
        print("🎓 Welcome to the Clidle tutorial!")
        print(
            "In this near future, megacorporations and rogue AIs fight a silent "
            "war for control of the networks."
        )
        print(
            "Your secure terminal is your entry point into this world. Let's "
            "start with the basic commands."
        )

        # Step 1: require help
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "help":
                print("✅ Well done! The main commands are: help, ls, cat, edit, run, exit")
                break
            else:
                print("Type the 'help' command to continue.")

        # Step 2: require ls
        print("\nNow try 'ls' to list the files.")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "ls":
                print("money.cl")
                break
            else:
                print("Type the 'ls' command to continue.")

        # Step 3: require cat money.cl
        print("\nGreat! Now type 'cat money.cl' to see its content.")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "cat money.cl":
                print("(The file is currently empty...)")
                break
            else:
                print("Type 'cat money.cl' to continue.")

        # Step 4: require edit money.cl with makeMoney
        print("\nNow edit the file using 'edit money.cl'")
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "edit money.cl":
                print("Enter the file content (finish with an empty line):")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)
                content = "\n".join(lines)
                if "makeMoney()" in content:
                    self.fake_files["money.cl"] = content
                    print("File saved successfully.")
                    print(
                        "These first lines will generate enough credits to catch "
                        "the attention of Clidle's factions."
                    )
                    break
                else:
                    print("⚠️ You must include 'makeMoney()' in the file.")
            else:
                print("Type 'edit money.cl' to continue.")

        # Explanation of the computer power
        print("\n🧠 Your PC can currently call makeMoney() 10 times per second,")
        print("and each call earns you $0.01. You will be able to improve this later.")
        print("Now type 'run money.cl' to launch your script.")

        # Step 5: require run money.cl
        while True:
            cmd = input("> ").strip().lower()
            if cmd == "run money.cl":
                print("▶️ Script started (Ctrl+C to stop).")
                try:
                    while True:
                        print("💰 +0.01$")
                        time.sleep(0.1)
                except KeyboardInterrupt:
                    print("\n⏹️ Script stopped.")
                    break
            else:
                print("Type 'run money.cl' to continue.")

        print(
            "\nYour first profits are modest, but they already open the gates "
            "to Clidle's universe."
        )

        # End of tutorial
        print("\n🎉 Congratulations, you have completed the tutorial!")
        print("The network is waiting for you.")
        choice = input("Would you like to see this tutorial again next launch? (y/n) ").strip().lower()
        if choice == "n":
            with open(TUTORIAL_FLAG, "w") as f:
                f.write("done")
            print("The tutorial will not be shown again.")
        else:
            print("The tutorial will appear again at the next launch.")
