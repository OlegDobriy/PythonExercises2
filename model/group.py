from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):  # если задать '', то поле будет очищаться
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return '{%s:%s}' % (self.id, self.name)

    def __eq__(self, other):  # сравнивать по id и name, а не по расположению в памяти
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def sorting_id_or_maxsize(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
