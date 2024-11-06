import time
from init_helpers import *
from pages.record_consent_page import YES_CONSENT_RADIO_BUTTON

ELIGIBLE_YES_RADIOBUTTON = ("#EligibleYes")
ELIGIBLE_NO_RADIOBUTTON = ("#EligibleNo")
ASSESSING_CLINICIAN_DROPDOWN_ELEMENT = ("#AssessmentClinicianId")
ELIGIBILITY_TYPE_DROPDOWN_ELEMENT = ("#EligibilityTypeId")
ASSESSMENT_DATE_INPUT_ELEMENT = ("#AssessmentDate")
COMMENTS_INPUT_ELEMENT = ("#AssessmentComments")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
BACK_TO_CHOOSE_VACCINE_BUTTON= ("//a[contains(@href, '/vaccination/add')]")
DATE_INPUT_ELEMENT = ("#AssessmentDate")
GIVE_VACCINE_RADIOBUTTON = ("#AssessmentOutcomeId-1")
VACCINE_NOT_GIVEN_RADIOBUTTON = ("#AssessmentOutcomeId-2")
CONTINUE_TO_RECORD_CONSENT_BUTTON = ("//button[text()='Continue']")
ASSESSMENT_NO_VACCINATION_REASON = ("#AssessmentNoVaccinationReasonId")
ASSESSMENT_DATE_INCORRECT_ERROR_MESSAGE = ("#AssessmentDateError")
STAFF_ROLE_DROPDOWN_ELEMENT = ("#StaffRoleId")
DUE_DATE_DAY = ("#ExpectedDueDateDay")
DUE_DATE_MONTH = ("#ExpectedDueDateMonth")
DUE_DATE_YEAR = ("#ExpectedDueDateYear")

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
    return check_element_exists(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)

def check_eligibility_type_is_enabled():
    return check_element_enabled(ELIGIBILITY_TYPE_DROPDOWN_ELEMENT)

def select_assessment_no_vaccination_reason(reason):
    find_element_and_perform_action(ASSESSMENT_NO_VACCINATION_REASON, "select_option", reason)

def select_staff_role(role):
    find_element_and_perform_action(STAFF_ROLE_DROPDOWN_ELEMENT, "select_option", role)

def select_assessing_clinician_with_name_and_council(name_and_council):
    find_element_and_perform_action(ASSESSING_CLINICIAN_DROPDOWN_ELEMENT, "select_option", name_and_council)

def click_give_vaccine_radiobutton():
    find_element_and_perform_action(GIVE_VACCINE_RADIOBUTTON, "click")

def click_vaccine_not_given_radiobutton():
    find_element_and_perform_action(VACCINE_NOT_GIVEN_RADIOBUTTON, "click")

def click_eligible_yes_radiobutton():
    find_element_and_perform_action(ELIGIBLE_YES_RADIOBUTTON, "click")

def click_eligible_no_radiobutton():
    find_element_and_perform_action(ELIGIBLE_NO_RADIOBUTTON, "click")

def click_back_button_on_assessing_patient_screen():
    find_element_and_perform_action(BACK_TO_CHOOSE_VACCINE_BUTTON, "click")

def set_assessment_date(date):
    find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "clear")
    find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "type_text", date)

def get_assessment_date_value():
    return find_element_and_perform_action(ASSESSMENT_DATE_INPUT_ELEMENT, "get_text")

def check_back_to_choose_vaccine_button_works():
    check_element_exists(BACK_TO_CHOOSE_VACCINE_BUTTON, True)

def check_assessment_outcome_give_vaccine_radiobutton_exists():
    return check_element_exists(GIVE_VACCINE_RADIOBUTTON, True)

def check_assessment_date_incorrect_error_message_exists():
    return check_element_exists(ASSESSMENT_DATE_INCORRECT_ERROR_MESSAGE, False)

def check_assessment_outcome_vaccine_not_given_radiobutton_exists():
    return check_element_exists(VACCINE_NOT_GIVEN_RADIOBUTTON, True)

def click_assessment_outcome_give_vaccine_radiobutton():
    return check_element_exists(GIVE_VACCINE_RADIOBUTTON, "click")

def click_assessment_outcome_vaccine_not_given_radiobutton():
    return check_element_exists(VACCINE_NOT_GIVEN_RADIOBUTTON, "click")

def enter_comments_for_assessing_patient(comments):
    find_element_and_perform_action(COMMENTS_INPUT_ELEMENT, "input_text", comments)

def click_save_and_return_button_on_assessment_screen():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_record_consent_button():
    find_element_and_perform_action(CONTINUE_TO_RECORD_CONSENT_BUTTON, "click")
    if check_assessment_date_incorrect_error_message_exists() == False:
        wait_for_element_to_appear(YES_CONSENT_RADIO_BUTTON)
    else:
        return True
