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

    def load(self):
        if os.path.exists(SAVE_PATH):
            try:
                with open(SAVE_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.balance = data.get("balance", 0.0)
                    self.power = data.get("power", 10)
                    self.income_per_call = data.get("income_per_call", 0.01)
                    self.total_money_earned = data.get("total_money_earned", 0.0)
                    self.inventory = data.get("inventory", [])
                    self.machines = data.get("machines", [])
            except Exception:
                print("⚠️ Erreur de chargement. Valeurs par défaut utilisées.")

    def save(self):
        data = {
            "balance": self.balance,
            "power": self.power,
            "income_per_call": self.income_per_call,
            "total_money_earned": self.total_money_earned,
            "inventory": self.inventory,
            "machines": self.machines
        }
        with open(SAVE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
