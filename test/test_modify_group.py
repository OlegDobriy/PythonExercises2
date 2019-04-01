from model.group import Group


def test_modify_first_group_name(app):
    app.session.login(username="Admin", password="secret")
    app.group.modify_first_group(Group(name='GroupName_MODIFIED'))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(username="Admin", password="secret")
    app.group.modify_first_group(Group(header='GroupHeader_MODIFIED'))
    app.session.logout()


def test_modify_first_group_footer(app):
    app.session.login(username="Admin", password="secret")
    app.group.modify_first_group(Group(footer='GroupFooter_MODIFIED'))
    app.session.logout()
