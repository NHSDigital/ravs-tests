from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
COVID_CHECK_BOX = ("label", "COVID-19")
FLU_CHECK_BOX = ("label", "Flu")
PERTUSSIS_CHECK_BOX = ("label", "Pertussis")
RSV_CHECK_BOX = ("label", "Respiratory syncytial virus (RSV)")
SELECT_VACCINES_ERROR_MESSAGE_LINK = ("role", "button", "Select vaccines")
SELECT_VACCINES_ERROR_MESSAGE_TEXT = ("text", "Select vaccines")
CONTINUE_TO_SELECT_SITE_BUTTON = ("role", "button", "Continue")
BACK_TO_SELECT_DATE_BUTTON = ("role", "button", "Back")

def check_covid_check_box_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(COVID_CHECK_BOX)
    return check_element_exists(COVID_CHECK_BOX)

def click_covid_check_box():
    wait_for_element_to_appear(COVID_CHECK_BOX)
    find_element_and_perform_action(COVID_CHECK_BOX, "check")

def check_flu_check_box_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(FLU_CHECK_BOX)
    return check_element_exists(FLU_CHECK_BOX)

def click_flu_check_box():
    wait_for_element_to_appear(FLU_CHECK_BOX)
    find_element_and_perform_action(FLU_CHECK_BOX, "check")

def check_pertussis_check_box_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(PERTUSSIS_CHECK_BOX)
    return check_element_exists(PERTUSSIS_CHECK_BOX)

def click_pertussis_check_box():
    wait_for_element_to_appear(PERTUSSIS_CHECK_BOX)
    find_element_and_perform_action(PERTUSSIS_CHECK_BOX, "check")

def check_rsv_check_box_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(RSV_CHECK_BOX)
    return check_element_exists(RSV_CHECK_BOX)

def click_rsv_check_box():
    wait_for_element_to_appear(RSV_CHECK_BOX)
    find_element_and_perform_action(RSV_CHECK_BOX, "check")

def check_vaccine_check_box_exists(vaccine):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", vaccine)
    wait_for_element_to_appear(element)
    return check_element_exists(element)

def click_vaccine_check_box_on_reports_page(vaccine):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", vaccine)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "check")

def check_select_vaccine_error_message_text_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SELECT_VACCINES_ERROR_MESSAGE_TEXT)
    return check_element_exists(SELECT_VACCINES_ERROR_MESSAGE_TEXT)

def check_select_vaccine_error_message_link_exists():
    wait_for_element_to_appear(SELECT_VACCINES_ERROR_MESSAGE_LINK)
    return check_element_exists(SELECT_VACCINES_ERROR_MESSAGE_LINK)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(SELECT_VACCINES_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(SELECT_VACCINES_ERROR_MESSAGE_LINK, "click")

def check_continue_to_reports_select_site_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_SELECT_SITE_BUTTON)
    return check_element_exists(CONTINUE_TO_SELECT_SITE_BUTTON)

def click_continue_to_reports_select_site_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_SELECT_SITE_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_SELECT_SITE_BUTTON, "click")

def check_back_to_select_date_page_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_DATE_BUTTON)
    return check_element_exists(BACK_TO_SELECT_DATE_BUTTON)

def click_back_to_select_date_page_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_SELECT_DATE_BUTTON)
    find_element_and_perform_action(BACK_TO_SELECT_DATE_BUTTON, "click")
