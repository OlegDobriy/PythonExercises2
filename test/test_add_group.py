# -*- coding: utf-8 -*-


from model.group import Group


def test_add_group(app, group_data):
    group = group_data
    old_groups_list = app.group.get_groups_list()
    app.group.create(group)
    assert len(old_groups_list) + 1 == app.group.count()  # справа берется только количество, а не весь список
    new_groups_list = app.group.get_groups_list()  # чтобы облегчить тест. Если прошел, то далее сравнить списки
    old_groups_list.append(group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


'''
загрузка тестовых данных из файла

from model.group import Group
import pytest
from data.groups import testdata


@pytest.mark.parametrize('group_data', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_data):
    old_groups_list = app.group.get_groups_list()
    app.group.create(group_data)
    assert len(old_groups_list) + 1 == app.group.count()  # справа берется только количество, а не весь список
    new_groups_list = app.group.get_groups_list()  # чтобы облегчить тест. Если прошел, то далее сравнить списки
    old_groups_list.append(group_data)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)
'''
