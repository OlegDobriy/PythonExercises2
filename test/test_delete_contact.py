from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


def test_delete_contact_by_name(app):
    app.session.login(username="Admin", password="secret")
    app.contact.delete_contact_by_name(Contact(lastname="lastname"))
    app.session.logout()
