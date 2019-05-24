from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()


@given('a contact with <firstname> and <lastname>')
def new_contact(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, contact_list, new_contact, check_ui):
    old_contacts_list = contact_list
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.append(new_contact)
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
               sorted(db.get_contacts_list(), key=Contact.sorting_id_or_maxsize)


@given('a non-empty contact list')
def non_empty_contact_list(app, db):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname='firstname'))
    return db.get_contacts_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_group_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    old_contacts_list = non_empty_contact_list
    new_contacts_list = db.get_contacts_list()
    old_contacts_list.remove(random_contact)
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) == sorted(old_contacts_list,
                                                                                  key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
               sorted(app.contact.get_contacts_list(), key=Contact.sorting_id_or_maxsize)

@given('new <firstname> and <lastname>')
def contact_modified(firstname, lastname):
    return Contact(firstname=firstname, lastname=lastname)


@when('I modify the contact from the list')
def modify_contact_by_id(app, contact_modified, random_contact):
    app.contact.modify_contact_by_id(random_contact.id, contact_modified)


@then('the new contact list is equal to the old contact list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, contact_modified, random_contact, check_ui):
    index = int(non_empty_contact_list.index(random_contact))
    contact_modified.id = random_contact.id
    non_empty_contact_list[index] = contact_modified
    old_contacts_list = non_empty_contact_list
    new_contacts_list = db.get_contacts_list()
    assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
        sorted(old_contacts_list, key=Contact.sorting_id_or_maxsize)
    if check_ui:
        assert sorted(new_contacts_list, key=Contact.sorting_id_or_maxsize) ==\
            sorted(app.contact.get_contacts_list(), key=Contact.sorting_id_or_maxsize)