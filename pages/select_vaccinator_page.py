from init_helpers import *

WHO_IS_VACCINATOR_TEXT_ELEMENT = ("role", "heading", "Who is the vaccinator?")
CONTINUE_TO_CHOOSE_VACCINE_SCREEN = ("role", "button", "Continue")
SELECT_VACCINATOR_ERROR_MESSAGE_LINK = ("role", "link", "Please select a vaccinator")
SELECT_VACCINATOR_ERROR_MESSAGE_TEXT = ("text", "Error: Please select a vaccinator")

def ensure_who_is_vaccinator_heading_label_is_visible():
    if not check_element_exists(WHO_IS_VACCINATOR_TEXT_ELEMENT):
        wait_for_element_to_appear(WHO_IS_VACCINATOR_TEXT_ELEMENT)

def check_who_is_vaccinator_label_exists():
    ensure_who_is_vaccinator_heading_label_is_visible()
    return check_element_exists(WHO_IS_VACCINATOR_TEXT_ELEMENT)

def click_vaccinator_radio_button(vaccinator):
    ensure_who_is_vaccinator_heading_label_is_visible()
    element = ("role", "radio", vaccinator)
    find_element_and_perform_action(element, "click")

def click_continue_to_choose_vaccine_screen():
    ensure_who_is_vaccinator_heading_label_is_visible()
    find_element_and_perform_action(CONTINUE_TO_CHOOSE_VACCINE_SCREEN, "click")

def check_select_vaccinator_error_message_link_exists():
    ensure_who_is_vaccinator_heading_label_is_visible()
    return check_element_exists(SELECT_VACCINATOR_ERROR_MESSAGE_LINK)

def check_select_vaccinator_error_message_text_exists():
    ensure_who_is_vaccinator_heading_label_is_visible()
    return check_element_exists(SELECT_VACCINATOR_ERROR_MESSAGE_TEXT)

def click_select_vaccinator_error_message_link():
    ensure_who_is_vaccinator_heading_label_is_visible()
    find_element_and_perform_action(SELECT_VACCINATOR_ERROR_MESSAGE_LINK, "click")
