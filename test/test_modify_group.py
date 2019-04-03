from model.group import Group


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name='GroupName_MODIFIED'))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header='GroupHeader_MODIFIED'))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer='GroupFooter_MODIFIED'))