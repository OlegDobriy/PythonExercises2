from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_fields):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # populating fields
        self.fill_contact_form(contact_fields)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_to_change_value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_to_change_value).clear()
            wd.find_element_by_name(field_to_change_value).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def delete_contact_by_name(self, contact):
        wd = self.app.wd
        # find contact by name
        wd.find_element_by_css_selector("[title*=" + contact.lastname + "]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name('selected[]').get_attribute('id')
                lastname = element.find_element_by_xpath('.//td[2]').text
                firstname = element.find_element_by_xpath('.//td[3]').text
                address = element.find_element_by_xpath('.//td[4]').text
                all_emails_from_edit_page = element.find_element_by_xpath('.//td[5]').text
                all_phones = element.find_element_by_xpath('.//td[6]').text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address,
                                                  all_emails_from_edit_page=all_emails_from_edit_page,
                                                  all_phones_from_edit_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        address = wd.find_element_by_name('address').text
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        secondaryphone = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3, address=address)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//input[@id="%s"]' % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self, new_data):
        self.modify_contact_by_index(0, new_data)

    def modify_contact_by_index(self, index, new_data):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        self.fill_contact_form(new_data)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def get_contact_info_from_view_page_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()
        whole_text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', whole_text).group(1)
        mobilephone = re.search('M: (.*)', whole_text).group(1)
        workphone = re.search('W: (.*)', whole_text).group(1)
        secondaryphone = re.search('P: (.*)', whole_text).group(1)
        return Contact(homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_id(contact.id)
        # choose group to add
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group.id).click()
        # submit adding contact to group
        wd.find_element_by_name('add').click()
        self.return_to_home_page()
        self.contact_cache = None

    def remove_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.return_to_home_page()
        # choose group to get contact list
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group.id).click()
        self.select_contact_by_id(contact.id)
        # submit removing
        wd.find_element_by_name('remove').click()
        self.return_to_home_page()
        self.contact_cache = None

    def get_contacts_in_group(self, group):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            # choose group to get contact list
            wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % group.id).click()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name('selected[]').get_attribute('id')
                lastname = element.find_element_by_xpath('.//td[2]').text
                firstname = element.find_element_by_xpath('.//td[3]').text
                address = element.find_element_by_xpath('.//td[4]').text
                all_emails_from_edit_page = element.find_element_by_xpath('.//td[5]').text
                all_phones = element.find_element_by_xpath('.//td[6]').text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address,
                                                  all_emails_from_edit_page=all_emails_from_edit_page,
                                                  all_phones_from_edit_page=all_phones))
        return list(self.contact_cache)
