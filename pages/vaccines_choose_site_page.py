import time
from init_helpers import *

SITE_SEARCH = ("placeholder", "Enter 3 or more characters to search")
CONTINUE_TO_ADD_VACCINE_BUTTON = ("role", "button", "Continue")
SITE_LIST = (".siteRows")
# ERROR_BATCH_ALREADY_EXISTS = "//p[text()='Error! One or more vaccine batches already exist at a site.']"
CHOOSE_SITE_TITLE = ("role", "heading", "Choose site")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def enter_site_name(site):
    if site.lower() == "Aspire Pharmacy".lower():
        site = "fhh39"
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if check_element_exists(SITE_SEARCH):
        time.sleep(2)
        find_element_and_perform_action(SITE_SEARCH, "input_text", site)

def select_site_from_list(site):
    # element = (f"//div[@class='siteRows' and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{site.lower()}')]")
    element = ("text", site)
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")

def click_continue_to_add_vaccine_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if check_element_exists(SITE_SEARCH):
        find_element_and_perform_action(CONTINUE_TO_ADD_VACCINE_BUTTON, "click")

def check_choose_site_title_exists(wait):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    return check_element_exists(CHOOSE_SITE_TITLE, wait)
