from init_helpers import *

SIGN_IN_BUTTON_ELEMENT = ("//input[@value='Sign in']")
KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT = ("//label[text()='Keep me signed in']")
EMAIL_INPUT_ELEMENT = ("#input28")
PASSWORD_INPUT_ELEMENT = ("#input36")
ALERT_TEXT_EMAILADDRESS = ("//p[contains(@id, 'input-container-error')]")
ALERT_TEXT_PASSWORD = ("//p[contains(@id, 'input-container-error')]")
ERROR_UNABLE_TO_SIGN_IN = ("//p[text()='Unable to sign in']")
FOUND_SOME_ERRORS = ("//p[text()='We found some errors. Please review the form and make corrections.']")

def navigate_to_nhs_signin_page(url):
    navigate_to_url(url)

def check_signin_button_exists():
    return check_element_exists(SIGN_IN_BUTTON_ELEMENT, True)

def click_nhs_signin_button():
    find_element_and_perform_action(SIGN_IN_BUTTON_ELEMENT, "click")

def enter_email_address(emailAddress):
    find_element_and_perform_action(EMAIL_INPUT_ELEMENT, "input_text", emailAddress)

def clear_emailAddress():
    clear_element(EMAIL_INPUT_ELEMENT)

def clear_password():
    clear_element(PASSWORD_INPUT_ELEMENT)

def enter_password(password):
    find_element_and_perform_action(PASSWORD_INPUT_ELEMENT, "input_text", password)

def click_keep_me_signedin():
    find_element_and_perform_action(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT, "click_checkbox")

def check_password_error_alert_exists():
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
    wait_for_page_to_load()
    return check_element_exists(ERROR_UNABLE_TO_SIGN_IN, True)
