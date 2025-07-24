import importlib
import os
import json
from game_state import GameState


class ClidleCLI:

    def __init__(self):
        self.running = True
        self.remote_name = None
        self.home_path = os.path.join(os.path.dirname(__file__), "home")
        os.makedirs(self.home_path, exist_ok=True)

        # Gestion des scripts lancés en arrière-plan
        self.background_tasks = {}
        self.task_counter = 0

        self.state = GameState()
        self.state_path = os.path.join(self.home_path, "save.json")
        self.state.load(path=self.state_path)

    def run(self):
        while self.running:
            try:
                prompt = f"{self.remote_name or 'main'}> "
                user_input = input(prompt).strip()
                if not user_input:
                    continue
                cmd, *args = user_input.split()
                self.execute_command(cmd, args)

            except KeyboardInterrupt:
                print()
                self.save_before_exit()
                if self.remote_name:
                    print(f"🔌 Interruption — déconnexion de la VM {self.remote_name}...\n")
                else:
                    print("🛑 Interruption du programme principal (Ctrl+C)")
                self.running = False

            except EOFError:
                print()
                self.save_before_exit()
                print("🔚 Déconnexion...")
                self.running = False

        self.save_before_exit()

    def execute_command(self, cmd, args):
        try:
            module = importlib.import_module(f"commands.{cmd}")
            module.run(args, self)
        except ModuleNotFoundError:
            print(f"Commande inconnue : '{cmd}' (tapez 'help')")
        except Exception as e:
            print(f"❌ Erreur pendant l'exécution de la commande : {e}")

    def save_before_exit(self):
        """Sauvegarde l'état courant (VM ou main) avant de quitter"""
        try:
            if self.remote_name:
                save_path = os.path.join(self.home_path, "save.json")
            else:
                save_path = self.state_path
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(self.state.__dict__, f, indent=2)
        except Exception as e:
            print(f"⚠️ Erreur de sauvegarde avant de quitter : {e}")

    def get_active_state(self):
        if self.remote_name is None:
            return self.state
        else:
            machine = next((m for m in self.state.machines if m["name"] == self.remote_name), None)
            if machine:
                return self.load_machine_state(machine["name"])
            else:
                return self.state  # fallback

    def load_machine_state(self, name):
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
