# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                               nickname='nickname', title='title', company='company', address='address',
                               home='home', mobile='mobile'))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)


def test_add_empty_contact(app):
    old_contacts_list = app.contact.get_contacts_list()
    app.contact.create(Contact(firstname='', middlename='', lastname='',
                               nickname='', title='', company='', address='',
                               home='', mobile=''))
    new_contacts_list = app.contact.get_contacts_list()
    assert len(old_contacts_list) + 1 == len(new_contacts_list)

