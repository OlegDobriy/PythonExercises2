from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="Admin", password="secret")
    app.contact.modify_first_contact((Contact(firstname='firstname_MODIFIED')))
    app.session.logout()
