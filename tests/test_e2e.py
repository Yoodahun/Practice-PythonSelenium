from typing import ClassVar
from selenium.webdriver import Chrome

from src.pages.home_page import HomePage
from utilities.base import DriverFactory


class TestOne(DriverFactory):
    driver: ClassVar[Chrome]

    def test_e2e(self):
        home_page = HomePage(self.driver)
        home_page.shop_item().click()

