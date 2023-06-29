from selenium.webdriver.common.by import By


class GoPageLocators:
    """Хранит локаторы для страницы https://klavogonki.ru/g/?gmid=...
     """
    CLOSE_MANUAL_BUTTON = (By.XPATH, '//*[@id="howtoplay"]/div[2]/div/table/tbody/tr[2]/td[2]/p[5]/input')
    START_GAME_TITLE = (By.XPATH, '//*[@id="host_start"]')
    START_GAME_WAITING = (By.XPATH, '//*[@id="waiting_timeout"]')
    TEXT_OUTPUT = (By.XPATH, '//*[@id="typetext"]')
    TEXT_INTPUT = (By.XPATH, '//*[@id="inputtext"]')
    SPEED_LABEL = (By.XPATH, '//*[@id="speed-label"]')
    ERROR_LABEL = (By.XPATH, '//*[@id="errors-label"]')
    FIX_TYPO = (By.XPATH, '//*[@id="fixtypo"]')
