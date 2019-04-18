from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group_fields):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group_fields)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to group page
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.change_field_value('group_name', group.name)
        self.change_field_value('group_header', group.header)
        self.change_field_value('group_footer', group.footer)

    def change_field_value(self, field_to_change_value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_to_change_value).clear()
            wd.find_element_by_name(field_to_change_value).send_keys(text)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith('group.php') and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def delete_group_by_name(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # select group by name
        wd.find_element_by_css_selector("[title*=%s]" % group.name).click()
        # submit deletion
        wd.find_element_by_name('delete').click()
        # return to group page
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name('selected[]'))

    group_cache = None  # чтобы использовать список групп повторно, а не в каждом тесте заново его составлять

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name('delete').click()
        # return to group page
        self.return_to_group_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def modify_first_group(self, new_data):
        self.modify_group_by_index(0, new_data)

    def modify_group_by_index(self, index, new_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit modifying
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_data)
        # submit group modifying
        wd.find_element_by_name("update").click()
        # return to group page
        self.return_to_group_page()
        self.group_cache = None
