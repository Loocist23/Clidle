import os
import importlib
import time
import threading


def run(args, cli):
    if not args:
        print("Utilisation : idle <nom_fichier>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    if not os.path.exists(path):
        print(f"Fichier introuvable : {filename}")
        return

    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    lines = [l.strip() for l in code.splitlines() if l.strip()]
    is_loop = any("while True:" in l for l in lines)
    instructions = [l for l in lines if l != "while True:" and not l.startswith("#")]

    def execute_instructions():
        for line in instructions:
            if "(" in line and line.endswith(")"):
                func_name = line.split("(", 1)[0]
                try:
                    module = importlib.import_module(f"scriptfuncs.{func_name}")
                    module.run(cli)
                except ModuleNotFoundError:
                    print(f"❌ Fonction inconnue : {func_name}")
                except Exception as e:
                    print(f"❌ Erreur dans {func_name} : {e}")
            else:
                print(f"⚠️ Ligne ignorée : {line}")

    def loop():
        if is_loop:
            while cli.running:
                execute_instructions()
                cli.state.save()
                time.sleep(1 / cli.state.power)
        else:
            execute_instructions()
            cli.state.save()

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    cli.background_threads.append(thread)
    print(f"🟢 Script {filename} exécuté en arrière-plan.")
