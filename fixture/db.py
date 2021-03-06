import pymysql.cursors
from model.group import Group
from model.contact import Contact
import allure


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.username = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    @allure.step('Get a group list')
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
            cursor.execute('select id, firstname, lastname, address, email, email2, email3, home, mobile, work from addressbook where deprecated is Null')
            for row in cursor.fetchall():
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work) = row
                all_emails_from_edit_page = '\n'.join([email, email2, email3])
                all_phones_from_edit_page = '\n'.join([home, mobile, work])
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    all_emails_from_edit_page=all_emails_from_edit_page,
                                    all_phones_from_edit_page=all_phones_from_edit_page))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
