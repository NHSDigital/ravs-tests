from init_helpers import *

WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT = ("role", "heading", "What is the patient's NHS number?")
CONTINUE_TO_PATIENT_DETAILS_SCREEN = ("role", "button", "Continue")
PATIENT_NHS_NUMBER_TEXTBOX = ("role", "textbox", "What is the patient's NHS number?")
ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter the patient's NHS number")
ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter the patient's NHS number")
ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter a valid NHS number")
ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a valid NHS number")
ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK = ("role", "link", "Enter a valid NHS number")
ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a valid NHS number")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_what_is_patients_nhs_number_heading_label_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)

def check_what_is_the_patients_nhs_number_label_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(WHAT_IS_THE_PATIENTS_NHS_NUMBER_TEXT_ELEMENT)

def enter_patient_nhs_number(nhs_number):
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    find_element_and_perform_action(PATIENT_NHS_NUMBER_TEXTBOX, "input_text", nhs_number)

def click_streamlining_eligibility_radio_button(location):
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    element = ("role", "radio", location, True, {"nth": 0})
    find_element_and_perform_action(element, "click")

def check_enter_patient_nhs_number_error_message_link_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_patient_nhs_number_error_message_text_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_patient_nhs_number_error_message_link_LINK():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    find_element_and_perform_action(ENTER_PATIENT_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def check_enter_valid_nhs_number_error_message_link_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_valid_nhs_number_error_message_text_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_valid_nhs_number_error_message_link_LINK():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    find_element_and_perform_action(ENTER_VALID_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def check_enter_10_digit_nhs_number_error_message_link_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK)

def check_enter_10_digit_nhs_number_error_message_text_exists():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    return check_element_exists(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_TEXT)

def click_enter_10_digit_nhs_number_error_message_link_LINK():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    find_element_and_perform_action(ENTER_10_DIGIT_NHS_NUMBER_ERROR_MESSAGE_LINK, "click")

def click_continue_to_patient_details_screen():
    ensure_what_is_patients_nhs_number_heading_label_is_visible()
    find_element_and_perform_action(CONTINUE_TO_PATIENT_DETAILS_SCREEN, "click")
    time.sleep(5)
    wait_for_element_to_disappear(PATIENT_NHS_NUMBER_TEXTBOX)
