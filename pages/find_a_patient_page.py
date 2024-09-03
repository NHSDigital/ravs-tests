from datetime import datetime
from init_helpers import *
import re

# Common
SEARCH_BY_DEMOGRAPHICS_LINK = ("//a[text()='By demographics']")
SEARCH_BY_NHS_NUMBER_LINK = ("//a[text()='By NHS number']")
SEARCH_BY_LOCAL_RECORDS_LINK = ("//a[text()='By local records']")
SEARCH_BUTTON = ("//button[text()='Search']")
RECORD_SAVED_DIALOGUE = ("//div[text()='Record saved']")
SUCCESSFULLY_SAVED_MESSAGE = ()
VIEW_RECORD_LINK = ("//a[text()='View record']")

# Shared
NHS_NUMBER_INPUT = ("#NhsNumber")

FIRST_NAME_INPUT = ("#FirstName")
LAST_NAME_INPUT = ("#LastName")
GENDER_SELECT = ("#GenderId")
POSTCODE_INPUT = ("#Postcode")
DOB_DAY_INPUT = ("//label[text()='Day']/following-sibling::input")
DOB_MONTH_INPUT = ("//label[text()='Month']/following-sibling::input")
DOB_YEAR_INPUT = ("//label[text()='Year']/following-sibling::input")

NHS_NUMBER_INPUT_ERROR_LABEL= ("#VaccineProgramIdError")
FIRST_NAME_INPUT_ERROR_LABEL = ("#FirstNameError")
LAST_NAME_INPUT_ERROR_LABEL = ("#LastNameError")
GENDER_SELECT_ERROR_LABEL = ("#GenderIdError")
POSTCODE_INPUT_ERROR_LABEL = ("#PostcodeError")
DOB_INPUT_ERROR_LABEL = ("#DateOfBirth > span[id^=DateOfBirthRequiredError]")

CREATE_NEW_PATIENT_BUTTON = ("//button[text()='Create new patient']")
SEARCH_TIPS_LINK = ("//a[text()='search tips']")
PATIENT_NAME_LINK = ("//span[@class='nhsuk-action-link__text']")

def enter_first_name(first_name):
    find_element_and_perform_action(FIRST_NAME_INPUT, "input_text", first_name)

def enter_last_name(last_name):
    find_element_and_perform_action(LAST_NAME_INPUT, "input_text", last_name)

def enter_dob_day(dob_day):
    find_element_and_perform_action(DOB_DAY_INPUT, "input_text", str(dob_day))

def enter_dob_month(dob_month):
    find_element_and_perform_action(DOB_MONTH_INPUT, "input_text", str(dob_month))

def enter_dob_year(dob_year):
    find_element_and_perform_action(DOB_YEAR_INPUT, "input_text", str(dob_year))

def enter_dob(dob):
    format="%d/%m/%Y"
    date = datetime.strptime(dob, format)

    enter_dob_day(date.day)
    enter_dob_month(date.month)
    enter_dob_year(date.year)

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

def click_patient_name_link():
    find_element_and_perform_action(PATIENT_NAME_LINK, "click")

def click_view_record():
    find_element_and_perform_action(VIEW_RECORD_LINK, "click")

def check_search_for_patient_button_visible():
    return check_element_exists(SEARCH_BUTTON, False)

def click_search_for_patient_button():
    find_element_and_perform_action(SEARCH_BUTTON, "click")

def click_create_a_new_patient_button():
    find_element_and_perform_action(CREATE_NEW_PATIENT_BUTTON, "click")

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

def get_postcode_error_message_text():
    return find_element_and_perform_action(POSTCODE_INPUT_ERROR_LABEL, "get_text")

def check_patient_name_search_result_exists(name, wait):
    element = (f"//span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{name.lower()}')]")
    return check_element_exists(element, wait)

def check_patient_postcode_search_result_exists(postcode, wait):
    element = (f"//td[text()='{postcode}']")
    return check_element_exists(element, wait)

def check_patient_nhs_number_search_result_exists(nhsNumber, wait):
    element = (f"//td[text()='{nhsNumber}']")
    return check_element_exists(element, wait)

def check_patient_not_found_for_nhs_number_message_exists(nhsNumber, wait):
    element = (f"//h3[contains(text(), 'No result') and contains(., '{nhsNumber}')]")
    return check_element_exists(element, wait)

def check_patient_nhs_number_not_found_message_exists(nhsnumber, wait):
    element = (f"//h3[contains(text(), 'No result found for') and contains(., '{nhsnumber}')]")
    return check_element_exists(element, wait)

def check_patient_not_found_message_exists(wait):
    element = (f"//h3[contains(text(), 'No result')]")
    return check_element_exists(element, wait)

def check_patient_multiple_results_found_message_exists(wait):
    element = (f"//h3[contains(text(), 'More than one result found')]")
    return check_element_exists(element, wait)

def check_create_new_patient_button_exists(wait):
    return check_element_exists(CREATE_NEW_PATIENT_BUTTON, wait)

def check_search_tips_link_exists(wait):
    return check_element_exists(SEARCH_TIPS_LINK, wait)

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
    return check_element_exists(FIRST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_surname(wait):
    return check_element_exists(LAST_NAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_dob(wait):
    return check_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_valid_field_error_appears_for_dob(wait):
    return check_element_exists(DOB_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_gender(wait):
    return check_element_exists(GENDER_SELECT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_postcode(wait):
    return check_element_exists(POSTCODE_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_nhsNumber(wait):
    return check_element_exists(NHS_NUMBER_INPUT_ERROR_LABEL, wait)

def check_record_saved_element_exists(wait):
    return check_element_exists(RECORD_SAVED_DIALOGUE, wait)

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
