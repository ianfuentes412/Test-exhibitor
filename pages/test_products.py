import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure


class productObjects:
    product_btn = (By.XPATH, "//*[@id='menu_products']/a")
    product_load = (By.XPATH, "//h2[text()='Products/Services']")
    add_prod_btn = (By.XPATH, "//*[@id='addproduct']")
    prod_title = (By.XPATH, "//*[@id='product_title']")
    prod_link = (By.XPATH, "//*[@id='product_link']")
    prod_save = (By.XPATH, "//*[@id='save']")
    check_newsave = (By.XPATH, "//*[@id='successmessage']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_product(self):
        self.browser.find_element(*self.product_btn).click()

    @allure.step('Check if Product tab has loaded')
    def check_product_loaded(self):
        try:
            self.browser.find_element(*self.product_load)
            assert True
        except:
            assert False

    @allure.step('Checking if Add Button Exists')
    def check_add_btn(self):
        try:
            self.browser.find_element(*self.add_prod_btn).click()
            assert True
        except:
            assert False

    @allure.step('Enter Title in Textbox')
    def add_product_title(self, prod_change):
        self.browser.find_element(*self.prod_title).clear()
        self.browser.find_element(*self.prod_title).send_keys(prod_change)

    @allure.step('Enter Link in Textbox')
    def add_product_link(self, prod_change2):
        self.browser.find_element(*self.prod_link).clear()
        self.browser.find_element(*self.prod_link).send_keys(prod_change2)

    @allure.step('Click to save Product')
    def save_new_product(self):
        try:
            self.browser.find_element(*self.prod_save).click()
            assert True
        except:
            assert False

    @allure.step('Check if product is saved')
    def check_new_product(self):
        try:
            self.browser.find_element(*self.check_newsave)
            assert True
        except:
            assert False
