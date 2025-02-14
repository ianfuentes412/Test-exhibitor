import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure, os


class prizesObjects:
    prizes_btn = (By.XPATH, "//*[@id='menu_prizedraws']/a")
    prizes_load = (By.XPATH, "//h2[text()='Prizes']")
    add_prize_btn = (By.XPATH, "//*[@id='addprize']")
    pri_title = (By.XPATH, "//*[@id='prize_title']")
    pri_link = (By.XPATH, "//*[@id='prize_link']")
    pri_message = (By.XPATH, "//*[@id='prize_message']")
    pri_photo = (By.XPATH, "//*[@id='prize_image']")
    prize_type = (By.XPATH, "//*[@id='formnew']/div[6]/div[2]/label")
    prize_type2 = (By.XPATH, "//*[@id='formedit']/div[6]/div[3]/label")
    pri_descript = (By.XPATH, "//*[@id='tinymce']")
    pri_save = (By.XPATH, "//button[@id='save']")
    check_newprize = (By.XPATH, "//*[@id='createdmessage']")
    edit_prizes_btn = (By.XPATH, "//*[@id='prizelist']/tbody//tr[1]//td[1]//a[1]")
    check_editprize = (By.XPATH, "//*[@id='updatemessage']")
    pri_delete = (By.XPATH, "//*//*[@id='prizelist']/tbody/tr[3]/td[1]/a[2]")
    check_deletedprize= (By.XPATH, "//*[@id='successdelete']")


    def __init__(self, browser):
        self.browser = browser

    @allure.step('Enter Prizes Tab')
    def enter_prizes(self):
        self.browser.find_element(*self.prizes_btn).click()

    @allure.step('Check if Prizes tab has loaded')
    def check_prize_loaded(self):
        try:
            self.browser.find_element(*self.prizes_load)
            assert True
        except:
            assert False

    @allure.step('Checking if Add Button Exists')
    def prize_click_add_btn(self):
        try:
            self.browser.find_element(*self.add_prize_btn).click()
            assert True
        except:
            assert False

    @allure.step('Enter Title in Textbox')
    def add_prizes_title(self, pri_change):
        self.browser.find_element(*self.pri_title).clear()
        self.browser.find_element(*self.pri_title).send_keys(pri_change)

    @allure.step('Enter Link in Textbox')
    def add_prizes_link(self, pri_change2):
        self.browser.find_element(*self.pri_link).clear()
        self.browser.find_element(*self.pri_link).send_keys(pri_change2)

    @allure.step('Enter Message in Textbox')
    def add_prizes_message(self, pri_change3):
        self.browser.find_element(*self.pri_message).clear()
        self.browser.find_element(*self.pri_message).send_keys(pri_change3)

    @allure.step('Choose Prize Type')
    def add_prizes_type(self):
        try:
            self.browser.find_element(*self.prize_type).click()
            assert True
        except:
            assert False

    @allure.step('Upload Pictures in Prizes')
    def add_prizes_image(self):
        path = os.getcwd()
        if os.name == "posix":
            photo_path = path + "/banner.jpg"
        else:
            photo_path = path + "\\banner.jpg"
        self.browser.find_element(*self.pri_photo).send_keys(photo_path)

    @allure.step('Add Description in Prizes Textbox')
    def add_prizes_description(self, PriDescription):
        try:
            # self.browser.find_element(*self.comp_close).click()
            iframe = self.browser.find_element_by_id('prize_description_ifr')
            self.browser.switch_to.frame(iframe)
            self.browser.find_element(*self.pri_descript).clear()
            self.browser.find_element(*self.pri_descript).send_keys(PriDescription)
            self.browser.switch_to.default_content()
            assert True
        except:
            assert False

    @allure.step('Click to save Prize')
    def save_new_prizes(self):
        self.browser.find_element(*self.pri_save).click()
        time.sleep(1)

    @allure.step('Check if prize is saved')
    def check_new_prizes(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='New_Prizes',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_newprize)
            return True
        except:
            return False

    @allure.step('Click Edit Button')
    def edit_prizes(self):
        self.browser.find_element(*self.edit_prizes_btn).click()

    @allure.step('Check if Edit form is loaded')
    def check_edit_prize(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Prizes_Edit_Form',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.pri_title)
            return True
        except:
            return False

    @allure.step('Change the type of Prize')
    def edit_prizes_type(self):
        self.browser.find_element(*self.prize_type2).click()

    @allure.step('Change Picture in Prizes')
    def change_prizes_image(self):
        path = os.getcwd()
        if os.name == "posix":
            photo_path = path + "/resources/changed_prize.jpg"
        else:
            photo_path = path + "\\resources\\changed_prize.jpg"
        self.browser.find_element(*self.pri_photo).send_keys(photo_path)

    @allure.step('Check if prize is updated')
    def check_edited_prize(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Changed_Prizes',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_editprize)
            return True
        except:
            return False

    @allure.step('Click to delete Prize')
    def delete_prizes(self):
        self.browser.find_element(*self.pri_delete).click()
        time.sleep(1)

    @allure.step('Check if prize is deleted')
    def check_deleted_prize(self):
        allure.attach(self.browser.get_screenshot_as_png(), name='Deleted_Prize',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_deletedprize)
            return True
        except:
            return False