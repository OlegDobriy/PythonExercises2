from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='firstname_modify_first_contact_firstname'))
    app.contact.modify_first_contact((Contact(firstname='firstname_MODIFIED')))

