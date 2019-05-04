from model.group import Group
from random import randrange


def test_modify_group(app, db, check_ui, json_groups):
    new_group = json_groups
    if len(db.get_groups_list()) == 0:  # создать новую группу, если нечего модицифировать
        app.group.create(Group(name='name_test_modify'))
    old_groups_list = sorted(db.get_groups_list(), key=Group.sorting_name)  # в интерфейсе сортируются по name
    index = randrange(len(old_groups_list))  # поэтому при взятии из бд тоже нужно сортировать по name, иначе
    app.group.modify_group_by_index(index, new_group)  # не совпадет index
    new_groups_list = sorted(db.get_groups_list(), key=Group.sorting_name)
    new_group.id = old_groups_list[index].id  # тк не знаем id группы, возьмем его из списка и подсунем в групу из json
    old_groups_list[index] = new_group
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_groups_list, key=Group.sorting_id_or_maxsize) ==\
               sorted(app.group.get_groups_list(), key=Group.sorting_id_or_maxsize)