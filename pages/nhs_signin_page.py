import time
from init_helpers import *

SIGN_IN_BUTTON_ELEMENT = ("role", "button", "Sign in")
KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT = ("text", "Keep me signed in")
EMAIL_INPUT_ELEMENT = ("label", "Email")
PASSWORD_INPUT_ELEMENT = ("label", "Password")
ALERT_TEXT_EMAILADDRESS = ("//p[contains(@id, 'input-container-error')]")
ALERT_TEXT_PASSWORD = ("//p[contains(@id, 'input-container-error')]")
ERROR_UNABLE_TO_SIGN_IN = ("text", "Unable to sign in")
FOUND_SOME_ERRORS = ("text", "We found some errors. Please review the form and make corrections.")
LOGOUT_NAV_ELEMENT = ("role", "link", "Log out")
PAGE_LOADING_ELEMENT = ("role", "status")
NHS_SIGN_IN_HEADING_ELEMENT = ("role", "heading", "NHS Sign In")

def ensure_sign_in_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(NHS_SIGN_IN_HEADING_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(NHS_SIGN_IN_HEADING_ELEMENT)

def navigate_to_nhs_signin_page(url):
    navigate_to_url(url)

def check_signin_button_exists():
    ensure_sign_in_heading_element_exists()
    return check_element_exists(SIGN_IN_BUTTON_ELEMENT, True)

def click_nhs_signin_button():
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(SIGN_IN_BUTTON_ELEMENT, "click")
    wait_for_page_to_load(timeout=10)
    time.sleep(2)

def enter_email_address(emailAddress):
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(EMAIL_INPUT_ELEMENT, "input_text", emailAddress)

def clear_emailAddress():
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(EMAIL_INPUT_ELEMENT, "clear")

def clear_password():
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "clear")

def enter_password(password):
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "input_text", password)

def click_keep_me_signed_in():
    ensure_sign_in_heading_element_exists()
    find_element_and_perform_action(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT, "click")

def check_password_error_alert_exists():
    wait_for_page_to_load(timeout=10)
    wait_for_element_to_appear(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT)
    wait_for_element_to_appear(ALERT_TEXT_PASSWORD)
    return check_element_exists(ALERT_TEXT_PASSWORD, True)

def check_emailAddress_error_alert_exists():
    wait_for_element_to_appear(ALERT_TEXT_EMAILADDRESS)
    return check_element_exists(ALERT_TEXT_EMAILADDRESS, True)

def check_found_some_errors_alert_exists():
    wait_for_element_to_appear(FOUND_SOME_ERRORS)
    return check_element_exists(FOUND_SOME_ERRORS, True)

def get_password_missing_error_text():
    wait_for_element_to_appear(ALERT_TEXT_PASSWORD)
    return find_element_and_perform_action(ALERT_TEXT_PASSWORD, "get_text")

def get_emailAddress_missing_error_text():
    wait_for_element_to_appear(ALERT_TEXT_EMAILADDRESS)
    return find_element_and_perform_action(ALERT_TEXT_EMAILADDRESS, "get_text")

def check_unable_to_sign_in_error_exists():
    wait_for_element_to_appear(ERROR_UNABLE_TO_SIGN_IN)
    return check_element_exists(ERROR_UNABLE_TO_SIGN_IN, True)
