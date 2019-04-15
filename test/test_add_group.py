# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name="GroupName", header="GroupHeader", footer="GroupFooter")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()  # справа берется только количество, а не весь список
    new_groups_list = app.group.get_groups_list()  # чтобы облегчить тест. Если прошел, то далее сравнить списки
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


def test_add_empty_group(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name="", header="", footer="")
    app.group.create(new_group)
    assert len(old_groups_list) + 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list, key=Group.sorting_id_or_maxsize)
