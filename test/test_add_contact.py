# -*- coding: utf-8 -*-

from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="Admin", password="secret")
    app.create_contact(Contact(firstname='firstname', middlename='middlename', lastname='lastname',
                                    nickname='nickname', title='title', company='company', address='address',
                                    home='home', mobile='mobile'))
    app.logout()

def test_add_empy_contact(app):
        app.login(username="Admin", password="secret")
        app.create_contact(Contact(firstname='', middlename='', lastname='',
                                        nickname='', title='', company='', address='',
                                        home='', mobile=''))
        app.logout()


