from init_helpers import *

FIRST_NAME_FIELD = ("//dt[text() = 'First name']/following-sibling::dd")
LAST_NAME_FIELD = ("//dt[text() = 'Last name']/following-sibling::dd")
GENDER_FIELD = ("//dt[text() = 'Gender']/following-sibling::dd")
POSTCODE_FIELD = ("//dt[text() = 'Full postcode']/following-sibling::dd")
DATE_OF_BIRTH_FIELD = ("//dt[text() = 'Date of birth']/following-sibling::dd")
CONFIRM_AND_SAVE_BUTTON = ("//button[text()='Confirm and save']")
CANCEL_BUTTON = ("//button[text()='Cancel']")

def click_confirm_and_save_button():
    find_element_and_perform_action(CONFIRM_AND_SAVE_BUTTON, "click")

def click_cancel_button():
    find_element_and_perform_action(CANCEL_BUTTON, "click")

def get_first_name_field_text():
    return find_element_and_perform_action(FIRST_NAME_FIELD, "get_text")

def get_last_name_field_text():
    return find_element_and_perform_action(LAST_NAME_FIELD, "get_text")

def get_gender_field_text():
    return find_element_and_perform_action(GENDER_FIELD, "get_text")

def get_postcode_field_text():
    return find_element_and_perform_action(POSTCODE_FIELD, "get_text")

def get_date_of_birth_field_text():
    return find_element_and_perform_action(DATE_OF_BIRTH_FIELD, "get_text")
