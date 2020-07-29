import pytest, allure, time, re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from resources.lists import *
from Tests.lists import *
#pytest -v -s Tests\test_signedin_elements.py

@allure.title('To check if Help btn is working')
class Test_help:
    def test_menu_help(self):
        pytest.skip('nope')
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get(URL)
        self.driver.find_element_by_id(email_id).send_keys(valid_email)
        self.driver.find_element_by_id(code_id).send_keys(valid_code)
        self.driver.find_element_by_id(signin_id).click()

        # self.driver.find_element_by_xpath(dropdownbtn_path).click()
        self.driver.find_element_by_xpath(helpbtn_path).click()
        time.sleep(1)
        html = self.driver.current_url
        find_closing = self.driver.find_element_by_xpath(closing_html).is_displayed()

        if html == URL_help and find_closing == True:
            assert True
        else:
            assert False

        #ADD Id for dropdown
        self.driver.find_element_by_id(dropdown1).click()
        self.driver.find_element_by_id(dropdown2).click()
        self.driver.find_element_by_id(dropdown3).click()
        self.driver.find_element_by_id(dropdown4).click()

        self.driver.close()