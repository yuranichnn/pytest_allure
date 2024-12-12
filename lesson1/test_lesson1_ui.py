import time

from helper import Helper

HOST = "https://opensource-demo.orangehrmlive.com/web/index.php"


class TestLogin(Helper):
    LOGIN_URL = f"{HOST}/auth/login"
    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    DASHBOARD_URL = f"{HOST}/dashboard/index"

    def setup_method(self):
        self.driver.get(self.LOGIN_URL)

    def test_login(self):
        self.is_opened(self.LOGIN_URL)
        self.fill_field(self.USERNAME_FIELD, "Admin")
        self.fill_field(self.PASSWORD_FIELD, "admin123")
        self.get_element(self.LOGIN_BUTTON).click()
        self.is_opened(self.DASHBOARD_URL)


class TestMenuElement(Helper):
    MENU = "//ul[@class='oxd-main-menu']"

    def test_menu_elements(self):
        self.check_by_click_menu_elements(self.MENU)
