import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для инициализации WebDrivers.

    Returns:
        WebDriver: Экземпляр WebDriver для управления браузером.
    """

    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument('--headless')
    service = FirefoxService(GeckoDriverManager().install())
    driver = Firefox(service=service, options=firefox_options)

    yield driver
    driver.quit()





