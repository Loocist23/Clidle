import os
import json

SAVE_PATH = os.path.join(os.path.dirname(__file__), "save.json")


class GameState:

    def __init__(self):
        self.balance = 0.0
        self.power = 10
        self.income_per_call = 0.01
        self.total_money_earned = 0.0
        self.inventory = []
        self.machines = []

    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.balance = data.get("balance", 0.0)
        state.power = data.get("power", 10)
        state.income_per_call = data.get("income_per_call", 0.01)
        state.total_money_earned = data.get("total_money_earned", 0.0)
        state.inventory = data.get("inventory", [])
        state.machines = data.get("machines", [])
        return state

    def load(self, path=SAVE_PATH):
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.__dict__.update(data)
            except Exception as e:
                print(f"⚠️ Erreur de chargement depuis {path} : {e}")
                print("➡️ Valeurs par défaut utilisées.")
        else:
            print(f"ℹ️ Aucun fichier de sauvegarde trouvé à {path}, initialisation par défaut.")

    def save(self, path=SAVE_PATH):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.__dict__, f, indent=2)
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde dans {path} : {e}")
