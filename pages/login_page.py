import time
from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("role", "button", "Log in")
YOU_ARE_NOT_LOGGED_IN_LABEL_ELEMENT = ("text", "You are not logged in.")
ACCEPT_COOKIES_ELEMENT = ("role", "button", "I'm OK with analytics cookies")
DO_NOT_USE_ANALYTICS_COOKIES_ELEMENT = ("role", "button", "Do not use analytics cookies")
PAGE_LOADING_ELEMENT = ("role", "status")
TOTAL_VACCINATIONS_TEXT_ELEMENT = ("role", "heading", "Total vaccinations")
LOGOUT_NAV_ELEMENT = ("role", "link", "Log out")

def ensure_you_are_not_logged_in_label_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(YOU_ARE_NOT_LOGGED_IN_LABEL_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(YOU_ARE_NOT_LOGGED_IN_LABEL_ELEMENT)

def navigate_to_ravs_login_page(url):
    navigate_to_url(url)
    if check_element_exists(ACCEPT_COOKIES_ELEMENT, False) is True:
        find_element_and_perform_action(ACCEPT_COOKIES_ELEMENT, "click")

def check_login_button_exists():
    return check_element_exists(LOGIN_BUTTON_ELEMENT, True)

def click_login_button():
    find_element_and_perform_action(LOGIN_BUTTON_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
