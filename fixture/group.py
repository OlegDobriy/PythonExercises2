class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # populating fields
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        wd.find_element_by_name('selected[]').click()
        # submit deletion
        wd.find_element_by_name('delete').click()
        # return to group page
        self.return_to_group_page()

    def delete_group_by_name(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select group by name
        wd.find_element_by_css_selector("[title*=" + group.name + "]").click()
        # submit deletion
        wd.find_element_by_name('delete').click()
        # return to group page
        self.return_to_group_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        wd.find_element_by_name('selected[]').click()
        # submit modifying
        wd.find_element_by_name('edit').click()
        # clear and modify fields
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group modifying
        wd.find_element_by_name("update").click()
        # return to group page
        self.return_to_group_page()

