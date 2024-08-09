from init_helpers import *

LOGOUT_NAV_ELEMENT = ("//a[text()='Log Out']")
LOGOUT_NAV_ELEMENT = ("//a[text()='Log Out']")
PROFILE_NAV_ELEMENT = ("//a[@href='/profile']")
APPOINTMENTS_NAV_ELEMENT = ("//a[@href='/appointment']")
PDS_SEARCH_NAV_ELEMENT = ("//a[@href='/patient-search/details']")
RECORDS_NAV_ELEMENT = ("//a[text()='Records']")
DASHBOARD_NAV_ELEMENT = ("//a[text()='Dashboard']")
FIND_A_PATIENT_NAV_ELEMENT = ("//a[text()='Find a patient']")
REPORTS_NAV_ELEMENT = ("//a[text()='Reports']")
SETTINGS_NAV_ELEMENT = ("//a[@href='/settings']")
MANAGE_USERS_NAV_ELEMENT = ("//a[@href='/manage-users']")
WORKFLOWS_NAV_ELEMENT = ("//a[text()='/Workflows']")
NAV_BAR_TOGGLER = ("//button[@class='navbar-toggler']")
NAV_LINK_BAR_TOGGLER = ("//button[@class='navbar-toggler p-2']")


def click_logout_button():
    find_element_and_perform_action(LOGOUT_NAV_ELEMENT, "click")

def click_navbar_toggler():
    find_element_and_perform_action(NAV_BAR_TOGGLER, "click")

def click_nav_link_bar_toggler():
    find_element_and_perform_action(NAV_LINK_BAR_TOGGLER, "click")

def check_logout_button_exists():
    return check_element_exists(LOGOUT_NAV_ELEMENT, True)

def check_navbar_toggle_exists_without_waiting():
    return check_element_exists(NAV_BAR_TOGGLER, False)

def check_navbar_toggle_exists():
    return check_element_exists(NAV_BAR_TOGGLER, True)

def check_nav_link_bar_toggle_exists_without_waiting():
    return check_element_exists(NAV_LINK_BAR_TOGGLER, False)

def check_nav_link_bar_toggle_exists():
    return check_element_exists(NAV_LINK_BAR_TOGGLER, True)

def check_logout_button_exists_without_waiting():
    return check_element_exists(LOGOUT_NAV_ELEMENT, False)

def click_profile_nav_link():
    find_element_and_perform_action(PROFILE_NAV_ELEMENT, "click")

def click_appointments_nav_link():
    find_element_and_perform_action(APPOINTMENTS_NAV_ELEMENT, "click")

def click_pds_search_nav_link():
    find_element_and_perform_action(PDS_SEARCH_NAV_ELEMENT, "click")

def click_records_nav_link():
    find_element_and_perform_action(RECORDS_NAV_ELEMENT, "click")

def click_dashboard_nav_link():
    find_element_and_perform_action(DASHBOARD_NAV_ELEMENT, "click")

def click_reports_nav_link():
    find_element_and_perform_action(REPORTS_NAV_ELEMENT, "click")

def click_settings_nav_link():
    find_element_and_perform_action(SETTINGS_NAV_ELEMENT, "click")

def click_manage_users_nav_link():
    find_element_and_perform_action(MANAGE_USERS_NAV_ELEMENT, "click")

def click_workflows_nav_link():
    find_element_and_perform_action(WORKFLOWS_NAV_ELEMENT, "click")

def click_find_a_patient_nav_link():
    find_element_and_perform_action(FIND_A_PATIENT_NAV_ELEMENT, "click")
