import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class previewObjects:

    preview_btn = (By.XPATH, "//*[@id='menu_preview']/a")
    preview_test = (By.XPATH, "//*[@id='company']")
    previewchat = (By.XPATH, "//*[@id='chat']")
    previewappoint=(By.XPATH, "//*[@id='appointment']")
    entrytest1=(By.XPATH, "//*[@id='highlights']")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_preview(self):
        self.browser.find_element(*self.preview_btn).click()

    @allure.step('Checking Preview Page Loaded')
    def check_preview_loaded(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Preview_Loaded',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.preview_test)
            return True
        except:
            return False

    @allure.step('Checking Preview Element')
    def check_book_element1(self):
        try:
            self.browser.find_element(*self.entrytest1)
            return True
        except:
            return False

    @allure.step('Checking if Chat Button Exists')
    def check_chat_btn(self):
        try:
            self.browser.find_element(*self.previewchat)
            return True
        except:
            return False

    @allure.step('Checking if Appointment Button Exists')
    def check_appoint_btn(self):
        try:
            self.browser.find_element(*self.previewappoint)
            return True
        except:
            return False
