from model.group import Group


def test_delete_first_group(app):
    old_groups_list = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name='GroupName_delete_first_group'))
    app.group.delete_first_group()
    assert len(old_groups_list) - 1 == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list[0:1] = []
    assert old_groups_list == new_groups_list

