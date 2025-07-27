import os
import time
import importlib

HELP = (
    "Execute a .cl script."\
    "\nExample: run myscript.cl"
)

def run(args, cli):
    if not args:
        print("Usage: run <filename>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    if not os.path.exists(path):
        print(f"File not found: {filename}")
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
                    print(f"❌ Unknown function: {func_name}")
                except Exception as e:
                    print(f"❌ Error in {func_name}: {e}")
            else:
                print(f"⚠️ Ignored line: {line}")

    state = cli.state

    if is_loop:
        print("▶️ Running script (Ctrl+C to stop)")
        try:
            while True:
                execute_instructions()
                print(f"\r💰 Total: {state.balance:.2f}$ (+{state.income_per_call:.2f}$/tick)", end="", flush=True)
                state.save()
                time.sleep(1 / state.power)
        except KeyboardInterrupt:
            print("\n⏹️ Script stopped.")
    else:
        execute_instructions()
        state.save()
        print(f"\n💼 Script executed once. Total: {state.balance:.2f}$")
