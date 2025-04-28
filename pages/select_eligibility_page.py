from init_helpers import *

WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT = ("role", "heading", "Why are you giving them the eligibility?")
CONTINUE_TO_VACCINATION_LOCATION_SCREEN = ("role", "button", "Continue")
SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK = ("role", "link", "Select why you are giving them the vaccine")
SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT = ("text", "Error: Select why you are giving them the vaccine")

def ensure_why_are_you_giving_vaccine_heading_label_is_visible():
    if not check_element_exists(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT):
        wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)

def check_why_are_you_giving_vaccination_label_exists():
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    return check_element_exists(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)

def click_eligibility_radio_button(eligibility):
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    element = ("role", "radio", eligibility)
    find_element_and_perform_action(element, "click")

def check_select_eligibility_error_message_link_exists():
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK)

def check_select_eligibility_error_message_text_exists():
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT)

def click_select_eligibility_error_message_link():
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    find_element_and_perform_action(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK, "click")

def click_continue_to_choose_vaccination_location_screen():
    ensure_why_are_you_giving_vaccine_heading_label_is_visible()
    find_element_and_perform_action(CONTINUE_TO_VACCINATION_LOCATION_SCREEN, "click")
