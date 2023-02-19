from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@fixture(autouse=True)
def setup_and_teardown(request) -> webdriver.Chrome:
    browser_name = request.config.getoption("browser_name")
    print(browser_name)

    if browser_name == "chrome":
        request.cls.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        )

        request.cls.driver.maximize_window()
        request.cls.driver.implicitly_wait(10)
        request.cls.driver.get("https://rahulshettyacademy.com/angularpractice/")

    yield

    request.cls.driver.close()
    request.cls.driver.quit()

