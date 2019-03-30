from model.contact import Contact


def test_modify_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.contact.modify_first_contact((Contact(firstname='firstname_MODIFIED', middlename='middlename_MODIFIED',
                                            lastname='lastname_MODIFIED', nickname='nickname_MODIFIED',
                                            title='title_MODIFIED', company='company_MODIFIED',
                                            address='address_MODIFIED', home='home', mobile='mobile')))
    app.session.logout()
