from selenium.webdriver import Chrome

from src.pages.checkout_page import CheckOutPage
from src.pages.home_page import HomePage
from utilities.base import DriverFactory


class TestOne(DriverFactory):
    driver: Chrome

    def test_e2e(self):
        home_page = HomePage(self.driver)
        checkout_page = CheckOutPage(self.driver)

        home_page.shop_item().click()
        cards = checkout_page.card_title

        for i in range(len(cards)):
            print(cards[i].text)

            if cards[i].text == "Blackberry":
                checkout_page.card_footer[i].click()
                break

        checkout_page.checkout_button.click()


