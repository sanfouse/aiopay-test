import importlib
import importlib.util
from pathlib import Path


def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec=spec)
    spec.loader.exec_module(module)
    return module

BOT_TOKEN = ''
loader = module_from_file('loader', 'C:/Users/gfgfu/Desktop/aiopay-bot/aiopay/loader.py')
