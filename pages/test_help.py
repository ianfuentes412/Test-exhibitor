import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class helpObjects:

    dropdown1 = (By.XPATH, "//*[@id='accordion']/div[1]/a")
    dropdown2 = (By.XPATH, "//*[@id='accordion']/div[2]/a")
    dropdown3 = (By.XPATH, "//*[@id='accordion']/div[3]/a")
    dropdown4 = (By.XPATH, "//*[@id='accordion']/div[4]/a")
    find_test1 = (By.XPATH, "//*[@id='accordion-item-1']/div/p[1]")
    find_test2 = (By.XPATH, "//*[@id='accordion-item-2']/div/p[1]")
    find_test3 = (By.XPATH, "//*[@id='accordion-item-3']/div/p[1]")
    find_test4 = (By.XPATH, "//*[@id='accordion-item-4']/div/p[1]")
    #find_test4 = (By.XPATH, "//*[@id='accordion']/div[4]/a/h6")
    help_btn = (By.XPATH, "//*[@id='menu_help']/a")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_help(self):
        self.browser.find_element(*self.help_btn).click()

    @allure.step('Checking Dropdown 1')
    def check_dropdown1(self):
        return self.browser.find_element(*self.find_test1).text


    @allure.step('Checking Dropdown 2')
    def check_dropdown2(self):
        return self.browser.find_element(*self.find_test2).text


    @allure.step('Checking Dropdown 3')
    def check_dropdown3(self):
            return self.browser.find_element(*self.find_test3).text

    @allure.step('Checking Dropdown 4')
    def check_dropdown4(self):
            return self.browser.find_element(*self.find_test4).text


    @allure.step('Clicking dropdown 1 works')
    def click_dropdown1(self):
        self.browser.find_element(*self.dropdown1).click()

    @allure.step('Clicking dropdown 2 works')
    def click_dropdown2(self):
        self.browser.find_element(*self.dropdown2).click()

    @allure.step('Clicking dropdown 3 works')
    def click_dropdown3(self):
        self.browser.find_element(*self.dropdown3).click()

    @allure.step('Clicking dropdown 4 works')
    def click_dropdown4(self):
        self.browser.find_element(*self.dropdown4).click()