from init_helpers import *

VACCINE_PROGRAM_OVERVIEW_SETTINGS_LINK = ("//a[text()='Vaccine program overview']")
SITES_SETTINGS_LINK = ("//a[text()='Sites']")
VACCINES_NAV_LINK = ("//a[@href='/vaccines']")
USERS_SETTINGS_LINK = ("//a[@href='/user/search']")

def Click_vaccines_settings():
    find_element_and_perform_action(VACCINES_NAV_LINK, "click")

def Click_sites_settings():
    find_element_and_perform_action(SITES_SETTINGS_LINK, "click")

def Click_vaccine_program_overview_settings():
    find_element_and_perform_action(VACCINE_PROGRAM_OVERVIEW_SETTINGS_LINK, "click")

def Click_users_settings():
    find_element_and_perform_action(USERS_SETTINGS_LINK, "click")
