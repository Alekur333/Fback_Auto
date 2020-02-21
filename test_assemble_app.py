import pytest
import time
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from pages.tempmail_page import TempMailPage
from pages.ineed_chat_page import IneedChatPage
from pages.locators import IneedchatPageLocators, AppsFunctionsLocators, TempmailPageLocators, SigninPageLocators, SignupPageLocators
from pages.create_app_page import CreateAppPage
from pages.apps_functions_page import AppsFunctionsPage
from pages.apps_title_page import AppsTitlePage
from pages.apps_color_page import AppsColorPage
from pages.apps_demo_page import AppsDemoPage
from pages.apps_page import AppsPage
# from test_lk_auth import TestLkSignup

landing_link = (IneedchatPageLocators.INEED_CHAT_LINK)
functions_link = (AppsFunctionsLocators.APPS_FUNCTIONS_LINK)
link_tempmail = (TempmailPageLocators.TEMPMAIL_LINK)
# link_signup = (SignupPageLocators.SIGNUP_LINK)
# link_signin = (SigninPageLocators.SIGNIN_LINK)

regname = "FeedBack Test"
regphone = '9111111111'

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
        apps_functions_page.select_news_function()

        # Выбрать опцию акции
        # apps_functions_page.select_action_function()
        #
        # # Выбрать опцию чаты
        # apps_functions_page.select_chats_function()
        #
        # # Выбрать опцию КАТАЛОГ
        # apps_functions_page.select_catalog_function()
        #
        # # Выбрать опцию ОНЛАЙН-ЗАКАЗ
        # # apps_functions_page.select_order_function()
        #
        # # Выбрать опцию ОНЛАЙН-ЗАПИСЬ
        # apps_functions_page.select_appointment_function()
        #
        # # Выбрать опцию ОЦЕНКИ
        # apps_functions_page.select_recall_function()
        #
        # # Выбрать опцию ПЕРЕЗВОНИТЬ
        # apps_functions_page.select_callback_function()
        #
        # # Выбрать опцию ЛОЯЛЬНОСТЬ
        # apps_functions_page.select_bonuscard_function()
        #
        # # Выбрать опцию ЗАЯВКИ
        # apps_functions_page.select_statement_function()

        # Нажать кнопку Продолжить
        apps_functions_page.should_be_functions_done_btn()
        # apps_functions_page.functions_done()
        time.sleep(1)

        # Ввести название приложения
        title_page = AppsTitlePage(browser, browser.current_url)
        title_page.should_be_title_field()
        title_page.insert_title()
        title_page.complete_title()
        title_page.image_download_skip()
        time.sleep(1)

        # Выбрать цвет приложения
        color_page = AppsColorPage(browser, browser.current_url)
        color_page.set_apps_color()

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

        window1 = browser.window_handles[0]

        signup_page = SignUpPage(browser, browser.current_url)


        # Открыть страницу временной почты
        browser.execute_script("window.open('{}', '_blank');".format(link_tempmail))
        window2 = browser.window_handles[1]
        browser.switch_to.window(window2)
        tempmail_page = TempMailPage(browser, browser.current_url)

        # взять мейл для регистрации
        temp_mail = tempmail_page.get_tempmail()

        # Открыть страницу регистрации и зарегистрироваться
        browser.switch_to.window(window1)
        signup_page.should_be_signup_page(regname, temp_mail, regphone)

        # Возврат в окно почты проверить наличие письма и взять пароль
        browser.switch_to.window(window2)
        temp_password = tempmail_page.get_letter_password(browser)

        # Проверяем переход на страницу входа после успешной регистрации
        # Заполняем обязательные поля и входим
        browser.switch_to.window(window2)
        signin_page = SignInPage(browser, browser.current_url)
        signin_page.should_be_signin_page(temp_mail, temp_password)

        # Проверяем переход на страницу приложений после успешного входа
        signin_page.should_be_apps_page()
        apps_page = AppsPage(browser, browser.current_url)
        apps_page.should_be_remove_app_btn()
        apps_page.remove_app()

        # Удаляем созданное приложение


        # time.sleep(5)

@pytest.mark.smoke
@pytest.mark.appsfunctions
class TestAssembleAppFunctions:

    def test_apps_functions(self, browser):
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
        apps_functions_page.select_news_function()
        time.sleep(1)
        # # Выбрать опцию акции
        apps_functions_page.select_action_function()
        time.sleep(1)
        # # Выбрать опцию чаты
        apps_functions_page.select_chats_function()
        time.sleep(1)
        # # Выбрать опцию КАТАЛОГ
        apps_functions_page.select_catalog_function()
        time.sleep(1)
        # Выбрать опцию ОНЛАЙН-ЗАКАЗ
        apps_functions_page.select_order_function()
        time.sleep(1)
        # # Выбрать опцию ОНЛАЙН-ЗАПИСЬ
        apps_functions_page.select_appointment_function()
        time.sleep(1)
        # # Выбрать опцию ОЦЕНКИ
        apps_functions_page.select_recall_function()
        time.sleep(1)
        # # Выбрать опцию ПЕРЕЗВОНИТЬ
        apps_functions_page.select_callback_function()
        time.sleep(1)
        # # Выбрать опцию ЛОЯЛЬНОСТЬ
        apps_functions_page.select_bonuscard_function()
        time.sleep(1)
        # # Выбрать опцию ЗАЯВКИ
        apps_functions_page.select_statement_function()
        time.sleep(1)
        # # Нажать кнопку Продолжить
        apps_functions_page.should_be_functions_done_btn()
        # apps_functions_page.functions_done()

