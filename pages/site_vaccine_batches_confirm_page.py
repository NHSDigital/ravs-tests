from init_helpers import *

CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON = ("role", "button", "Confirm")
CHANGE_SITE_BUTTON = ("role", "link", "Change site")
CHANGE_VACCINE_BUTTON = ("role", "link", "Change vaccine")
EDIT_BATCH_BUTTON = ("role", "link", "Edit batch")

def check_site_name_is_displayed(site):
    element = ("text", site)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_vaccine_is_displayed(vaccine):
    element = ("text", vaccine.upper())
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_vaccinetype_is_displayed(vaccineType):
    element = ("text", vaccineType)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_batchNumber_is_displayed(batch_number):
    element = ("text", batch_number)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def check_date_is_displayed(date):
    element = ("text", date)
    wait_for_element_to_appear(element)
    return check_element_exists(element, True)

def click_confirm_add_vaccine_and_batch_button():
    wait_for_element_to_appear(CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON)
    find_element_and_perform_action(CONFIRM_ADD_VACCINE_AND_BATCH_BUTTON, "click")
