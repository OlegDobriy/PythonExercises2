# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    new_contact = Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                          nickname='nickname', title='title', company='company', address='address',
                          homephone='homephone', mobilephone='mobilephone')
    app.contact.create(new_contact)
    assert len(old_contacts_list) + 1 == app.contact.count()
    new_contacts_list = app.contact.get_contacts_list()
    old_contacts_list.append(new_contact)
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)


'''
def test_add_empty_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname='', middlename='', lastname='',
                               nickname='', title='', company='', address='',
                               home='', mobile=''))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)
'''
