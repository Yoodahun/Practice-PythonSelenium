from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver: Chrome = driver

    def shop_item(self) -> WebElement:
        return self.driver.find_element(*HomePage.shop)
