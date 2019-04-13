from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_count = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts_count = app.contact.get_contacts_list()
    assert len(old_contacts_count) -1 == len(new_contacts_count)
