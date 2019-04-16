from model.contact import Contact


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
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)

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
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
        return list(self.contact_cache)

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

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self, new_data):
        self.modify_contact_by_index(0, new_data)

    def modify_contact_by_index(self, index, new_data):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_data)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
