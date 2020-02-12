from .base_page import BasePage
from .locators import AppsFunctionsLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsFunctionsPage(BasePage):

    # Функция "Новости и опросы"
    def should_be_news_in_detail_btn(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_IN_DETAIL_BTN)), \
            "Кнопка ПОДРОБНЕЕ о новостях не найдена"

    def go_to_news_in_detail_window(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_BTN).click()

    def should_be_close_news_in_detail_btn(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_IN_DETAIL_CLOSE)), \
            "Кнопка Закрыть окно 'ПОДРОБНЕЕ о новостях' не найдена"

    def close_news_in_detail_window(self):
        # window2 = self.browser.window_handles[0]
        # self.browser.switch_to.window(window2)
        self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_CLOSE).click()
        # close = self.browser.find_element(*AppsFunctionsLocators.NEWS_IN_DETAIL_CLOSE)
        # self.browser.execute_script("return arguments[0].scrollIntoView(true);", close)
        # close.click()

    def should_be_news_function_checkbox(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsFunctionsLocators.NEWS_CHECK)), \
            "Кнопка включить функцию НОВОСТИ не найдена"

    def check_news_function(self):
        self.browser.find_element(*AppsFunctionsLocators.NEWS_CHECK).click()
