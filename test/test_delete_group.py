from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_delete_group_by_name(app):
    app.session.login(username="Admin", password="secret")
    app.group.delete_group_by_name(Group(name="GroupName"))
    app.session.logout()
