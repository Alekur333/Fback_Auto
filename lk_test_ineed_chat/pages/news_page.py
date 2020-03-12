from .main_page import MainPage
from .locators import NewsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


class NewsPage(MainPage):

    # Проверяем переход на страницу новостей
    def should_be_news_page(self):
        # assert "news" in self.browser.current_url, 'Это не страница новостей'
        assert WebDriverWait(self.browser, 10).until(ec.url_contains("news")), 'Это не страница Новости'

    def news_creation(self):

        self.should_be_create_new_option()
        time.sleep(2)
        self.add_new_start()
        self.should_be_news_creation_page()
        self.should_be_back_from_new_btn()
        self.should_be_news_title()
        self.add_news_title()
        self.should_be_news_description()
        self.add_news_description()
        self.should_be_news_start_date()
        time.sleep(2)
        self.should_be_news_end_date()
        # time.sleep(2)
        self.should_be_push_switcher()
        self.should_be_safe_new_btn()
        self.should_be_news_page()
        time.sleep(15)
        self.delete_created_new()

    def should_be_create_new_option(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(NewsPageLocators.ADD_NEW)), 'Нет опции "Добавить новость"'
        # assert self.browser.find_element('news-list > div > div:nth-child(1)'), 'Нет опции "Добавить новость"'

    def add_new_start(self):
        # self.browser.find_element(*NewsPageLocators.ADD_NEW).click()
        WebDriverWait(self.browser, 30).until \
            (ec.element_to_be_clickable(NewsPageLocators.ADD_NEW)).click()

    def should_be_news_creation_page(self):
        assert WebDriverWait(self.browser, 12).until(ec.url_contains("create")), 'Это не страница создания Новости'

    def should_be_back_from_new_btn(self):
        assert self.browser.find_element(*NewsPageLocators.BACK_FROM_CREATE_NEW), 'Нет кнопки Назад из Создания новости'

    def should_be_news_title(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_TITLE), 'Нет поля для названия новости'

    def add_news_title(self):
        self.browser.find_element(*NewsPageLocators.NEWS_TITLE).send_keys('Auto-new')

    def should_be_news_description(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_DESCRIPTION), 'Нет поля для описания новости'

    def add_news_description(self):
        self.browser.find_element(*NewsPageLocators.NEWS_DESCRIPTION).send_keys('Created by AleKur QA')

    def should_be_news_start_date(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_START_DATE), 'Нет кнопки начала отображения новости'
        now_date = datetime.now().date()
        print(now_date)
        current_month = str(now_date.month)
        print(f'Месяц: {current_month}')
        current_day = str(now_date.day)
        print(f'День:  {current_day}')
        # self.browser.find_element(*NewsPageLocators.INPUT_START_DATE).send_keys(now_date) #Message: element not interactable
        self.browser.find_element(*NewsPageLocators.NEWS_START_DATE).click()
        self.browser.find_element(*NewsPageLocators.CURRENT_DAY).click()
        # self.browser.find_element(*NewsPageLocators.NEWS_DATE_ACCEPT).click()

    def should_be_news_end_date(self):
        # assert self.browser.find_element(*NewsPageLocators.NEWS_END_DATE), 'Нет поля конца отображения новости'
        self.browser.find_element(*NewsPageLocators.NEWS_END_DATE).click()
        self.browser.find_element(*NewsPageLocators.CURRENT_DAY).click()
        # self.browser.find_element(*NewsPageLocators.NEWS_END_DATE).send_keys(Keys.ENTER)
        # self.browser.find_element(*NewsPageLocators.NEWS_END_DATE).send_keys(Keys.ARROW_RIGHT)
        # self.browser.find_element(*NewsPageLocators.NEWS_END_DATE).send_keys(Keys.ENTER)

    def should_be_safe_new_btn(self):
        # assert self.browser.find_element(*NewsPageLocators.NEWS_SAFE), 'Нет кнопки Сохранить новость'
        assert WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(NewsPageLocators.NEWS_SAFE))
        # self.browser.find_element(*NewsPageLocators.NEWS_SAFE).click()
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(NewsPageLocators.NEWS_SAFE)).click()

    def should_be_push_switcher(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_SEND_PUSH_CHECK_BOX), '"Включить пуш" не найдено'
        self.browser.find_element(*NewsPageLocators.NEWS_SEND_PUSH_CHECK_BOX).click()

    def delete_created_new(self):
        self.browser.find_element(*NewsPageLocators.DELETE_NEW).click()
        assert self.browser.find_element(*NewsPageLocators.DELETE_NEW_NO), 'Кнопка Потвердить удаление-НЕТ не найдена'
        assert self.browser.find_element(*NewsPageLocators.DELETE_NEW_YES), 'Кнопка Потвердить удаление-ДА не найдена'
        self.browser.find_element(*NewsPageLocators.DELETE_NEW_YES).click()



