# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string


def random_sting(prefix, max_len):
    symbols = string.ascii_letters + string.digits
    return prefix + (''.join([random.choice(symbols) for i in range(random.randrange(max_len))]))


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_sting('name', 5)]
    for header in ['', random_sting('header', 10)]
    for footer in ['', random_sting('footer', 15)]
]


@pytest.mark.parametrize('group_data', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group_data):
    old_groups_list = app.group.get_groups_list()
    app.group.create(group_data)
    assert len(old_groups_list) + 1 == app.group.count()  # справа берется только количество, а не весь список
    new_groups_list = app.group.get_groups_list()  # чтобы облегчить тест. Если прошел, то далее сравнить списки
    old_groups_list.append(group_data)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)
