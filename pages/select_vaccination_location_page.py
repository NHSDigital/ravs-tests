from init_helpers import *

WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT = ("role", "heading", "Where did the vaccination take place?")
CONTINUE_TO_PATIENT_NHS_NUMBER_SCREEN = ("role", "button", "Continue")
SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK = ("role", "link", "Select where the vaccination is taking place")
SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT = ("text", "Error: Select where the vaccination is taking place")

def check_why_are_you_giving_eligibility_label_exists():
    wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)
    return check_element_exists(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)

def click_eligibility_radio_button(location):
    wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)
    element = ("role", "radio", location)
    find_element_and_perform_action(element, "click")

def check_select_eligibility_error_message_link_exists():
    wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK)

def check_select_eligibility_error_message_text_exists():
    wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)
    return check_element_exists(SELECT_ELIGIBILITY_ERROR_MESSAGE_TEXT)

def click_select_eligibility_error_message_link():
    wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_ELIGIBILITY_ERROR_MESSAGE_LINK, "click")

def click_continue_to_find_patient_nhs_number_screen():
    find_element_and_perform_action(CONTINUE_TO_PATIENT_NHS_NUMBER_SCREEN, "click")
