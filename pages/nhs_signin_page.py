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
LOGOUT_NAV_ELEMENT = ("role", "link", "Log Out")

def navigate_to_nhs_signin_page(url):
    navigate_to_url(url)

def check_signin_button_exists():
    wait_for_element_to_appear(EMAIL_INPUT_ELEMENT)
    wait_for_element_to_appear(PASSWORD_INPUT_ELEMENT)
    wait_for_element_to_appear(SIGN_IN_BUTTON_ELEMENT)
    return check_element_exists(SIGN_IN_BUTTON_ELEMENT, True)

def click_nhs_signin_button():
    wait_for_element_to_appear(EMAIL_INPUT_ELEMENT)
    wait_for_element_to_appear(PASSWORD_INPUT_ELEMENT)
    wait_for_element_to_appear(SIGN_IN_BUTTON_ELEMENT)
    find_element_and_perform_action(SIGN_IN_BUTTON_ELEMENT, "click")
    wait_for_page_to_load(timeout=10)
    wait_for_element_to_appear(LOGOUT_NAV_ELEMENT)

def enter_email_address(emailAddress):
    wait_for_element_to_appear(EMAIL_INPUT_ELEMENT)
    find_element_and_perform_action(EMAIL_INPUT_ELEMENT, "input_text", emailAddress)

def clear_emailAddress():
    wait_for_element_to_appear(EMAIL_INPUT_ELEMENT)
    find_element_and_perform_action(EMAIL_INPUT_ELEMENT, "clear")

def clear_password():
    wait_for_element_to_appear(PASSWORD_INPUT_ELEMENT)
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "clear")

def enter_password(password):
    wait_for_element_to_appear(PASSWORD_INPUT_ELEMENT)
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "input_text", password)

def click_keep_me_signedin():
    find_element_and_perform_action(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT, "click")

def check_password_error_alert_exists():
    wait_for_page_to_load()
    return check_element_exists(ALERT_TEXT_PASSWORD, True)

def check_emailAddress_error_alert_exists():
    return check_element_exists(ALERT_TEXT_EMAILADDRESS, True)

def check_found_some_errors_alert_exists():
    return check_element_exists(FOUND_SOME_ERRORS, True)

def get_password_missing_error_text():
    return find_element_and_perform_action(ALERT_TEXT_PASSWORD, "get_text")

def get_emailAddress_missing_error_text():
    return find_element_and_perform_action(ALERT_TEXT_EMAILADDRESS, "get_text")

def check_unable_to_sign_in_error_exists():
    return check_element_exists(ERROR_UNABLE_TO_SIGN_IN, True)
