from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = "https://test.ineed.chat/login"
    PHONE_FIELD = (By.CSS_SELECTOR, "input[name='phone']")
    GET_SMS_BTN = (By.CSS_SELECTOR, "#ident > button")
    SMS_FIELD = (By.CSS_SELECTOR, "input[name='verifiedCode']")
    LOGIN_BTN = (By.CSS_SELECTOR, "#auth > button")

class MainPageLocators:
    MAIN_PAGE_LINK = "https://test.ineed.chat"
    COMPANIES_BTN = (By.CSS_SELECTOR, "a[href='/companies']")
    USER_MENU_BTN = (By.CSS_SELECTOR, 'img.mat-menu-trigger')
    USER_MENU_PROFILE_BTN = (By.CSS_SELECTOR, 'div[role="menu"] button:nth-child(1)')
    USER_MENU_FULLSCREEN_BTN = (By.CSS_SELECTOR, 'div[role="menu"] button:nth-child(2)')
    USER_MENU_LOGOUT_BTN = (By.CSS_SELECTOR, 'div[role="menu"] button:nth-child(3)')
    NEWS_BTN = (By.CSS_SELECTOR, 'a[href="/news"]')

class CompaniesPageLocators:
    COMPANIES_LINK = "https://test.ineed.chat/companies"
    COMPANY1_BTN = (By.CSS_SELECTOR, "body > app-root > company-list > div > div.row > div:nth-child(1)")
    COMPANY1_NAME = (By.CSS_SELECTOR, "company-list > div > div.row > div:nth-child(1) > mat-card > "
                                      "mini-card > div > div.info-text.deny-overflow > span")
    COMPANY1_MUST_BE_NAME = "Newbee"

class NewsPageLocators:
    NEWS_LINK = "https://test.ineed.chat/news"
    NEWS_CREATE_LINK = "https://test.ineed.chat/news/create"
    ADD_NEW = (By.CSS_SELECTOR, "news-list > div > div:nth-child(1)")
    BACK_FROM_CREATE_NEW = (By.CSS_SELECTOR, "news-details > div > div > button-back")
    NEWS_TITLE = (By.CSS_SELECTOR, "input[name='name']")
    NEWS_DESCRIPTION = (By.CSS_SELECTOR, 'textarea[name="text"]')
    NEWS_DATE_DAYS_LIST = (By.CSS_SELECTOR, 'td[role="button"]')
    NEWS_START_DATE_BTN = (By.XPATH, '/html/body/app-root/company-home/mat-drawer-container/mat-drawer-content/div' \
                                     '/news-home/news-details/div/mat-card/form/mat-form-field[3]/div/div[1]/div[2]' \
                                     '/mat-datepicker-toggle/button')
    NEWS_START_CURRENT_DAY = (By.CSS_SELECTOR, 'tr:nth-child(3) > td.mat-calendar-body-cell.mat-focus-indicator.'
                                               'mat-calendar-body-active.ng-star-inserted > div')
    NEWS_END_DATE_BTN = (By.XPATH, '/html/body/app-root/company-home/mat-drawer-container/mat-drawer-content/div/'
                                   'news-home/news-details/div/mat-card/form/mat-form-field[4]/div/div[1]/div[2]/'
                                   'mat-datepicker-toggle/button')
    NEWS_END_CURRENT_DAY = (By.CSS_SELECTOR, '#mat-datepicker-2 > div > mat-month-view > table > tbody > '
                                             'tr:nth-child(3) > td.mat-calendar-body-cell.mat-focus-indicator.'
                                             'mat-calendar-body-active.ng-star-inserted > div')
    NEWS_END_DAY = (By.XPATH, '//div[text()=" 5 "]') # //div[contains(text(), "5")]
    NEWS_NEXT_MONTH_BTN = (By.CSS_SELECTOR, 'button.mat-calendar-next-button')
    NEWS_END_MONTH_YEAR = (By.CSS_SELECTOR, 'button.mat-calendar-period-button span.mat-button-wrapper')
    NEWS_SEND_PUSH_CHECK_BOX = (By.XPATH, '//*[@id="mat-slide-toggle-1"]/label/div')
    NEWS_ATTACH_PICTURE = (By.CSS_SELECTOR, 'input[type="file"]')
    # NEWS_SAFE появляется после ввода названия новости
    NEWS_SAFE = (By.XPATH, '/html/body/app-root/company-home/mat-drawer-container/mat-drawer-content/div/'
                           'news-home/news-details/div/div/button')
    DELETE_NEW = (By.CSS_SELECTOR, 'news-list > div > div:nth-child(2) > news-item > div > button')
    DELETE_NEW_YES = (By.CSS_SELECTOR, '#mat-dialog-0 > app-dialog-confirm > div.text-right > button:nth-child(2)')
    DELETE_NEW_NO = (By.CSS_SELECTOR, '#mat-dialog-0 > app-dialog-confirm > div.text-right > button:nth-child(1)')
