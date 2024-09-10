import time
from init_helpers import *

YES_CONSENT_RADIO_BUTTON=("#ConsentedYes")
NO_CONSENT_RADIO_BUTTON=("#ConsentedNo")
CONSENT_TYPE_DROPDOWN_ELEMENT = ("//select[@name='ConsentTypeId']")
CONSENT_CLINICIAN_DROPDOWN_ELEMENT = ("#ConsentClinicianId")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_TO_VACCINATE_BUTTON=("//button[text()='Continue']")
REQUIRED_ALERT_BUTTON = ("//span[text()='Required']")
NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT = ("#NameOfPersonConsenting")
RELATION_TO_PATIENT_INPUT_ELEMENT = ("#RelationshipToPatient")
RESPONSIBLE_CLINICIAN_INPUT_ELEMENT = ("#ConsentResponsibleClinicianId")
NO_CONSENT_REASON_DROPDOWN_ELEMENT = ("#NoConsentReasonId")
CONSENT_GIVEN_BY_DROPDOWN_ELEMENT = ("#ConsentTypeId")

def check_yes_to_consent_radiobutton_exists():
    check_element_exists(YES_CONSENT_RADIO_BUTTON, True)

def check_no_to_consent_radiobutton_exists():
    check_element_exists(NO_CONSENT_RADIO_BUTTON, True)

def click_yes_to_consent():
    find_element_and_perform_action(YES_CONSENT_RADIO_BUTTON, "click")

def click_no_to_consent():
    find_element_and_perform_action(NO_CONSENT_RADIO_BUTTON, "click")

def select_consent_clinician_with_name_and_council(nameandcouncil):
    if check_element_enabled(CONSENT_CLINICIAN_DROPDOWN_ELEMENT):
        find_element_and_perform_action(CONSENT_CLINICIAN_DROPDOWN_ELEMENT, "select_option", nameandcouncil)

def select_reason_for_no_consent(reason):
    find_element_and_perform_action(NO_CONSENT_REASON_DROPDOWN_ELEMENT, "select_option", reason)

def select_consent_given_by_from_dropdown(givenBy):
    find_element_and_perform_action(CONSENT_GIVEN_BY_DROPDOWN_ELEMENT, "select_option", givenBy)

def select_consentType(consentType):
    find_element_and_perform_action(CONSENT_TYPE_DROPDOWN_ELEMENT, "select_option", consentType)

def click_save_and_return_button_on_record_consent_page():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_vaccinate_button():
    find_element_and_perform_action(CONTINUE_TO_VACCINATE_BUTTON, "click")

def check_continue_to_vaccinate_patient_button_exists():
    return check_element_exists(CONTINUE_TO_VACCINATE_BUTTON)

def check_required_alert_exists(wait):
    return check_element_exists(REQUIRED_ALERT_BUTTON, wait)

def check_name_of_person_consenting_input_element_exists(wait):
    return check_element_exists(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, wait)

def check_relation_to_parent_input_element_exists(wait):
    return check_element_exists(RELATION_TO_PATIENT_INPUT_ELEMENT, wait)

def check_clinician_details_input_element_exists(wait):
    return check_element_exists(RESPONSIBLE_CLINICIAN_INPUT_ELEMENT, wait)

def enter_person_consenting_details(person):
    find_element_and_perform_action(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, "input_text", person)

def enter_relationship_to_patient(relationship):
    find_element_and_perform_action(RELATION_TO_PATIENT_INPUT_ELEMENT, "input_text", relationship)

def enter_clinician_details(clinician):
    find_element_and_perform_action(RESPONSIBLE_CLINICIAN_INPUT_ELEMENT, "input_text", clinician)
