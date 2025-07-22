import os

def run(args, cli):
    files = os.listdir(cli.home_path)
    for f in files:
        print(f)
