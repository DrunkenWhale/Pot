from app.walk import files_map

string_format = "| %-20s | %20s | %20s | %20s | %20s |"

line_sep = "=" * 116


def format_print():
    desc_list = list(files_map.values())
    desc_list.sort(key=lambda x: x.line)
    print(line_sep)
    print(string_format % ("Type", "File", "Line", "Blank", "Code"))
    print(line_sep)
    file_number = 0
    line = 0
    blank = 0
    for desc in desc_list:
        print(string_format % (desc.tpe, desc.file_number, desc.line - desc.blank, desc.blank, desc.line))
        file_number += desc.file_number
        line += desc.line
        blank += desc.blank
    print(line_sep)
    print(string_format % ("Sum", file_number, line - blank, blank, line))
    print(line_sep)
