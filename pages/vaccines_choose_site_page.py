import time
from init_helpers import *

SITE_SEARCH = ("role", "textbox", "Enter 3 or more characters to search")
CONTINUE_TO_ADD_VACCINE_BUTTON = ("role", "button", "Continue")
SITE_LIST = (".siteRows")
# ERROR_BATCH_ALREADY_EXISTS = "//p[text()='Error! One or more vaccine batches already exist at a site.']"
CHOOSE_SITE_TITLE = ("role", "heading", "Choose site")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_choose_site_heading_text_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CHOOSE_SITE_TITLE):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CHOOSE_SITE_TITLE)

def enter_site_name(site):
    if site.lower() == "Aspire Pharmacy".lower():
        site = "fhh39"
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    time.sleep(3)
    if check_element_exists(SITE_SEARCH):
        time.sleep(3)
        find_element_and_perform_action(SITE_SEARCH, "input_text", site)

def select_site_from_list(site):
    element = ("text", site)
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")

def click_continue_to_add_vaccine_button():
    if check_element_exists(SITE_SEARCH):
        find_element_and_perform_action(CONTINUE_TO_ADD_VACCINE_BUTTON, "click")

def check_choose_site_title_exists(wait):
    return check_element_exists(CHOOSE_SITE_TITLE, wait)
