from init_helpers import *

FIRST_ADD_BATCH_BUTTON = ("role", "link", "Add batch")
BACK_BUTTON_ON_VACCINE_BATCHES_PAGE = ("role", "link", "Back", True)
CONTINUE_TO_CHECK_AND_CONFIRM_VACCINE_BATCH_BUTTON = ("role", "button", "Continue")
SAVE_CHANGES_TO_VACCINE_BATCH_BUTTON = ("role", "button", "Save Changes")
BATCH_NUMBER_INPUT_FIELD = ("label", "Batch number")
EXPIRY_DATE_DAY_INPUT_FIELD = ("label", "Day")
EXPIRY_DATE_MONTH_INPUT_FIELD = ("label", "Month")
EXPIRY_DATE_YEAR_INPUT_FIELD = ("label", "Year")
ADD_BATCH_TITLE = ("role", "heading", "Add batch")
SINGLE_VIAL_PACK_SIZE_RADIO_BUTTON = ("role", "radio", "Single vial")
MULTI_VIALS_PACK_SIZE_RADIO_BUTTON = ("role", "radio", "10 vials")
CONTINUE_TO_CONFIRM_BATCH_BUTTON = ("role", "button", "Continue")
ERROR_MESSAGE_BATCH_ALREADY_EXISTS = ("text", "Error: There is already a batch with this number and expiry date")
ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER = ("text", "Error: Enter the batch number")
ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE = ("text", "Error: Enter the expiry date")
ERROR_MESSAGE_SELECT_THE_PACK_SIZE = ("text", "Error: Select a pack size")
ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS = ("role", "link", "There is already a batch with this number and expiry date")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER = ("role", "link", "Enter the batch number")
ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE = ("role", "link", "Enter the expiry date")
ERROR_MESSAGE_LINK_SELECT_PACK_SIZE = ("role", "link", "Select a pack size")
ERROR_MESSAGE_TEXT_EXPIRY_DATE_MUST_BE_IN_FUTURE = ("text", "Error: Expiry date must be in the future")
ERROR_MESSAGE_LINK_EXPIRY_DATE_MUST_BE_IN_FUTURE = ("role", "link", "Expiry date must be in the future")
PAGE_LOADING_ELEMENT = ("role", "status")
VACCINES_HEADING_TEXT_ELEMENT = ("role", "heading", "Vaccines")
ADD_BATCH_HEADING_TEXT_ELEMENT = ("role", "heading", "Add batch")
ADD_BATCH_BUTTON = ("role", "link", "Add batch")
EDIT_BATCH_BUTTON = ("role", "link", "Add batch")

def ensure_vaccines_heading_text_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(VACCINES_HEADING_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(VACCINES_HEADING_TEXT_ELEMENT)

def ensure_add_batch_heading_text_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(ADD_BATCH_HEADING_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(ADD_BATCH_HEADING_TEXT_ELEMENT)

def ensure_edit_batch_heading_text_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(ensure_edit_batch_heading_text_is_visible):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(ensure_edit_batch_heading_text_is_visible)

def ensure_add_batch_button_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(FIRST_ADD_BATCH_BUTTON)
    if not check_element_exists(FIRST_ADD_BATCH_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(FIRST_ADD_BATCH_BUTTON)

def select_pack_size(pack_size):
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(select_single_vial_pack_radio_button)
    if pack_size == "Single vial":
        select_single_vial_pack_radio_button()
    elif pack_size == "10 vials":
        select_multi_vial_pack_radio_button()
    else:
        print("Pack size is not available")

def get_selected_pack_size_radio_button_value_on_choose_vaccine_page():
    ensure_add_batch_button_is_visible()
    selected_value = get_checked_radio_button_text("Pack size")
    if selected_value != "":
        return selected_value
    else:
        return "Pack size not already selected"

def select_single_vial_pack_radio_button():
    ensure_add_batch_heading_text_is_visible()
    if check_element_exists(SINGLE_VIAL_PACK_SIZE_RADIO_BUTTON):
        find_element_and_perform_action(SINGLE_VIAL_PACK_SIZE_RADIO_BUTTON, "check")

def select_multi_vial_pack_radio_button():
    ensure_add_batch_heading_text_is_visible()
    if check_element_exists(MULTI_VIALS_PACK_SIZE_RADIO_BUTTON):
        find_element_and_perform_action(MULTI_VIALS_PACK_SIZE_RADIO_BUTTON, "check")

def check_select_pack_size_error_message_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_SELECT_THE_PACK_SIZE)
    return check_element_exists(ERROR_MESSAGE_SELECT_THE_PACK_SIZE, True)

def check_select_pack_size_error_message_link_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_SELECT_PACK_SIZE)
    return check_element_exists(ERROR_MESSAGE_LINK_SELECT_PACK_SIZE, True)

def click_add_batch_button():
    ensure_add_batch_button_is_visible()
    first_add_batch_button = get_element_by_type(*FIRST_ADD_BATCH_BUTTON).nth(0)
    wait_for_element_to_appear(first_add_batch_button)
    find_element_and_perform_action(first_add_batch_button, "click")

def check_batch_already_exists_error_message_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_BATCH_ALREADY_EXISTS)
    return check_element_exists(ERROR_MESSAGE_BATCH_ALREADY_EXISTS, False)

