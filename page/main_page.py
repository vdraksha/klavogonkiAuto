from page.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators

    def quick_start_title_click(self):
        """Нажимает на заголовок 'Быстрый старт'
        """
        self.element_is_visible(self.locators.QUICK_START_TITLE).click()
