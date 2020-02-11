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


