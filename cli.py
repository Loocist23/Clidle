import importlib
import os
from game_state import GameState

class ClidleCLI:
    def __init__(self):
        self.running = True
        self.home_path = os.path.join(os.path.dirname(__file__), "home")
        os.makedirs(self.home_path, exist_ok=True)

        self.state = GameState()
        self.state.load()

    def run(self):
        while self.running:
            try:
                user_input = input("> ").strip()
                if not user_input:
                    continue
                cmd, *args = user_input.split()
                self.execute_command(cmd, args)
            except (KeyboardInterrupt, EOFError):
                print("\nDéconnexion...")
                self.running = False

    def execute_command(self, cmd, args):
        try:
            module = importlib.import_module(f"commands.{cmd}")
            module.run(args, self)
        except ModuleNotFoundError:
            print(f"Commande inconnue : '{cmd}' (tapez 'help')")
        except Exception as e:
            print(f"❌ Erreur pendant l'exécution de la commande : {e}")
