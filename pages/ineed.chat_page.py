from .base_page import BasePage
from .locators import IneedchatPageLocators

class IneedChat(BasePage):

    def should_be_main_menu_open_btn(self):
        try:
            self.browser.find_element(*IneedchatPageLocators.MAIN_MENU_OPEN)
            result = True
        except:
            result = False
        assert result == True, "Кнопка МЕНЮ не найдена"

    def should_be_main_menu_close_btn(self):
        try:
            self.browser.find_element(*IneedchatPageLocators.MAIN_MENU_CLOSE)
            result = True
        except:
            result = False
        assert result == True, "Кнопка Закрыть МЕНЮ не найдена"

    def should_be_clients_entrance_btn_in_main_menu(self):
        try:
            self.browser.find_element(*IneedchatPageLocators.MAIN_MENU_CLIENTS_ENTRANCE)
            result = True
        except:
            result = False
        assert result == True, "Кнопка 'Вход для клиентов' не найдена"
