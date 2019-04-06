from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='GroupName_modify_first_group_name'))
    app.group.modify_first_group(Group(name='GroupName_MODIFIED'))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header='GroupHeader_modify_first_group_header'))
    app.group.modify_first_group(Group(header='GroupHeader_MODIFIED'))


def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer='GroupFooter_modify_first_group_footer'))
    app.group.modify_first_group(Group(footer='GroupFooter_MODIFIED'))
