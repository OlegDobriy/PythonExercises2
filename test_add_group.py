# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        # open group page
        self.open_groups_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # populating fields
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_group_page(wd)


    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

    def test_add_group(self):
        wd = self.wd
        self.login(wd, username="Admin", password="secret")
        self.create_group(wd, Group(name="GroupName", header="GroupHeader", footer="GroupFooter"))
        self.logout(wd)

    def test_add_empy_group(self):
        wd = self.wd
        self.login(wd, username="Admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.logout(wd)

if __name__ == "__main__":
    unittest.main()
