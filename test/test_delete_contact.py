from model.contact import Contact
import random


def test_delete_random_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = db.get_contacts_list()
    contact = random.choice(old_contacts_list)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.remove(contact)  # вырезать кусок от index до index+1
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
               sorted(db.get_contacts_list(), key=Contact.sorting_id_or_maxsize)
