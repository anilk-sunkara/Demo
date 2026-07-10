import pytest

from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()   ## setup
    driver.maximize_window()
    # driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()     ## teardown