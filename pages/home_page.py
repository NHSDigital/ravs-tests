from init_helpers import *

FIND_A_PATIENT_NAV_ELEMENT = ("role", "link", "Find a patient")
VACCINES_NAV_ELEMENT = ("role", "link", "Vaccines")
REPORTS_NAV_ELEMENT = ("role", "link", "Reports")
MANAGE_USERS_NAV_ELEMENT = ("role", "link", "Manage users")
NHS_LOGO_NAV_ELEMENT = ("role", "link", "NHS Logo Record a vaccination")
LOGOUT_NAV_ELEMENT = ("role", "link", "Log Out")
NAV_BAR_TOGGLER = ("//button[@class='navbar-toggler']")
NAV_LINK_BAR_TOGGLER = ("//button[@class='navbar-toggler p-2']")
FEEDBACK_LINK = ("role", "link", "feedback (opens in a new tab)")
REPORT_AN_ISSUE_LINK = ("role", "link", "Report an issue")
CONTACT_US_LINK = ("role", "link", "Contact us")
HELP_AND_GUIDANCE_LINK = ("role", "link", "Help and guidance")
ADD_USER_BUTTON = ("role", "button", "Add user")
SEARCH_BUTTON = ("role", "button", "Search")
ADD_VACCINE_BUTTON = ("role", "button", "Add vaccine")
CREATE_REPORT_BUTTON = ("role", "button", "Create report")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def check_feedback_link_exists():
    wait_for_element_to_appear(FEEDBACK_LINK)
    return check_element_exists(FEEDBACK_LINK)

def click_feedback_link_exists():
    wait_for_element_to_appear(FEEDBACK_LINK)
    find_element_and_perform_action(FEEDBACK_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_report_an_issue_link_exists():
    wait_for_element_to_appear(REPORT_AN_ISSUE_LINK)
    return check_element_exists(REPORT_AN_ISSUE_LINK)

def click_report_an_issue_link_exists():
    wait_for_element_to_appear(REPORT_AN_ISSUE_LINK)
    find_element_and_perform_action(REPORT_AN_ISSUE_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_contact_us_link_exists():
    wait_for_element_to_appear(CONTACT_US_LINK)
    return check_element_exists(CONTACT_US_LINK)

def click_contact_us_link_exists():
    wait_for_element_to_appear(CONTACT_US_LINK)
    find_element_and_perform_action(CONTACT_US_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_help_and_guidance_link_exists():
    wait_for_element_to_appear(HELP_AND_GUIDANCE_LINK)
    return check_element_exists(HELP_AND_GUIDANCE_LINK)

def click_help_and_guidance_link_exists():
    wait_for_element_to_appear(HELP_AND_GUIDANCE_LINK)
    find_element_and_perform_action(HELP_AND_GUIDANCE_LINK, "click")

def click_logout_button():
    wait_for_element_to_appear(LOGOUT_NAV_ELEMENT)
    find_element_and_perform_action(LOGOUT_NAV_ELEMENT, "click")

def click_navbar_toggler():
    wait_for_element_to_appear(NAV_BAR_TOGGLER)
    find_element_and_perform_action(NAV_BAR_TOGGLER, "click")

def click_nav_link_bar_toggler():
    wait_for_element_to_appear(NAV_LINK_BAR_TOGGLER)
    find_element_and_perform_action(NAV_LINK_BAR_TOGGLER, "click")

def check_logout_button_exists():
    wait_for_element_to_appear(LOGOUT_NAV_ELEMENT)
    return check_element_exists(LOGOUT_NAV_ELEMENT, True)

def check_navbar_toggle_exists_without_waiting():
    return check_element_exists(NAV_BAR_TOGGLER, False)

def check_navbar_toggle_exists():
    wait_for_element_to_appear(NAV_BAR_TOGGLER)
    return check_element_exists(NAV_BAR_TOGGLER, True)

def check_nav_link_bar_toggle_exists_without_waiting():
    return check_element_exists(NAV_LINK_BAR_TOGGLER, False)

def check_nav_link_bar_toggle_exists():
    wait_for_element_to_appear(NAV_LINK_BAR_TOGGLER)
    return check_element_exists(NAV_LINK_BAR_TOGGLER, True)

def check_logout_button_exists_without_waiting():
    return check_element_exists(LOGOUT_NAV_ELEMENT, False)

def click_profile_nav_link(email):
    element = ("role", "link", email)
    handle_unresponsive_page()
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_reports_nav_link_exists():
    handle_unresponsive_page()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(REPORTS_NAV_ELEMENT)

def click_reports_nav_link():
    handle_unresponsive_page()
    wait_for_element_to_appear(REPORTS_NAV_ELEMENT)
    find_element_and_perform_action(REPORTS_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CREATE_REPORT_BUTTON)

def check_vaccines_nav_link_exists():
    handle_unresponsive_page()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(VACCINES_NAV_ELEMENT)

def click_vaccines_nav_link():
    handle_unresponsive_page()
    wait_for_element_to_appear(VACCINES_NAV_ELEMENT)
    find_element_and_perform_action(VACCINES_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_VACCINE_BUTTON)

def check_manage_users_nav_link_exists():
    handle_unresponsive_page()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(MANAGE_USERS_NAV_ELEMENT)

def click_manage_users_nav_link():
    handle_unresponsive_page()
    wait_for_element_to_appear(MANAGE_USERS_NAV_ELEMENT)
    find_element_and_perform_action(MANAGE_USERS_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)

def click_find_a_patient_nav_link():
    handle_unresponsive_page()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    find_element_and_perform_action(FIND_A_PATIENT_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SEARCH_BUTTON)
