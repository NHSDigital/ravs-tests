import time
from init_helpers import *

YES_CONSENT_RADIO_BUTTON=("label", "Yes, they consent")
NO_CONSENT_RADIO_BUTTON=("label", "No")
CONSENT_GIVEN_BY_DROPDOWN_ELEMENT = ("label", "Consent given by")
CONSENT_CLINICIAN_DROPDOWN_ELEMENT = ("label", "Consenting clinician")
SAVE_AND_RETURN_BUTTON=("role", "button", "Save and return")
CONTINUE_TO_VACCINATE_BUTTON=("role", "button", "Continue")
REQUIRED_ALERT_BUTTON = ("//span[text()='Required']")
NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT = ("label", "Name of the person consenting")
RELATION_TO_PATIENT_INPUT_ELEMENT = ("label", "Relationship to the patient")
NO_CONSENT_REASON_DROPDOWN_ELEMENT = ("label", "No consent reason")
CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_LINK = ("Select the person giving consent")
CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_TEXT = ("Error: Select the person giving consent")
CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_LINK = ("Select the consenting clinician")
CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_TEXT = ("Error: Select the consenting clinician")
NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_LINK = ("Select a no consent reason")
NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_TEXT = ("Error: Select a no consent reason")

def check_consent_given_by_missing_detail_error_message_text_exists():
    wait_for_element_to_appear(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_TEXT)
    return check_element_exists(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_TEXT)

def check_consent_given_by_missing_detail_error_message_link_exists():
    wait_for_element_to_appear(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_LINK)
    return check_element_exists(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_LINK)

def click_consent_given_by_missing_detail_error_message_link():
    wait_for_element_to_appear(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(CONSENT_GIVEN_BY_MISSING_DETAIL_ERROR_MESSAGE_LINK, "click")

def check_consent_clinician_by_missing_detail_error_message_text_exists():
    wait_for_element_to_appear(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_TEXT)
    return check_element_exists(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_TEXT)

def check_consent_clinician_missing_detail_error_message_link_exists():
    wait_for_element_to_appear(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_LINK)
    return check_element_exists(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_LINK)

def click_consent_clinician_missing_detail_error_message_link():
    wait_for_element_to_appear(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(CONSENT_CLINICIAN_MISSING_DETAIL_ERROR_MESSAGE_LINK, "click")

def check_no_consent_reason_missing_detail_error_message_text_exists():
    wait_for_element_to_appear(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_TEXT)

def check_no_consent_reason_missing_detail_error_message_link_exists():
    wait_for_element_to_appear(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_LINK)

def click_no_consent_reason_missing_detail_error_message_link():
    wait_for_element_to_appear(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(NO_CONSENT_REASON_MISSING_ERROR_MESSAGE_LINK, "click")

def check_yes_to_consent_radiobutton_exists():
    wait_for_element_to_appear(YES_CONSENT_RADIO_BUTTON)
    return check_element_exists(YES_CONSENT_RADIO_BUTTON, True)

def check_no_to_consent_radiobutton_exists():
    wait_for_element_to_appear(NO_CONSENT_RADIO_BUTTON)
    return check_element_exists(NO_CONSENT_RADIO_BUTTON, True)

def click_yes_to_consent():
    wait_for_element_to_appear(YES_CONSENT_RADIO_BUTTON)
    find_element_and_perform_action(YES_CONSENT_RADIO_BUTTON, "check")

def click_no_to_consent():
    wait_for_element_to_appear(NO_CONSENT_RADIO_BUTTON)
    find_element_and_perform_action(NO_CONSENT_RADIO_BUTTON, "check")

def select_consent_clinician_with_name_and_council(nameandcouncil):
    wait_for_element_to_appear(CONSENT_CLINICIAN_DROPDOWN_ELEMENT)
    if check_element_enabled(CONSENT_CLINICIAN_DROPDOWN_ELEMENT):
        find_element_and_perform_action(CONSENT_CLINICIAN_DROPDOWN_ELEMENT, "select_option", nameandcouncil)

def select_reason_for_no_consent(reason):
    wait_for_element_to_appear(NO_CONSENT_REASON_DROPDOWN_ELEMENT)
    find_element_and_perform_action(NO_CONSENT_REASON_DROPDOWN_ELEMENT, "select_option", reason)

def select_consent_given_by_from_dropdown(givenBy):
    wait_for_element_to_appear(CONSENT_GIVEN_BY_DROPDOWN_ELEMENT)
    find_element_and_perform_action(CONSENT_GIVEN_BY_DROPDOWN_ELEMENT, "select_option", givenBy)

def click_save_and_return_button_on_record_consent_page():
    wait_for_element_to_appear(SAVE_AND_RETURN_BUTTON)
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_vaccinate_button():
    wait_for_element_to_appear(CONTINUE_TO_VACCINATE_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_VACCINATE_BUTTON, "click")

def check_continue_to_vaccinate_patient_button_exists():
    wait_for_element_to_appear(CONTINUE_TO_VACCINATE_BUTTON)
    return check_element_exists(CONTINUE_TO_VACCINATE_BUTTON)

def check_name_of_person_consenting_input_element_exists(wait):
    return check_element_exists(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, wait)

def check_relation_to_parent_input_element_exists(wait):
    return check_element_exists(RELATION_TO_PATIENT_INPUT_ELEMENT, wait)

def check_clinician_details_input_element_exists(wait):
    wait_for_element_to_appear(CONSENT_CLINICIAN_DROPDOWN_ELEMENT)
    return check_element_exists(CONSENT_CLINICIAN_DROPDOWN_ELEMENT, wait)

def enter_person_consenting_details(person):
    wait_for_element_to_appear(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT)
    find_element_and_perform_action(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, "input_text", person)

def enter_relationship_to_patient(relationship):
    wait_for_element_to_appear(RELATION_TO_PATIENT_INPUT_ELEMENT)
    find_element_and_perform_action(RELATION_TO_PATIENT_INPUT_ELEMENT, "input_text", relationship)

def enter_clinician_details(clinician):
    find_element_and_perform_action(CONSENT_CLINICIAN_DROPDOWN_ELEMENT, "select_option", clinician)

def get_consenting_clinician_details():
    return find_element_and_perform_action(CONSENT_CLINICIAN_DROPDOWN_ELEMENT, "get_selected_option")

def get_patient_consent_value_on_consent_page():
    selected_value = get_checked_radio_button_text("Does the patient or someone on their behalf consent to the vaccination?")
    if selected_value != "":
        if "they consent" in selected_value:
            return selected_value.replace(", they consent", "").strip()
        else:
            return selected_value
    else:
        return "Patient consent selection did not persist"

def get_patient_consent_given_by_value_on_consent_page():
    return find_element_and_perform_action(CONSENT_GIVEN_BY_DROPDOWN_ELEMENT,"get_selected_option")

