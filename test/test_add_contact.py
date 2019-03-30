# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="Admin", password="secret")
    app.contact.create(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                               nickname='nickname', title='title', company='company', address='address',
                               home='home', mobile='mobile'))
    app.session.logout()


def test_add_empty_contact(app):
        app.session.login(username="Admin", password="secret")
        app.contact.create(Contact(firstname='', middlename='', lastname='',
                                   nickname='', title='', company='', address='',
                                   home='', mobile=''))
        app.session.logout()


