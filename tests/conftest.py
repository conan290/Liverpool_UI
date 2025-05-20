import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_setting_values.geolocation": 2
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.liverpool.com.mx/tienda/home")
    yield driver
    driver.quit()

