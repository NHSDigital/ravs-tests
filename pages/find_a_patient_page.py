from datetime import datetime
import time
from init_helpers import *
import re

# Common
SEARCH_BY_DEMOGRAPHICS_LINK = ("link", "By demographics")
SEARCH_BY_NHS_NUMBER_LINK = ("link", "By NHS number")
SEARCH_BY_LOCAL_RECORDS_LINK = ("link", "By local records")
SEARCH_BUTTON = ("role", "button", "Search")
RECORD_SAVED_DIALOGUE = ("text", "Record saved")
CLOSE_RECORD_SAVED_DIALOGUE_BUTTON = ("text", "Close")
SUCCESSFULLY_SAVED_MESSAGE = ("text", "You successfully saved")
VIEW_RECORD_LINK = ("text", "View record")
PAGE_LOADING_ELEMENT = ("role", "status")

# Shared
NHS_NUMBER_INPUT = ("id", "NhsNumber")

FIRST_NAME_INPUT = ("label", "First name")
LAST_NAME_INPUT = ("label", "Last name")
GENDER_OPTIONAL_SELECT = ("id", "GenderId")
POSTCODE_OPTIONAL_INPUT = ("id", "Postcode")
GENDER_SELECT = ("label", "Gender")
POSTCODE_INPUT = ("label", "Postcode")
DOB_DAY_INPUT = ("label", "Day")
DOB_MONTH_INPUT = ("label", "Month")
DOB_YEAR_INPUT = ("label", "Year")
FIND_A_PATIENT_LABEL_ELEMENT = ("role", "heading", "Find a patient", True)
CREATE_A_PATIENT_LABEL_ELEMENT = ("role", "heading", "Create a patient", True)
NHS_NUMBER_INPUT_ERROR_LABEL= ("text", "Error: Enter an NHS number")
NHS_NUMBER_INPUT_ERROR_BUTTON = ("button", "Enter an NHS number")
NHS_NUMBER_ENTER_10_DIGITS_ERROR_LABEL= ("text", "Enter 10 digits")
NHS_NUMBER_ENTER_10_DIGITS_ERROR_BUTTON = ("button", "Enter 10 digits")
FIRST_NAME_INPUT_ERROR_LABEL = ("text", "Error: Enter the first name")
LAST_NAME_INPUT_ERROR_LABEL = ("text", "Error: Enter the last name")
GENDER_SELECT_ERROR_LABEL = ("#GenderIdError")
POSTCODE_INVALID_INPUT_ERROR_LABEL = ("role", "link", "Enter the full postcode in the correct format")
DOB_INPUT_ERROR_LABEL = ("text", "Error: Enter the date of birth")
CREATE_NEW_PATIENT_BUTTON = ("role", "button", "Create new patient")
SEARCH_TIPS_LINK = ("link", "search tips")
PATIENT_NAME_LINK = ("//span[@class='nhsuk-action-link__text']")
CHOOSE_VACCINE_BUTTON=("role", "button", "Choose Vaccine")

GENDER_MAPPING = {
    "Male": "1",
    "Female": "2",
    "Other": "3",
    "Unknown": "4"
}

def ensure_find_a_patient_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(FIND_A_PATIENT_LABEL_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(FIND_A_PATIENT_LABEL_ELEMENT)

def ensure_create_a_patient_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CREATE_A_PATIENT_LABEL_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CREATE_A_PATIENT_LABEL_ELEMENT)

def format_nhs_number(nhs_number):
    formatted_nhs_number = f"{nhs_number[:3]} {nhs_number[3:6]} {nhs_number[6:]}"
    return formatted_nhs_number

def enter_first_name(first_name):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(FIRST_NAME_INPUT)
    wait_for_element_to_appear(LAST_NAME_INPUT)
    find_element_and_perform_action(FIRST_NAME_INPUT, "input_text", first_name)

def enter_first_name_create_a_patient_page(first_name):
    ensure_create_a_patient_heading_element_exists()
    wait_for_element_to_appear(FIRST_NAME_INPUT)
    wait_for_element_to_appear(LAST_NAME_INPUT)
    find_element_and_perform_action(FIRST_NAME_INPUT, "input_text", first_name)

