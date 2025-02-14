from selenium.webdriver.common.by import By

class TempmailPageLocators:
    TEMPMAIL_LINK = 'https://dropmail.me/'
    TEMPMAIL = (By.CSS_SELECTOR, 'span.email')
    LETTER_PASSWORD = (By.CSS_SELECTOR, 'ul pre[data-bind]')

class SignupPageLocators:
    SIGNUP_LINK = 'https://lk.ineed.chat/auth/signup'
    REG_NAIM_FIELD = (By.CSS_SELECTOR, 'input[formcontrolname="nameFormControl"]')
    REG_MAIL_FIELD = (By.CSS_SELECTOR, 'input[formcontrolname="emailFormControl"]')
    REG_PHONE_FIELD = (By.CSS_SELECTOR, 'input[formcontrolname="phoneFormControl"]')
    REG_AGREE_BTN = (By.CSS_SELECTOR, "label.mat-checkbox-layout")
    REG_CREATE_BTN = (By.ID, "createacc")

class SigninPageLocators:
    SIGNIN_LINK = "https://lk.ineed.chat/auth/signin"
    MAIL_FIELD = (By.CSS_SELECTOR, "app-sign-in input[name='email']")
    PASSWORD_FIELD = (By.NAME, "password")
    SIGNIN_BTN = (By.CSS_SELECTOR, "button.w-100.mat-flat-button.mat-primary")

class IneedchatPageLocators:
    INEED_CHAT_LINK = "https://ineed.chat"
    MAIN_MENU_OPEN = (By.CSS_SELECTOR, '.menu-btn')
    MAIN_MENU_CLOSE = (By.CSS_SELECTOR, ".close-menu-btn")
    MAIN_MENU_CLIENTS_ENTRANCE = (By.XPATH, '//div[@class="main-menu"]/ul/li/a[contains(text(), "Вход для клиентов")]')
    CREATE_APP_BTN_LANDING = (By.CSS_SELECTOR, "#create-prichiny")

class CreateAppPageLocators:
    CREATE_APP_LINK = "https://lk.ineed.chat/apps/start"
    CREATE_APP_BTN = (By.CSS_SELECTOR, "#lk-apps-start-create-btn")

class AppsFunctionsLocators:
    APPS_FUNCTIONS_LINK = "https://lk.ineed.chat/apps/details/function/f87f30c2-81c5-42b4-a45f-12912781bc33"
    FUNCTIONS_DONE_BTN = (By.CSS_SELECTOR, "#lk-step-1-complete")
    FUNCTIONS_IN_DETAIL_WINDOW_CLOSE_BTN = (By.CSS_SELECTOR, '.close-btn')

    HELP_BUTTON = (By.CSS_SELECTOR, "#cbh_button_container")
    HELP_BUTTON_OPEN = (By.CSS_SELECTOR, ".main-button.active")
    # HELP_BUTTON_CLOSE = (By.CSS_SELECTOR, ".main-button.close")
    HELP_BUTTON_CLOSE = (By.CSS_SELECTOR, "iframe#cbh_button_container")
    INPUT_MESSAGE = (By.CSS_SELECTOR, 'body input[placeholder="Text your message"]')

    # Функция НОВОСТИ
    NEWS_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-news")
    NEWS_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-news")
    NEWS_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-news")

    # Функция АКЦИИ
    ACTION_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-action")
    ACTION_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-action")
    ACTION_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-action")

    # Функция ЧАТЫ
    CHATS_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-chats")
    CHATS_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-chats")
    CHATS_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-chats")

    # Функция КАТАЛОГ
    CATALOG_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-catalog")
    CATALOG_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-catalog")
    CATALOG_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-catalog")

    # Функция ОНЛАЙН-ЗАКАЗ
    ORDER_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-order")
    ORDER_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-order")
    ORDER_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-order")
    DELIVERY_CHECK = (By.CSS_SELECTOR, ".mat-dialog-container mat-checkbox:nth-child(1)")
    SELF_EXPORT_CHECK = (By.CSS_SELECTOR, ".mat-dialog-container mat-checkbox:nth-child(2)")
    ONLINE_PAY_CHECK = (By.CSS_SELECTOR, ".mat-dialog-container mat-checkbox:nth-child(3)")
    APPLY_ADDITIONAL_PARAMETER_BTN = (By.CSS_SELECTOR, "mat-dialog-container button.mat-flat-button")
    CLOSE_ADDITIONAL_PARAMETER_BTN = (By.CSS_SELECTOR, "button.close-btn.mat-icon-button.ng-star-inserted")

    # Функция ОНЛАЙН-ЗАПИСЬ
    APPOINTMENT_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-appointment")
    APPOINTMENT_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-appointment")
    APPOINTMENT_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-appointment")

    # Функция ОЦЕНКИ
    RECALL_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-recall")
    RECALL_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-recall")
    RECALL_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-recall")

    # Функция ОЦЕНКИ
    CALLBACK_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-callback")
    CALLBACK_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-callback")
    CALLBACK_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-callback")

    # Функция ЛОЯЛЬНОСТЬ
    BONUSCARD_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-bonus")
    BONUSCARD_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-bonus")
    BONUSCARD_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-bonus")

    # Функция ЗАЯВКИ
    STATEMENT_CHECK = (By.CSS_SELECTOR, "#lk-app-func-on-statement")
    STATEMENT_UNCHECK = (By.CSS_SELECTOR, "#lk-app-func-off-statement")
    STATEMENT_IN_DETAIL_BTN = (By.CSS_SELECTOR, "#lk-app-func-question-statement")

