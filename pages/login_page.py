import time
from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("role", "button", "Log In")
ACCEPT_COOKIES_ELEMENT = ("role", "button", "I'm OK with analytics cookies")
DO_NOT_USE_ANALYTICS_COOKIES_ELEMENT = ("role", "button", "Do not use analytics cookies")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def navigate_to_ravs_login_page(url):
    navigate_to_url(url)
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    add_cookie(url, "ravs-cookie-consent", "false")
    if check_element_exists(ACCEPT_COOKIES_ELEMENT, False) is True:
        find_element_and_perform_action(ACCEPT_COOKIES_ELEMENT, "click")

def check_login_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    return check_element_exists(LOGIN_BUTTON_ELEMENT, True)

def click_login_button():
    wait_for_element_to_appear(LOGIN_BUTTON_ELEMENT)
    find_element_and_perform_action(LOGIN_BUTTON_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
