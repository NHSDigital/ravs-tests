from init_helpers import *

CONFIRM_BUTTON = ("//button[text()='Confirm']")
PAGE_LOADING_ELEMENT = ("role", "status")

def click_confirm_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CONFIRM_BUTTON):
        wait_for_element_to_appear(CONFIRM_BUTTON)
    find_element_and_perform_action(CONFIRM_BUTTON, "click")

