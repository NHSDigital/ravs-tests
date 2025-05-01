from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
SELECT_SITES_ERROR_MESSAGE_LINK = ("role", "button", "Select sites")
SELECT_SITES_ERROR_MESSAGE_TEXT = ("text", "Select sites")
CONTINUE_TO_CHOOSE_DATA_BUTTON = ("role", "button", "Continue")
BACK_TO_SELECT_VACCINE_BUTTON = ("role", "button", "Back")

def check_site_check_box_exists(site):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", site)
    wait_for_element_to_appear(element)
    return check_element_exists(element)

def check_site_check_box(site):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", site)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "check")

def check_select_site_error_message_text_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SELECT_SITES_ERROR_MESSAGE_TEXT)
    return check_element_exists(SELECT_SITES_ERROR_MESSAGE_TEXT)

def check_select_vaccine_error_message_link_exists():
    wait_for_element_to_appear(SELECT_SITES_ERROR_MESSAGE_LINK)
    return check_element_exists(SELECT_SITES_ERROR_MESSAGE_LINK)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(SELECT_SITES_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(SELECT_SITES_ERROR_MESSAGE_LINK, "click")

def check_continue_to_reports_select_data_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_CHOOSE_DATA_BUTTON)
    return check_element_exists(CONTINUE_TO_CHOOSE_DATA_BUTTON)

def click_continue_to_reports_select_data_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_CHOOSE_DATA_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_CHOOSE_DATA_BUTTON, "click")

def check_back_to_select_vaccine_page_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_VACCINE_BUTTON)
    return check_element_exists(BACK_TO_SELECT_VACCINE_BUTTON)

def click_back_to_select_vaccine_page_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_VACCINE_BUTTON)
    find_element_and_perform_action(BACK_TO_SELECT_VACCINE_BUTTON, "click")
