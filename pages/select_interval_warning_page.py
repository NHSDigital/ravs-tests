from init_helpers import *

# This locator finds the "Continue anyway" link on the interval warning page
CONTINUE_ANYWAY_LINK = ("role", "link", "Continue anyway")

def click_continue_anyway_on_interval_warning_page():
    wait_for_element_to_appear(CONTINUE_ANYWAY_LINK)
    find_element_and_perform_action(CONTINUE_ANYWAY_LINK, "click")
