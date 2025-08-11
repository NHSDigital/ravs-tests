from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK = ("role", "button", "Select data for report")
SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT = ("text", "Select data for report")
CHANGE_DATE_BUTTON = ("role", "link", "Change date")
CHANGE_VACCINES_BUTTON = ("role", "link", "Change vaccines")
CHANGE_SITES_BUTTON = ("role", "link", "Change sites")
CHANGE_DATA_BUTTON = ("role", "link", "Change data")
CONFIRM_AND_CREATE_REPORT_BUTTON = ("role", "button", "Confirm and create report")
BACK_TO_SELECT_DATA_BUTTON = ("role", "button", "Back")

def check_reports_change_date_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_DATE_BUTTON)
    return check_element_exists(CHANGE_DATE_BUTTON)

def click_reports_change_date_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_DATE_BUTTON)
    find_element_and_perform_action(CHANGE_DATE_BUTTON, "click")

def check_reports_change_vaccines_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_VACCINES_BUTTON)
    return check_element_exists(CHANGE_VACCINES_BUTTON)

def click_reports_change_vaccines_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_VACCINES_BUTTON)
    find_element_and_perform_action(CHANGE_VACCINES_BUTTON, "click")

def check_reports_change_sites_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_SITES_BUTTON)
    return check_element_exists(CHANGE_SITES_BUTTON)

def click_reports_change_sites_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_SITES_BUTTON)
    find_element_and_perform_action(CHANGE_SITES_BUTTON, "click")

def check_reports_change_data_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_DATA_BUTTON)
    return check_element_exists(CHANGE_DATA_BUTTON)

def click_reports_change_data_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CHANGE_DATA_BUTTON)
    find_element_and_perform_action(CHANGE_DATA_BUTTON, "click")

def check_select_site_error_message_text_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT)
    return check_element_exists(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT)

def check_select_vaccine_error_message_link_exists():
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)
    return check_element_exists(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK, "click")

def check_continue_to_confirm_and_create_report_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONFIRM_AND_CREATE_REPORT_BUTTON)
    return check_element_exists(CONFIRM_AND_CREATE_REPORT_BUTTON)

def click_continue_to_confirm_and_create_report_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONFIRM_AND_CREATE_REPORT_BUTTON)
    find_element_and_perform_action(CONFIRM_AND_CREATE_REPORT_BUTTON, "click")

def check_back_to_select_data_page_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_DATA_BUTTON)
    return check_element_exists(BACK_TO_SELECT_DATA_BUTTON)

def click_back_to_select_data_page_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_DATA_BUTTON)
    find_element_and_perform_action(BACK_TO_SELECT_DATA_BUTTON, "click")
