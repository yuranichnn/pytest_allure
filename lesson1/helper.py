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

    def get_element(self, locator:str) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(("xpath", f"{locator}")),
                               f"Элемент с локатором '{locator}' не найден.")

    def fill_field(self, locator: str, data: str):
        field = self.get_element(locator)
        field.send_keys(data)
        assert data == field.get_attribute("value"), "Значение не просело в поле"

    def is_opened(self, expect_url: str):
        assert self.wait.until(EC.url_to_be(expect_url)), "Неверный адрес страницы"

    def _get_menu_elements(self, locator: str) -> list[WebElement]:
        menu = self.get_element(locator)
        menu_elements = menu.find_elements("xpath", "./li")
        assert menu_elements, "Нет элементов меню"
        return menu_elements

    def check_by_click_menu_elements(self, locator_menu):

        for i in range(len(self._get_menu_elements(locator_menu))):
            elements_menu = self._get_menu_elements(locator_menu)
            elem = elements_menu[i]
            current_url = self.driver.current_url
            elem.click()
            url_after_click = self.driver.current_url
            if url_after_click == "https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee":
                self.get_element("//div[@class='orangehrm-card-container']//button[1]").click()
                continue

            self.wait.until(EC.url_changes(current_url))