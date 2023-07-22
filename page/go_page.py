from page.base_page import BasePage
from locators.go_page_locators import GoPageLocators
from selenium.common import TimeoutException


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
        while True:
            try:
                timeout = self.element_is_present(self.locators.START_GAME_WAITING).text[3:]
                int(timeout)
            except ValueError:
                pass
            else:
                break
        return self.element_is_visible(self.locators.TEXT_OUTPUT, timeout).text

    def set_text(self, text):
        """Вводит полученный текст в поле.
        :return: Возвращает среднюю скорость ввода текста и количество ошибок.
        """
        speed_list = []
        input_field = self.element_is_visible(self.locators.TEXT_INTPUT)
        for symbol in text:
            input_field.send_keys(self.check_symbol(symbol))
            speed_list.append(self.get_speed())
        return sum(speed_list)/len(speed_list), self.get_error()

    def get_speed(self):
        """Получает текущую скорость набора текста.
        """
        return int(self.element_is_visible(self.locators.SPEED_LABEL).text)

    def get_error(self):
        """Получает количество ошибок.
        """
        return int(self.element_is_visible(self.locators.ERROR_LABEL).text)

    def check_symbol(self, symbol):
        """Проверяет символ на соответствие латинице в юникоде.
        :return: Возвращает похожий по написанию символ в кириллице.
        """
        if symbol in ['-', ',', '.', ' ', ':', '!', '»', '«']:
            return symbol
        num = ord(symbol)
        if num == 99:   # c
            return chr(num + 990)
        if num == 72:   # H
            return chr(num + 981)
        if num < 123:   # 122 = z
            return chr(num + 975)
        return chr(num)

