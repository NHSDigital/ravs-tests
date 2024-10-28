import time
from init_helpers import *
from pages.record_consent_page import YES_CONSENT_RADIO_BUTTON

ELIGIBLE_YES_RADIOBUTTON = ("label", "Yes")
ELIGIBLE_NO_RADIOBUTTON = ("label", "No")
ASSESSING_CLINICIAN_DROPDOWN_ELEMENT = ("label", "Assessing clinician")
ELIGIBILITY_TYPE_DROPDOWN_ELEMENT = ("label", "Eligibility type")
ASSESSMENT_DATE_INPUT_ELEMENT = ("label", "Assessment date")
COMMENTS_INPUT_ELEMENT = ("label", "Comments (Optional)")
SAVE_AND_RETURN_BUTTON=("role", "button" "Save and return")
BACK_TO_CHOOSE_VACCINE_BUTTON= ("link", "Back")
DATE_INPUT_ELEMENT = ("label", "Assessment date")
GIVE_VACCINE_RADIOBUTTON = ("label", "Give vaccine")
VACCINE_NOT_GIVEN_RADIOBUTTON = ("text", "Vaccine not given")
CONTINUE_TO_RECORD_CONSENT_BUTTON = ("role", "button", "Continue")
ASSESSMENT_NO_VACCINATION_REASON = ("label", "Reason vaccine not given")
ASSESSMENT_DATE_INCORRECT_ERROR_MESSAGE = ("text", "Error: Date cannot be older")
ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select an assessment date")
ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_LINK = ("text", "Select an assessment date")
EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Expected due date is required")
EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_LINK = ("text", "Expected due date is required")
ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select the assessing clinician")
ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_LINK = ("text", "Select the assessing clinician")
LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select a legal mechanism")
LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_LINK = ("text", "Select a legal mechanism")
ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select an assessment outcome")
ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_LINK = ("text", "Select an assessment outcome")
STAFF_ROLE_DROPDOWN_ELEMENT = ("label", "Staff role")
DUE_DATE_DAY = ("label", "Day")
DUE_DATE_MONTH = ("label", "Month")
DUE_DATE_YEAR = ("label", "Year")
SCREENING_CONSIDERATIONS_ELEMENT = ("text", "Screening considerations")

def check_screening_considerations_exist():
    wait_for_element_to_appear(SCREENING_CONSIDERATIONS_ELEMENT)
    return check_element_exists(SCREENING_CONSIDERATIONS_ELEMENT)

def click_screening_considerations():
    wait_for_element_to_appear(SCREENING_CONSIDERATIONS_ELEMENT)
    find_element_and_perform_action(SCREENING_CONSIDERATIONS_ELEMENT, "click")

def check_assessment_date_missing_error_message_text_exists():
    wait_for_element_to_appear(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_TEXT)

def check_assessment_date_missing_error_message_link_exists():
    wait_for_element_to_appear(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_LINK)

