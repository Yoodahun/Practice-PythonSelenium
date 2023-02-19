from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome

from src.pages.confirm_page import ConfirmPage


class CheckOutPage:
    __card_title = (By.CSS_SELECTOR, ".card-title a")
    __card_footer = (By.CSS_SELECTOR, ".card-footer button")
    __checkout_button = (By.CSS_SELECTOR, "#navbarResponsive > ul > li > a")
    __checkout_button2 = (By.CSS_SELECTOR, "body > app-root > app-shop > div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(5) > button")

    def __init__(self, driver: Chrome):
        self.driver = driver

    @property
    def card_title(self) -> List[WebElement]:
        return self.driver.find_elements(*CheckOutPage.__card_title)

    @property
    def card_footer(self) -> List[WebElement]:
        return self.driver.find_elements(*CheckOutPage.__card_footer)

    def move_checkout_page(self):
        return self.driver.find_element(*CheckOutPage.__checkout_button).click()

    def move_confirm_page(self) -> ConfirmPage:
        self.driver.find_element(*CheckOutPage.__checkout_button2).click()
        return ConfirmPage(self.driver)
