from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("role", "button", "Log In")
ACCEPT_COOKIES_ELEMENT = ("role", "button", "I'm ok with analytics cookies")

def navigate_to_ravs_login_page(url):
    navigate_to_url(url)
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    if check_if_element_exists(ACCEPT_COOKIES_ELEMENT, False) is True:
        click_element(ACCEPT_COOKIES_ELEMENT)

def check_login_button_exists():
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    return check_if_element_exists(LOGIN_BUTTON_ELEMENT, True)

def click_login_button():
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    click_element(LOGIN_BUTTON_ELEMENT)
