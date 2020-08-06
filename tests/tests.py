
import time, allure
from pages.loginpage import loginpageObjects
from pages.homepage import homepageObjects
from pages.test_help import helpObjects
from pages.test_announce import announceObjects
from pages.test_banner import bannerObjects
from pages.test_preview import previewObjects
from resources.variables import *
#heeeasfsfasfasfasf
@allure.title('To check if login page loads and all elements present')
def test_loginpage_elements(browser):
    login_page = loginpageObjects(browser)
    login_page.load()
    assert login_page.check_input_email() == True, "Email field is not found on the login page"
    assert login_page.check_input_regcode() == True, "Registration Code field is not found on the login page"
    assert login_page.check_button_signin() == True, "Sign in button is not found on the login page"

@allure.title('To check if login fails with invalid credentials')
def test_login_invalid(browser):
    login_page = loginpageObjects(browser)
    login_page.enter_email(invalid_email)
    login_page.enter_regcode(invalid_regcode)
    login_page.click_signin()
    login_page.check_invalid_login() == "This is not a valid email address and registration code combination",\
        "Invalid login alert message is not correct."

@allure.title('To check if login succeedes with valid credentials')
def test_login_valid(browser):
    login_page = loginpageObjects(browser)
    home_page = homepageObjects(browser)
    login_page.enter_email(valid_email)
    login_page.enter_regcode(valid_regcode)
    login_page.click_signin()
    assert "Welcome" in home_page.check_valid_login_header(), "Valid login probably failed or wrong username found after login"
    assert valid_username in home_page.check_valid_login_usermenu(), "Valid login probably failed or wrong username found after login"

 #@allure.title('Checking if the video works when clicked')
#def test_home_video(browser):
   # home_page = homepageObjects(browser)
   # home_page.check_valid_video()
   # assert True

@allure.title('Checking if Help Screen Elements are Present')
def test_help_page(browser):
    help_page = helpObjects(browser)
    help_page.enter_help()
    help_page.click_dropdown1()
    help_page.check_dropdown1()
    help_page.click_dropdown2()
    help_page.check_dropdown2()
    help_page.click_dropdown3()
    help_page.check_dropdown3()
    help_page.click_dropdown4()
    help_page.check_dropdown4()

@allure.title('Checking Announcements Tab')
def test_announcement_page(browser):
    announce_page = announceObjects(browser)
    announce_page.enter_announce()
    announce_page.check_announce_load()

    announce_page.add_new_announce()

    announce_page.click_ann_edit()
    announce_page.edit_announcement(demo2_announce)
    announce_page.saveupdated_announcement()
    announce_page.check_ann_change2()
    announce_page.del_ann()

#@allure.title('Checking Banner Tab')
#def test_banner_page(browser):
    #banner_page = bannerObjects(browser)
    #banner_page.enter_banner()
    #banner_page.check_ban_load()
    #banner_page.check_button_signin()
    #banner_page.add_banner()
    #banner_page.check_title_text()
    #banner_page.check_link_text()
    #banner_page.edit_title_text(title)
    #banner_page.edit_link_text(link)
    #banner_page.add_new_image(banner)
    #banner_page.save_banner_btn()
    #banner_page.check_newbanner()
    #banner_page.delete_banner_btn()
    #banner_page.check_deleted_banner()

#@allure.title('Checking Preview Tab')
#def test_preview_page(browser):
    #preview_page = previewObjects(browser)
    #preview_page.enter_preview()
    #preview_page.check_preview_loaded()
    #preview_page.check_book_element1()




# @allure.title('To check if login succeedes with valid credentials (Failed intentionally)')
# def test_login_valid_failed(browser):
#     login_page = loginpageObjects(browser)
#     home_page = homepageObjects(browser)
#     home_page.logout()
#     login_page.enter_email(valid_email)
#     login_page.enter_regcode(valid_regcode)
#     login_page.click_signin()
#     assert "Sandeep Kumar" in home_page.check_valid_login_header(), "Valid login probably failed or wrong username found after login"
#     assert "Sandeep Kumar" in home_page.check_valid_login_usermenu(), "Valid login probably failed or wrong username found after login"



