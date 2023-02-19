from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from src.pages.checkout_page import CheckOutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver: Chrome = driver

    def move_shop_checkout_page(self) -> CheckOutPage:
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)
