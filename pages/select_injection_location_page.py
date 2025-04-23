from init_helpers import *

WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT = ("role", "heading", "Where did you give the injection?")
CONTINUE_TO_CHECK_AND_CONFIRM_SCREEN = ("role", "button", "Continue")
SELECT_INJECTION_LOCATION_ERROR_MESSAGE_LINK = ("role", "link", "Select the injection site")
SELECT_INJECTION_LOCATION_ERROR_MESSAGE_TEXT = ("text", "Error: Select the injection site")

def check_where_did_you_give_the_injection_label_exists():
    wait_for_element_to_appear(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)
    return check_element_exists(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)

def click_injection_location_radio_button(location):
    wait_for_element_to_appear(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)
    if "arm" not in location.lower():
        element = ("role", "radio", "Somewhere else")
        find_element_and_perform_action(element, "click")
    element = ("role", "radio", location)
    find_element_and_perform_action(element, "click")

def check_select_injection_location_error_message_link_exists():
    wait_for_element_to_appear(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)
    return check_element_exists(SELECT_INJECTION_LOCATION_ERROR_MESSAGE_LINK)

def check_select_injection_location_error_message_text_exists():
    wait_for_element_to_appear(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)
    return check_element_exists(SELECT_INJECTION_LOCATION_ERROR_MESSAGE_TEXT)

def click_select_injection_location_error_message_link():
    wait_for_element_to_appear(WHERE_DID_YOU_GIVE_THE_INJECTION_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_INJECTION_LOCATION_ERROR_MESSAGE_LINK, "click")

def click_continue_to_check_and_confirm_screen():
    find_element_and_perform_action(CONTINUE_TO_CHECK_AND_CONFIRM_SCREEN, "click")
