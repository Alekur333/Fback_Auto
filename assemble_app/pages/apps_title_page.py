from .base_page import BasePage
from .locators import AppsTitleLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class AppsTitlePage(BasePage):

    def should_be_title_field(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsTitleLocators.TITLE_FIELD)), \
            "Поле для Названия не найдено"

    def insert_title(self):
        self.browser.find_element(*AppsTitleLocators.TITLE_FIELD).send_keys(AppsTitleLocators.TITLE)

    def complete_title(self):
        self.browser.find_element(*AppsTitleLocators.TITLE_COMPLETE_BTN).click()

    def should_be_image_skip_btn(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsTitleLocators.IMAGE_DOWNLOAD_SKIP_BTN)), \
            "Кнопка Пропустить загрузку изображения не найдена"

    def image_download_skip(self):
        self.browser.find_element(*AppsTitleLocators.IMAGE_DOWNLOAD_SKIP_BTN).click()

    def should_be_image_download_btn(self):
        assert WebDriverWait(self.browser, 2).until\
            (ec.presence_of_element_located(AppsTitleLocators.IMAGE_DOWNLOAD_BTN)), \
            "Кнопка Загрузить изображение не найдена"

    def image_download(self):
        self.browser.find_element(*AppsTitleLocators.IMAGE_DOWNLOAD_BTN).click()