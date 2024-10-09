from datetime import datetime
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

# Shared
NHS_NUMBER_INPUT = ("label", "Enter a 10 digit NHS number")

FIRST_NAME_INPUT = ("label", "First name")
LAST_NAME_INPUT = ("label", "Last name")
GENDER_OPTIONAL_SELECT = ("label", "Gender field optional")
POSTCODE_OPTIONAL_INPUT = ("label", "Postcode field optional")
GENDER_SELECT = ("label", "Gender")
POSTCODE_INPUT = ("label", "Full postcode")
DOB_DAY_INPUT = ("placeholder", "DD")
DOB_MONTH_INPUT = ("placeholder", "MM")
DOB_YEAR_INPUT = ("placeholder", "YYYY")

NHS_NUMBER_INPUT_ERROR_LABEL= ("text", "Error: Enter an NHS number")
NHS_NUMBER_INPUT_ERROR_BUTTON = ("button", "Enter an NHS number")
NHS_NUMBER_ENTER_10_DIGITS_ERROR_LABEL= ("text", "Enter 10 digits")
NHS_NUMBER_ENTER_10_DIGITS_ERROR_BUTTON = ("button", "Enter 10 digits")
FIRST_NAME_INPUT_ERROR_LABEL = ("text", "Error: Enter the first name")
LAST_NAME_INPUT_ERROR_LABEL = ("text", "Error: Enter the last name")
GENDER_SELECT_ERROR_LABEL = ("#GenderIdError")
POSTCODE_INVALID_INPUT_ERROR_LABEL = ("text", "Error: Enter the full postcode in the correct format")
DOB_INPUT_ERROR_LABEL = ("text", "Error: Enter the date of birth")

CREATE_NEW_PATIENT_BUTTON = ("role", "button", "Create new patient")
SEARCH_TIPS_LINK = ("link", "search tips")
PATIENT_NAME_LINK = ("//span[@class='nhsuk-action-link__text']")

GENDER_MAPPING = {
    "Male": "1",
    "Female": "2",
    "Other": "3",
    "Unknown": "4"
}

def format_nhs_number(nhs_number):
    formatted_nhs_number = f"{nhs_number[:3]} {nhs_number[3:6]} {nhs_number[6:]}"
    return formatted_nhs_number

def enter_first_name(first_name):
    input_text_into_element(FIRST_NAME_INPUT, first_name)

def enter_last_name(last_name):
    input_text_into_element(LAST_NAME_INPUT,last_name)

def enter_dob_day(dob_day):
    input_text_into_element(DOB_DAY_INPUT, str(dob_day))

def enter_dob_month(dob_month):
    input_text_into_element(DOB_MONTH_INPUT, str(dob_month))

def enter_dob_year(dob_year):
    input_text_into_element(DOB_YEAR_INPUT, str(dob_year))

def enter_dob(dob):
    format="%d/%m/%Y"
    date = datetime.strptime(dob, format)

    enter_dob_day(date.day)
    enter_dob_month(date.month)
    enter_dob_year(date.year)

def select_optional_gender(gender):
    gender_value = GENDER_MAPPING.get(gender)
    select_option(GENDER_OPTIONAL_SELECT, str(gender_value))

def enter_optional_postcode(postcode):
    input_text_into_element(POSTCODE_OPTIONAL_INPUT, postcode)

def select_gender(gender):
    gender_value = GENDER_MAPPING.get(gender)
    select_option(GENDER_SELECT, str(gender_value))

def enter_postcode(postcode):
    input_text_into_element(POSTCODE_INPUT, postcode)

def enter_nhs_number(nhsNumber):
    input_text_into_element(NHS_NUMBER_INPUT, nhsNumber)

def click_search_by_nhs_number_link():
    click_element(SEARCH_BY_NHS_NUMBER_LINK)

def click_search_by_demographics_link():
    click_element(SEARCH_BY_DEMOGRAPHICS_LINK)

def click_search_by_local_records_link():
    click_element(SEARCH_BY_LOCAL_RECORDS_LINK)

