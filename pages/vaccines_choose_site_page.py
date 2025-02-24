from init_helpers import *

SITE_SEARCH = ("placeholder", "Enter 3 or more characters to search")
CONTINUE_TO_ADD_VACCINE_BUTTON = ("role", "button", "Continue")
SITE_LIST = (".siteRows")
# ERROR_BATCH_ALREADY_EXISTS = "//p[text()='Error! One or more vaccine batches already exist at a site.']"
CHOOSE_SITE_TITLE = ("role", "heading", "Choose site")

def enter_site_name(site):
    wait_for_element_to_appear(SITE_SEARCH)
    if check_element_exists(SITE_SEARCH): # site search will not be available for community pharmacy
        find_element_and_perform_action(SITE_SEARCH, "input_text", site)

def select_site_from_list(site):
    # element = (f"//div[@class='siteRows' and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{site.lower()}')]")
    element = ("text", site)
    wait_for_element_to_appear(element)
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")

def click_continue_to_add_vaccine_button():
    wait_for_element_to_appear(CONTINUE_TO_ADD_VACCINE_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_ADD_VACCINE_BUTTON, "click")

def check_choose_site_title_exists(wait):
    wait_for_element_to_appear(CHOOSE_SITE_TITLE)
    return check_element_exists(CHOOSE_SITE_TITLE, wait)
