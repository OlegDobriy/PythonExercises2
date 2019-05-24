import re


def test_all_cells_on_home_page(app, db):
    home_page = app.contact.get_contacts_list()
    from_db = db.get_contacts_list()
    for i in range(len(db.get_contacts_list())):
        assert home_page[i].firstname == from_db[i].firstname
        assert home_page[i].lastname == from_db[i].lastname
        assert clear(home_page[i].address) == clear(from_db[i].address)
        assert clear(home_page[i].all_emails_from_edit_page) == clear(from_db[i].all_emails_from_edit_page)
        assert clear(home_page[i].all_phones_from_edit_page) == clear(from_db[i].all_phones_from_edit_page)


def clear(phrase):
    return re.sub('[()\r \n-]', '', phrase)


def merge_emails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
