from init_helpers import *

CONFIRM_DETAILS_AND_SAVE_BUTTON = ("//button[text()='Confirm details and save']")
CANCEL_CHECK_AND_CONFIRM_BUTTON = ("//button[text()='Cancel']")

def click_confirm_details_and_save_vaccines_button():
    find_element_and_perform_action(CONFIRM_DETAILS_AND_SAVE_BUTTON, "click")

def click_cancel_check_and_confirm_vaccines_button():
    find_element_and_perform_action(CANCEL_CHECK_AND_CONFIRM_BUTTON, "click")
