import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.username = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit = True)

    def get_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname from addressbook where deprecated is Null')
            for row in cursor.fetchall():
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

