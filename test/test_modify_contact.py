from model.contact import Contact
from random import randrange


def test_modify_contact(app, db, check_ui, json_contacts):
    new_contact = json_contacts
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='firstname_test_modify'))
    old_contacts_list = sorted(db.get_contacts_list(), key=Contact.sorting_name)
    index = randrange(len(old_contacts_list))
    new_contact.id = old_contacts_list[index].id  # получить id первого контакта
    new_contact.lastname = old_contacts_list[index].lastname  # получить lastname первого контакта
    app.contact.modify_contact_by_index(index, new_contact)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list[index] = new_contact
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
        sorted(old_contacts_list, key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
            sorted(app.contact.get_contacts_list(), key=Contact.sorting_id_or_maxsize)
