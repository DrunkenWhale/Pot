class Desc(object):
    def __init__(self, tpe, line, blank):
        self.blank = blank
        self.line = line
        self.tpe = tpe


class TypeDesc(Desc):
    def __init__(self, file_number, tpe, line, blank):
        super().__init__(tpe, line, blank)
        self.file_number = file_number
