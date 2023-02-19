import inspect
import logging

from pytest import fixture, mark
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@mark.usefixtures("setup_and_teardown")
class DriverFactory:

    def verify_link_presence(self, text) -> WebElement:
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.LINK_TEXT, text)
            )
        )

        return element

    def select_option_by_text(self, select_tag: WebElement, text):
        option = Select(select_tag)
        option.select_by_visible_text(text)

    def getlogger(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler('logging.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        return logger
