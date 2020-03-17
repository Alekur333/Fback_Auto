from .main_page import MainPage
from .locators import NewsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.support.ui import Select
import os


class NewsPage(MainPage):

    # Проверяем переход на страницу новостей
    def should_be_news_page(self):
        assert WebDriverWait(self.browser, 10).until(ec.url_contains("news")), 'Это не страница Новости'

    # Создаем новость и в финале её удаляем
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
        # time.sleep(2)
        self.should_be_news_end_date()
        # time.sleep(2)
        self.should_be_push_switcher()
        self.news_attach_picture()
        time.sleep(3)
        self.should_be_save_new_btn()
        self.should_be_news_page()
        time.sleep(2)
        self.delete_created_new()

    def should_be_create_new_option(self):
        assert WebDriverWait(self.browser, 10).until\
            (ec.presence_of_element_located(NewsPageLocators.ADD_NEW)), 'Нет опции "Добавить новость"'

    def add_new_start(self):
        WebDriverWait(self.browser, 30).until \
            (ec.element_to_be_clickable(NewsPageLocators.ADD_NEW)).click()

    def should_be_news_creation_page(self):
        assert WebDriverWait(self.browser, 12).until(ec.url_contains("create")), 'Это не страница создания Новости'

    def should_be_back_from_new_btn(self):
        assert self.browser.find_element(*NewsPageLocators.BACK_FROM_CREATE_NEW), 'Нет кнопки Назад из Создания новости'

    def should_be_news_title(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_TITLE), 'Нет поля для названия новости'

    def add_news_title(self):
        self.browser.find_element(*NewsPageLocators.NEWS_TITLE).send_keys('Automation new')

    def should_be_news_description(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_DESCRIPTION), 'Нет поля для описания новости'

    def add_news_description(self):
        self.browser.find_element(*NewsPageLocators.NEWS_DESCRIPTION).send_keys('Auto-test created by AleKur QA')

    def should_be_news_start_date(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_START_DATE_BTN), 'Нет кнопки начала отображения новости'
        now_date = datetime.now().date()
        print(now_date)
        current_year = str(now_date.year)
        print(f'Год: {current_year}')
        current_month = str(now_date.month)
        print(f'Месяц: {current_month}')
        current_day = str(now_date.day)
        print(f'День:  {current_day}')
        self.browser.find_element(*NewsPageLocators.NEWS_START_DATE_BTN).click()
        start_day = self.browser.find_element(*NewsPageLocators.NEWS_START_CURRENT_DAY).text
        print(f'Новость начинается {start_day}.{current_month}.{current_year}')
        self.browser.find_element(*NewsPageLocators.NEWS_START_CURRENT_DAY).click()

    def should_be_news_end_date(self):
        self.browser.find_element(*NewsPageLocators.NEWS_END_DATE_BTN).click()
        self.browser.find_element(*NewsPageLocators.NEWS_NEXT_MONTH_BTN).click()
        # time.sleep(2)
        self.browser.find_element(*NewsPageLocators.NEWS_END_DAY).click()
        month_year_end = self.browser.find_element(*NewsPageLocators.NEWS_END_MONTH_YEAR).text
        print(f'Окончание новости: 5 {month_year_end}')

    def should_be_save_new_btn(self):
        assert WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(NewsPageLocators.NEWS_SAFE))
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(NewsPageLocators.NEWS_SAFE)).click()

    def should_be_push_switcher(self):
        assert self.browser.find_element(*NewsPageLocators.NEWS_SEND_PUSH_CHECK_BOX), '"Включить пуш" не найдено'
        self.browser.find_element(*NewsPageLocators.NEWS_SEND_PUSH_CHECK_BOX).click()

    def news_attach_picture(self):
        # print(os.path.abspath(__file__))
        # print(os.path.abspath(os.path.dirname(__file__)))
        # current_dir = os.path.abspath(os.path.dirname(__file__))
        current_dir = os.path.dirname(r'C:\Users\user\pics\\')
        file_path = os.path.join(current_dir, 'autotest_se.png')
        print(file_path)
        self.browser.find_element(*NewsPageLocators.NEWS_ATTACH_PICTURE).send_keys(file_path)

    def delete_created_new(self):
        self.browser.find_element(*NewsPageLocators.DELETE_NEW).click()
        assert self.browser.find_element(*NewsPageLocators.DELETE_NEW_NO), 'Кнопка Потвердить удаление-НЕТ не найдена'
        assert self.browser.find_element(*NewsPageLocators.DELETE_NEW_YES), 'Кнопка Потвердить удаление-ДА не найдена'
        self.browser.find_element(*NewsPageLocators.DELETE_NEW_YES).click()

