from model.group import Group


def test_delete_first_group(app):
    old_groups_count = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name='GroupName_delete_first_group'))
    app.group.delete_first_group()
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) - 1 == len(new_groups_count)
