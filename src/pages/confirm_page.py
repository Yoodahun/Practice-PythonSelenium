from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def input_country(self, text):
        self.driver.find_element(
            By.ID, "country"
        ).send_keys(text)
