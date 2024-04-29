from datetime import datetime
from init_helpers import *

SEARCH_BY_PDS_TAB_ELEMENT = ("//a[text()='By demographics']") 
SEARCH_BY_NHS_NUMBER_TAB_ELEMENT = ("//a[text()='By NHS number']") 
SEARCH_BY_RECORDS_TAB_ELEMENT = ("//a[text()='By local records']") 
FIRSTNAME_INPUT_ELEMENT = ("#FirstName")
LASTNAME_INPUT_ELEMENT = ("#LastName")
DATEOFBIRTH_INPUT_ELEMENT = ("#DateOfBirth")
GENDER_DROPDOWN_ELEMENT = ("#GenderId")
POSTCODE_INPUT_ELEMENT = ("#Postcode")
NHS_NUMBER_INPUT_ELEMENT = ("#NhsNumber")
SEARCH_BUTTON_ELEMENT = ("//button[text()='Search']")
FIRSTNAME_INPUT_ERROR_LABEL = ("#FirstNameError")
LASTNAME_INPUT_ERROR_LABEL = ("#LastNameError")
DOB_INPUT_REQUIRED_ERROR_LABEL = ("#DateOfBirthRequiredError2")
DOB_INPUT_VALID_ERROR_LABEL = ("#DateOfBirthRequiredError1")
GENDER_INPUT_ERROR_LABEL = ("#GenderIdError")
POSTCODE_INPUT_ERROR_LABEL = ("#PostcodeError")
# NHSNUMBER_INPUT_ERROR_LABEL= ("#NhsNumberError")
NHSNUMBER_INPUT_ERROR_LABEL= ("//span[text()='NHS number cannot be found']")
NHSNUMBER_INPUT_ELEMENT=("#NhsNumber")
CREATE_NEW_PATIENT_BUTTON = ("//button[text()='Create new patient']")

def enter_forename(forename):
    find_element_and_perform_action(FIRSTNAME_INPUT_ELEMENT, "input_text", forename)

def enter_surname(surname):
    find_element_and_perform_action(LASTNAME_INPUT_ELEMENT, "input_text", surname)

def enter_dateofbirth(dob):
    find_element_and_perform_action(DATEOFBIRTH_INPUT_ELEMENT, "input_text", dob)    

def select_gender(gender):
    find_element_and_perform_action(GENDER_DROPDOWN_ELEMENT, "select_option", gender)        

def enter_postcode(postcode):
    find_element_and_perform_action(POSTCODE_INPUT_ELEMENT, "input_text", postcode)

def enter_NHSNumber(nhsNumber):
    find_element_and_perform_action(NHS_NUMBER_INPUT_ELEMENT, "input_text", nhsNumber)    

def click_search_byNHSNumber_tab():
    find_element_and_perform_action(SEARCH_BY_NHS_NUMBER_TAB_ELEMENT, "click")    

def click_search_byPatientDetails_tab():
    find_element_and_perform_action(SEARCH_BY_PDS_TAB_ELEMENT, "click")     

def click_search_byNHSNumber_tab():
    find_element_and_perform_action(SEARCH_BY_NHS_NUMBER_TAB_ELEMENT, "click")     

def click_search_byRecords_tab():
    find_element_and_perform_action(SEARCH_BY_RECORDS_TAB_ELEMENT, "click")     

def check_search_for_patient_button_visible():
    return check_element_exists(SEARCH_BUTTON_ELEMENT, False)   

def click_search_for_patient_button():
    find_element_and_perform_action(SEARCH_BUTTON_ELEMENT, "click")   

def click_search_by_pds_tab():
    find_element_and_perform_action(SEARCH_BY_PDS_TAB_ELEMENT, "click")

def click_search_by_records_tab():
    find_element_and_perform_action(SEARCH_BY_RECORDS_TAB_ELEMENT, "click")

def check_required_field_error_appears_for_forename(wait):
    return check_element_exists(FIRSTNAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_surname(wait):
    return check_element_exists(LASTNAME_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_dob(wait):
    return check_element_exists(DOB_INPUT_REQUIRED_ERROR_LABEL, wait)

def check_valid_field_error_appears_for_dob(wait):
    return check_element_exists(DOB_INPUT_VALID_ERROR_LABEL, wait)

def check_required_field_error_appears_for_gender(wait):
    return check_element_exists(GENDER_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_postcode(wait):
    return check_element_exists(POSTCODE_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_nhsNumber(wait):
    return check_element_exists(NHSNUMBER_INPUT_ERROR_LABEL, wait)

def check_patient_name_search_result_exists(name, wait):
    element = (f"//span[text()='{name}']")
    return check_element_exists(element, wait)

def check_patient_nhsnumber_search_result_exists(nhsnumber, wait):
    element = (f"//td[text()='{nhsnumber}']")
    return check_element_exists(element, wait)

def check_patient_not_found_message_exists(nhsnumber, wait):
    element = (f"//h3[contains(text(), 'No result found for') and contains(., '{nhsnumber}')]")
    return check_element_exists(element)

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