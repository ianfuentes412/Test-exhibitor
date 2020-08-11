import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure


class compObjects:
    comp_btn = (By.XPATH, "//*[@id='menu_company']/a")
    comp_loaded = (By.XPATH, "//*[@id='updateform']")
    comp_title = (By.XPATH, "//input[@id='exhibitor_company']")
    comp_fname = (By.XPATH, "//*[@id='exhibitor_contact_firstname']")
    comp_lname = (By.XPATH, "//*[@id='exhibitor_contact_lastname']")
    comp_email = (By.XPATH, "//*[@id='exhibitor_contact_email']")
    comp_number = (By.XPATH, "//*[@id='exhibitor_contact_phone_cell']")

    comp_addtab = (By.XPATH, "//*[@id='addresstab']")
    comp_add1 = (By.XPATH, "//*[@id='exhibitor_street']")
    comp_add2 = (By.XPATH, "//*[@id='exhibitor_street2']")
    comp_city = (By.XPATH, "//*[@id='exhibitor_city']")
    comp_province = (By.XPATH, "//*[@id='exhibitor_province']")
    comp_postal = (By.XPATH, "//*[@id='exhibitor_postalcode']")
    comp_country = (By.XPATH, "//*[@id='exhibitor_country']")

    comp_webtab = (By.XPATH, "//*[@id='websitetab']")
    comp_website = (By.XPATH, "//*[@id='exhibitor_website']")

    comp_desctab = (By.XPATH, "//*[@id='descriptiontab']")
    comp_close = (By.XPATH, "//*[@id='exhibitor_text_ifr']")
    comp_decript = (By.XPATH, "//*[@id='exhibitor_text']")

    def __init__(self, browser):
        self.browser = browser

    @allure.step('Enter Comp Info Through Home Page')
    def enter_comp(self):
        self.browser.find_element(*self.comp_btn).click()

    @allure.step('Check if Comp Info is Loaded')
    def check_comp_loaded(self):
        try:
            self.browser.find_element(*self.comp_loaded)
            assert True
        except:
            assert False

    @allure.step('Fill in Comp Title')
    def enter_comp_title(self, CTitle):
        self.browser.find_element(*self.comp_title).clear()
        self.browser.find_element(*self.comp_title).send_keys(CTitle)

    @allure.step('Fill in First Name')
    def enter_first_name(self, CFName):
        self.browser.find_element(*self.comp_fname).clear()
        self.browser.find_element(*self.comp_fname).send_keys(CFName)

    @allure.step('Fill in Last Name')
    def enter_last_name(self, CLName):
        self.browser.find_element(*self.comp_lname).clear()
        self.browser.find_element(*self.comp_lname).send_keys(CLName)

    @allure.step('Fill in email address')
    def enter_email(self, CEmail):
        self.browser.find_element(*self.comp_email).clear()
        self.browser.find_element(*self.comp_email).send_keys(CEmail)

    @allure.step('Fill in Phone Number')
    def enter_phone(self, CPhone):
        self.browser.find_element(*self.comp_number).clear()
        self.browser.find_element(*self.comp_number).send_keys(CPhone)


    @allure.step('Switch Tab to Address')
    def click_addtab(self):
        try:
            self.browser.find_element(*self.comp_addtab).click()
            assert True
        except:
            assert False


    @allure.step('Fill in Address 1')
    def enter_add1(self, CAddress1):
        try:
            self.browser.find_element(*self.comp_add1).clear()
            self.browser.find_element(*self.comp_add1).send_keys(CAddress1)
            assert True
        except:
            assert False

    @allure.step('Fill in Address 2')
    def enter_add2(self, CAddress2):
        try:
            self.browser.find_element(*self.comp_add2).clear()
            self.browser.find_element(*self.comp_add2).send_keys(CAddress2)
            assert True
        except:
            assert False

    @allure.step('Fill in City')
    def enter_city(self, CCity):
        try:
            self.browser.find_element(*self.comp_city).clear()
            self.browser.find_element(*self.comp_city).send_keys(CCity)
            assert True
        except:
            assert False


    @allure.step('Fill in Province')
    def enter_province(self, CProv):
        try:
            self.browser.find_element(*self.comp_province).clear()
            self.browser.find_element(*self.comp_province).send_keys(CProv)
            assert True
        except:
            assert False

    @allure.step('Fill in Postal Code')
    def enter_postal(self, CPostal):
        try:
            self.browser.find_element(*self.comp_postal).clear()
            self.browser.find_element(*self.comp_postal).send_keys(CPostal)
            assert True
        except:
            assert False

    @allure.step('Fill in Country')
    def enter_country(self, CCountry):
        try:
            self.browser.find_element(*self.comp_country).clear()
            self.browser.find_element(*self.comp_country).send_keys(CCountry)
            assert True
        except:
            assert False

    @allure.step('Switch Tab to Website')
    def click_webtab(self):
        try:
            self.browser.find_element(*self.comp_webtab).click()
            assert True
        except:
            assert False

    @allure.step('Fill in Website')
    def enter_website(self, CWebsite):
        try:
            self.browser.find_element(*self.comp_website).clear()
            self.browser.find_element(*self.comp_website).send_keys(CWebsite)
            assert True
        except:
            assert False

    @allure.step('Switch Tab to Description')
    def click_desctab(self):
        try:
            self.browser.find_element(*self.comp_desctab).click()
            assert True
        except:
            assert False

    @allure.step('Fill in Description')
    def enter_description(self, CDescription):
        try:
            #self.browser.find_element(*self.comp_close).click()
            #self.browser.find_element(*self.comp_decript).clear()
            self.browser.find_element(*self.comp_decript).send_keys(CDescription)
            assert True
        except:
            assert False

