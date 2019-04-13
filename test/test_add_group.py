# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name="GroupName", header="GroupHeader", footer="GroupFooter")
    app.group.create(new_group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


def test_add_empty_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name="", header="", footer="")
    app.group.create(new_group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list, key=Group.sorting_id_or_maxsize)
