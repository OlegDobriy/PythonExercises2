from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
def group_list(db):
    return db.get_groups_list()


@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old group list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups_list = group_list
    new_groups_list = db.get_groups_list()
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.sorting_id_or_maxsize) == sorted(new_groups_list,
                                                                              key=Group.sorting_id_or_maxsize)


@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name='for_deletion'))
    return db.get_groups_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(app, db, non_empty_group_list, random_group, check_ui):
    old_groups_list = non_empty_group_list
    new_groups_list = db.get_groups_list()
    old_groups_list.remove(random_group)
    assert old_groups_list == new_groups_list
    if check_ui:
        assert sorted(new_groups_list, key=Group.sorting_id_or_maxsize) ==\
               sorted(app.group.get_groups_list(), key=Group.sorting_id_or_maxsize)