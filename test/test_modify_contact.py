from model.contact import Contact


def test_modify_first_contact_firstname(app):
    old_contacts_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname='firstname_MODIFIED')
    new_contact.id = old_contacts_list[0].id  # получить id первого контакта
    new_contact.lastname = old_contacts_list[0].lastname  # получить lastname первого контакта
    if app.contact.count() == 0:
        app.contact.create(new_contact)
    app.contact.modify_first_contact(new_contact)
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) == len(new_contacts_list)
    old_contacts_list[0] = new_contact
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)