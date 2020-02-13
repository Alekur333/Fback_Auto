import pytest
import time
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from pages.tempmail_page import TempMailPage
from pages.ineed_chat_page import IneedChatPage
from pages.locators import IneedchatPageLocators
from pages.create_app_page import CreateAppPage
from pages.apps_functions_page import AppsFunctionsPage
from pages.locators import AppsFunctionsLocators
from pages.apps_title_page import AppsTitlePage

landing_link = (IneedchatPageLocators.INEED_CHAT_LINK)

class TestAssembleAppFull:

    def test_assemble_app(self, browser):
        # Открыть лэндинг
        ineedchat_page = IneedChatPage(browser, landing_link)
        ineedchat_page.open()
        # Открыть меню
        ineedchat_page.should_be_clients_entrance_btn_in_main_menu()
        ineedchat_page.go_to_main_menu()
        # Сделать вход для клиентов
        ineedchat_page.should_be_main_menu_close_btn()
        ineedchat_page.should_be_clients_entrance_btn_in_main_menu()
        ineedchat_page.go_to_clients_entrance_in_main_menu()
        # Открыть страницу создания приложения
        create_app_page = CreateAppPage(browser, browser.current_url)
        create_app_page.should_be_create_app_btn()
        create_app_page.go_to_create_app_page()
        apps_functions_page = AppsFunctionsPage(browser, browser.current_url)
        # Выбрать опцию новости и опросы
        apps_functions_page.should_be_news_in_detail_btn()
        # apps_functions_page.go_to_news_in_detail_window()
        # time.sleep(2)
        # apps_functions_page.close_news_in_detail_window()
        apps_functions_page.should_be_news_function_checkbox()
        apps_functions_page.check_news_function()

        # Нажать кнопку Продолжить
        apps_functions_page.should_be_functions_done_btn()
        apps_functions_page.functions_done()

        # Ввести название приложения
        title_page = AppsTitlePage(browser, browser.current_url)
        title_page.should_be_title_field()
        title_page.insert_title()
        title_page.complete_title()
        title_page.image_download_skip()

        time.sleep(2)

