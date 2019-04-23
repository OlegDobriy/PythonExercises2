# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [
    Contact(firstname=random_sting('firstname_', 10), lastname=random_sting('lastname_', 10),
            address=random_sting('address_', 10), homephone=random_sting('homephone_', 10),
            email3=random_sting('email3_', 10))
    for i in range(5)
]


@pytest.mark.parametrize('contact_data', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact_data):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(contact_data)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list.append(contact_data)
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
