import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """Вызывает драйвер для управления работой браузера на базе выбранного webdriver.
    """
    options = webdriver.ChromeOptions()
    options.set_capability("pageLoadStrategy", "eager")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
