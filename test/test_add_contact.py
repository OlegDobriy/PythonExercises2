# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [Contact(firstname=firstname, lastname=lastname, homephone=homephone, email3=email3)
            for firstname in ['', random_sting('firstname', 5)]
            for lastname in ['', random_sting('lastname', 15)]
            for homephone in ['', random_sting('homephone', 10)]
            for email3 in ['', random_sting('email3', 10)]
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
