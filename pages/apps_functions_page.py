import time
from .base_page import BasePage
from .locators import AppsFunctionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsFunctionsPage(BasePage):

    def should_be_functions_done_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.FUNCTIONS_DONE_BTN)), \
            "Кнопка ПРОДОЛЖИТЬ на странице функций не найдена"
        self.browser.find_element(*AppsFunctionsLocators.FUNCTIONS_DONE_BTN).click()

    def help_window_close(self):
        if WebDriverWait(self.browser, 3).until(ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON)):
            self.browser.find_element(*AppsFunctionsLocators.HELP_BUTTON).click()
        else:
            pass

    def should_be_help_chat(self):
        # self.browser.find_element(*AppsFunctionsLocators.HELP_BUTTON).click()
        # time.sleep(5)
        # self.browser.find_element(*AppsFunctionsLocators.HELP_BUTTON).click()
        WebDriverWait(self.browser, 3).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON)).click()

        # self.browser.find_element(AppsFunctionsLocators.INPUT_MESSAGE).send_keys("hello")
        time.sleep(3)
        self.browser.find_element(AppsFunctionsLocators.HELP_BUTTON).click()
        time.sleep(3)

    def should_be_close_functions_in_detail_window_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN)), \
            "Кнопка Закрыть окно 'ПОДРОБНЕЕ о функции' не найдена"

    def close_functions_in_detail_window_btn(self):
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN)).click()
        # self.browser.find_element(*AppsFunctionsLocators.FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN).click()


    # Функция "Отправлять клиентам новости и проводить опросы"
    def select_news_function(self):
        self.should_be_news_in_detail_btn()
        self.go_to_news_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_news_function_check_btn()
        self.check_news_function()
        self.should_be_news_function_uncheck_btn()
        self.uncheck_news_function()
        self.check_news_function()

    def should_be_news_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о новостях не найдена"
        # WebDriverWait(self.browser, 10).until \
        #     (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_IN_DETAIL_BTN)).click()
        # self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_BTN).click()

    def go_to_news_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_BTN).click()
        # WebDriverWait(self.browser, 10).until \
        #     (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_IN_DETAIL_BTN)).click()

    def should_be_news_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_news_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.NEWS_CHECK).click()
        # news = self.browser.find_element(*AppsFunctionsLocators.NEWS_CHECK)
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", news)
        # news.click()
        WebDriverWait(self.browser, 10).until \
                 (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_CHECK)).click()

    def should_be_news_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_UNCHECK)), \
            "Кнопка выключить функцию НОВОСТИ не найдена"

    def uncheck_news_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.NEWS_UNCHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.NEWS_UNCHECK)).click()


    # Функция "Проводить с клиентами акции"
    def select_action_function(self):
        self.should_be_action_in_detail_btn()
        self.go_to_action_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_action_function_check_btn()
        self.check_action_function()
        self.should_be_action_function_uncheck_btn()
        self.uncheck_action_function()
        self.check_action_function()
    
    def should_be_action_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_action_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.ACTION_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_IN_DETAIL_BTN)).click()

    def should_be_action_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_CHECK)), \
            "Кнопка включить функцию АКЦИИ не найдена"

    def check_action_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.ACTION_CHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_CHECK)).click()
        # action = self.browser.find_element(*AppsFunctionsLocators.ACTION_CHECK)
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", action)
        # action.click()

    def should_be_action_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_UNCHECK)), \
            "Кнопка выключить функцию АКЦИИ не найдена"

    def uncheck_action_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.ACTION_UNCHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.ACTION_UNCHECK)).click()

    # Функция "Разговаривать с клиентами в чате"
    def select_chats_function(self):
        self.should_be_chats_in_detail_btn()
        self.go_to_chats_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_chats_function_check_btn()
        self.check_chats_function()
        self.should_be_chats_function_uncheck_btn()
        self.uncheck_chats_function()
        self.check_chats_function()
    
    def should_be_chats_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о чатах не найдена"

    def go_to_chats_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.CHATS_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_IN_DETAIL_BTN)).click()

    def should_be_chats_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_CHECK)), \
            "Кнопка включить функцию ЧАТЫ не найдена"

    def check_chats_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.CHATS_CHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_CHECK)).click()

    def should_be_chats_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_UNCHECK)), \
            "Кнопка выключить функцию ЧАТЫ не найдена"

    def uncheck_chats_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.CHATS_UNCHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CHATS_UNCHECK)).click()

    # Функция "Показывать клиентам каталог товаров и услуг"
    def select_catalog_function(self):
        self.should_be_catalog_in_detail_btn()
        self.go_to_catalog_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_catalog_function_check_btn()
        self.check_catalog_function()
        time.sleep(1)
        self.should_be_catalog_function_uncheck_btn()
        self.uncheck_catalog_function()
        time.sleep(1)
        self.check_catalog_function()
    
    def should_be_catalog_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об КАТАЛОГЕ не найдена"

    def go_to_catalog_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.CATALOG_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_IN_DETAIL_BTN)).click()

    def should_be_catalog_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_CHECK)), \
            "Кнопка включить функцию КАТАЛОГ не найдена"

    def check_catalog_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.CATALOG_CHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_CHECK)).click()
        

    def should_be_catalog_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_UNCHECK)), \
            "Кнопка выключить функцию КАТАЛОГ не найдена"

    def uncheck_catalog_function(self):
        # self.browser.find_element(*AppsFunctionsLocators.CATALOG_UNCHECK).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CATALOG_UNCHECK)).click()

    # Функция "Чтобы клиенты могли оформлять онлайн-заказы"
    def select_order_function(self):
        self.should_be_order_in_detail_btn()
        # self.go_to_order_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_order_function_check()
        # self.check_order_function()
        self.should_be_close_ordrer_additional_parameter_btn()
        # self.should_be_order_function_uncheck_btn()
        # self.uncheck_order_function()
        self.should_be_order_function_check()
        self.should_be_order_function_check()
        self.should_be_delivery_check()
        # time.sleep(1)
        self.should_be_selfexport_check()
        # time.sleep(1)
        self.should_be_online_pay_check()
        # time.sleep(1)
        self.should_be_apply_additional_parameter_btn()

        
    def should_be_order_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ORDER_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об Онлайн-заказы не найдена"
        self.browser.find_element(*AppsFunctionsLocators.ORDER_IN_DETAIL_BTN).click()

    # def go_to_order_in_detail_window(self):
    #     # self.browser.find_element(*AppsFunctionsLocators.ORDER_IN_DETAIL_BTN).click()
    #     WebDriverWait(self.browser, 10).until \
    #         (ec.element_to_be_clickable(AppsFunctionsLocators.ORDER_IN_DETAIL_BTN)).click()

    def should_be_order_function_check(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ORDER_CHECK)), \
            "Кнопка включить функцию Онлайн-заказы не найдена"
        self.browser.find_element(*AppsFunctionsLocators.ORDER_CHECK).click()

    # def check_order_function(self):
    #     self.browser.find_element(*AppsFunctionsLocators.ORDER_CHECK).click()

    def should_be_order_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.ORDER_UNCHECK)), \
            "Кнопка выключить функцию Онлайн-заказы не найдена"
        self.browser.find_element(*AppsFunctionsLocators.ORDER_UNCHECK).click()

    # def uncheck_order_function(self):
    #     self.browser.find_element(*AppsFunctionsLocators.ORDER_UNCHECK).click()

    def should_be_close_ordrer_additional_parameter_btn(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.CLOSE_ADDITIONAL_PARAMETER_BTN)), \
            "Кнопка закрыть окно доп.параметры Онлайн-заказов не найдена"
        self.browser.find_element(*AppsFunctionsLocators.CLOSE_ADDITIONAL_PARAMETER_BTN).click()

    def should_be_delivery_check(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.presence_of_element_located(AppsFunctionsLocators.DELIVERY_CHECK)), \
            "Кнопка включить функцию доставки не найдена"
        self.browser.find_element(*AppsFunctionsLocators.DELIVERY_CHECK).click()

    def should_be_selfexport_check(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.SELF_EXPORT_CHECK)), \
            "Кнопка включить функцию самовывоза не найдена"
        self.browser.find_element(*AppsFunctionsLocators.SELF_EXPORT_CHECK).click()

    def should_be_online_pay_check(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.ONLINE_PAY_CHECK)), \
            "Кнопка включить функцию онлайн-оплаты не найдена"
        self.browser.find_element(*AppsFunctionsLocators.ONLINE_PAY_CHECK).click()

    def should_be_apply_additional_parameter_btn(self):
        assert WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.APPLY_ADDITIONAL_PARAMETER_BTN)), \
            "Кнопка Применить доп.параметры не найдена"
        self.browser.find_element(*AppsFunctionsLocators.APPLY_ADDITIONAL_PARAMETER_BTN).click()

    # Функция "Использовать онлайн-запись"
    def select_appointment_function(self):
        self.should_be_appointment_in_detail_btn()
        self.go_to_appointment_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_appointment_function_check_btn()
        self.check_appointment_function()
        self.should_be_appointment_function_uncheck_btn()
        self.uncheck_appointment_function()
        self.check_appointment_function()   
    
    def should_be_appointment_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об онлайн-записи не найдена"
        # assert WebDriverWait(self.browser, 10).until \
        #     (ec.element_to_be_clickable(AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN)).click() \
        #      "Кнопка ПОДРОБНЕЕ об акциях не найдена"

    def go_to_appointment_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN).click()
        # WebDriverWait(self.browser, 10).until \
        #     (ec.element_to_be_clickable(AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN)).click()
        # appointment_det = self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_IN_DETAIL_BTN)
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", appointment_det)
        # appointment_det.click()

    def should_be_appointment_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.APPOINTMENT_CHECK)), \
            "Кнопка включить функцию онлайн-запись не найдена"

    def check_appointment_function(self):
        # appointment = self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_CHECK)
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", appointment)
        # appointment.click()
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_CHECK).click()

    def should_be_appointment_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.APPOINTMENT_UNCHECK)), \
            "Кнопка выключить функцию онлайн-запись не найдена"

    def uncheck_appointment_function(self):
        self.browser.find_element(*AppsFunctionsLocators.APPOINTMENT_UNCHECK).click()

    # Функция "Получать оценки качества обслуживания, работы персонала или продукта"
    def select_recall_function(self):
        self.should_be_recall_in_detail_btn()
        self.go_to_recall_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_recall_function_check_btn()
        self.check_recall_function()
        self.should_be_recall_function_uncheck_btn()
        self.uncheck_recall_function()
        self.check_recall_function()   
    
    def should_be_recall_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.RECALL_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об оценках не найдена"

    def go_to_recall_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.RECALL_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.RECALL_IN_DETAIL_BTN)).click()

    def should_be_recall_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.RECALL_CHECK)), \
            "Кнопка включить функцию оценки не найдена"

    def check_recall_function(self):
        self.browser.find_element(*AppsFunctionsLocators.RECALL_CHECK).click()

    def should_be_recall_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.RECALL_UNCHECK)), \
            "Кнопка выключить функцию оценки не найдена"

    def uncheck_recall_function(self):
        self.browser.find_element(*AppsFunctionsLocators.RECALL_UNCHECK).click()

    # Функция "Получать от клиентов заявки на обратный звонок"
    def select_callback_function(self):
        self.should_be_callback_in_detail_btn()
        self.go_to_callback_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_callback_function_check_btn()
        self.check_callback_function()
        self.should_be_callback_function_uncheck_btn()
        self.uncheck_callback_function()
        self.check_callback_function()   
    
    def should_be_callback_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ об обратный звонок не найдена"

    def go_to_callback_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN).click()
        # try:
        #     WebDriverWait(self.browser, 3).\
        #         until(ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON_CLOSE)).click().\
        #         find_element(*AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN).click()
        # except:
        #     self.browser.find_element(*AppsFunctionsLocators.CALLBACK_IN_DETAIL_BTN).click()

    def should_be_callback_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CALLBACK_CHECK)), \
            "Кнопка включить функцию обратный звонок не найдена"

    def check_callback_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_CHECK).click()
        # try:
        #     WebDriverWait(self.browser, 3).\
        #         until(ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON_CLOSE)).click().\
        #         find_element(*AppsFunctionsLocators.CALLBACK_CHECK).click()
        # except:
        #     self.browser.find_element(*AppsFunctionsLocators.CALLBACK_CHECK).click()

    def should_be_callback_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.CALLBACK_UNCHECK)), \
            "Кнопка выключить функцию обратный звонок не найдена"

    def uncheck_callback_function(self):
        self.browser.find_element(*AppsFunctionsLocators.CALLBACK_UNCHECK).click()
        # try:
        #     WebDriverWait(self.browser, 3).\
        #         until(ec.element_to_be_clickable(AppsFunctionsLocators.HELP_BUTTON_CLOSE)).click().\
        #         find_element(*AppsFunctionsLocators.CALLBACK_UNCHECK).click()
        # except:
        #     self.browser.find_element(*AppsFunctionsLocators.CALLBACK_UNCHECK).click()

    # Функция "Использовать систему лояльности"
    def select_bonuscard_function(self):
        self.should_be_bonuscard_in_detail_btn()
        self.go_to_bonuscard_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_bonuscard_function_check_btn()
        self.check_bonuscard_function()
        self.should_be_bonuscard_function_uncheck_btn()
        self.uncheck_bonuscard_function()
        self.check_bonuscard_function()   
    
    def should_be_bonuscard_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.BONUSCARD_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о лояльности не найдена"

    def go_to_bonuscard_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.BONUSCARD_IN_DETAIL_BTN)).click()

    def should_be_bonuscard_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.BONUSCARD_CHECK)), \
            "Кнопка включить функцию лояльности не найдена"

    def check_bonuscard_function(self):
        self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_CHECK).click()

    def should_be_bonuscard_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.BONUSCARD_UNCHECK)), \
            "Кнопка выключить функцию лояльности не найдена"

    def uncheck_bonuscard_function(self):
        self.browser.find_element(*AppsFunctionsLocators.BONUSCARD_UNCHECK).click()

    # Функция "Получать заявки от клиентов"
    def select_statement_function(self):
        self.should_be_statement_in_detail_btn()
        self.go_to_statement_in_detail_window()
        time.sleep(1)
        self.close_functions_in_detail_window_btn()
        time.sleep(1)
        self.should_be_statement_function_check_btn()
        self.check_statement_function()
        self.should_be_statement_function_uncheck_btn()
        self.uncheck_statement_function()
        self.check_statement_function()   
    
    def should_be_statement_in_detail_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.STATEMENT_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о заявках не найдена"

    def go_to_statement_in_detail_window(self):
        # self.browser.find_element(*AppsFunctionsLocators.STATEMENT_IN_DETAIL_BTN).click()
        WebDriverWait(self.browser, 10).until \
            (ec.element_to_be_clickable(AppsFunctionsLocators.STATEMENT_IN_DETAIL_BTN)).click()

    def should_be_statement_function_check_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.STATEMENT_CHECK)), \
            "Кнопка включить функцию заявки не найдена"

    def check_statement_function(self):
        self.browser.find_element(*AppsFunctionsLocators.STATEMENT_CHECK).click()

    def should_be_statement_function_uncheck_btn(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.element_to_be_clickable(AppsFunctionsLocators.STATEMENT_UNCHECK)), \
            "Кнопка выключить функцию заявки не найдена"

    def uncheck_statement_function(self):
        self.browser.find_element(*AppsFunctionsLocators.STATEMENT_UNCHECK).click()