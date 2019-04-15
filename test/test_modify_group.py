from model.group import Group


def test_modify_first_group_name(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(name='GroupName_MODIFIED')
    new_group.id = old_groups_list[0].id  # получить id первой группы
    if app.group.count() == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(new_group)
    app.group.modify_first_group(new_group)
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list[0] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)
'''
def test_modify_first_group_header(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(header='GroupHeader_MODIFIED')
    new_group.id = old_groups_list[0].id  # получить id первой группы
    if app.group.count() == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(new_group)
    app.group.modify_first_group(new_group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


def test_modify_first_group_footer(app):
    old_groups_list = app.group.get_groups_list()
    new_group = Group(footer='GroupFooter_MODIFIED')
    new_group.id = old_groups_list[0].id  # получить id первой группы
    if app.group.count() == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(new_group)
    app.group.modify_first_group(new_group)
    new_groups_list = app.group.get_groups_list()
    assert len(old_groups_list) == len(new_groups_list)
    old_groups_list[0] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)
'''