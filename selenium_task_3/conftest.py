import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('headless')                # Use it when do not need UI
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome('C:/Users/User/PycharmProjects/selenium_tasks/chromedriver.exe',
                              options=get_chrome_options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    yield driver
    driver.quit()
