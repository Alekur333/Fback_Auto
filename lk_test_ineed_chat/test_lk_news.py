import pytest
import time
from .pages.login_page import LoginPage
from .pages.news_page import NewsPage
from .pages.locators import LoginPageLocators, NewsPageLocators, MainPageLocators

login_link = (LoginPageLocators.LOGIN_LINK)
phone = "79523401124"
sms = "111111"


class TestNews:

    def test_news_page(self, browser):
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.should_be_login_page(phone, sms)
        login_page.should_be_companies_page()
        login_page.should_be_company1()
        news_page = NewsPage(browser, browser.current_url)
        news_page.should_be_news_page()
        news_page.news_creation()
        news_page.should_be_user_menu()
        news_page.go_to_user_menu()
        news_page.should_be_logout_btn()
        news_page.make_logout()
