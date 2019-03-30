from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.modify_first_group(Group(name='GroupName_MODIFIED',
                                            header='GroupHeader_MODIFIED', footer='GroupFooter_MODIFIED'))
    app.session.logout()
