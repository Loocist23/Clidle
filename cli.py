import importlib
import os
from game_state import GameState

class ClidleCLI:
    def __init__(self):
        self.running = True
        self.home_path = os.path.join(os.path.dirname(__file__), "home")
        os.makedirs(self.home_path, exist_ok=True)
        self.remote_machine = None  # None = machine principale
        self.remote_name = None  # None = machine principale

        self.state = GameState()
        self.state.load()

    def run(self):
        while self.running:
            try:
                prompt = f"{self.remote_name or 'main'}> "
                user_input = input(prompt).strip()
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
            
            
    def get_active_state(self):
        if self.remote_machine is None:
            return self.state
        else:
            machine = next((m for m in self.state.machines if m["name"] == self.remote_machine), None)
            if machine:
                return self.load_machine_state(machine["name"])
            else:
                return self.state  # fallback

    def load_machine_state(self, name):
        import json
        path = os.path.join(self.home_path, f"remote_{name}", "save.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                state = GameState()
                state.__dict__.update(data)
                return state
        except Exception:
            print(f"⚠️ Impossible de charger l'état de {name}.")
            return GameState()

