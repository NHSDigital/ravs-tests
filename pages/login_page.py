from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("//button[text()='Log In']")

def navigate_to_ravs_login_page(url):
    navigate_to_url(url)
    wait_for_page_to_load()

def check_login_button_exists():
    wait_for_page_to_load()
    return check_element_exists(LOGIN_BUTTON_ELEMENT, True)

def click_login_button():
    find_element_and_perform_action(LOGIN_BUTTON_ELEMENT, "click")
