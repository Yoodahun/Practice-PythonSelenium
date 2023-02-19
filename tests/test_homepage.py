from selenium.webdriver import Chrome

from src.pages.home_page import HomePage
from utilities.base import DriverFactory


class TestHomePage(DriverFactory):

    def test_form_submission(self, get_homepage_data):
        home_page = HomePage(self.driver)
        print(get_homepage_data)
        home_page.input_name(get_homepage_data["first_name"])
        home_page.input_email(get_homepage_data["email"])
        home_page.check_icecream_checkbox()
        self.select_option_by_text(
            home_page.gender,
            get_homepage_data["gender"]
        )
        home_page.click_submit_button()

        print(home_page.alert_text)

        assert "Success" in home_page.alert_text
