from model.group import Group
from random import randrange


def test_modify_some_group_name(app):
    new_group = Group(name='GroupName_MODIFIED')
    if app.group.count() == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(new_group)
    old_groups_list = app.group.get_groups_list()
    index = randrange(len(old_groups_list))
    new_group.id = old_groups_list[index].id  # получить id группы[index], которая будет меняться,
    app.group.modify_group_by_index(index, new_group)  # чтобы в последнем assert сравнить ее с измененной
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list[index] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


def test_modify_first_group_header(app):
    new_group = Group(header='GroupHeader_MODIFIED')
    if app.group.count() == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(new_group)
    old_groups_list = app.group.get_groups_list()
    new_group.id = old_groups_list[0].id  # получить id первой группы
    new_group.name = old_groups_list[0].name  # получить name первой группы
    app.group.modify_first_group(new_group)
    assert len(old_groups_list) == app.group.count()
    new_groups_list = app.group.get_groups_list()
    old_groups_list[0] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


'''
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