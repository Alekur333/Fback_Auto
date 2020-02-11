import pytest
import time
from pages.signup_page import SignUpPage
from pages.signin_page import SignInPage
from pages.tempmail_page import TempMailPage

link_tempmail = 'https://dropmail.me/'
link_signup = 'https://lk.ineed.chat/auth/signup'
link_signin = "https://lk.ineed.chat/auth/signin"
regname = "Feed Test"
regphone = '9111111111'
signin_mail = "aok@ineed.chat"
signin_password = "test111"

@pytest.mark.smoke
@pytest.mark.signup
class TestLkSignup:

    def test_signup_full(self, browser):

        # Открыть страницу временной почты
        tempmail_page = TempMailPage(browser, link_tempmail)
        tempmail_page.open()
        window1 = browser.window_handles[0]

        # взять мейл для регистрации
        temp_mail = tempmail_page.get_tempmail()

        # Открыть в новом окне страницу регистрации и зарегистрироваться
        browser.execute_script("window.open('{}', '_blank');" .format(link_signup))
        window2 = browser.window_handles[1]
        browser.switch_to.window(window2)
        signup_page = SignUpPage(browser, browser.current_url)
        signup_page.should_be_signup_page(regname, temp_mail, regphone)


        # Возврат в окно почты проверить наличие письма и взять пароль
        browser.switch_to.window(window1)
        temp_password = tempmail_page.get_letter_password(browser)

        # Проверяем переход на страницу входа после успешной регистрации
        # Заполняем обязательные поля и входим
        browser.switch_to.window(window2)
        signin_page = SignInPage(browser, browser.current_url)
        signin_page.should_be_signin_page(temp_mail, temp_password)

        # Проверяем переход на страницу приложений после успешного входа
        signin_page.should_be_apps_page()

        # time.sleep(3)

@pytest.mark.smoke
@pytest.mark.signin
class TestLkSignin:

    def test_signin_full(self, browser):
        signin_page = SignInPage(browser, link_signin)
        signin_page.open()
        signin_page.should_be_signin_page(signin_mail, signin_password)


