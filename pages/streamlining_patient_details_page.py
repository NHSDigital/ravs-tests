import re
import time
from init_helpers import *

REPORT_ERRORS_BUTTON = ("//button[text()='Report Errors']")
EXPANDED_COVID_19_BUTTON = ("(//button[@class='accordion-button'])[1]")
COLLAPSED_COVID_19_BUTTON = ("(//button[@class='accordion-button collapsed'])[1]")
EXPANDED_FLU_BUTTON = ("(//button[@class='accordion-button'])[2]")
COLLAPSED_FLU_BUTTON = ("(//button[@class='accordion-button collapsed'])[2]")
EXPANDED_RSV_BUTTON = ("(//button[@class='accordion-button'])[3]")
COLLAPSED_RSV_BUTTON = ("(//button[@class='accordion-button collapsed'])[3]")
EXPANDED_PERTUSSIS_BUTTON = ("(//button[@class='accordion-button'])[4]")
COLLAPSED_PERTUSSIS_BUTTON = ("(//button[@class='accordion-button collapsed'])[4]")
CHECK_IN_AND_RETURN_BUTTON=("//button[text()='Check in and return']")
CHOOSE_VACCINE_BUTTON=("role", "button", "Choose Vaccine")
PATIENT_DID_NOT_SHOW_BUTTON=("//button[text()='Patient did not show']")
BACK_BUTTON_ON_PATIENT_DETAILS_PAGE = ("link", "Back")
SHOW_ALL_BUTTON_COVID_RECORDS = ("(//h2[contains(text(), 'COVID-19')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_FLU_RECORDS = ("(//h2[contains(text(), 'Flu')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_RSV_RECORDS = ("(//h2[contains(text(), 'Respiratory syncytial virus (RSV)')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_PERTUSSIS_RECORDS = ("(//h2[contains(text(), 'Pertussis')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
EDIT_HISTORY_BUTTON = ("xpath", "//span[text()='Edit']")
DELETE_HISTORY_BUTTON = ("xpath", "//span[text()='Delete']")
VACCINE_SUMMARY_LIST_ROWS_ELEMENTS = ("xpath", "//dl[@class='nhsuk-summary-list mb-1']")
COVID_HISTORY_ELEMENT = ("xpath", "//div[text()='COVID-19']")
FLU_HISTORY_ELEMENT = ("xpath", "//div[text()='Flu']")
RSV_HISTORY_ELEMENT = ("xpath", "(//div[text()='Respiratory syncytial virus (RSV)'])[1]")
PERTUSSIS_HISTORY_ELEMENT = ("xpath", "//div[text()='Pertussis']")
PAGE_LOADING_ELEMENT = ("role", "status")
VACCINATION_HISTORY_NOT_AVAILABLE = ("role", "heading", "No vaccination history available")
PATIENT_NAME_ELEMENT = ("xpath", "//dt[text()='Name']/following-sibling::dd")
PATIENT_NHS_NUMBER_ELEMENT = ("xpath", "//dt[text()='NHS number']/following-sibling::dd")
PATIENT_DATE_OF_BIRTH_ELEMENT = ("xpath", "//dt[text()='Date of birth']/following-sibling::dd")
PATIENT_GENDER_ELEMENT = ("xpath", "//dt[text()='Gender']/following-sibling::dd")
PATIENT_PHONE_NUMBER_ELEMENT = ("xpath", "//dt[text()='Phone number']/following-sibling::dd")
PATIENT_ADDRESS_ELEMENT = ("xpath", "//dt[text()='Address']/following-sibling::dd")
PATIENT_DETAILS_TEXT_HEADING_ELEMENT = ("role", "heading", "Patient details", True)
VACCINATION_HISTORY_TEXT_HEADING_ELEMENT = ("role", "heading", "Vaccination history", True)
VACCINATION_HISTORY_TEXT_MESSAGE_ELEMENT = ("text", "This shows NHS vaccinations given in England. Currently it includes COVID-19, flu, pertussis and RSV.")
VACCINATION_HISTORY_PERTUSSIS_TEXT_MESSAGE_ELEMENT = ("text", "However, pertussis vaccinations given at a GP surgery are not shown.")
CONTINUE_TO_SELECT_CONSENTING_PERSON = ("role", "link", "Continue")
SCREENING_CONSIDERATIONS_LINK = ("text", "Screening considerations")
SCREENING_CONSIDERATIONS_QUESTION_1 = ("text", "Does the patient have a history of anaphylaxis or significant allergic reactions to any vaccines or their ingredients?")
SCREENING_CONSIDERATIONS_QUESTION_2 = ("text", "Has the patient had a serious adverse reaction after the COVID-19 vaccine?")
SCREENING_CONSIDERATIONS_QUESTION_3 = ("text", "Is the patient pregnant or could they be?")

def ensure_patient_details_heading_element_exists(patient_name):
    check_patient_details_label_element = ("role", "heading", f"Check {patient_name}'s details and vaccination history")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_disappear(CONTINUE_TO_SELECT_CONSENTING_PERSON)
    wait_for_element_to_appear(check_patient_details_label_element)
    if not check_element_exists(check_patient_details_label_element):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_disappear(CONTINUE_TO_SELECT_CONSENTING_PERSON)
        wait_for_element_to_appear(check_patient_details_label_element)
        wait_for_element_to_appear(VACCINATION_HISTORY_TEXT_HEADING_ELEMENT)
        wait_for_element_to_appear(VACCINATION_HISTORY_TEXT_MESSAGE_ELEMENT)
        wait_for_element_to_appear(VACCINATION_HISTORY_PERTUSSIS_TEXT_MESSAGE_ELEMENT)

def ensure_vaccination_history_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(VACCINATION_HISTORY_TEXT_HEADING_ELEMENT)
    if not check_element_exists(VACCINATION_HISTORY_TEXT_HEADING_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(VACCINATION_HISTORY_TEXT_HEADING_ELEMENT)

def check_screening_considerations_link_exists():
    ensure_vaccination_history_element_exists()
    return check_element_exists(SCREENING_CONSIDERATIONS_LINK)

def click_screening_considerations_link():
    ensure_vaccination_history_element_exists()
    find_element_and_perform_action(SCREENING_CONSIDERATIONS_LINK, "click")

def check_screening_considerations_question_1_exists():
    ensure_vaccination_history_element_exists()
    return check_element_exists(SCREENING_CONSIDERATIONS_QUESTION_1)

def check_screening_considerations_question_2_exists():
    ensure_vaccination_history_element_exists()
    return check_element_exists(SCREENING_CONSIDERATIONS_QUESTION_2)

def check_screening_considerations_question_3_exists():
    ensure_vaccination_history_element_exists()
    return check_element_exists(SCREENING_CONSIDERATIONS_QUESTION_3)

def check_patient_details_heading_exists(patient_name):
    check_patient_details_label_element = ("role", "heading", f"Check {patient_name}'s details and vaccination history")
    ensure_patient_details_heading_element_exists(patient_name)
    return check_element_exists(check_patient_details_label_element)

def get_patient_name_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_NAME_ELEMENT, "get_text")

def get_patient_nhs_number_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_NHS_NUMBER_ELEMENT, "get_text")

def get_patient_date_of_birth_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_DATE_OF_BIRTH_ELEMENT, "get_text")

def get_patient_gender_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_GENDER_ELEMENT, "get_text")

def get_patient_phone_number_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_PHONE_NUMBER_ELEMENT, "get_text")

def get_patient_address_value_in_patient_details_screen():
    return find_element_and_perform_action(PATIENT_ADDRESS_ELEMENT, "get_text")

def click_continue_to_select_consenting_person_screen():
    find_element_and_perform_action(CONTINUE_TO_SELECT_CONSENTING_PERSON, "click")
