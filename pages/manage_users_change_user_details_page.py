from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON = ("role", "button", "Continue")
YES_REGISTERED_CLINICIAN_RADIO_BUTTON = ("label", "Yes")
NO_REGISTERED_CLINICIAN_RADIO_BUTTON = ("label", "No")
RECORDER_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Recorder")
LEAD_ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Lead administrator")
ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON = ("label", "Administrator", True)
DEACTIVATE_THE_ACCOUNT_LINK = ("role", "link", "Deactivate this account")
BACK_TO_MANAGE_USERS_PAGE_LINK = ("role", "button", "Back")
ADD_USER_BUTTON = ("role", "button", "Add user")
ARE_THEY_NO_LONGING_WORKING_HERE_TEXT_ELEMENT = ("text", "Are they no longer working here?")

def ensure_are_they_no_longer_working_test_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(ARE_THEY_NO_LONGING_WORKING_HERE_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(ARE_THEY_NO_LONGING_WORKING_HERE_TEXT_ELEMENT)

def get_users_name():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    element = ("xpath", "//h1[@class='nhsuk-fieldset__heading']")
    return find_element_and_perform_action(element, "get_text")

def check_users_name_is_displayed(name):
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    element = ("role", "heading", name)
    return check_element_exists(element)

def click_change_to_yes_registered_clinician_radio_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(YES_REGISTERED_CLINICIAN_RADIO_BUTTON, "check")

def click_change_to_no_registered_clinician_radio_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(NO_REGISTERED_CLINICIAN_RADIO_BUTTON, "check")

def click_change_to_recorder_permission_level_radio_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(RECORDER_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def click_change_to_administrator_permission_level_radio_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def click_change_to_lead_administrator_permission_level_radio_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(LEAD_ADMINISTRATOR_PERMISSION_LEVEL_RADIO_BUTTON, "check")

def click_change_to_permission_level_radio_button(permission):
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    element = ("label", permission, True)
    find_element_and_perform_action(element, "check")

def check_continue_to_change_user_details_button_exists():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    return check_element_exists(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)

def click_continue_to_change_user_details_user_button():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON, "click")
    wait_for_element_to_appear(ADD_USER_BUTTON)

def check_deactivate_user_link_exists():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    return check_element_exists(DEACTIVATE_THE_ACCOUNT_LINK)

def click_deactivate_user_link():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(DEACTIVATE_THE_ACCOUNT_LINK, "click")

def check_back_to_manage_users_link_exists():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    return check_element_exists(BACK_TO_MANAGE_USERS_PAGE_LINK)

def click_back_to_manage_users_link():
    wait_for_element_to_appear(CONTINUE_TO_CHANGE_USER_DETAILS_USER_BUTTON)
    find_element_and_perform_action(BACK_TO_MANAGE_USERS_PAGE_LINK, "click")
