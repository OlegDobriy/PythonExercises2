from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='FirstName_delete_first_contact'))
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.delete_first_contact()
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) - 1 == len(new_contacts_list)
    old_contacts_list[0:1] = []
    assert old_contacts_list == new_contacts_list

