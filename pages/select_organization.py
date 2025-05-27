from init_helpers import *

CONTINUE_TO_HOME_PAGE_BUTTON = ("role", "button", "Continue")
CHOOSE_YOUR_ORGANISATION_HEADING_TEXT_ELEMENT = ("role", "heading", "Choose your organisation")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_select_organisation_text_heading_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CHOOSE_YOUR_ORGANISATION_HEADING_TEXT_ELEMENT):
        wait_for_element_to_appear(CHOOSE_YOUR_ORGANISATION_HEADING_TEXT_ELEMENT)

def click_continue_to_home_page_button():
    ensure_select_organisation_text_heading_exists()
    if check_element_exists(CONTINUE_TO_HOME_PAGE_BUTTON):
        find_element_and_perform_action(CONTINUE_TO_HOME_PAGE_BUTTON, "click")

def select_site(site):
    ensure_select_organisation_text_heading_exists()
    element = ("role", "radio", site)
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")
    else:
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        find_element_and_perform_action(element, "click")

