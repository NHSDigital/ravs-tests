import time
from init_helpers import *

CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON=("role", "button", "Continue")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_to_enter_batch_details_button_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON)

def click_continue_to_add_batch_button():
    find_element_and_perform_action(CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON, "click")

def click_vaccine_radiobutton_on_add_vaccine_screen(vaccine):
    element = ("radio", vaccine, None, { "exact": True })
    find_element_and_perform_action(element, "click")

def click_vaccine_type_radiobutton_on_add_vaccine_screen(vaccine_type):
    element = ("radio", vaccine_type, None, { "exact": True })
    find_element_and_perform_action(element, "click")
