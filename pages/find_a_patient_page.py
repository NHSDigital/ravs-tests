from datetime import datetime
from init_helpers import *

# Common
SEARCH_BY_DEMOGRAPHICS_LINK = ("//a[text()='By demographics']")
SEARCH_BY_NHS_NUMBER_LINK = ("//a[text()='By NHS number']")
SEARCH_BY_LOCAL_RECORDS_LINK = ("//a[text()='By local records']")
SEARCH_BUTTON = ("//button[text()='Search']")

# Shared
NHS_NUMBER_INPUT = ("#NhsNumber")

FIRST_NAME_INPUT = ("#FirstName")
LAST_NAME_INPUT = ("#LastName")
GENDER_SELECT = ("#GenderId")
POSTCODE_INPUT = ("#Postcode")
DATE_OF_BIRTH_INPUT = ("#DateOfBirth")

NHS_NUMBER_INPUT_ERROR_LABEL= ("#VaccineProgramIdError")
FIRST_NAME_INPUT_ERROR_LABEL = ("#FirstNameError")
LAST_NAME_INPUT_ERROR_LABEL = ("#LastNameError")
GENDER_SELECT_ERROR_LABEL = ("#GenderIdError")
POSTCODE_INPUT_ERROR_LABEL = ("#PostcodeError")
DOB_INPUT_ERROR_LABEL = ("#DateOfBirth > span[id^=DateOfBirthRequiredError]")

CREATE_NEW_PATIENT_BUTTON = ("//button[text()='Create new patient']")

def enter_first_name(first_name):
    find_element_and_perform_action(FIRST_NAME_INPUT, "input_text", first_name)

def enter_last_name(last_name):
    find_element_and_perform_action(LAST_NAME_INPUT, "input_text", last_name)

def enter_dob(dob):
    find_element_and_perform_action(DATE_OF_BIRTH_INPUT, "input_text", dob)

def select_gender(gender):
    find_element_and_perform_action(GENDER_SELECT, "select_option", gender)

def enter_postcode(postcode):
    find_element_and_perform_action(POSTCODE_INPUT, "input_text", postcode)

def enter_nhs_number(nhsNumber):
    find_element_and_perform_action(NHS_NUMBER_INPUT, "input_text", nhsNumber)

def click_search_by_nhs_number_link():
    find_element_and_perform_action(SEARCH_BY_NHS_NUMBER_LINK, "click")

def click_search_by_demographics_link():
    find_element_and_perform_action(SEARCH_BY_DEMOGRAPHICS_LINK, "click")

def click_search_by_local_records_link():
    find_element_and_perform_action(SEARCH_BY_LOCAL_RECORDS_LINK, "click")

def check_search_for_patient_button_visible():
    return check_element_exists(SEARCH_BUTTON, False)

def click_search_for_patient_button():
    find_element_and_perform_action(SEARCH_BUTTON, "click")

def check_error_appears_for_first_name(wait):
    return check_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def get_nhs_number_error_message_text():
    return find_element_and_perform_action(NHS_NUMBER_INPUT_ERROR_LABEL, "get_text")

def get_first_name_error_message_text():
    return find_element_and_perform_action(FIRST_NAME_INPUT_ERROR_LABEL, "get_text")

def get_last_name_error_message_text():
    return find_element_and_perform_action(LAST_NAME_INPUT_ERROR_LABEL, "get_text")

def get_dob_error_message_text():
    return find_element_and_perform_action(DOB_INPUT_ERROR_LABEL, "get_text")

def check_patient_name_search_result_exists(name, wait):
    element = (f"//span[text()='{name}']")
    return check_element_exists(element, wait)

def check_patient_nhs_number_search_result_exists(nhsNumber, wait):
    element = (f"//td[text()='{nhsNumber}']")
    return check_element_exists(element, wait)

def check_patient_not_found_message_exists(nhsNumber, wait):
    element = (f"//h3[contains(text(), 'No result found for') and contains(., '{nhsNumber}')]")
    return check_element_exists(element, wait)

def check_create_new_patient_button_exists(wait):
    return check_element_exists(CREATE_NEW_PATIENT_BUTTON, wait)

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
