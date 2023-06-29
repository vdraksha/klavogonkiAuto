import random
import time
from page.base_page import BasePage
from locators.go_page_locators import GoPageLocators
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys


class GoPage(BasePage):
    locators = GoPageLocators

    def close_manual_button_click(self):
        """Нажимает на заголовок 'Быстрый старт'
        """
        self.element_is_visible(self.locators.CLOSE_MANUAL_BUTTON).click()

    def start_game_button_click(self):
        """Нажимает на заголовок 'Начать игру'
        """
        try:
            self.element_is_visible(self.locators.START_GAME_TITLE).click()
        except TimeoutException:
            pass

    def get_text(self):
        """Ждет указанное время в timeout для получения текста.
        :return: Возвращает текст.
        """
        time.sleep(5)   # Необходимо для избежания ошибки JS error
        timeout = self.element_is_visible(self.locators.START_GAME_WAITING).text[3:]
        return self.element_is_visible(self.locators.TEXT_OUTPUT, timeout).text

    def set_text(self, text: str):
        """Вводит полученный текст в поле.
        :return: Возвращает среднюю скорость ввода текста и количество ошибок.
        """
        speed_list = []
        error_count = 0
        time.sleep(5)  # Необходимо для избежания ошибки ElementNotInteractable
        for word in text.split():
            i = 0
            while True:
                time.sleep(random.uniform(0.01, 1.9))
                self.element_is_visible(self.locators.TEXT_INTPUT).send_keys(word[i])
                speed_list.append(self.get_speed())
                error_count = self.get_error()
                if self.check_error():
                    i += 1
                    if i >= len(word):
                        break
                else:
                    self.element_is_visible(self.locators.TEXT_INTPUT).send_keys(Keys.BACKSPACE)
            self.element_is_visible(self.locators.TEXT_INTPUT).send_keys(" ")
        return sum(speed_list)/len(speed_list), error_count

    def get_speed(self):
        """Получает текущую скорость набора текста.
        """
        return int(self.element_is_visible(self.locators.SPEED_LABEL).text)

    def get_error(self):
        """Получает текущее количество ошибок.
        """
        return int(self.element_is_visible(self.locators.ERROR_LABEL).text)

    def check_error(self):
        try:
            self.element_is_visible(self.locators.FIX_TYPO, random.uniform(0.4, 0.8))
            return False
        except TimeoutException:
            return True

