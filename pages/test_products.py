import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure, os


class productObjects:
    product_btn = (By.XPATH, "//*[@id='menu_products']/a")
    product_load = (By.XPATH, "//h2[text()='Products/Services']")
    add_prod_btn = (By.XPATH, "//*[@id='addproduct']")
    prod_title = (By.XPATH, "//*[@id='product_title']")
    prod_link = (By.XPATH, "//*[@id='product_link']")
    prod_save = (By.XPATH, "//*[@id='save']")
    prod_photo = (By.XPATH, "//*[@id='product_image']")
    prod_descript = (By.XPATH, "//*[@id='tinymce']")
    check_newsave = (By.XPATH, "//*[@id='successmessage']")
    delete_newsave = (By.XPATH, "//tbody/tr[4]/td/a[2]")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Enter Product Through Home Page')
    def enter_product(self):
        self.browser.find_element(*self.product_btn).click()

    @allure.step('Check if Product tab has loaded')
    def check_product_loaded(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Product_Tab_Loaded',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.product_load)
            return True
        except:
            return False

    @allure.step('Checking if Add Button Exists')
    def check_add_btn(self):
        try:
            self.browser.find_element(*self.add_prod_btn).click()
            return True
        except:
            return False

    @allure.step('Enter Title in Textbox')
    def add_product_title(self, prod_change):
        self.browser.find_element(*self.prod_title).clear()
        self.browser.find_element(*self.prod_title).send_keys(prod_change)

    @allure.step('Enter Link in Textbox')
    def add_product_link(self, prod_change2):
        self.browser.find_element(*self.prod_link).clear()
        self.browser.find_element(*self.prod_link).send_keys(prod_change2)

    @allure.step('Enter upload new image')
    def add_product_image(self):
        path = os.getcwd()
        if os.name == "posix":
            photo_path = path + "/banner.jpg"
        else:
            photo_path = path + "\\banner.jpg"
        self.browser.find_element(*self.prod_photo).send_keys(photo_path)

    @allure.step('Add product text')
    def enter_prod_description(self, PDescription):
            # self.browser.find_element(*self.comp_close).click()
            iframe = self.browser.find_element_by_id('product_description_ifr')
            self.browser.switch_to.frame(iframe)
            self.browser.find_element(*self.prod_descript).clear()
            self.browser.find_element(*self.prod_descript).send_keys(PDescription)
            self.browser.switch_to.default_content()

    @allure.step('Click to save Product')
    def save_new_product(self):
            allure.attach(self.browser.get_screenshot_as_png(), name='Product_Details_Added',
                      attachment_type=allure.attachment_type.PNG)
            self.browser.find_element(*self.prod_save).click()

    @allure.step('Check if product is saved')
    def check_new_product(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Product_Saved',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_newsave)
            return True
        except:
            return False

    @allure.step('Delete Product')
    def delete_new_product(self):
        self.browser.find_element(*self.delete_newsave).click()

    @allure.step('Check if product is Deleted')
    def check_deleted_product(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Product_Deleted',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_newsave)
            return False
        except:
            return True