class CommandError(Exception):
    def __init__(self, msg=None):
        self.message = msg


class TableError(Exception):
    def __init__(self, msg=None):
        self.message = msg