def click_patient_name_link():
    find_element_and_perform_action(PATIENT_NAME_LINK, "click")

def click_view_record():
    click_element(VIEW_RECORD_LINK)

def check_search_for_patient_button_visible():
    return check_if_element_exists(SEARCH_BUTTON)

def click_search_for_patient_button():
    click_element(SEARCH_BUTTON)

def click_create_a_new_patient_button():
    click_element(CREATE_NEW_PATIENT_BUTTON)

def check_error_appears_for_first_name(wait):
    return check_if_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def check_nhs_number_error_message_text_exists(errorMessage):
    element = ("text", f"Error: {errorMessage}")
    return check_if_element_exists(element)

def check_first_name_error_message_text_exists():
    return check_if_element_exists(FIRST_NAME_INPUT_ERROR_LABEL)

def check_last_name_error_message_text_exists():
    return check_if_element_exists(LAST_NAME_INPUT_ERROR_LABEL)

def check_dob_error_message_text_exists():
    return check_if_element_exists(DOB_INPUT_ERROR_LABEL)

def check_postcode_invalid_error_message_text_exists():
    return check_if_element_exists(POSTCODE_INVALID_INPUT_ERROR_LABEL)

def check_patient_name_search_result_exists(name, wait):
    element = (f"//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{name.lower()}')]")
    return check_element_exists(element, wait)

def check_patient_postcode_search_result_exists(postcode, wait):
    element = ("role", "cell", postcode)
    return check_if_element_exists(element, wait)

def check_patient_nhs_number_search_result_exists(nhsNumber, wait):
    element = ("role", "cell", nhsNumber)
    wait_for_element_to_appear(get_element_by_type(*element))
    return check_if_element_exists(element, wait)

def check_patient_not_found_for_nhs_number_message_exists(nhsNumber, wait):
    element = ("role", "heading", f"No result found for {nhsNumber}")
    return check_if_element_exists(element, wait)

def check_patient_not_found_message_exists(wait):
    element = (f"//h3[contains(text(), 'No result')]")
    return check_element_exists(element, wait)

def check_patient_multiple_results_found_message_exists(wait):
    element = (f"//h3[contains(text(), 'More than one result found')]")
    return check_element_exists(element, wait)

def check_create_new_patient_button_exists(wait):
    return check_if_element_exists(CREATE_NEW_PATIENT_BUTTON, wait)

def check_search_tips_link_exists(wait):
    return check_if_element_exists(SEARCH_TIPS_LINK, wait)

def click_on_patient_name_search_result(name):
    element = (f"//span[text()='{name}']")
    find_element_and_perform_action(element, "click")

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
    parts = address.rsplit(",", 1)
    address = parts[0].strip()
    postcode = parts[1].strip()
    element = (f"//td[contains(text(), '{address}') and contains(., '{postcode}')]")
    return check_element_exists(element, wait)

def get_patient_added_message(firstName):
    element = (f"//p[contains(text(),'{firstName}')]")
    return find_element_and_perform_action(element, "get_text")

def check_required_field_error_appears_for_forename(wait):
    return check_if_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_surname(wait):
    return check_if_element_exists(LAST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_dob(wait):
    return check_if_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_valid_field_error_appears_for_dob(wait):
    return check_if_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_gender(wait):
    return check_element_exists(GENDER_SELECT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_nhsNumber(wait):
    return check_if_element_exists(NHS_NUMBER_INPUT_ERROR_LABEL, wait)

def check_record_saved_element_exists(wait):
    return check_if_element_exists(RECORD_SAVED_DIALOGUE, wait)

def check_record_saved_message_appears(name):
    # checks the message exists, includes the patient name, includes a valid time value, and is the expected format

    element = (f"You successfuly saved {name} record")
    saved_message = find_element_and_perform_action(element, "get_text")

    pattern = r"You successfuly saved (.+) record at (\d{2}:\d{2})"

    # Check if the string matches the pattern
    if re.match(pattern, saved_message):
        return True
    else:
        return False