def enter_last_name(last_name):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(LAST_NAME_INPUT)
    find_element_and_perform_action(LAST_NAME_INPUT, "input_text", last_name)

def enter_dob_day(dob_day):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(DOB_DAY_INPUT)
    find_element_and_perform_action(DOB_DAY_INPUT, "input_text", str(dob_day))

def enter_dob_month(dob_month):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(DOB_MONTH_INPUT)
    find_element_and_perform_action(DOB_MONTH_INPUT, "input_text", str(dob_month))

def enter_dob_year(dob_year):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(DOB_YEAR_INPUT)
    find_element_and_perform_action(DOB_YEAR_INPUT, "input_text", str(dob_year))

def enter_dob(dob):
    format="%d/%m/%Y"
    date = datetime.strptime(dob, format)

    enter_dob_day(date.day)
    enter_dob_month(date.month)
    enter_dob_year(date.year)

def select_optional_gender(gender):
    ensure_find_a_patient_heading_element_exists()
    gender_value = GENDER_MAPPING.get(gender)
    wait_for_element_to_appear(GENDER_OPTIONAL_SELECT)
    find_element_and_perform_action(GENDER_OPTIONAL_SELECT, "select_option", gender_value)

def enter_optional_postcode(postcode):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(POSTCODE_OPTIONAL_INPUT)
    find_element_and_perform_action(POSTCODE_OPTIONAL_INPUT, "input_text", postcode)

def select_gender(gender):
    gender_value = GENDER_MAPPING.get(gender)
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(GENDER_SELECT)
    find_element_and_perform_action(GENDER_SELECT, "select_option", gender_value)

def enter_postcode(postcode):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(POSTCODE_INPUT)
    find_element_and_perform_action(POSTCODE_INPUT, "input_text", postcode)

def enter_nhs_number(nhsNumber):
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(NHS_NUMBER_INPUT)
    find_element_and_perform_action(NHS_NUMBER_INPUT, "input_text", nhsNumber)

def click_search_by_nhs_number_link():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(SEARCH_BY_NHS_NUMBER_LINK)
    find_element_and_perform_action(SEARCH_BY_NHS_NUMBER_LINK, "click")

def click_search_by_demographics_link():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(SEARCH_BUTTON)
    wait_for_element_to_appear(SEARCH_BY_DEMOGRAPHICS_LINK)
    find_element_and_perform_action(SEARCH_BY_DEMOGRAPHICS_LINK, "click")
    wait_for_element_to_appear(SEARCH_BUTTON)

def click_search_by_local_records_link():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(SEARCH_BY_LOCAL_RECORDS_LINK)
    find_element_and_perform_action(SEARCH_BY_LOCAL_RECORDS_LINK, "click")

def click_patient_name_link():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(PATIENT_NAME_LINK)
    find_element_and_perform_action(PATIENT_NAME_LINK, "scroll_to")
    find_element_and_perform_action(PATIENT_NAME_LINK, "click")

def click_view_record():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(VIEW_RECORD_LINK)
    find_element_and_perform_action(VIEW_RECORD_LINK, "click")

def check_search_for_patient_button_visible():
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(SEARCH_BUTTON)

def click_search_for_patient_button():
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(SEARCH_BUTTON)
    find_element_and_perform_action(SEARCH_BUTTON, "click")
    ensure_find_a_patient_heading_element_exists()

def click_create_a_new_patient_button():#
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(CREATE_NEW_PATIENT_BUTTON)
    find_element_and_perform_action(CREATE_NEW_PATIENT_BUTTON, "click")

