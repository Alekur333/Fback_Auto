import pytest
import time
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from pages.tempmail_page import TempMailPage
from pages.ineed_chat_page import IneedChatPage
from pages.locators import IneedchatPageLocators, TempmailPageLocators, SigninPageLocators, SignupPageLocators
from pages.create_app_page import CreateAppPage
from pages.apps_functions_page import AppsFunctionsPage
from pages.apps_title_page import AppsTitlePage
from pages.apps_color_page import AppsColorPage
from pages.apps_demo_page import AppsDemoPage
from test_lk_auth import TestLkSignup

landing_link = (IneedchatPageLocators.INEED_CHAT_LINK)
# link_tempmail = (TempmailPageLocators.TEMPMAIL_LINK)
# link_signup = (SignupPageLocators.SIGNUP_LINK)
# link_signin = (SigninPageLocators.SIGNIN_LINK)
# regname = "Feed Test"
# regphone = '9111111111'

@pytest.mark.smoke
@pytest.mark.assembleapp
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
        apps_functions_page.go_to_news_in_detail_window()
        # time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_news_function_check_btn()
        apps_functions_page.check_news_function()
        apps_functions_page.should_be_news_function_uncheck_btn()
        apps_functions_page.uncheck_news_function()
        apps_functions_page.check_news_function()
        # time.sleep(2)

        # Выбрать опцию акции
        apps_functions_page.should_be_action_in_detail_btn()
        apps_functions_page.go_to_action_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_action_function_check_btn()
        apps_functions_page.check_action_function()
        apps_functions_page.should_be_action_function_uncheck_btn()
        apps_functions_page.uncheck_action_function()
        apps_functions_page.check_action_function()
        # time.sleep(2)
        
        # Выбрать опцию чаты
        apps_functions_page.should_be_chats_in_detail_btn()
        apps_functions_page.go_to_chats_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_chats_function_check_btn()
        apps_functions_page.check_chats_function()
        apps_functions_page.should_be_chats_function_uncheck_btn()
        apps_functions_page.uncheck_chats_function()
        apps_functions_page.check_chats_function()
        # time.sleep(2)

        # Выбрать опцию КАТАЛОГ
        apps_functions_page.should_be_catalog_in_detail_btn()
        apps_functions_page.go_to_catalog_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_catalog_function_check_btn()
        apps_functions_page.check_catalog_function()
        apps_functions_page.should_be_catalog_function_uncheck_btn()
        apps_functions_page.uncheck_catalog_function()
        apps_functions_page.check_catalog_function()

        # Выбрать опцию ОНЛАЙН-ЗАКАЗ
        # apps_functions_page.should_be_order_in_detail_btn()
        # apps_functions_page.go_to_order_in_detail_window()
        # time.sleep(2)
        # apps_functions_page.close_functions_in_detail_window_btn()
        # apps_functions_page.should_be_order_function_check_btn()
        # apps_functions_page.check_order_function()
        # apps_functions_page.should_be_order_function_uncheck_btn()
        # apps_functions_page.uncheck_order_function()
        # apps_functions_page.check_order_function()


        # Выбрать опцию ОНЛАЙН-ЗАПИСЬ
        apps_functions_page.should_be_appointment_in_detail_btn()
        apps_functions_page.go_to_appointment_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_appointment_function_check_btn()
        apps_functions_page.check_appointment_function()
        apps_functions_page.should_be_appointment_function_uncheck_btn()
        apps_functions_page.uncheck_appointment_function()
        apps_functions_page.check_appointment_function()

        # Выбрать опцию ОЦЕНКИ
        apps_functions_page.should_be_recall_in_detail_btn()
        apps_functions_page.go_to_recall_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_recall_function_check_btn()
        apps_functions_page.check_recall_function()
        apps_functions_page.should_be_recall_function_uncheck_btn()
        apps_functions_page.uncheck_recall_function()
        apps_functions_page.check_recall_function()

        # Выбрать опцию ПЕРЕЗВОНИТЬ
        apps_functions_page.should_be_callback_in_detail_btn()
        apps_functions_page.go_to_callback_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_callback_function_check_btn()
        apps_functions_page.check_callback_function()
        apps_functions_page.should_be_callback_function_uncheck_btn()
        apps_functions_page.uncheck_callback_function()
        apps_functions_page.check_callback_function()

        time.sleep(2)
        # Выбрать опцию ЛОЯЛЬНОСТЬ
        apps_functions_page.should_be_bonuscard_in_detail_btn()
        apps_functions_page.go_to_bonuscard_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_bonuscard_function_check_btn()
        apps_functions_page.check_bonuscard_function()
        apps_functions_page.should_be_bonuscard_function_uncheck_btn()
        apps_functions_page.uncheck_bonuscard_function()
        apps_functions_page.check_bonuscard_function()
        
        # Выбрать опцию ЗАЯВКИ
        apps_functions_page.should_be_statement_in_detail_btn()
        apps_functions_page.go_to_statement_in_detail_window()
        time.sleep(2)
        apps_functions_page.close_functions_in_detail_window_btn()
        apps_functions_page.should_be_statement_function_check_btn()
        apps_functions_page.check_statement_function()
        apps_functions_page.should_be_statement_function_uncheck_btn()
        apps_functions_page.uncheck_statement_function()
        apps_functions_page.check_statement_function()

        # Нажать кнопку Продолжить
        apps_functions_page.should_be_functions_done_btn()
        apps_functions_page.functions_done()

        # Ввести название приложения
        title_page = AppsTitlePage(browser, browser.current_url)
        title_page.should_be_title_field()
        title_page.insert_title()
        title_page.complete_title()
        title_page.image_download_skip()

        # Выбрать цвет приложения
        color_page = AppsColorPage(browser, browser.current_url)
        color_page.should_be_apps_color()
        color_page.select_apps_color()
        color_page.should_be_color_complete_btn()
        color_page.color_complete()

        # Сохранить код приложения
        demo_page = AppsDemoPage(browser, browser.current_url)
        demo_page.demo_app_store_code()

        # Сохранить демо приложение
        demo_page.should_be_demo_safe_btn()
        demo_page.demo_safe_btn()

        # Перейти к регистрации
        demo_page.should_be_signin_btn_for_demo_app_on_popup_window()
        demo_page.should_be_signup_btn_for_demo_app_on_popup_window()
        demo_page.should_be_close_popup_window_btn()
        demo_page.signup_for_demo_app_on_popup_window()

        time.sleep(10)




