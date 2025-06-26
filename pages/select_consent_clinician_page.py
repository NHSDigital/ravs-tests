from init_helpers import *
import re

WHO_IS_GIVING_CONSENT_TEXT_ELEMENT = ("role", "heading", "Who is giving consent?")
CONTINUE_TO_INJECTION_SITE_SCREEN = ("role", "link", "Continue")
SELECT_WHO_GAVE_CONSENT_ERROR_MESSAGE_LINK = ("role", "link", "Select who gave consent")
SELECT_WHO_GAVE_CONSENT_ERROR_MESSAGE_TEXT = ("text", "Error: Select who gave consent")
ENTER_A_NAME_ERROR_MESSAGE_LINK = ("role", "link", "Enter a name")
ENTER_A_NAME_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a name")
ENTER_THE_RELATIONSHIP_TO_THE_PATIENT_MESSAGE_LINK = ("role", "link", "Enter the relationship to the patient")
ENTER_THE_RELATIONSHIP_TO_THE_PATIENT_MESSAGE_TEXT = ("text", "Error: Enter the relationship to the patient")
NAME_OF_PERSON_CONSENTING_TEXTBOX = ("role", "textbox", "Name")
RELATIONSHIP_OF_PERSON_CONSENTING_TO_THE_PATIENT_TEXTBOX = ("role", "textbox", "Relationship to the patient")

def ensure_who_is_giving_consent_label_is_visible():
    if not check_element_exists(WHO_IS_GIVING_CONSENT_TEXT_ELEMENT):
        wait_for_element_to_appear(WHO_IS_GIVING_CONSENT_TEXT_ELEMENT)

def check_who_is_giving_consent_label_exists():
    ensure_who_is_giving_consent_label_is_visible()
    return check_element_exists(WHO_IS_GIVING_CONSENT_TEXT_ELEMENT)

def click_consenting_person_radio_button(option):
    ensure_who_is_giving_consent_label_is_visible()
    pattern = re.compile(f"^{option.strip()}$", re.IGNORECASE)
    element = ("role", "radio", pattern, {"exact": True})
    find_element_and_perform_action(element, "click")
    
def check_select_who_gave_consent_error_message_link_exists():
    ensure_who_is_giving_consent_label_is_visible()
    return check_element_exists(SELECT_WHO_GAVE_CONSENT_ERROR_MESSAGE_LINK)

def check_select_who_gave_consent_error_message_text_exists():
    ensure_who_is_giving_consent_label_is_visible()
    return check_element_exists(SELECT_WHO_GAVE_CONSENT_ERROR_MESSAGE_TEXT)

def click_who_gave_consent_error_message_link():
    ensure_who_is_giving_consent_label_is_visible()
    find_element_and_perform_action(SELECT_WHO_GAVE_CONSENT_ERROR_MESSAGE_LINK, "click")

def click_continue_to_select_injection_site_screen():
    ensure_who_is_giving_consent_label_is_visible()
    find_element_and_perform_action(CONTINUE_TO_INJECTION_SITE_SCREEN, "click")

def enter_name_of_person_consenting(name):
    ensure_who_is_giving_consent_label_is_visible()
    find_element_and_perform_action(NAME_OF_PERSON_CONSENTING_TEXTBOX, "input_text", name)

def enter_relationship_of_person_consenting_to_patient(relationship):
    ensure_who_is_giving_consent_label_is_visible()
    find_element_and_perform_action(RELATIONSHIP_OF_PERSON_CONSENTING_TO_THE_PATIENT_TEXTBOX, "input_text", relationship)
