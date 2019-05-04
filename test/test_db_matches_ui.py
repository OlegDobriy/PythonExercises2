from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_groups_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())  # убрать лишние пробелы
    db_list = map(clean, db.get_groups_list())
    assert sorted(ui_list, key=Group.sorting_id_or_maxsize) == sorted(db_list, key=Group.sorting_id_or_maxsize)


def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list()

    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, db.get_contacts_list())
    assert sorted(ui_list, key=Contact.sorting_id_or_maxsize) == sorted(db_list, key=Contact.sorting_id_or_maxsize)