class AppsTitleLocators:
    APPS_TITILE_LINK = "https://lk.ineed.chat/apps/details/info/f87f30c2-81c5-42b4-a45f-12912781bc33"
    TITLE = "TestAppFback"
    TITLE_FIELD = (By.CSS_SELECTOR, "#mat-input-0")
    TITLE_COMPLETE_BTN = (By.CSS_SELECTOR, "#lk-step-2-1-complete")
    IMAGE_DOWNLOAD_SKIP_BTN = (By.CSS_SELECTOR, "#lk-step-2-1-image-skip")
    IMAGE_DOWNLOAD_BTN = (By.CSS_SELECTOR, "#lk-step-2-1-image-select")

class AppsColorLocators:
    APPS_COLOR_LINK = "https://lk.ineed.chat/apps/details/design/f87f30c2-81c5-42b4-a45f-12912781bc33"
    APPS_COLOR = (By.CSS_SELECTOR, "div[style='background-color: rgb(38, 166, 91);']")
    COLOR_COMPLETE_BTN = (By.CSS_SELECTOR, "#lk-step-3-complete")

class AppsDemoLocators:
    DEMO_APPS_LINK = "https://lk.ineed.chat/apps/details/demo/f87f30c2-81c5-42b4-a45f-12912781bc33"
    DEMO_APPS_CODE = (By.CSS_SELECTOR, "app-demo .cursor-pointer")
    DEMO_SAFE_BTN = (By.CSS_SELECTOR, "#lk-step-4-1-complete")
    DEMO_SIGNIN_BTN = (By.CSS_SELECTOR, "#lk-step-finish-to-signin")
    DEMO_SIGNUP_BTN = (By.CSS_SELECTOR, "#lk-step-finish-to-signup")
    DEMO_POPUP_WINDOW_CLOSE = (By.CSS_SELECTOR, ".close-btn")
    DEMO_GRATE_SIGN = (By.XPATH, '//h5["Отлично"]')

class AppDoneLocators:
    REMOVE_APP_BTN = (By.CSS_SELECTOR, "#lk-apps-app-remove")
    REMOVE_APP_CONTINUE_BTN = (By.CSS_SELECTOR, ".btn-big.mt-3.mt-md-0.ml-md-3.mat-flat-button.mat-primary")









