from selenium.webdriver import Chrome
from src.pages.checkout_page import CheckOutPage
from src.pages.home_page import HomePage
from utilities.base import DriverFactory


class TestOne(DriverFactory):
    driver: Chrome

    def test_checkout_link_text(self):
        logger = self.getlogger()
        home_page = HomePage(self.driver)
        checkout_page = home_page.move_shop_checkout_page()
        cards = checkout_page.card_title

        for i in range(len(cards)):
            logger.info(cards[i].text)

            if cards[i].text == "Blackberry":
                checkout_page.card_footer[i].click()
                break

        checkout_page.move_checkout_page()
        confirm_page = checkout_page.move_confirm_page()
        confirm_page.input_country("ind")
        link_item = self.verify_link_presence("India")
        logger.info(link_item.text)

        assert "India" == link_item.text
