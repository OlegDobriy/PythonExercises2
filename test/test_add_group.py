# -*- coding: utf-8 -*-

from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
    app.logout()

def test_add_empy_group(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
