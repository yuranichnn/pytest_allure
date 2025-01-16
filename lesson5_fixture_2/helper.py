import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from driver import DriverOptions


class Helper(DriverOptions):
    driver = webdriver.Chrome(options=DriverOptions.options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    wait = WebDriverWait(driver, 10, 1)

    def get_element(self, locator: str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(("xpath", f"{locator}")),
                               f"Элемент с локатором '{locator}' не найден.")

    def fill_field(self, locator: str, data: str):
        field = self.get_element(locator)
        field.send_keys(data)
        assert data == field.get_attribute("value"), "Значение не просело в поле"

    def is_opened(self, expect_url: str):
        self.driver.get(expect_url)
        assert self.wait.until(EC.url_to_be(expect_url)), "Неверный адрес страницы"

    def check_post(self, locator: tuple, post_data: str):
        posts = self.driver.find_elements(*locator)
        post_founded = False
        for post in posts:
            post_founded = post_data.strip() == post.text.strip()

            if post_founded:
                print(f"The message was posted with the text: {post.text}")
                break
        assert post_founded, f"The message was NOT published with the text: {post_data}"
