from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname_modify_first_contact_firstname'))
    old_contacts_count = app.contact.get_contacts_list()
    app.contact.modify_first_contact((Contact(firstname='firstname_MODIFIED')))
    new_contacts_count = app.contact.get_contacts_list()
    assert len(old_contacts_count) == len(new_contacts_count)
