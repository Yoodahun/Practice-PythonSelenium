import pytest
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

from tests.test_data.homepage_data import HomePageData

driver: webdriver.Chrome = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@fixture(autouse=True)
def setup_and_teardown(request) -> webdriver.Chrome:
    global driver
    browser_name = request.config.getoption("browser_name")
    print(browser_name)

    if browser_name == "chrome":
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        )

    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver

    yield

    request.cls.driver.close()
    request.cls.driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the pytest library to take and embedded sccrenshot in html report
    :param item:
    :return:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    reports = outcome.get_result()
    extra = getattr(reports, 'extra', [])

    if reports.when == 'call' or reports.when == "setup":
        xfail = hasattr(reports, 'wasxfail')
        if (reports.skipped and xfail) or (reports.failed and not xfail):
            file_name = reports.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alr="screenshot" style="width:304px;height:228px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))

    reports.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@fixture(params=HomePageData.TEST_HOME_PAGE_DATA)
def get_homepage_data(request):
    return request.param