def check_error_appears_for_first_name(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def check_nhs_number_error_message_text_exists(errorMessage):
    ensure_find_a_patient_heading_element_exists()
    element = ("text", f"Error: {errorMessage}")
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_first_name_error_message_text_exists():
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(FIRST_NAME_INPUT_ERROR_LABEL)

def check_last_name_error_message_text_exists():
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(LAST_NAME_INPUT_ERROR_LABEL)

def check_dob_error_message_text_exists():
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(DOB_INPUT_ERROR_LABEL)

def check_postcode_invalid_error_message_text_exists():
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(POSTCODE_INVALID_INPUT_ERROR_LABEL)

def check_patient_name_search_result_exists(name, wait):
    ensure_find_a_patient_heading_element_exists()
    element = ("xpath", f"//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), \"{name.lower()}\")]")
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_patient_postcode_search_result_exists(postcode, wait):
    ensure_find_a_patient_heading_element_exists()
    element = ("role", "cell", postcode)
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_patient_nhs_number_search_result_exists(nhsNumber, wait):
    ensure_find_a_patient_heading_element_exists()
    element = ("role", "cell", nhsNumber)
    time.sleep(2)
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_patient_not_found_for_nhs_number_message_exists(nhsNumber, wait):
    ensure_find_a_patient_heading_element_exists()
    element = ("role", "heading", f"No result found for {nhsNumber}")
    time.sleep(2)
    ensure_find_a_patient_heading_element_exists()
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_patient_not_found_message_exists(wait):
    ensure_find_a_patient_heading_element_exists()
    element = (f"//h3[contains(text(), 'No result')]")
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_patient_multiple_results_found_message_exists(wait):
    ensure_find_a_patient_heading_element_exists()
    element = (f"//h3[contains(text(), 'More than one result found')]")
    wait_for_element_to_appear(element)
    return check_element_exists(element, wait)

def check_create_new_patient_button_exists(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(CREATE_NEW_PATIENT_BUTTON, wait)

def check_search_tips_link_exists(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(SEARCH_TIPS_LINK, wait)

def click_on_patient_name_search_result(name):
    element = (
        f"//span[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')="
        f"translate('{name}', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')]"
    )
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "click")
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)

def check_patient_dob_search_result_exists(dob, wait):
    try:
        dob_datetime = datetime.strptime(dob, '%d/%m/%Y')
    except ValueError:
        try:
            dob_datetime = datetime.strptime(dob, '%Y%m%d')
        except ValueError:
            raise ValueError("Unable to parse date: {}".format(dob))

    formatted_date = f"{dob_datetime.day}/{dob_datetime.month}/{dob_datetime.year}"

    element = f"//td[text()='{formatted_date}']"

    return check_element_exists(element, wait)

def check_patient_address_search_result_exists(address, wait):
    ensure_find_a_patient_heading_element_exists()
    parts = address.rsplit(",", 1)
    address = parts[0].strip()
    postcode = parts[1].strip()
    element = (f"//td[contains(text(), '{address}') and contains(., '{postcode}')]")
    return check_element_exists(element, wait)

def get_patient_added_message(firstName):
    ensure_find_a_patient_heading_element_exists()
    element = (f"//p[contains(text(),'{firstName}')]")
    wait_for_element_to_appear(element)
    return find_element_and_perform_action(element, "get_text")

def check_required_field_error_appears_for_forename(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_surname(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(LAST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_dob(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_valid_field_error_appears_for_dob(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_gender(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(GENDER_SELECT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_nhsNumber(wait):
    ensure_find_a_patient_heading_element_exists()
    return check_element_exists(NHS_NUMBER_INPUT_ERROR_LABEL, wait)

def check_record_saved_element_exists(wait):
    ensure_find_a_patient_heading_element_exists()
    time.sleep(2)
    wait_for_element_to_appear(RECORD_SAVED_DIALOGUE)
    return check_element_exists(RECORD_SAVED_DIALOGUE, wait)

def check_record_saved_message_appears(name):
    ensure_find_a_patient_heading_element_exists()
    element = (f"You successfully saved {name} record")
    saved_message = find_element_and_perform_action(element, "get_text")

    pattern = r"You successfully saved (.+) record at (\d{2}:\d{2})"

    # Check if the string matches the pattern
    if re.match(pattern, saved_message):
        return True
    else:
        return False
