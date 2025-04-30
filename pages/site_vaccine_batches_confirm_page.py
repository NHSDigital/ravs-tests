from init_helpers import *

CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON = ("role", "button", "Confirm")
CHANGE_SITE_BUTTON = ("role", "link", "Change site")
CHANGE_VACCINE_BUTTON = ("role", "link", "Change vaccine")
EDIT_BATCH_BUTTON = ("role", "link", "Edit batch")
CHECK_AND_CONFIRM_HEADING_TEXT_ELEMENT = ("role", "heading", "Check and confirm")

def ensure_check_and_confirm_heading_text_is_visible():
    if not check_element_exists(CHECK_AND_CONFIRM_HEADING_TEXT_ELEMENT):
        wait_for_element_to_appear(CHECK_AND_CONFIRM_HEADING_TEXT_ELEMENT)

def check_site_name_is_displayed(site):
    ensure_check_and_confirm_heading_text_is_visible()
    element = ("text", site)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_vaccine_is_displayed(vaccine):
    ensure_check_and_confirm_heading_text_is_visible()
    element = ("text", vaccine.upper())
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_vaccine_type_is_displayed(vaccineType):
    ensure_check_and_confirm_heading_text_is_visible()
    element = ("text", vaccineType)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_batchNumber_is_displayed(batch_number):
    ensure_check_and_confirm_heading_text_is_visible()
    element = ("text", batch_number)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_date_is_displayed(date):
    ensure_check_and_confirm_heading_text_is_visible()
    element = ("text", date)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def click_confirm_add_vaccine_and_batch_button():
    ensure_check_and_confirm_heading_text_is_visible
    wait_for_element_to_appear(CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON)
    find_element_and_perform_action(CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON, "click")
