from model.contact import Contact
from random import randrange


def test_delete_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = db.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts_list = db.get_contacts_list()
    old_contacts_list[0:1] = []
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
               sorted(db.get_contacts_list(), key=Contact.sorting_id_or_maxsize)


def test_delete_random_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = db.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list[index:index+1] = []  # вырезать кусок от index до index+1
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
               sorted(db.get_contacts_list(), key=Contact.sorting_id_or_maxsize)
