import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import allure

class helpObjects:

    preview_btn = (By.XPATH, "//*[@id='menu_preview']/a")
    preview_test = (By.XPATH, "//*[@id='company']")
    previewchat = (By.XPATH, "//*[@id='chat']")
    previewappoint=(By.XPATH, "//*[@id='appointment']")
    entrytest1=(By.XPATH,"//a[@text()='Business and Professional Communication']")
