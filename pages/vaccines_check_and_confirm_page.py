from init_helpers import *

CONFIRM_BUTTON = ("//button[text()='Confirm']")

def click_confirm_button():
    find_element_and_perform_action(CONFIRM_BUTTON, "click")