def click_assessment_date_missing_error_message_link():
    wait_for_element_to_appear(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(ASSESSMENT_DATE_MISSING_ERROR_MESSAGE_LINK, "click")

def check_expected_due_date_missing_error_message_text_exists():
    wait_for_element_to_appear(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_TEXT)

def check_expected_due_date_missing_error_message_link_exists():
    wait_for_element_to_appear(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_LINK)

def click_expected_due_date_missing_error_message_link():
    wait_for_element_to_appear(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(EXPECTED_DUE_DATE_MISSING_ERROR_MESSAGE_LINK, "click")

def check_assessing_clinician_missing_error_message_text_exists():
    wait_for_element_to_appear(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_TEXT)

def check_assessing_clinician_missing_error_message_link_exists():
    wait_for_element_to_appear(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_LINK)

def click_assessing_clinician_missing_error_message_link():
    wait_for_element_to_appear(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(ASSESSING_CLINICIAN_MISSING_ERROR_MESSAGE_LINK, "click")

def check_legal_mechanism_missing_error_message_text_exists():
    wait_for_element_to_appear(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_TEXT)

def check_legal_mechanism_missing_error_message_link_exists():
    wait_for_element_to_appear(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_LINK)

def click_legal_mechanism_missing_error_message_link():
    wait_for_element_to_appear(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(LEGAL_MECHANISM_MISSING_ERROR_MESSAGE_LINK, "click")

def check_assessment_outcome_missing_error_message_text_exists():
    wait_for_element_to_appear(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_TEXT)
    return check_element_exists(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_TEXT)

def check_assessment_outcome_missing_error_message_link_exists():
    wait_for_element_to_appear(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_LINK)
    return check_element_exists(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_LINK)

def click_assessment_outcome_missing_error_message_link():
    wait_for_element_to_appear(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(ASSESSMENT_OUTCOME_MISSING_ERROR_MESSAGE_LINK, "click")

def select_eligibility_type(type):
    if check_eligibility_type_is_visible() == True:
        find_element_and_perform_action(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT, "select_option", type)
    else:
        click_eligible_yes_radiobutton()

def enter_due_date(due_date):
    day, month, year = due_date.split('/')
    find_element_and_perform_action(DUE_DATE_DAY, "input_text", day)
    find_element_and_perform_action(DUE_DATE_MONTH,"input_text", month)
    find_element_and_perform_action(DUE_DATE_YEAR, "input_text", year)

def click_legal_mechanism(legal_mechanism):
    xpath_map = {
        "national protocol (np)": "//label[@for='LegalMechanismId-1']",
        "patient group directions (pgd)": "//label[@for='LegalMechanismId-2']",
        "patient specific directions (psd)": "//label[@for='LegalMechanismId-3']",
    }
    element = xpath_map.get(legal_mechanism.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def check_eligibility_type_is_visible():
    wait_for_element_to_appear(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)
    return check_element_exists(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)

def check_eligibility_type_is_enabled():
    wait_for_element_to_appear(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)
    return check_element_enabled(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)

def select_assessment_no_vaccination_reason(reason):
    wait_for_element_to_appear(ASSESSMENT_NO_VACCINATION_REASON)
    find_element_and_perform_action(ASSESSMENT_NO_VACCINATION_REASON, "select_option", reason)

def select_staff_role(role):
    wait_for_element_to_appear(STAFF_ROLE_DROPDOWN_ELEMENT)
    find_element_and_perform_action(STAFF_ROLE_DROPDOWN_ELEMENT, "select_option", role)

def select_assessing_clinician_with_name_and_council(name_and_council):
    wait_for_element_to_appear(ASSESSING_CLINICIAN_DROPDOWN_ELEMENT)
    find_element_and_perform_action(ASSESSING_CLINICIAN_DROPDOWN_ELEMENT, "select_option", name_and_council)

def click_give_vaccine_radiobutton():
    wait_for_element_to_appear(GIVE_VACCINE_RADIOBUTTON)
    find_element_and_perform_action(GIVE_VACCINE_RADIOBUTTON, "click")

def click_vaccine_not_given_radiobutton():
    wait_for_element_to_appear(VACCINE_NOT_GIVEN_RADIOBUTTON)
    find_element_and_perform_action(VACCINE_NOT_GIVEN_RADIOBUTTON, "click")

def click_eligible_yes_radiobutton():
    wait_for_element_to_appear(ELIGIBLE_YES_RADIOBUTTON)
    find_element_and_perform_action(ELIGIBLE_YES_RADIOBUTTON, "click")

def click_eligible_no_radiobutton():
    wait_for_element_to_appear(ELIGIBLE_NO_RADIOBUTTON)
    find_element_and_perform_action(ELIGIBLE_NO_RADIOBUTTON, "click")

def click_back_button_on_assessing_patient_screen():
    wait_for_element_to_appear(BACK_TO_CHOOSE_VACCINE_BUTTON)
    find_element_and_perform_action(BACK_TO_CHOOSE_VACCINE_BUTTON, "click")

def set_assessment_date(date):
    wait_for_element_to_appear(ASSESSMENT_DATE_INPUT_ELEMENT)
    find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "clear")
    find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "type_text", date)

def get_assessment_date_value():
    wait_for_element_to_appear(ASSESSMENT_DATE_INPUT_ELEMENT)
    return find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "get_text")

def check_back_to_choose_vaccine_button_works():
    wait_for_element_to_appear(BACK_TO_CHOOSE_VACCINE_BUTTON)
    return check_element_exists(BACK_TO_CHOOSE_VACCINE_BUTTON, True)

def check_assessment_outcome_give_vaccine_radiobutton_exists():
    wait_for_element_to_appear(GIVE_VACCINE_RADIOBUTTON)
    return check_element_exists(GIVE_VACCINE_RADIOBUTTON, True)

def check_assessment_date_incorrect_error_message_exists():
    wait_for_element_to_appear(ASSESSMENT_DATE_INCORRECT_ERROR_MESSAGE)
    return check_element_exists(ASSESSMENT_DATE_INCORRECT_ERROR_MESSAGE, False)

def check_assessment_outcome_vaccine_not_given_radiobutton_exists():
    wait_for_element_to_appear(VACCINE_NOT_GIVEN_RADIOBUTTON)
    return check_element_exists(VACCINE_NOT_GIVEN_RADIOBUTTON, True)

def click_assessment_outcome_give_vaccine_radiobutton():
    wait_for_element_to_appear(GIVE_VACCINE_RADIOBUTTON)
    find_element_and_perform_action(GIVE_VACCINE_RADIOBUTTON, "click")

def click_assessment_outcome_vaccine_not_given_radiobutton():
    wait_for_element_to_appear(VACCINE_NOT_GIVEN_RADIOBUTTON)
    find_element_and_perform_action(VACCINE_NOT_GIVEN_RADIOBUTTON, "click")

def enter_comments_for_assessing_patient(comments):
    wait_for_element_to_appear(COMMENTS_INPUT_ELEMENT)
    find_element_and_perform_action(COMMENTS_INPUT_ELEMENT, "input_text", comments)

def click_save_and_return_button_on_assessment_screen():
    wait_for_element_to_appear(SAVE_AND_RETURN_BUTTON)
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_record_consent_button():
    wait_for_element_to_appear(CONTINUE_TO_RECORD_CONSENT_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_RECORD_CONSENT_BUTTON, "click")
    if check_assessment_date_incorrect_error_message_exists() == False:
        wait_for_element_to_appear(YES_CONSENT_RADIO_BUTTON)
    else:
        return True
