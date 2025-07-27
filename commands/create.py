import os

HELP = (
    "Create a new .cl script."\
    "\nExample: create myscript.cl"
)


def run(args, cli):
    if not args:
        print("Usage: create <script_name.cl>")
        return

    filename = args[0]
    if not filename.endswith('.cl'):
        print("❌ Only .cl scripts can be created")
        return

    path = os.path.join(cli.home_path, filename)
    if os.path.exists(path):
        print(f"⚠️ File {filename} already exists")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write('# New Clidle script\n')

    print(f"📄 File {filename} created")
