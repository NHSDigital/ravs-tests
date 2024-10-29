from init_helpers import *

VACCINE_BATCH_NUMBER_INPUT = ("#OtherBatchNumber")
BATCH_NUMBER_PREFIX_INPUT = ("#CovidBatchNumberPrefix")
BATCH_NUMBER_SUFFIX_INPUT = ("#CovidBatchNumberSuffix")
EXPIRY_DAY_INPUT = ("#ExpiryDate_1")
EXPIRY_MONTH_INPUT = ("#ExpiryDate_2")
EXPIRY_YEAR_INPUT = ("#ExpiryDate_3")
CONTINUE_BUTTON = ("//button[text()='Continue']")
ADD_BATCH_TITLE = ("role", "heading", "Add batch")
CONTINUE_TO_CONFIRM_BATCH_BUTTON = ("role", "button", "Continue")
ERROR_MESSAGE_BATCH_ALREADY_EXISTS = ("text", "Error: Batch number already exists")
ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER = ("text", "Error: Enter the batch number")
ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE = ("text", "Error: Enter the expiry date")
ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS = ("role", "link", "Batch number already exists")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER = ("role", "link", "Enter the batch number")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE = ("role", "link", "Enter the expiry date")

def check_batch_already_exists_error_message_is_displayed():
    return check_element_exists(ERROR_MESSAGE_BATCH_ALREADY_EXISTS, False)

def check_batch_already_exists_error_message_link_is_displayed():
    return check_element_exists(ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS, True)

def check_enter_batch_number_error_message_is_displayed():
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_number_error_message_link_is_displayed():
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_expiry_date_error_message_is_displayed():
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE, False)

def check_enter_batch_expiry_date_error_message_link_is_displayed():
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE, True)

def click_continue_to_confirm_batch_details_button():
    find_element_and_perform_action(CONTINUE_TO_CONFIRM_BATCH_BUTTON, "click")

def check_add_batch_title_exists(wait):
    return check_element_exists(ADD_BATCH_TITLE, wait)

def enter_batch_number(batch_number):
    if check_element_exists(VACCINE_BATCH_NUMBER_INPUT, False):
        find_element_and_perform_action(VACCINE_BATCH_NUMBER_INPUT, "input_text", batch_number)
    else:
        prefix, suffix = batch_number.split('-')
        find_element_and_perform_action(BATCH_NUMBER_PREFIX_INPUT, "input_text", prefix)
        find_element_and_perform_action(BATCH_NUMBER_SUFFIX_INPUT, "input_text", suffix)

def enter_vaccine_batch_number(batch_number):
    find_element_and_perform_action(VACCINE_BATCH_NUMBER_INPUT, "input_text", batch_number)

def enter_expiry_date(expiry_date):
    try:
        day, month, year = expiry_date.split('/')
        find_element_and_perform_action(EXPIRY_DAY_INPUT, "input_text", day)
        find_element_and_perform_action(EXPIRY_MONTH_INPUT, "input_text", month)
        find_element_and_perform_action(EXPIRY_YEAR_INPUT, "input_text", year)
    except ValueError:
        raise ValueError("Invalid expiry date format. Please use the format 'dd/MM/yyyy'.")

def click_continue_button():
    find_element_and_perform_action(CONTINUE_BUTTON, "click")

