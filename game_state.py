import os
import json

# By default all saves are stored in the ``home`` folder at the project root.
# This avoids accidentally creating another ``save.json`` at the repository root.
SAVE_PATH = os.path.join(os.path.dirname(__file__), "home", "save.json")


class GameState:

    def __init__(self):
        self.balance = 0.0
        self.power = 10
        self.income_per_call = 0.01
        self.total_money_earned = 0.0
        self.inventory = []
        self.machines = []
        # AI attack system
        self.under_attack = False
        self.attack_level = 0
        self.next_attack_at = 50.0

    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.balance = data.get("balance", 0.0)
        state.power = data.get("power", 10)
        state.income_per_call = data.get("income_per_call", 0.01)
        state.total_money_earned = data.get("total_money_earned", 0.0)
        state.inventory = data.get("inventory", [])
        state.machines = data.get("machines", [])
        state.under_attack = data.get("under_attack", False)
        state.attack_level = data.get("attack_level", 0)
        state.next_attack_at = data.get("next_attack_at", 50.0)
        return state

    def load(self, path=SAVE_PATH):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.__dict__.update(data)
            except Exception as e:
                print(f"⚠️ Error loading from {path}: {e}")
                print("➡️ Default values used.")
        else:
            print(f"ℹ️ No save file found at {path}, using defaults.")

    def save(self, path=SAVE_PATH):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.__dict__, f, indent=2)
        except Exception as e:
            print(f"❌ Error while saving to {path}: {e}")
