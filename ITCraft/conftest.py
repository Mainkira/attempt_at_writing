import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  #разворачивает на весь экран окно браузера
    yield driver  #после yield начинается teardown
    driver.quit()