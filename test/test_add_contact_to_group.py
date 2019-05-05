from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, orm, check_ui):
    if len(db.get_groups_list()) == 0:  # если нет хотя бы одной группы, то создать
        app.group.create(Group(name='GroupName_delete_first_group'))
    group = random.choice(db.get_groups_list())
    if len(db.get_contacts_list()) == 0:  # если нет хотя бы одного контакта, то создать
        app.contact.create(Contact(firstname='FirstName_test_add_contact_to_group'))
    old_contacts_list = db.get_contacts_list()
    contact = random.choice(old_contacts_list)
    old_contacts_in_group_list = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group_list = orm.get_contacts_in_group(group)
    if contact not in old_contacts_in_group_list:  # если конт уже был в группе, то не нужно еще раз  добавлять в список
        old_contacts_in_group_list.append(contact)
    new_contacts_in_group_list_from_ui = app.contact.get_contacts_in_group(group)
    assert sorted(new_contacts_in_group_list, key=Contact.sorting_id_or_maxsize) ==\
        sorted(old_contacts_in_group_list, key=Contact.sorting_id_or_maxsize)
    if check_ui:
        # убрать пробелы, потому что в БД лежат записи с пробелами, а в интерфейсе — без них
        def clean(cl_contact):
            return Contact(id=cl_contact.id, firstname=cl_contact.firstname.strip(),
                           lastname=cl_contact.lastname.strip())
        new_contacts_in_group_list = list(map(clean, orm.get_contacts_in_group(group)))

        assert sorted(new_contacts_in_group_list, key=Contact.sorting_id_or_maxsize) ==\
            sorted(new_contacts_in_group_list_from_ui, key=Contact.sorting_id_or_maxsize)
