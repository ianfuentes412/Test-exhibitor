"""
This module contains the page object
for the homepage.
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class loginpageObjects:
    """
    Define all web element locators and test steps
    in this class for homepage
    """

    URL = "https://test-exhibitors.easyreg.ca/"
    input_email = (By.XPATH, "//*[@id='exhibitor_email']")
    input_regcode = (By.XPATH, "//*[@id='exhibitor_code']")
    button_signin = (By.XPATH, "//button[text()='Sign in']")
    invalid_login_alert = (By.XPATH, "//div[contains(@class,'alert-danger')]")


    def __init__(self, browser):
        self.browser = browser

    @allure.step('Loading login page in browser')
    def load(self):
        self.browser.get(self.URL)

    @allure.step('Checking if Email field exists')
    def check_input_email(self):
        try:
            self.browser.find_element(*self.input_email)
            return True
        except:
            return False

    @allure.step('Checking if Registration Code field exists')
    def check_input_regcode(self):
        try:
            self.browser.find_element(*self.input_regcode)
            return True
        except:
            return False

    @allure.step('Checking if Sign in button exists')
    def check_button_signin(self):
        try:
            self.browser.find_element(*self.button_signin)
            return True
        except:
            return False

    @allure.step('Entering email into login page')
    def enter_email(self, email):
        self.browser.find_element(*self.input_email).clear()
        self.browser.find_element(*self.input_email).send_keys(email)

    @allure.step('Entering registration code into login page')
    def enter_regcode(self, regcode):
        self.browser.find_element(*self.input_regcode).clear()
        self.browser.find_element(*self.input_regcode).send_keys(regcode)

    @allure.step('Clicking Sign in button')
    def click_signin(self):
        self.browser.find_element(*self.button_signin).click()

    @allure.step('Checking invalid login alert message')
    def check_invalid_login(self):
        return self.browser.find_element(*self.invalid_login_alert).text