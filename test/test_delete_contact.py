from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact_by_name(app):
    app.contact.delete_contact_by_name(Contact(lastname="lastname"))