def check_batch_already_exists_error_message_link_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS)
    return check_element_exists(ERROR_MESSAGE_LINK_BATCH_ALREADY_EXISTS, True)

def check_enter_batch_number_error_message_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER)
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_number_error_message_link_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER)
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_NUMBER, True)

def check_enter_batch_expiry_date_error_message_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE)
    return check_element_exists(ERROR_MESSAGE_ENTER_THE_BATCH_EXPIRY_DATE, False)

def check_enter_batch_expiry_date_error_message_link_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE)
    return check_element_exists(ERROR_MESSAGE_LINK_ENTER_THE_BATCH_EXPIRY_DATE, True)

def click_continue_to_confirm_batch_details_button():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(CONTINUE_TO_CONFIRM_BATCH_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_CONFIRM_BATCH_BUTTON, "click")

def check_add_batch_title_exists(wait):
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ADD_BATCH_TITLE)
    return check_element_exists(ADD_BATCH_TITLE, wait)

def enter_batch_number(batch_number):
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(BATCH_NUMBER_INPUT_FIELD)
    if check_element_exists(BATCH_NUMBER_INPUT_FIELD, False):
        find_element_and_perform_action(BATCH_NUMBER_INPUT_FIELD, "input_text", batch_number)

def enter_vaccine_batch_number(batch_number):
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(BATCH_NUMBER_INPUT_FIELD)
    find_element_and_perform_action(BATCH_NUMBER_INPUT_FIELD, "input_text", batch_number)

def enter_expiry_date(expiry_date):
    ensure_add_batch_heading_text_is_visible()
    try:
        day, month, year = expiry_date.split('/')
        wait_for_element_to_appear(EXPIRY_DATE_DAY_INPUT_FIELD)
        find_element_and_perform_action(EXPIRY_DATE_DAY_INPUT_FIELD, "input_text", day)
        find_element_and_perform_action(EXPIRY_DATE_MONTH_INPUT_FIELD, "input_text", month)
        find_element_and_perform_action(EXPIRY_DATE_YEAR_INPUT_FIELD, "input_text", year)
    except ValueError:
        raise ValueError("Invalid expiry date format. Please use the format 'dd/MM/yyyy'.")

def click_continue_To_confirm_vaccine_details_button():
    ensure_add_batch_heading_text_is_visible()
    find_element_and_perform_action(CONTINUE_TO_CONFIRM_BATCH_BUTTON, "click")

def click_save_changes_to_vaccine_details_button():
    ensure_edit_batch_heading_text_is_visible()
    find_element_and_perform_action(SAVE_CHANGES_TO_VACCINE_BATCH_BUTTON, "click")

def check_expiry_date_must_be_in_future_error_message_text_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_TEXT_EXPIRY_DATE_MUST_BE_IN_FUTURE)
    return check_element_exists(ERROR_MESSAGE_TEXT_EXPIRY_DATE_MUST_BE_IN_FUTURE, False)

def check_expiry_date_must_be_in_future_error_message_link_is_displayed():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_EXPIRY_DATE_MUST_BE_IN_FUTURE)
    return check_element_exists(ERROR_MESSAGE_LINK_EXPIRY_DATE_MUST_BE_IN_FUTURE, False)

def click_expiry_date_must_be_in_future_error_message_link():
    ensure_add_batch_heading_text_is_visible()
    wait_for_element_to_appear(ERROR_MESSAGE_LINK_EXPIRY_DATE_MUST_BE_IN_FUTURE)
    find_element_and_perform_action(ERROR_MESSAGE_LINK_EXPIRY_DATE_MUST_BE_IN_FUTURE, "click")
