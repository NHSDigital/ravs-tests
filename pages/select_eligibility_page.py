from init_helpers import *

WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT = ("role", "heading", "Why are you giving them the eligibility?")
CONTINUE_TO_VACCINATION_LOCATION_SCREEN = ("role", "button", "Continue")
SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK = ("role", "link", "Select why you are giving them the vaccine")
SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT = ("text", "Error: Select why you are giving them the vaccine")

def check_why_are_you_giving_eligibility_label_exists():
    wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)
    return check_element_exists(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)

def click_eligibility_radio_button(eligibility):
    wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)
    element = ("role", "radio", eligibility)
    find_element_and_perform_action(element, "click")

def check_select_eligibility_error_message_link_exists():
    wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK)

def check_select_eligibility_error_message_text_exists():
    wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT)

def click_select_eligibility_error_message_link():
    wait_for_element_to_appear(WHY_ARE_YOU_GIVING_THE_THEM_THE_VACCINE_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK, "click")

def click_continue_to_choose_vaccination_location_screen():
    find_element_and_perform_action(CONTINUE_TO_VACCINATION_LOCATION_SCREEN, "click")
