import os
import sys

files = []

ignore_dir = [".git"]

files_map = {}


def walk(path):
    for node in os.listdir(path):
        children_node = os.path.join(path, node)
        if os.path.isfile(children_node):
            files.append(children_node)
        else:
            if node not in ignore_dir:
                walk(children_node)


if __name__ == '__main__':
    args = sys.argv
    path = os.getcwd() + args[1]
    # path = os.getcwd() + "/.."
    walk(path)
    for filename in files:
        f = open(filename,encoding="utf-8")
        type_name = filename.split(".")[-1]
        if not files_map.__contains__(type_name):
            files_map[type_name] = 0
        files_map[type_name] += len(f.readlines())
        f.close()
    print(files_map)