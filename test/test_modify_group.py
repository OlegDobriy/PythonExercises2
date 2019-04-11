from model.group import Group


def test_modify_first_group_name(app):
    old_groups_count = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(name='GroupName_modify_first_group_name'))
    app.group.modify_first_group(Group(name='GroupName_MODIFIED'))
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) == len(new_groups_count)


def test_modify_first_group_header(app):
    old_groups_count = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(header='GroupHeader_modify_first_group_header'))
    app.group.modify_first_group(Group(header='GroupHeader_MODIFIED'))
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) == len(new_groups_count)


def test_modify_first_group_footer(app):
    old_groups_count = app.group.get_groups_list()
    if app.group.count() == 0:
        app.group.create(Group(footer='GroupFooter_modify_first_group_footer'))
    app.group.modify_first_group(Group(footer='GroupFooter_MODIFIED'))
    new_groups_count = app.group.get_groups_list()
    assert len(old_groups_count) == len(new_groups_count)
