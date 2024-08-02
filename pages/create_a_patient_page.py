from init_helpers import *
from pages.find_a_patient_page import *

CHECK_AND_CONFIRM_BUTTON = ("//button[text()='Check and confirm']")
CANCEL_BUTTON = ("//button[text()='Cancel']")

def click_check_and_confirm_button():
    find_element_and_perform_action(CHECK_AND_CONFIRM_BUTTON, "click")

def click_cancel_button():
    find_element_and_perform_action(CANCEL_BUTTON, "click")

def check_check_and_confirm_button_exists(wait):
    return check_element_exists(CHECK_AND_CONFIRM_BUTTON, wait)

def check_cancel_button_exists(wait):
    return check_element_exists(CANCEL_BUTTON, wait)