import os
from app.walk import generate, files_map
from app.format import format_print


def run(args):
    if len(args) < 2:
        print("lack argument: path")
        return
    if args[1].startswith(("C:\\", "D:\\", "A:\\", "B:\\", "E:\\", "F:\\", "G:\\", "H:\\")):
        path = args[1]
    else:
        path = os.getcwd() + args[1]
    if os.path.exists(path):
        generate(path)
        format_print()
    else:
        print("illegal path: " + path)
