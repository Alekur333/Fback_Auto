from selenium.webdriver.common.by import By

class TempmailPageLocators:
    TEMPMAIL = (By.CSS_SELECTOR, 'span.email')
    LETTER_PASSWORD = (By.CSS_SELECTOR, 'ul pre[data-bind]')

class SignupPageLocators:
    REG_NAIM_FIELD = (By.CSS_SELECTOR, "#mat-input-0")
    REG_MAIL_FIELD = (By.CSS_SELECTOR, "#mat-input-1")
    REG_PHONE_FIELD = (By.CSS_SELECTOR, "#mat-input-2")
    REG_AGREE_BTN = (By.CSS_SELECTOR, "label.mat-checkbox-layout")
    REG_CREATE_BTN = (By.ID, "createacc")

class SigninPageLocators:
    MAIL_FIELD = (By.CSS_SELECTOR, "app-sign-in input[name='email']")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGNIN_BTN = (By.CSS_SELECTOR, "button.w-100.mat-flat-button.mat-primary")

class IneedchatPageLocators:
    INEED_CHAT_LINK = "https://ineed.chat"
    MAIN_MENU_OPEN = (By.CSS_SELECTOR, '.menu-btn')
    MAIN_MENU_CLOSE = (By.CSS_SELECTOR, ".close-menu-btn")
    MAIN_MENU_CLIENTS_ENTRANCE = (By.XPATH, '//div[@class="main-menu"]/ul/li/a[contains(text(), "Вход для клиентов")]')

class CreateAppPageLocators:
    CREATE_APP_LINK = "https://lk.ineed.chat/apps/start"
    CREATE_APP_BTN = (By.CSS_SELECTOR, "#lk-apps-start-create-btn")

class AppsFunctionsLocators:
    APPS_FUNCTIONS_LINK = "https://lk.ineed.chat/apps/details/function/f87f30c2-81c5-42b4-a45f-12912781bc33"
    FUNCTIONS_DONE_BTN = (By.CSS_SELECTOR, "#lk-step-1-complete")

    NEWS_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-news")
    NEWS_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-news")
    NEWS_IN_DETAIL_CLOSE = (By.CSS_SELECTOR, 'div[class="mat-button-ripple mat-ripple mat-button-ripple-round"]')






