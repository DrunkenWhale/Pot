import os
from app.walk import generate, files_map
from app.format import format_print


def run(args):
    if args == 0:
        print("Illegal Path")
        return
    path = os.getcwd() + args[1]
    generate(path)
    format_print()
