from init_helpers import *

CONFIRM_BUTTON = ("//button[text()='Confirm']")
ERROR_BATCH_ALREADY_EXISTS = ("//p[text()='Error! One or more vaccine batches aleady exist at a site.']")

def check_site_name_is_displayed(sitename):
    element = (f"//div[text()='{sitename}']")
    return check_element_exists(element, True)

def check_vaccine_is_displayed(vaccine):
    element = (f"//b[text()='{vaccine}']")
    return check_element_exists(element, True)

def check_vaccinetype_is_displayed(vaccineType):
    element = (f"//div[text()='{vaccineType}']")
    return check_element_exists(element, True)

def check_batchNumber_is_displayed(batchnumber):
    element = (f"//div[text()='{batchnumber}']")
    return check_element_exists(element, True)

def check_date_is_displayed(date):
    element = (f"//div[text()='{date}']")
    return check_element_exists(element, True)

def check_batch_already_exists_error_is_displayed():
    return check_element_exists(ERROR_BATCH_ALREADY_EXISTS, True)

def click_confirm_button():
    find_element_and_perform_action(CONFIRM_BUTTON, "click")
