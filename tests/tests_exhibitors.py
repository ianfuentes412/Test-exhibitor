import time, allure
from pages.loginpage import loginpageObjects
from pages.homepage import homepageObjects
from pages.test_help import helpObjects
from pages.test_announce import announceObjects
from pages.test_compinfo import compObjects
from pages.test_banner import bannerObjects
from pages.test_preview import previewObjects
from pages.test_products import productObjects
from pages.test_prizes import prizesObjects
from resources.variables import *


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
    login_page.check_invalid_login() == "This is not a valid email address and registration code combination", \
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


@allure.title('Checking if Help Screen Elements are Present')
def test_help_page(browser):
    help_page = helpObjects(browser)
    help_page.enter_help()
    assert "Lorem ipsum" in help_page.check_dropdown1(), "Text did not display in dropdown 1"
    help_page.click_dropdown2()
    assert "Lorem ipsum" in help_page.check_dropdown2(), "Text did not display in dropdown 2"
    help_page.click_dropdown3()
    assert "Lorem ipsum" in help_page.check_dropdown3(), "Text did not display in dropdown 3"
    help_page.click_dropdown4()
    assert "Lorem ipsum" in help_page.check_dropdown4(), "Text did not display in dropdown 4"


@allure.title('Checking Announcements Tab')
def test_announcement_page(browser):
    announce_page = announceObjects(browser)
    announce_page.enter_announce()
    assert announce_page.check_announce_load() == True, "Announcement Page was not loaded"

    announce_page.add_new_announce()

    announce_page.click_ann_edit()
    announce_page.edit_announcement(demo2_announce)
    announce_page.saveupdated_announcement()
    assert announce_page.check_ann_change() == True, "Announcement is not Changed"
    announce_page.delete_ann()
    assert announce_page.check_ann_delete() == True, "Announcement is not Deleted"


@allure.title('Checking Banner Tab')
def test_banner_page(browser):
    banner_page = bannerObjects(browser)
    banner_page.enter_banner()
    assert banner_page.check_ban_load() == True, "Banner Page is not Loaded"
    assert banner_page.check_button_signin() == True, "Add Announcement Button was not Loaded"
    banner_page.add_banner()
    assert banner_page.check_title_text() == True, "Banner Title was not loaded"
    assert banner_page.check_link_text() == True, "Banner Link was not Loaded"
    banner_page.edit_title_text(title)
    banner_page.edit_link_text(link)
    banner_page.upload__banner_photo()
    banner_page.save_banner_btn()
    assert banner_page.check_new_banner() == True, "Banner was not Added"
    banner_page.delete_banner_btn()
    assert banner_page.check_deleted_banner() == True, "Banner was not Deleted"


# @allure.title('Checking Preview Tab')
# def test_preview_page(browser):
# preview_page = previewObjects(browser)
# preview_page.enter_preview()
# preview_page.check_preview_loaded()
# preview_page.check_book_element1()

@allure.title('Checking Products Tab')
def test_product_page(browser):
    product_page = productObjects(browser)
    product_page.enter_product()
    assert product_page.check_product_loaded() == True, "Product page is not Loaded"
    assert product_page.check_add_btn() == True, "Add Button is not Loaded"
    product_page.add_product_title(demo_prod_title)
    product_page.add_product_link(demo_prod_link)
    product_page.add_product_image()
    product_page.enter_prod_description(demo_comp_description)
    product_page.save_new_product()
    assert product_page.check_new_product() == True, "Product has not been added"
    product_page.delete_new_product()
    assert product_page.check_deleted_product() == True, "Product was not Deleted"

# @allure.title('Checking Prizes Tab')
# def test_prizes_page(browser):
# prizes_page = prizesObjects(browser)
# prizes_page.enter_prizes()
# prizes_page.check_prize_loaded()
# prizes_page.prize_click_add_btn()
# prizes_page.add_prizes_title(demo_pri_title)
# prizes_page.add_prizes_link(demo_pri_link)
# prizes_page.add_prizes_message(demo_pri_message)
# prizes_page.add_prizes_type()
# prizes_page.add_prizes_image()
# prizes_page.add_prizes_message(demo_comp_description)
# prizes_page.save_new_prizes()

# @allure.title('Checking Company Info Tab')
# def test_company_page(browser):
# comp_page = compObjects(browser)
# comp_page.enter_comp()
# comp_page.check_comp_loaded()
# comp_page.enter_comp_title(demo_comp_title)
# comp_page.enter_first_name(demo_comp_fname)
# comp_page.enter_last_name(demo_comp_lname)
# comp_page.enter_email(demo_comp_email)
# comp_page.enter_phone(demo_comp_phone)

# comp_page.click_addtab()
# comp_page.enter_add1(demo_comp_add1)
# comp_page.enter_add2(demo_comp_add2)
# comp_page.enter_city(demo_comp_city)
# comp_page.enter_postal(demo_comp_postal)
# comp_page.enter_province(demo_comp_province)
# comp_page.enter_country(demo_comp_country)
# comp_page.click_webtab()
# comp_page.enter_website(demo_comp_website)
# comp_page.click_desctab()
# comp_page.enter_description(demo_comp_description)

# comp_page.click_logotab()
# comp_page.upload_photo()

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
