import pytest
import time
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from pages.tempmail_page import TempMailPage
from pages.ineed_chat_page import IneedChatPage
from pages.locators import IneedchatPageLocators
from pages.create_app_page import CreateAppPage

landing_link = (IneedchatPageLocators.INEED_CHAT_LINK)

class TestAssembleAppFull:

    def test_assemble_app(self, browser):
        page = IneedChatPage(browser, landing_link)
        page.open()
        page.should_be_clients_entrance_btn_in_main_menu()
        page.go_to_main_menu()
        page.should_be_main_menu_close_btn()
        page.should_be_clients_entrance_btn_in_main_menu()
        page.go_to_clients_entrance_in_main_menu()
        page.

        # time.sleep(5)
