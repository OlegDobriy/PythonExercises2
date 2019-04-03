from model.group import Group


def test_delete_first_group(app):
    app.group.delete_first_group()


def test_delete_group_by_name(app):
    app.group.delete_group_by_name(Group(name="GroupName"))
