from selenium.webdriver.common.by import By


class MainPageLocators:
    """Хранит локаторы для страницы https://klavogonki.ru/
    """
    QUICK_START_TITLE = (By.XPATH, '//*[@id="index"]/div[1]/div[2]/div/a[2]')
