import allure


class SessionHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Login')
    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page(wd)
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    @allure.step('Logout')
    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def check_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        self.app.open_home_page(wd)
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath('//div/div[1]/form/b').text[1:-1]  # 1:-1 чтобы убрать скобки

    def check_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
