import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from resources.variables import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class announceObjects:
    ann_btn = (By.XPATH, "//*[@id='menu_announcements']/a")
    ann_add_ann = (By.XPATH, "//*[@id='addbutton']")
    ann_editbtn = (By.XPATH, "//*[@class='btn btn-primary mr-2']")
    ann_edittxtbox = (By.XPATH, "//*[@id='announcement_text']")
    ann_savebtn = (By.XPATH, "//*[@id='save']")
    ann_updatebtn=(By.XPATH, "//*[@id='update']")
    announcetype= (By.XPATH, "//*[@id='formnew']/div[2]/div[1]/label")
    loaded_ann = (By.XPATH, "//h2[text()='Announcements']")
    del_ann = (By.XPATH, "//*[@class='btn btn-primary']")
    check_change = (By.XPATH, "//*[@id='oneannouncement']")
    check_change2 = (By.XPATH, "//*[@id='successmessage']")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_announce(self):
        self.browser.find_element(*self.ann_btn).click()

    @allure.step('Checking If Announcement Loaded')
    def check_announce_load(self):
        time.sleep(1)
        allure.attach(self.browser.get_screenshot_as_png(), name='Announcement Tab Loaded',
                      attachment_type=allure.attachment_type.PNG)
        return self.browser.find_element(*self.loaded_ann)


    @allure.step('Clicking Add Announcement')
    def click_add_ann(self):
        self.browser.find_element(*self.ann_add_ann).click()

    @allure.step('Clicking Edit Announcement Button')
    def click_ann_edit(self):
        self.browser.find_element(*self.ann_editbtn).click()

    @allure.step('Enter New Announcement in Textbox')
    def new_announcement(self, ann_change):
        self.browser.find_element(*self.ann_edittxtbox).clear()
        self.browser.find_element(*self.ann_edittxtbox).send_keys(ann_change)

    @allure.step('Saving the New Announcement')
    def savenew_announcement(self):
        self.browser.find_element(*self.ann_savebtn).click()

    @allure.step('Select Type of Announcement')
    def announce_type(self):
        self.browser.find_element(*self.announcetype).click()

    @allure.step('Edit New Announcement in Textbox')
    def edit_announcement(self, ann_change):
        self.browser.find_element(*self.ann_edittxtbox).clear()
        self.browser.find_element(*self.ann_edittxtbox).send_keys(ann_change)

    @allure.step('Saving the Updated Announcement')
    def saveupdated_announcement(self):
        self.browser.find_element(*self.ann_updatebtn).click()

    @allure.step('Click the Delete Announcement Button')
    def delete_ann(self):
        self.browser.find_element(*self.del_ann).click()


    @allure.step('Check if Announcement is added')
    def check_ann_created(self):
        time.sleep(1)
        allure.attach(self.browser.get_screenshot_as_png(), name='Announcement Added',
                      attachment_type=allure.attachment_type.PNG)
        try:
            self.browser.find_element(*self.check_change)
            assert True
        except:
            assert False

    @allure.step('Check if Announcement is changed')
    def check_ann_change(self):
        time.sleep(1)
        allure.attach(self.browser.get_screenshot_as_png(), name='Announcement Changed',
                      attachment_type=allure.attachment_type.PNG)
        return self.browser.find_element(*self.check_change2)


    @allure.step('Adds a new Announcement')
    def add_new_announce(self):
        try:
            if self.browser.find_elements(*self.ann_add_ann):

                self.click_add_ann()
                self.edit_announcement(demo_announce)
                self.announce_type()
                self.savenew_announcement()
                self.check_ann_created()
        except NoSuchElementException:
            print("Announcement already done")

    @allure.step('Check if Announcement is deleted')
    def check_ann_delete(self):
        time.sleep(1)
        allure.attach(self.browser.get_screenshot_as_png(), name='Announcement Deleted',
                          attachment_type=allure.attachment_type.PNG)
        return self.browser.find_element(*self.check_change2)