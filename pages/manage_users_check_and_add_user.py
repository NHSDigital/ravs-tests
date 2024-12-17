from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
CONFIRM_AND_SEND_BUTTON = ("role", "button", "Continue")
CHANGE_NAME_LINK = ("role", "button", "Change name")
CHANGE_EMAIL_ADDRESS_LINK = ("role", "button", "Change email address")
CHANGE_CLINICAL_LINK = ("role", "button", "Change clinical")
CHANGE_PERMISSION_LEVEL_LINK = ("role", "button", "Change permission level")
# WELCOME_TO_OKTA_

def check_confirm_and_send_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CONFIRM_AND_SEND_BUTTON)

def click_confirm_and_send_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CONFIRM_AND_SEND_BUTTON, "click")
