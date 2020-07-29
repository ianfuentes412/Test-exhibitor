# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Trytest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_try(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1172,722 | ]]
        driver.get("https://test-exhibitors.easyreg.ca/index.php")
        driver.find_element_by_css_selector("#menu_preview > a.nk-menu-link > span.nk-menu-text").click()
        driver.find_element_by_link_text("Request Catalogue").click()
        driver.find_element_by_id("request_company").click()
        driver.find_element_by_id("request_company").clear()
        driver.find_element_by_id("request_company").send_keys("Here")
        driver.find_element_by_id("request_firstname").click()
        driver.find_element_by_id("request_firstname").clear()
        driver.find_element_by_id("request_firstname").send_keys("asdasd")
        driver.find_element_by_id("request_lastname").click()
        driver.find_element_by_id("request_lastname").clear()
        driver.find_element_by_id("request_lastname").send_keys("asdasd")
        driver.find_element_by_id("request_street").click()
        driver.find_element_by_id("request_street").clear()
        driver.find_element_by_id("request_street").send_keys("asfasf")
        driver.find_element_by_id("request_street2").click()
        driver.find_element_by_id("request_street2").clear()
        driver.find_element_by_id("request_street2").send_keys("asfasf")
        driver.find_element_by_id("request_city").click()
        driver.find_element_by_id("request_city").clear()
        driver.find_element_by_id("request_city").send_keys("sdasd")
        driver.find_element_by_id("request_province").click()
        driver.find_element_by_id("request_province").clear()
        driver.find_element_by_id("request_province").send_keys("agaga")
        driver.find_element_by_id("request_postalcode").click()
        driver.find_element_by_id("request_postalcode").clear()
        driver.find_element_by_id("request_postalcode").send_keys("sdasd")
        driver.find_element_by_id("request_country").click()
        driver.find_element_by_id("request_country").clear()
        driver.find_element_by_id("request_country").send_keys("asfasfa")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
