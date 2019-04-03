from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact((Contact(firstname='firstname_MODIFIED')))

