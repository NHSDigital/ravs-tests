from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
REACTIVATE_BUTTON = ("role", "button", "Reactivate")

def check_reactivate_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    return check_element_exists(REACTIVATE_BUTTON)

def click_reactivate_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    find_element_and_perform_action(REACTIVATE_BUTTON, "click")
