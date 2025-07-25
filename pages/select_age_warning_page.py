from init_helpers import *

# This locator finds the "Continue anyway" button on the age warning page
CONTINUE_ANYWAY_BUTTON = ("role", "button", "Continue anyway")

def click_continue_anyway_on_age_warning_page():
    wait_for_element_to_appear(CONTINUE_ANYWAY_BUTTON)
    find_element_and_perform_action(CONTINUE_ANYWAY_BUTTON, "click")
