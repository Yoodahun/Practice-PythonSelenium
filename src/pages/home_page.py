from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from src.pages.checkout_page import CheckOutPage


class HomePage:

    __shop = (By.CSS_SELECTOR, "a[href*='shop']")
    __name = (By.CSS_SELECTOR, "[name='name']")
    __email = (By.NAME, "email")
    __icecream_checkbox = (By.ID, "exampleCheck1")
    __gender = (By.ID, "exampleFormControlSelect1")
    __submit_button = (By.XPATH, "//input[@value='Submit']")
    __alert_text = (By.CSS_SELECTOR, "[class*='alert-success']")


    def __init__(self, driver):
        self.driver: Chrome = driver

    @property
    def name(self) -> WebElement:
        return self.driver.find_element(*HomePage.__name)

    @property
    def alert_text(self) -> str:
        return self.driver.find_element(*HomePage.__alert_text).text

    @property
    def gender(self) -> WebElement:
        """
        gender 를 리턴하며 select option이다.

        :return: WebElement
        """
        return self.driver.find_element(*HomePage.__gender)

    def move_shop_checkout_page(self) -> CheckOutPage:
        self.driver.find_element(*HomePage.__shop).click()
        return CheckOutPage(self.driver)

    def input_name(self, text):
        self.name.send_keys(text)

    def input_email(self, text):
        self.driver.find_element(*HomePage.__email).send_keys(text)

    def check_icecream_checkbox(self):
        self.driver.find_element(*HomePage.__icecream_checkbox).click()

    def click_submit_button(self):
        self.driver.find_element(*HomePage.__submit_button).click()





