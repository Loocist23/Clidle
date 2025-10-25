import os
from cli import ClidleCLI
from tutorial import ClidleTutorial, TUTORIAL_FLAG

BANNER = r"""
 _______  _       _________ ______   _        _______ 
(  ____ \( \      \__   __/(  __  \ ( \      (  ____ \
| (    \/| (         ) (   | (  \  )| (      | (    \/
| |      | |         | |   | |   ) || |      | (__    
| |      | |         | |   | |   | || |      |  __)   
| |      | |         | |   | |   ) || |      | (      
| (____/\| (____/\___) (___| (__/  )| (____/\| (____/\
(_______/(_______/\_______/(______/ (_______/(_______/
"""

# Simulated game file system
fake_files = {
    "money.cl": ""
}
os.makedirs("home", exist_ok=True)

def main():
    if not os.path.exists(TUTORIAL_FLAG):
        tutorial = ClidleTutorial(fake_files)
        tutorial.run()

    print(BANNER)
    print("🖥️ Welcome to Clidle. Type 'help' to show the commands.")
    cli = ClidleCLI()
    cli.fake_files = fake_files  # Inject tutorial files
    cli.run()

if __name__ == "__main__":
    main()
