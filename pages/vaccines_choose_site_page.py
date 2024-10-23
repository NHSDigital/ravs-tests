from init_helpers import *

SITE_SEARCH = ("#Site")
CONTINUE_BUTTON = ("//button[text()='Continue']")
SITE_LIST = (".siteRows")
ERROR_BATCH_ALREADY_EXISTS = "//p[text()='Error! One or more vaccine batches already exist at a site.']"
CHOOSE_SITE_TITLE = ("//h1[text()='Choose site']")

def enter_site_name(site):
    find_element_and_perform_action(SITE_SEARCH, "input_text", site)

def select_site_from_list(site):
    element = (f"//div[@class='siteRows' and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{site.lower()}')]")
    find_element_and_perform_action(SITE_LIST, "click")

def click_continue_button():
    find_element_and_perform_action(CONTINUE_BUTTON, "click")

def check_choose_site_title_exists(wait):
    wait_for_element_to_appear(CHOOSE_SITE_TITLE)
    return check_element_exists(CHOOSE_SITE_TITLE, wait)
