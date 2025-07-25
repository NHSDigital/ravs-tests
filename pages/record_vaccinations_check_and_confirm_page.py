import time
from init_helpers import *

CHECK_AND_CONFIRM_LABEL_ELEMENT = ("role", "heading", "Check and confirm")
PATIENT_NAME_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Name']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_DOB_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Date of birth']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ADDRESS_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Address']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_NHS_NUMBER_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='NHS number']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Eligibility']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ASSESSMENT_PAGE_DETAILS_BUTTON = ("xpath", "//button[text()='Change assess the patient page details']")
PATIENT_CONSENT_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Consent?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CONSENT_GIVEN_BY_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Consent given by']/following-sibling::dd[@class='nhsuk-summary-list__value']")
GIVEN_VACCINE_LABEL_ELEMENT = ("xpath", "(//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccine']/following-sibling::dd[@class='nhsuk-summary-list__value'])")
GIVEN_TEAM_LABEL_ELEMENT = ("xpath", "(//div[@class='nhsuk-summary-list__row']/dt[text()='Team']/following-sibling::dd[@class='nhsuk-summary-list__value'])")
PATIENT_VACCINATION_LOCATION_LABEL_ELEMENT = ("xpath", "(//div[@class='nhsuk-summary-list__row']/dt[text()='Location']/following-sibling::dd[@class='nhsuk-summary-list__value'])")
PATIENT_VACCINATION_VACCINATOR_LABEL_ELEMENT = ("xpath", "(//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccinator']/following-sibling::dd[@class='nhsuk-summary-list__value'])")
PATIENT_VACCINATION_INJECTION_SITE_LABEL_ELEMENT = ("xpath", "(//div[@class='nhsuk-summary-list__row']/dt[text()='Injection site']/following-sibling::dd[@class='nhsuk-summary-list__value'])")
PATIENT_VACCINE_BATCH_LABEL_ELEMENT = ("xpath", "//div[@class='nhsuk-summary-list__row']/dt[text()='Batch']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_NHS_NUMBER_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='NHS number']]//a[text()='Change']")
CHANGE_VACCINE_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Vaccine']]//a[text()='Change']")
CHANGE_VACCINATOR_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Vaccinator']]//a[text()='Change']")
CHANGE_BATCH_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Batch']]//a[text()='Change']")
CHANGE_ELIGIBILITY_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Eligibility']]//a[text()='Change']")
CHANGE_LOCATION_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Location']]//a[text()='Change']")
CHANGE_INJECTION_SITE_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Injection site']]//a[text()='Change']")
CHANGE_CONSENT_GIVEN_BY_VALUE_BUTTON = ("xpath", "//div[@class='nhsuk-summary-list__row'][dt[text()='Consent given by']]//a[text()='Change']")
OPTIONAL_NOTE_TEXT_BOX_ELEMENT = ("role", "textbox", "Optional note")
OPTIONAL_NOTE_TEXT_LABEL_ELEMENT = ("text", "Optional note")
OPTIONAL_NOTE_TEXT_MESSAGE_ELEMENT = ("text", "This will not be sent to the patient's GP. Only your organisation will see it.")
CONFIRM_AND_SAVE_BUTTON = ("role", "button", "Confirm and save")
CANCEL_CONFIRM_DETAILS_BUTTON = ("role", "button", "Cancel")
BACK_ON_CONFIRM_DETAILS_PAGE_BUTTON = ("role", "link", "Back")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_check_and_confirm_label_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CHECK_AND_CONFIRM_LABEL_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CHECK_AND_CONFIRM_LABEL_ELEMENT)

def check_change_patient_nhs_number_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_PATIENT_NHS_NUMBER_VALUE_BUTTON)

def check_change_vaccine_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_VACCINE_VALUE_BUTTON)

def check_optional_note_text_box_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(OPTIONAL_NOTE_TEXT_BOX_ELEMENT)

def check_optional_note_text_label_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(OPTIONAL_NOTE_TEXT_LABEL_ELEMENT)

def check_optional_note_text_message_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(OPTIONAL_NOTE_TEXT_MESSAGE_ELEMENT)

def check_change_batch_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_BATCH_VALUE_BUTTON)

def check_change_eligibility_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_ELIGIBILITY_VALUE_BUTTON)

def check_change_location_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_LOCATION_VALUE_BUTTON)

def check_change_injection_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_LOCATION_VALUE_BUTTON)

def check_change_patient_nhs_number_link_exists():
    ensure_check_and_confirm_label_is_visible()
    return check_element_exists(CHANGE_PATIENT_NHS_NUMBER_VALUE_BUTTON)

def click_change_patient_nhs_number_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_PATIENT_NHS_NUMBER_VALUE_BUTTON, "click")

def click_change_assess_patient_page_details_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_PATIENT_ASSESSMENT_PAGE_DETAILS_BUTTON, "click")

def click_change_recorded_vaccine_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_VACCINE_VALUE_BUTTON, "click")

def click_change_vaccinator_value_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_VACCINATOR_VALUE_BUTTON, "click")

def click_change_eligibility_value_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_ELIGIBILITY_VALUE_BUTTON, "click")

def click_change_location_value_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_LOCATION_VALUE_BUTTON, "click")

def enter_optional_note(note):
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(OPTIONAL_NOTE_TEXT_BOX_ELEMENT, "input_text", note)

def click_change_injection_site_value_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_INJECTION_SITE_VALUE_BUTTON, "click")

def click_change_consent_given_by_value_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CHANGE_CONSENT_GIVEN_BY_VALUE_BUTTON, "click")

def click_confirm_and_save_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CONFIRM_AND_SAVE_BUTTON, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_back_button_on_check_and_confirm_record_vaccination_screen():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(BACK_ON_CONFIRM_DETAILS_PAGE_BUTTON, "click")

def click_cancel_confirm_details_button():
    ensure_check_and_confirm_label_is_visible()
    find_element_and_perform_action(CANCEL_CONFIRM_DETAILS_BUTTON, "click")

def get_patient_name_value_in_check_and_confirm_screen():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_NAME_LABEL_ELEMENT, "get_text")

def get_patient_dob_value_in_check_and_confirm_screen():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_DOB_LABEL_ELEMENT, "get_text")

def get_patient_address_value_in_check_and_confirm_screen():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_ADDRESS_LABEL_ELEMENT, "get_text")

def get_patient_nhs_number_value_in_check_and_confirm_screen():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_NHS_NUMBER_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_LABEL_ELEMENT, "get_text")

def get_given_vaccine_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(GIVEN_VACCINE_LABEL_ELEMENT, "get_text")

def get_team_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(GIVEN_TEAM_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_injection_site_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_VACCINATION_INJECTION_SITE_LABEL_ELEMENT, "get_text")

def get_vaccination_location_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_VACCINATION_LOCATION_LABEL_ELEMENT, "get_text")

def get_patient_consent_given_by_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_CONSENT_GIVEN_BY_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_batch_number_value():
    ensure_check_and_confirm_label_is_visible()
    return find_element_and_perform_action(PATIENT_VACCINE_BATCH_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_vaccinator_value():
    ensure_check_and_confirm_label_is_visible()
    text = find_element_and_perform_action(PATIENT_VACCINATION_VACCINATOR_LABEL_ELEMENT, "get_text")
    return text
