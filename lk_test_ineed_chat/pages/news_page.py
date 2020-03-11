from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators, CompaniesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NewsPage(MainPage, BasePage):

    # Проверяем переход на страницу новостей
    def should_be_news_page(self):
        # assert "news" in self.browser.current_url, 'Это не страница новостей'
        assert WebDriverWait(self.browser, 10).until(ec.url_contains("news")), 'Это не страница Новости'

