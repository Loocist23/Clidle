import os
import importlib
import time
import threading

HELP = (
    "Run a script in the background."\
    "\nExample: idle myscript.cl"
)


def run(args, cli):
    if "tool_idle" not in cli.state.inventory:
        print("❌ You don't have the 'idle' module. Buy it in the shop.")
        return
    if not args:
        print("Usage: idle <filename>")
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

    make_money_count = sum(1 for l in instructions if l.startswith("makeMoney("))
    if make_money_count > 1:
        print("⚠️ makeMoney() is called multiple times, only one execution will be used")
        first_index = next(i for i, l in enumerate(instructions) if l.startswith("makeMoney("))
        # remove further occurrences
        instructions = [instr for i, instr in enumerate(instructions) if not (instr.startswith("makeMoney(") and i != first_index)]

    if make_money_count >= 1 and any(t["has_money"] for t in cli.background_tasks.values()):
        print("❌ A script using makeMoney() is already running in the background")
        return

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

    def loop(stop_event):
        if is_loop:
            while cli.running and not stop_event.is_set():
                execute_instructions()
                cli.state.save()
                time.sleep(1 / cli.state.power)
        else:
            execute_instructions()
            cli.state.save()

    stop_event = threading.Event()
    thread = threading.Thread(target=loop, args=(stop_event,), daemon=True)
    thread.start()
    cli.task_counter += 1
    cli.background_tasks[cli.task_counter] = {
        "thread": thread,
        "stop": stop_event,
        "name": filename,
        "has_money": make_money_count >= 1,
    }
    print(f"🟢 Script {filename} running in background with ID {cli.task_counter}.")
