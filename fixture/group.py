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
