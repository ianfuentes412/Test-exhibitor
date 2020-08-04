import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class homepageObjects:

    valid_login_header = (By.XPATH, "//h2[contains(text(),'Welcome')]")
    valid_login_usermenu = (By.XPATH, "//a[@class='dropdown-toggle']")
    signout = (By.XPATH, "//span[text()='Sign out']")
    video_play = (By.XPATH, "//*[@id='player']/div[7]/div[3]/button")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Checking valid login user name in header')
    def check_valid_login_header(self):
        return self.browser.find_element(*self.valid_login_header).text

    @allure.step('Checking valid login user name in user menu')
    def check_valid_login_usermenu(self):
        return self.browser.find_element(*self.valid_login_usermenu).text

    @allure.step('Checking if video works when played')
    def check_valid_video(self):
        try:
            self.browser.find_element(*self.video_play).click()
            assert True
        except:
            assert False


    @allure.step('Logging out current user')
    def logout(self):
        self.browser.find_element(*self.valid_login_usermenu).click()
        self.browser.find_element(*self.signout).click()

