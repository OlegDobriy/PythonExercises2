# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups_count = app.group.get_groups_list()
    app.group.create(Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) + 1 == len(new_groups_count)


def test_add_empty_group(app):
    old_groups_count = app.group.get_groups_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) + 1 == len(new_groups_count)