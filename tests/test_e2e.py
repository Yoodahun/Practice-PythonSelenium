from typing import ClassVar
from selenium.webdriver import Chrome

from util.base import BaseDriver


class TestOne(BaseDriver):
    driver: ClassVar[Chrome]

    def test_e2e(self):
        print(self.driver.title)
