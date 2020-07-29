import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class helpobjects:

    dropdown1 = (By.XPATH, "//*[@id='accordion']/div[1]/a")
    dropdown2 = (By.XPATH, "//*[@id='accordion']/div[2]/a")
    dropdown3 = (By.XPATH, "//*[@id='accordion']/div[3]/a")
    dropdown4 = (By.XPATH, "//*[@id='accordion']/div[4]/a")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Checking for Help Elements')
    def dropdown1(self):
        return self.browser.find_element(*self.dropdown1).click()