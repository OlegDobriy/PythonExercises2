from model.contact import Contact
from random import randrange


def test_modify_first_contact_firstname(app):
    new_contact = Contact(firstname='firstname_MODIFIED')
    if app.contact.count() == 0:
        app.contact.create(new_contact)
    old_contacts_list = app.contact.get_contacts_list()
    new_contact.id = old_contacts_list[0].id  # получить id первого контакта
    new_contact.lastname = old_contacts_list[0].lastname  # получить lastname первого контакта
    app.contact.modify_first_contact(new_contact)
    assert len(old_contacts_list) == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[0] = new_contact
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)


def test_modify_random_contact_firstname(app):
    new_contact = Contact(firstname='firstname_MODIFIED')
    if app.contact.count() == 0:
        app.contact.create(new_contact)
    old_contacts_list = app.contact.get_contacts_list()
    index = randrange(len(old_contacts_list))
    new_contact.id = old_contacts_list[index].id  # получить id первого контакта
    new_contact.lastname = old_contacts_list[index].lastname  # получить lastname первого контакта
    app.contact.modify_contact_by_index(index, new_contact)
    assert len(old_contacts_list) == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list[index] = new_contact
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
