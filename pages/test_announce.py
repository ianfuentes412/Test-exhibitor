import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class announceObjects:
    ann_btn = (By.XPATH, "//*[@id='menu_announcements']/a")
    ann_add_ann = "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/a"
    ann_editbtn = (By.XPATH, "//*[@id='edit10']")
    ann_edittxtbox = (By.XPATH, "//*[@id='announcement_text']")
    ann_savebtn = (By.XPATH, "//*[@id='update']")
    announcetype= (By.XPATH, "//*[@id='formupdate']/div[2]/div[2]/label")
    loaded_ann = (By.XPATH, "//h2[text()='Announcements']")
    del_ann=(By.XPATH, "//a[@text()='Delete']")
    check_change = (By.XPATH, "//*[contains('Thank')]")
    check_change2 = (By.XPATH, "//*[contains('dummy')]")

    def __init__(self,browser):
        self.browser = browser

    @allure.step('Enter Help Through Home Page')
    def enter_announce(self):
        self.browser.find_element(*self.ann_btn).click()

    @allure.step('Checking If Announcement Loaded')
    def check_announce_load(self):
        try:
            self.browser.find_element(*self.loaded_ann)
            assert True
        except:
            assert False

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

    @allure.step('Click the Delete Announcement Button')
    def delete_ann(self):
        self.browser.find_element(*self.del_ann).click()


    @allure.step('Check if Announcement is changed')
    def check_ann_change(self):
        try:
            self.browser.find_element(*self.check_change)
            assert True
        except:
            assert False

    @allure.step('Check if Announcement is changed')
    def check_ann_change2(self):
        try:
            self.browser.find_element(*self.check_change2)
            assert True
        except:
            assert False
