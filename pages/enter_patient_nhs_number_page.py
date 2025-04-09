from init_helpers import *

WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT = ("role", "heading", "What is the patient's NHS number?")
CONTINUE_TO_INJECTION_LOCATION_SCREEN = ("role", "button", "Continue")
ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter the patient's NHS number")
ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter the patient's NHS number")
ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter a valid NHS number")
ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a valid NHS number")
ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter a valid NHS number")
ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a valid NHS number")

def check_what_is_the_patients_nhs_number_label_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)

def click_eligibility_radio_button(location):
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    element = ("role", "radio", location)
    find_element_and_perform_action(element, "click")

def check_enter_patient_nhs_number_error_message_link_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_patient_nhs_number_error_message_text_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_patient_nhs_number_error_message_link_LINK():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    find_element_and_perform_action(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def check_enter_valid_nhs_number_error_message_link_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_valid_nhs_number_error_message_text_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_valid_nhs_number_error_message_link_LINK():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    find_element_and_perform_action(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def check_enter_10_digit_nhs_number_error_message_link_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_10_digit_nhs_number_error_message_text_exists():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    return check_element_exists(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_10_digit_nhs_number_error_message_link_LINK():
    wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)
    find_element_and_perform_action(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def click_continue_to_injection_location_screen():
    find_element_and_perform_action(CONTINUE_TO_INJECTION_LOCATION_SCREEN, "click")
