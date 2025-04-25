from init_helpers import *

WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT = ("role", "heading", "Where did the vaccination take place?")
CONTINUE_TO_PATIENT_NHS_NUMBER_SCREEN = ("role", "button", "Continue")
SELECT_VACCINATION_LOCATION_ERROR_MESSAGE_LINK = ("role", "link", "Select where the vaccination is taking place")
SELECT_VACCINATION_LOCATION_ERROR_MESSAGE_TEXT = ("text", "Error: Select where the vaccination is taking place")
SELECT_CARE_HOME_ERROR_MESSAGE_LINK = ("role", "link", "Select the care home")
SELECT_CARE_HOME_ERROR_MESSAGE_TEXT = ("text", "Error: Select the care home")
CARE_HOME_TEXTBOX = ("role", "combobox", "Care home details")

def ensure_where_did_the_vaccination_take_place_heading_label_is_visible():
    if not check_element_exists(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT):
        wait_for_element_to_appear(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)

def check_where_did_the_vaccination_take_place_label_exists():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    return check_element_exists(WHERE_DID_THE_VACCINATION_TAKE_PLACE_TEXT_ELEMENT)

def click_vaccination_location_radio_button(location):
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    element = ("role", "radio", location)
    find_element_and_perform_action(element, "click")

def check_select_vaccination_location_error_message_link_exists():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    return check_element_exists(SELECT_VACCINATION_LOCATION_ERROR_MESSAGE_LINK)

def check_select_vaccination_location_error_message_text_exists():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    return check_element_exists(SELECT_VACCINATION_LOCATION_ERROR_MESSAGE_TEXT)

def click_select_vaccination_location_error_message_link():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    find_element_and_perform_action(SELECT_VACCINATION_LOCATION_ERROR_MESSAGE_LINK, "click")

def click_continue_to_find_patient_by_nhs_number_screen():
    find_element_and_perform_action(CONTINUE_TO_PATIENT_NHS_NUMBER_SCREEN, "click")

def check_select_care_home_error_message_link_exists():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    return check_element_exists(SELECT_CARE_HOME_ERROR_MESSAGE_LINK)

def check_select_care_home_error_message_text_exists():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    return check_element_exists(SELECT_CARE_HOME_ERROR_MESSAGE_TEXT)

def click_select_care_home_error_message_link():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    find_element_and_perform_action(SELECT_CARE_HOME_ERROR_MESSAGE_LINK, "click")

def click_continue_to_find_patient_by_nhs_number_screen():
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    find_element_and_perform_action(CONTINUE_TO_PATIENT_NHS_NUMBER_SCREEN, "click")

def enter_care_home_details(care_home):
    ensure_where_did_the_vaccination_take_place_heading_label_is_visible()
    find_element_and_perform_action(CARE_HOME_TEXTBOX, "input_text", care_home)
    element = ("role", "option", care_home)
    find_element_and_perform_action(element, "click")
