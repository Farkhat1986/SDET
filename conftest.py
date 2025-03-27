import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для инициализации WebDrivers.

    Returns:
        WebDriver: Экземпляр WebDriver для управления браузером.
    """

    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)


    yield driver
    driver.quit()





