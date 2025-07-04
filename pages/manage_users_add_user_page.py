from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
CONTINUE_TO_ADD_USER_BUTTON = ("role", "button", "Continue")
FIRST_NAME_INPUT_ELEMENT = ("label", "First name")
LAST_NAME_INPUT_ELEMENT = ("label", "Last name")
EMAIL_ADDRESS_INPUT_ELEMENT = ("label", "NHS-approved email address")
YES_REGISTERED_CLINICIAN_RADIO_BUTTON = ("label", "Yes")
NO_REGISTERED_CLINICIAN_RADIO_BUTTON = ("label", "No")
RECORDER_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Recorder")
LEAD_ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Lead administrator")
ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Administrator", True)
ENTER_FIRST_NAME_ERROR_MESSAGE_LINK = ("role", "button", "Enter a first name")
ENTER_FIRST_NAME_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a first name")
ENTER_LAST_NAME_ERROR_MESSAGE_LINK = ("role", "button", "Enter a last name")
ENTER_LAST_NAME_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a last name")
ENTER_EMAIL_ADDRESS_ERROR_MESSAGE_LINK = ("role", "button", "Enter an NHS-approved email address")
ENTER_EMAIL_ADDRESS_ERROR_MESSAGE_TEXT = ("text", "Error: Enter an NHS-approved email address")
ENTER_AN_NHS_EMAIL_ADDRESS_ERROR_MESSAGE_LINK = ("role", "button", "Enter an NHS-approved email address")
ENTER_AN_NHS_EMAIL_ADDRESS_ERROR_MESSAGE_TEXT = ("text", "Error: Enter an NHS-approved email address")
EMAIL_ADDRESS_MUST_BE_NHS_APPROVED_ERROR_MESSAGE_LINK = ("role", "button", "Email address must be NHS-approved")
EMAIL_ADDRESS_MUST_BE_NHS_APPROVED_ERROR_MESSAGE_TEXT = ("text", "Error: Email address must be NHS-approved")
SELECT_CLINICIAN_ERROR_MESSAGE_LINK = ("role", "button", "Select if they are a clinician")
SELECT_CLINICIAN_ERROR_MESSAGE_TEXT = ("text", "Error: Select if they are a clinician")
SELECT_PERMISSION_LEVEL_ERROR_MESSAGE_LINK = ("role", "button", "Select a permission level")
SELECT_PERMISSION_LEVEL_ERROR_MESSAGE_TEXT = ("text", "Error: Select a permission level")
EMAIL_ALREADY_EXISTS_IN_THIS_ORG_ERROR_MESSAGE_LINK = ("role", "button", "This email address has already been added")
EMAIL_ALREADY_EXISTS_IN_THIS_ORG_ERROR_MESSAGE_TEXT = ("text", "Error: This email address has already been added")
ADD_USER_HEADER_ELEMENT = ("role", "heading", "Add user")

def ensure_add_user_heading_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(ADD_USER_HEADER_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(ADD_USER_HEADER_ELEMENT)

def enter_first_name_to_add_user(first_name):
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(FIRST_NAME_INPUT_ELEMENT, "input_text", first_name)

def enter_last_name_to_add_user(last_name):
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(LAST_NAME_INPUT_ELEMENT, "input_text", last_name)

def enter_email_address_to_add_user(email_address):
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(EMAIL_ADDRESS_INPUT_ELEMENT, "input_text", email_address)

def select_yes_registered_clinician_radio_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(YES_REGISTERED_CLINICIAN_RADIO_BUTTON, "check")

def select_no_registered_clinician_radio_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(NO_REGISTERED_CLINICIAN_RADIO_BUTTON, "check")

def select_recorder_permission_level_radio_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(RECORDER_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def select_administrator_permission_level_radio_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def select_lead_administrator_permission_level_radio_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(LEAD_ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def select_permission_level_radio_button(permission):
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    element = ("label", permission, True)
    find_element_and_perform_action(element, "check")

def check_continue_to_add_user_button_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(CONTINUE_TO_ADD_USER_BUTTON)

def click_continue_to_add_user_button():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_ADD_USER_BUTTON, "click")

def check_enter_first_name_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_FIRST_NAME_ERROR_MESSAGE_LINK)

def click_enter_first_name_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(ENTER_FIRST_NAME_ERROR_MESSAGE_LINK, "click")

def check_enter_first_name_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_FIRST_NAME_ERROR_MESSAGE_TEXT)

def check_enter_last_name_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_LAST_NAME_ERROR_MESSAGE_LINK)

def click_enter_last_name_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(ENTER_LAST_NAME_ERROR_MESSAGE_LINK, "click")

def check_enter_last_name_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_LAST_NAME_ERROR_MESSAGE_TEXT)

def check_enter_email_address_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_EMAIL_ADDRESS_ERROR_MESSAGE_LINK)

def click_enter_email_address_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(ENTER_EMAIL_ADDRESS_ERROR_MESSAGE_LINK, "click")

def check_enter_email_address_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_EMAIL_ADDRESS_ERROR_MESSAGE_TEXT)

def check_enter_an_nhs_email_address_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_AN_NHS_EMAIL_ADDRESS_ERROR_MESSAGE_LINK)

def click_enter_an_nhs_email_address_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(ENTER_AN_NHS_EMAIL_ADDRESS_ERROR_MESSAGE_LINK, "click")

def check_enter_an_nhs_email_address_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(ENTER_AN_NHS_EMAIL_ADDRESS_ERROR_MESSAGE_TEXT)

def check_email_address_must_be_nhs_approved_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(EMAIL_ADDRESS_MUST_BE_NHS_APPROVED_ERROR_MESSAGE_LINK)

def click_email_address_must_be_nhs_approved_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(EMAIL_ADDRESS_MUST_BE_NHS_APPROVED_ERROR_MESSAGE_LINK, "click")

def check_email_address_must_be_nhs_approved_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(EMAIL_ADDRESS_MUST_BE_NHS_APPROVED_ERROR_MESSAGE_TEXT)

def check_select_clinician_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(SELECT_CLINICIAN_ERROR_MESSAGE_LINK)

def click_select_clinician_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(SELECT_CLINICIAN_ERROR_MESSAGE_LINK, "click")

def check_select_clinician_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(SELECT_CLINICIAN_ERROR_MESSAGE_TEXT)

def check_select_permission_level_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(SELECT_PERMISSION_LEVEL_ERROR_MESSAGE_LINK)

def click_select_permission_level_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(SELECT_PERMISSION_LEVEL_ERROR_MESSAGE_LINK, "click")

def check_select_permission_level_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(SELECT_PERMISSION_LEVEL_ERROR_MESSAGE_TEXT)

def check_email_already_exists_in_organisation_error_message_link_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(EMAIL_ALREADY_EXISTS_IN_THIS_ORG_ERROR_MESSAGE_LINK)

def click_email_already_exists_in_organisation_error_message_link():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    find_element_and_perform_action(EMAIL_ALREADY_EXISTS_IN_THIS_ORG_ERROR_MESSAGE_LINK, "click")

def check_email_already_exists_in_organisation_error_message_text_exists():
    ensure_add_user_heading_exists()
    wait_for_element_to_appear(CONTINUE_TO_ADD_USER_BUTTON)
    return check_element_exists(EMAIL_ALREADY_EXISTS_IN_THIS_ORG_ERROR_MESSAGE_TEXT)
