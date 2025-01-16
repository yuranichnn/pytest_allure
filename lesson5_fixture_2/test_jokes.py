import time

from selenium import webdriver
from helper import Helper

# //div[@class="orangehrm-buzz-post-body"]
HOST = "https://opensource-demo.orangehrmlive.com/web/index.php"


class TestPostJoke(Helper):
    LOGIN_URL = f"{HOST}/auth/login"
    BUZZ_URL = f"{HOST}/buzz/viewBuzz"
    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    POST_FIELD = "//div/textarea"
    POST_BUTTON = "//div/button[@type='submit']"
    POSTS_OUT_FIELD = ("xpath", "//div[@class='orangehrm-buzz-post-body']/p")

    def setup_method(self):
        self.is_opened(self.LOGIN_URL)
        self.fill_field(self.USERNAME_FIELD, "Admin")
        self.fill_field(self.PASSWORD_FIELD, "admin123")
        self.get_element(self.LOGIN_BUTTON).click()

    def test_post_joke(self, get_joke):
        joke = get_joke
        self.is_opened(self.BUZZ_URL)
        self.fill_field(self.POST_FIELD, joke)
        self.get_element(self.POST_BUTTON).click()
        self.driver.refresh()
        time.sleep(3) # не смог сделать через ЕС(visibility_of_all_elements_located не работает)
        self.check_post(self.POSTS_OUT_FIELD, joke)

    def teardown_method(self):
        self.driver.quit()
