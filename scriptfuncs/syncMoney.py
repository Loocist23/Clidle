import importlib

def run(cli, *args):
    try:
        module = importlib.import_module('commands.syncmoney')
        module.run([], cli)
    except Exception as e:
        print(f"❌ Error during syncMoney: {e}")
