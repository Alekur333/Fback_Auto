from .base_page import BasePage
from .locators import AppsFunctionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsFunctionsPage(BasePage):

    def should_be_functions_done_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.FUNCTIONS_DONE_BTN)), \
            "Кнопка ПРОДОЛЖИТЬ на странице функций не найдена"

    def functions_done(self):
        self.browser.find_element(*AppsFunctionsLocators.FUNCTIONS_DONE_BTN).click()

    def should_be_close_functions_in_detail_window_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN)), \
            "Кнопка Закрыть окно 'ПОДРОБНЕЕ о функции' не найдена"

    def close_functions_in_detail_window_btn(self):
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN)).click()
        # self.browser.find_element(*AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN).click()

    # Функция "Отправлять клиентам новости и проводить опросы"
    def should_be_news_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о новостях не найдена"

    def go_to_news_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_BTN).click()

    def should_be_news_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_news_function(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_CHECK).click()

    def should_be_news_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_news_function(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_UNCHECK).click()


    # Функция "Проводить с клиентами акции"
    def should_be_action_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ACTION_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_action_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.ACTION_IN_DETAIL_BTN).click()

    def should_be_action_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ACTION_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_action_function(self):
        self.browser.find_element(*AppsFunctionsLocators.ACTION_CHECK).click()

    def should_be_action_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ACTION_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_action_function(self):
        self.browser.find_element(*AppsFunctionsLocators.ACTION_UNCHECK).click()

    # Функция "Разговаривать с клиентами в чате"
    def should_be_chats_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CHATS_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_chats_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.CHATS_IN_DETAIL_BTN).click()

    def should_be_chats_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CHATS_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_chats_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CHATS_CHECK).click()

    def should_be_chats_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CHATS_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_chats_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CHATS_UNCHECK).click()

    # Функция "Показывать клиентам каталог товаров и услуг"
    def should_be_catalog_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CATALOG_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_catalog_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.CATALOG_IN_DETAIL_BTN).click()

    def should_be_catalog_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CATALOG_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_catalog_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CATALOG_CHECK).click()

    def should_be_catalog_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CATALOG_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_catalog_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CATALOG_UNCHECK).click()

    # Функция "Чтобы клиенты могли оформлять онлайн-заказы"
    def should_be_order_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ORDER_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_order_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.ORDER_IN_DETAIL_BTN).click()

    def should_be_order_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ORDER_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_order_function(self):
        self.browser.find_element(*AppsFunctionsLocators.ORDER_CHECK).click()

    def should_be_order_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.ORDER_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_order_function(self):
        self.browser.find_element(*AppsFunctionsLocators.ORDER_UNCHECK).click()

   # Функция "Использовать онлайн-запись"
    def should_be_appointment_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_appointment_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN).click()

    def should_be_appointment_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.APPOINTMENT_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_appointment_function(self):
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_CHECK).click()

    def should_be_appointment_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.APPOINTMENT_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_appointment_function(self):
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_UNCHECK).click()

    # Функция "Получать оценки качества обслуживания, работы персонала или продукта"
    def should_be_recall_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.RECALL_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_recall_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.RECALL_IN_DETAIL_BTN).click()

    def should_be_recall_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.RECALL_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_recall_function(self):
        self.browser.find_element(*AppsFunctionsLocators.RECALL_CHECK).click()

    def should_be_recall_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.RECALL_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_recall_function(self):
        self.browser.find_element(*AppsFunctionsLocators.RECALL_UNCHECK).click()

    # Функция "Получать от клиентов заявки на обратный звонок"
    def should_be_callback_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_callback_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN).click()

    def should_be_callback_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CALLBACK_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_callback_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_CHECK).click()

    def should_be_callback_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.CALLBACK_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_callback_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_UNCHECK).click()

    # Функция "Использовать систему лояльности"
    def should_be_bonuscard_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.BONUSCARD_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_bonuscard_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_IN_DETAIL_BTN).click()

    def should_be_bonuscard_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.BONUSCARD_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_bonuscard_function(self):
        self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_CHECK).click()

    def should_be_bonuscard_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.BONUSCARD_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_bonuscard_function(self):
        self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_UNCHECK).click()

    # Функция "Получать заявки от клиентов"
    def should_be_statement_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.STATEMENT_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_statement_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.STATEMENT_IN_DETAIL_BTN).click()

    def should_be_statement_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.STATEMENT_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_statement_function(self):
        self.browser.find_element(*AppsFunctionsLocators.STATEMENT_CHECK).click()

    def should_be_statement_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.STATEMENT_UNCHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def uncheck_statement_function(self):
        self.browser.find_element(*AppsFunctionsLocators.STATEMENT_UNCHECK).click()