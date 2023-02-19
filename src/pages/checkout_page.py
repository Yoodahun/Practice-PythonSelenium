from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome


class CheckOutPage:
    __card_title = (By.CSS_SELECTOR, ".card-title a")
    __card_footer = (By.CSS_SELECTOR, ".card-footer button")
    __checkout_button = (By.CSS_SELECTOR, "#navbarResponsive > ul > li > a")

    def __init__(self, driver: Chrome):
        self.driver = driver

    @property
    def card_title(self) -> List[WebElement]:
        return self.driver.find_elements(*CheckOutPage.__card_title)

    @property
    def card_footer(self) -> List[WebElement]:
        return self.driver.find_elements(*CheckOutPage.__card_footer)

    @property
    def checkout_button(self) -> WebElement:
        return self.driver.find_element(*CheckOutPage.__checkout_button)
