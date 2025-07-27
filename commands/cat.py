import os

# Description used by the "help" command.
HELP = (
    "Display the contents of a file."\
    "\nExample: cat script.cl"
)

def run(args, cli):
    if not args:
        print("Usage: cat <filename>")
        return

    filename = args[0]
    path = os.path.join(cli.home_path, filename)

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                print("(empty file)")
            else:
                print(f"📄 {filename}:\n")
                print(content)
    else:
        print(f"❌ File not found: {filename}")
