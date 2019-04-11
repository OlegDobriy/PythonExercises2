class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):  # если задать '', то поле будет очищаться
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id
