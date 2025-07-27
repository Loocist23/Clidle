import os
from cli import ClidleCLI
from tutorial import ClidleTutorial, TUTORIAL_FLAG

# Simulated game file system
fake_files = {
    "money.cl": ""
}

def main():
    if not os.path.exists(TUTORIAL_FLAG):
        tutorial = ClidleTutorial(fake_files)
        tutorial.run()

    print("🖥️ Welcome to Clidle. Type 'help' to show the commands.")
    cli = ClidleCLI()
    cli.fake_files = fake_files  # Inject tutorial files
    cli.run()

if __name__ == "__main__":
    main()