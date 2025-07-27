import os

HELP = (
    "Edit a file line by line."\
    "\nExample: edit myscript.cl"
)

def run(args, cli):
    if not args:
        print("Usage: edit <filename>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    existing = ""
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            existing = f.read()

    print("(Simple editor — finish with an empty line)")
    if existing:
        print(existing)

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            break
        lines.append(line)

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"{filename} saved.")
