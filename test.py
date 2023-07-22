from page.main_page import MainPage
from page.go_page import GoPage


class TestKeyboardChampion:

    def test_keyboard_champion(self, driver):
        main_page = MainPage(driver, "https://klavogonki.ru/")
        main_page.open_url()
        main_page.quick_start_title_click()

        go_page = GoPage(driver)
        go_page.close_manual_button_click()
        go_page.start_game_button_click()
        speed, err = go_page.set_text(go_page.get_text())

        print(f"Скорость набора текста: {speed:.2f}\nКоличество ошибок: {err}")
        assert speed > 400, 'Скорость ниже требуемой(400 зн/мин)'
        assert err == 0, 'В тексте есть ошибки'
