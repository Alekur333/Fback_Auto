import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        # print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == "firefox":
        # print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # print("\nquit browser..")
    browser.quit()

# @pytest.fixture()
# def mail_field_check_fill(browser, mail, password):
#     try:
#         input1 = browser.find_element_by_css_selector("app-sign-in input[name='email']")
#         result = True
#         input1.send_keys(mail)
#     except:
#         result = False
#     assert result == True, 'Поле "Электронная почта" не найдено'
#
#     try:
#         input2 = browser.find_element_by_name("password")
#         result = True
#         input2.send_keys(password)
#     except:
#         result = False
#     assert result == True, 'Поле "Пароль" не найдено'

# Заходим на страницу входа
# @pytest.fixture(scope="class")
# def open_signin_page(browser):
    # link = "https://lk.ineed.chat/auth/signin"
    # browser.get(link)
    # browser.get('https://lk.ineed.chat/auth/signin')

# @pytest.fixture()
#     def open_temp_mail_page(browser):
#         # Открыть страницу временной почты и взять мейл для регистрации
#         browser.get('https://dropmail.me/ru/')
#         # window1 = browser.window_handles[0]
#         # temp_mail = browser.find_element_by_css_selector('span.email').text
#         # print(temp_mail)
