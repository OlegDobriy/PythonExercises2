from model.group import Group
import random


def test_delete_random_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name='GroupName_delete_first_group'))
    old_groups_list = db.get_groups_list()
    group = random.choice(old_groups_list)
    app.group.delete_group_by_id(group.id)
    new_groups_list = db.get_groups_list()
    old_groups_list.remove(group)
    assert old_groups_list == new_groups_list
    if check_ui:
        assert sorted(new_groups_list, key=Group.sorting_id_or_maxsize) ==\
               sorted(app.group.get_groups_list(), key=Group.sorting_id_or_maxsize)
