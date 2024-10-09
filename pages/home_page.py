from init_helpers import *

FIND_A_PATIENT_NAV_ELEMENT = ("role", "link", "Find a patient")
VACCINES_NAV_ELEMENT = ("role", "link", "Vaccines")
REPORTS_NAV_ELEMENT = ("role", "link", "Reports")
MANAGE_USERS_NAV_ELEMENT = ("role", "link", "Manage users")
NHS_LOGO_NAV_ELEMENT = ("role", "link", "NHS Logo Record a vaccination")
LOGOUT_NAV_ELEMENT = ("role", "link", "Log Out")
NAV_BAR_TOGGLER = ("//button[@class='navbar-toggler']")
NAV_LINK_BAR_TOGGLER = ("//button[@class='navbar-toggler p-2']")

def click_logout_button():
    click_element(LOGOUT_NAV_ELEMENT)

def click_navbar_toggler():
    click_element(NAV_BAR_TOGGLER)

def click_nav_link_bar_toggler():
    click_element(NAV_LINK_BAR_TOGGLER)

def check_logout_button_exists():
    wait_for_element_to_appear(LOGOUT_NAV_ELEMENT)
    return check_if_element_exists(LOGOUT_NAV_ELEMENT, True)

def check_navbar_toggle_exists_without_waiting():
    return check_element_exists(NAV_BAR_TOGGLER, False)

def check_navbar_toggle_exists():
    return check_element_exists(NAV_BAR_TOGGLER, True)

def check_nav_link_bar_toggle_exists_without_waiting():
    return check_element_exists(NAV_LINK_BAR_TOGGLER, False)

def check_nav_link_bar_toggle_exists():
    return check_element_exists(NAV_LINK_BAR_TOGGLER, True)

def check_logout_button_exists_without_waiting():
    return check_if_element_exists(LOGOUT_NAV_ELEMENT, False)

def click_profile_nav_link(email):
    element = ("role", "link", email)
    click_element(element)

def click_reports_nav_link():
    click_element(REPORTS_NAV_ELEMENT)

def click_vaccines_nav_link():
    click_element(VACCINES_NAV_ELEMENT)

def click_manage_users_nav_link():
    click_element(MANAGE_USERS_NAV_ELEMENT)

def click_find_a_patient_nav_link():
    click_element(FIND_A_PATIENT_NAV_ELEMENT)
