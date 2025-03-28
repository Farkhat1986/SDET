from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest



@pytest.fixture(scope='module')
def driver():
    global driver
    options = Options()

    # Основные настройки
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    options.add_argument("--headless")

    # Критически важные параметры
    options.set_preference("browser.tabs.remote.autostart", False)
    options.set_preference("browser.tabs.remote.autostart.1", False)
    options.set_preference("browser.tabs.remote.autostart.2", False)
    options.set_preference("browser.tabs.remote.force-enable", False)

    # Настройки для CI
    options.set_preference("network.http.response.timeout", 300)
    options.set_preference("dom.max_script_run_time", 300)

    service = Service(
        executable_path=GeckoDriverManager().install(),
        service_args=['--log', 'trace'],
        timeout=300
    )

    try:
        driver = Firefox(service=service, options=options)
        driver.set_page_load_timeout(60)
        driver.implicitly_wait(30)
        yield driver
    finally:
        if 'driver' in locals():
            driver.quit()




