from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Класс базовой страницы и её методов, которые будут наследовать классы
       других страниц для работы с их элементами.
    """
    def __init__(self, driver, url=''):
        """Инициализация переменных для открытия страницы.
        :param driver: Вызывает указанный драйвер.
        :param url: Адрес страницы.
        """
        self.driver = driver
        self.url = url

    def open_url(self):
        """Открытие страницы по адресу.
        """
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=3):
        """Ожидает загрузку и появление одного элемента на странице, для взаимодействия с ним.
        :param locator: Указание на место элемента в html-документе(xpath, css-селектор и т.д.)
        :param timeout: Время ожидания загрузки элемента. По умолчанию 3 секунды.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_present(self, locator, timeout=3):
        """Ожидает загрузку в DOM одного элемента на странице, для взаимодействия с ним.
        :param locator: Указание на место элемента в html-документе(xpath, css-селектор и т.д.)
        :param timeout: Время ожидания загрузки элемента. По умолчанию 3 секунды.
        """
        return WebDriverWait(self.driver, timeout).until((EC.presence_of_element_located(locator)))
