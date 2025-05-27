from init_helpers import *

CONFIRM_DETAILS_AND_SAVE_BUTTON = ("//button[text()='Confirm details and save']")
CANCEL_CHECK_AND_CONFIRM_BUTTON = ("//button[text()='Cancel']")
ERROR_VACCINE_ALREADY_EXIST_AT_SITE = ("#error-summary-title")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_confirm_details_and_save_button_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CONFIRM_DETAILS_AND_SAVE_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CONFIRM_DETAILS_AND_SAVE_BUTTON)

def check_confirm_details_and_save_button_exists():
    ensure_confirm_details_and_save_button_is_visible()
    return check_element_exists(CONFIRM_DETAILS_AND_SAVE_BUTTON, False)

def click_confirm_details_and_save_vaccines_button():
    ensure_confirm_details_and_save_button_is_visible()
    find_element_and_perform_action(CONFIRM_DETAILS_AND_SAVE_BUTTON, "click")

def click_cancel_check_and_confirm_vaccines_button():
    if not check_element_exists(CANCEL_CHECK_AND_CONFIRM_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CANCEL_CHECK_AND_CONFIRM_BUTTON)
    find_element_and_perform_action(CANCEL_CHECK_AND_CONFIRM_BUTTON, "click")

def check_vaccine_already_exists_error_exists():
    ensure_confirm_details_and_save_button_is_visible()
    return check_element_exists(ERROR_VACCINE_ALREADY_EXIST_AT_SITE, False)
