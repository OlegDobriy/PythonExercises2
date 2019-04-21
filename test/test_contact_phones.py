import re
from random import randrange


def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(index)
    assert contact_from_home_page.all_phones_from_edit_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_edit_page(app):
    index = randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_info_from_view_page_by_index(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_by_index(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(phrase):
    return re.sub('[() -]', '', phrase)
    # эти символы можно ввести, но на дом. странице они не отображаются
    # поэтому они вырезаются из строки для правильного сравнения


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
# сначала берется список телефонов, затем выбрасываются те, что имеют знач None, потом к оставшимся применяется clear(),
# после те, что не пустые, объединяются через перевод строки.
# В итоге получится такой же список из телефонов, как и на домашней странице.
# Это нужно потому, что на дом. стр. номера идут без обозначения где какой, а на стр. редактиврования конкретный
# номер пишется в конкретном поле.

