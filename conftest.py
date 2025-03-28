import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='module')
def driver():
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--headless")

    service = Service(
        GeckoDriverManager().install(),
        service_args=['--log', 'debug'],
        timeout=300  # Увеличенный таймаут
    )

    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()





