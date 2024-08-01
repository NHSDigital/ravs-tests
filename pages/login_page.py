from init_helpers import *

LOGIN_BUTTON_ELEMENT = ("//button[text()='Log In']")
ACCEPT_COOKIES_ELEMENT = ("#nhsuk-cookie-banner__link_accept_analytics")

def navigate_to_ravs_login_page(url):
    navigate_to_url(url)
    wait_for_element_to_appear(ACCEPT_COOKIES_ELEMENT)
    if check_element_exists(ACCEPT_COOKIES_ELEMENT):
        find_element_and_perform_action(ACCEPT_COOKIES_ELEMENT, "click")

def check_login_button_exists():
    return check_element_exists(LOGIN_BUTTON_ELEMENT, True)

def click_login_button():
    find_element_and_perform_action(LOGIN_BUTTON_ELEMENT, "click")
