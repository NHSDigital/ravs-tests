from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK = ("role", "button", "Select data for report")
SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT = ("text", "Select data for report")
CONTINUE_TO_REPORTS_CHECK_AND_CONFIRM_BUTTON = ("role", "button", "Continue")
BACK_TO_SELECT_SITE_BUTTON = ("role", "button", "Back")
PATIENTS_CHECKBOX_ELEMENT = ("label", "Patients")
STAFF_CHECKBOX_ELEMENT = ("label", "Staff")
SITE_DELIVERY_TEAM_CHECKBOX_ELEMENT = ("label", "Site or delivery team")
ASSESSMENT_AND_CONSENT_CHECKBOX_ELEMENT = ("label", "Assessment and consent")
VACCINATION_CHECKBOX_ELEMENT = ("label", "Vaccination")


def check_reports_data_check_box_checked(data):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", data)
    wait_for_element_to_appear(element)
    return check_element_checked(element)

def uncheck_all_data_filters():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    find_element_and_perform_action(PATIENTS_CHECKBOX_ELEMENT, "uncheck")
    find_element_and_perform_action(STAFF_CHECKBOX_ELEMENT, "uncheck")
    find_element_and_perform_action(SITE_DELIVERY_TEAM_CHECKBOX_ELEMENT, "uncheck")
    find_element_and_perform_action(ASSESSMENT_AND_CONSENT_CHECKBOX_ELEMENT, "uncheck")
    find_element_and_perform_action(VACCINATION_CHECKBOX_ELEMENT, "uncheck")

def check_reports_data_check_box_exists(data):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", data)
    wait_for_element_to_appear(element)
    return check_element_exists(element)

def check_reports_data_check_box(data):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", data)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "check")

def uncheck_reports_data_check_box(data):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", data)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "uncheck")

def check_reports_select_site_error_message_text_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT)
    return check_element_exists(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_TEXT)

def check_reports_select_vaccine_error_message_link_exists():
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)
    return check_element_exists(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(SELECT_DATA_FOR_REPORT_ERROR_MESSAGE_LINK, "click")

def check_continue_to_reports_check_and_confirm_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_REPORTS_CHECK_AND_CONFIRM_BUTTON)
    return check_element_exists(CONTINUE_TO_REPORTS_CHECK_AND_CONFIRM_BUTTON)

def click_continue_to_reports_check_and_confirm_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_REPORTS_CHECK_AND_CONFIRM_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_REPORTS_CHECK_AND_CONFIRM_BUTTON, "click")

def check_reports_back_to_select_vaccine_page_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_SITE_BUTTON)
    return check_element_exists(BACK_TO_SELECT_SITE_BUTTON)

def click_reports_back_to_select_vaccine_page_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_SITE_BUTTON)
    find_element_and_perform_action(BACK_TO_SELECT_SITE_BUTTON, "click")
