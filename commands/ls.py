import os

HELP = (
    "List the files in the current folder."\
    "\nExample: ls"
)

IGNORE_LIST = [
    "save.json",
    # Add other files or folders to ignore here
]

def run(args, cli):
    files = os.listdir(cli.home_path)
    for f in files:
        if f in IGNORE_LIST:
            continue
        if not (os.path.isdir(os.path.join(cli.home_path, f)) and f.startswith("remote_")):
            print(f)
