import os
from app.config import ignore_dir, lanuage_map
from app.model import TypeDesc

files = []

files_map = {}


def walk(path):
    for node in os.listdir(path):
        children_node = os.path.join(path, node)
        if os.path.isfile(children_node):
            files.append(children_node)
        else:
            if node not in ignore_dir:
                walk(children_node)


def generate(path):
    walk(path)
    for filename in files:
        if filename.__contains__("."):
            type_name = filename.split(".")[-1]
            if lanuage_map.__contains__(type_name):
                f = open(filename, mode="rb")
                content_list = f.readlines()
                line = len(content_list)
                blank = (content_list.count(b'\r\n'))
                if not files_map.__contains__(type_name):
                    files_map[type_name] = TypeDesc(1, lanuage_map[type_name], line, blank)
                else:
                    desc = files_map[type_name]
                    desc.file_number += 1
                    desc.blank += blank
                    desc.line += line
                f.close()
