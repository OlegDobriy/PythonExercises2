class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group_fields):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_fields)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_group_page()

    def fill_group_form(self, group):
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)

    def change_field_value(self, field_to_change_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_to_change_name).clear()
            wd.find_element_by_name(field_to_change_name).send_keys(text)

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
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name('delete').click()
        # return to group page
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

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

    def modify_first_group(self, new_data):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # select first group
        self.select_first_group()
        # submit modifying
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_data)
        # submit group modifying
        wd.find_element_by_name("update").click()
        # return to group page
        self.return_to_group_page()
