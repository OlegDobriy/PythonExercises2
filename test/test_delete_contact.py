from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    assert len(old_contacts_list) - 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[0:1] = []
    assert old_contacts_list == new_contacts_list


def test_delete_random_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts_list) - 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[index:index+1] = []  # вырезать кусок от index до index+1
    assert old_contacts_list == new_contacts_list
