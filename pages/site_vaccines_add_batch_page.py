from init_helpers import *

ADD_BATCH_BUTTON = ("role", "link", "Add batch")
BACK_BUTTON_ON_VACCINE_BATCHES_PAGE = ("role", "link", "Back", True)
CONTINUE_TO_CHECK_AND_CONFIRM_VACCINE_BATCH_BUTTON = ("role", "button", "Continue")
BATCH_NUMBER_INPUT_FIELD = ("label", "Batch number")
EXPIRY_DATE_DAY_INPUT_FIELD = ("label", "Day")
EXPIRY_DATE_MONTH_INPUT_FIELD = ("label", "Month")
EXPIRY_DATE_YEAR_INPUT_FIELD = ("label", "Year")
ADD_BATCH_TITLE = ("role", "heading", "Add batch")
CONTINUE_TO_CONFIRM_BATCH_BUTTON = ("role", "button", "Continue")
ERROR_MESSAGE_BATCH_ALREADY_EXISTS = ("text", "Error: There is already a batch with this number and expiry date")
ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER = ("text", "Batch numberEnter the batch")
ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE = ("text", "Error: Enter the expiry date")
ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS = ("role", "button", "There is already a batch with this number and expiry date")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER = ("role", "button", "Enter the batch number")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE = ("role", "button", "Enter the expiry date")

def click_add_batch_button():
    wait_for_element_to_appear(ADD_BATCH_BUTTON)
    find_element_and_perform_action(ADD_BATCH_BUTTON, "click")

def check_batch_already_exists_error_message_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_BATCH_ALREADY_EXISTS)
    return check_element_exists(ERROR_MESSAGE_BATCH_ALREADY_EXISTS, False)

def check_batch_already_exists_error_message_link_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS)
    return check_element_exists(ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS, True)

def check_enter_batch_number_error_message_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER)
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_number_error_message_link_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER)
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_expiry_date_error_message_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE)
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE, False)

def check_enter_batch_expiry_date_error_message_link_is_displayed():
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE)
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE, True)

def click_continue_to_confirm_batch_details_button():
    wait_for_element_to_appear(CONTINUE_TO_CONFIRM_BATCH_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_CONFIRM_BATCH_BUTTON, "click")

def check_add_batch_title_exists(wait):
    wait_for_element_to_appear(ADD_BATCH_TITLE)
    return check_element_exists(ADD_BATCH_TITLE, wait)

def enter_batch_number(batch_number):
    wait_for_element_to_appear(BATCH_NUMBER_INPUT_FIELD)
    if check_element_exists(BATCH_NUMBER_INPUT_FIELD, False):
        find_element_and_perform_action(BATCH_NUMBER_INPUT_FIELD, "input_text", batch_number)

def enter_vaccine_batch_number(batch_number):
    wait_for_element_to_appear(BATCH_NUMBER_INPUT_FIELD)
    find_element_and_perform_action(BATCH_NUMBER_INPUT_FIELD, "input_text", batch_number)

def enter_expiry_date(expiry_date):
    try:
        day, month, year = expiry_date.split('/')
        wait_for_element_to_appear(EXPIRY_DATE_DAY_INPUT_FIELD)
        find_element_and_perform_action(EXPIRY_DATE_DAY_INPUT_FIELD, "input_text", day)
        find_element_and_perform_action(EXPIRY_DATE_MONTH_INPUT_FIELD, "input_text", month)
        find_element_and_perform_action(EXPIRY_DATE_YEAR_INPUT_FIELD, "input_text", year)
    except ValueError:
        raise ValueError("Invalid expiry date format. Please use the format 'dd/MM/yyyy'.")

def click_continue_To_confirm_vaccine_details_button():
    find_element_and_perform_action(CONTINUE_TO_CONFIRM_BATCH_BUTTON, "click")

