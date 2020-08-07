import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class bannerObjects:
    banner_btn = (By.XPATH, "//*[@id='menu_banners']/a")
    add_btn = (By.XPATH, "//*[@id='addbutton']")
    check_loadbanner = (By.XPATH, "//h2[text()='Banners']")
    title_textbox = (By.XPATH, "//*[@id='banner_title']")
    link_textbox = (By.XPATH, "//*[@id='banner_link']")
    banner_upload = (By.XPATH, "//*[@id='banner_image']")
    save_newbtn = (By.XPATH, "//*[@id='newsave']")
    check_newbanner = (By.XPATH, "//td[text()='DemoAdd']")
    delete_newbtn = (By.XPATH, "//tbody/tr[2]/td/a[2]")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_banner(self):
        self.browser.find_element(*self.banner_btn).click()

    @allure.step('Check If Banner Loaded')
    def check_ban_load(self):
        try:
            self.browser.find_element(*self.check_loadbanner)
            assert True
        except:
            assert False

    @allure.step('Checking if Add Banner button exists')
    def check_button_signin(self):
        try:
            self.browser.find_element(*self.add_btn)
            assert True
        except:
            assert False

    @allure.step('Click Add Banner')
    def add_banner(self):
        self.browser.find_element(*self.add_btn).click()

    @allure.step('Check if Title Text Box Exists')
    def check_title_text(self):
        try:
            self.browser.find_element(*self.title_textbox)
            assert True
        except:
            assert False

    @allure.step('Check if Link Text Box Exists')
    def check_link_text(self):
        try:
            self.browser.find_element(*self.link_textbox)
            assert True
        except:
            assert False

    @allure.step('Enter New Title in Textbox')
    def edit_title_text(self, title):
        self.browser.find_element(*self.title_textbox).clear()
        self.browser.find_element(*self.title_textbox).send_keys(title)

    @allure.step('Enter New Links in Textbox')
    def edit_link_text(self, links):
        self.browser.find_element(*self.link_textbox).clear()
        self.browser.find_element(*self.link_textbox).send_keys(links)

    @allure.step('Enter Image')
    def add_new_image(self, banner):
        self.browser.find_element(*self.banner_upload).send_keys(banner)

    @allure.step('Click Save Button')
    def save_banner_btn(self):
        self.browser.find_element(*self.save_newbtn).click()

    @allure.step('Check If New Banner is Saved')
    def check_new_banner(self):
        try:
            self.browser.find_element(*self.check_newbanner)
            assert True
        except:
            assert False

    @allure.step('Click Delete Button')
    def delete_banner_btn(self):
        self.browser.find_element(*self.delete_newbtn).click()

    @allure.step('Check If New Banner is Deleted')
    def check_deleted_banner(self):
        try:
            self.browser.find_element(*self.check_newbanner)
            assert False
        except:
            assert True