import time
from init_helpers import *

FIND_A_PATIENT_NAV_ELEMENT = ("role", "link", "Find a patient")
VACCINES_NAV_ELEMENT = ("role", "link", "Vaccines")
REPORTS_NAV_ELEMENT = ("role", "link", "Reports")
MANAGE_USERS_NAV_ELEMENT = ("role", "link", "Manage users")
RECORD_VACCINATIONS_NAV_ELEMENT = ("role", "link", "Record vaccinations")
NHS_LOGO_NAV_ELEMENT = ("role", "link", "NHS Logo Record a vaccination")
LOGOUT_NAV_ELEMENT = ("role", "link", "Log out")
NAV_BAR_TOGGLER = ("//button[@class='navbar-toggler']")
NAV_LINK_BAR_TOGGLER = ("//button[@class='navbar-toggler p-2']")
FEEDBACK_LINK = ("role", "link", "feedback (opens in a new tab)")
REPORT_AN_ISSUE_LINK = ("role", "link", "Report an issue")
ADD_VACCINES_LINK = ("role", "link", "Add vaccines")
ADD_USERS_LINK = ("role", "link", "Add users")
FIND_A_PATIENT_LINK = ("nested_role", "link", "Find a patient", True, "#maincontent")
CONTACT_US_LINK = ("role", "link", "Contact us")
HELP_AND_GUIDANCE_LINK = ("role", "link", "Help and guidance")
USER_GUIDE_LINK = ("role", "link", "User guide (opens in new tab)")
TERMS_OF_USE_LINK = ("role", "link", "Terms of use")
COOKIES_LINK = ("role", "link", "Cookies")
ACCESSIBILITY_STATEMENT_LINK = ("role", "link", "Accessibility statement")
ADD_USER_BUTTON = ("role", "button", "Add user")
SEARCH_BUTTON = ("role", "button", "Search")
ADD_VACCINE_BUTTON = ("role", "button", "Add vaccine")
CREATE_REPORT_BUTTON = ("role", "button", "Create report")
PAGE_LOADING_ELEMENT = ("role", "status")
TODAY_VACCINATION_COUNT = ("id", "today-vaccinations")
WEEK_VACCINATION_COUNT = ("id", "week-vaccinations")
MONTH_VACCINATION_COUNT = ("id", "month-vaccinations")
CREATE_A_REPORT_LINK = ("role", "link", "create a report")
TOTAL_VACCINATIONS_TEXT_ELEMENT = ("role", "heading", "Total vaccinations")

def ensure_log_out_nav_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(LOGOUT_NAV_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(LOGOUT_NAV_ELEMENT)

def check_feedback_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(FEEDBACK_LINK)

def check_accessibility_statement_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(ACCESSIBILITY_STATEMENT_LINK)

def check_terms_of_use_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(TERMS_OF_USE_LINK)

def check_user_guide_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(USER_GUIDE_LINK)

def click_accessibility_statement_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(ACCESSIBILITY_STATEMENT_LINK, "click")

def click_user_guide_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(USER_GUIDE_LINK, "click")

def click_terms_of_use_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(TERMS_OF_USE_LINK, "click")

def check_add_vaccines_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(ADD_VACCINES_LINK)

def check_add_users_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(ADD_USERS_LINK)

def check_find_a_patient_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(FIND_A_PATIENT_LINK)

def click_add_vaccines_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(ADD_VACCINES_LINK, "click")

def click_add_users_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(ADD_USERS_LINK, "click")

def click_find_a_patient_link():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(FIND_A_PATIENT_LINK, "click")

def check_site_name_exists_in_dashboard(site):
    ensure_log_out_nav_element_exists()
    element = ("role", "heading", site)
    return check_element_exists(element)

def get_today_vaccinations_count():
    ensure_log_out_nav_element_exists()
    text = find_element_and_perform_action(TODAY_VACCINATION_COUNT, "get_text")
    count = re.findall(r'\d+', text)
    return count[0]

def get_week_vaccinations_count():
    ensure_log_out_nav_element_exists()
    text = find_element_and_perform_action(WEEK_VACCINATION_COUNT, "get_text")
    count = re.findall(r'\d+', text)
    return count[0]

def get_month_vaccinations_count():
    ensure_log_out_nav_element_exists()
    text = find_element_and_perform_action(MONTH_VACCINATION_COUNT, "get_text")
    count = re.findall(r'\d+', text)
    return count[0]

def check_create_a_report_link_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(CREATE_A_REPORT_LINK)

def click_feedback_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FEEDBACK_LINK)
    find_element_and_perform_action(FEEDBACK_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_report_an_issue_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(REPORT_AN_ISSUE_LINK)
    return check_element_exists(REPORT_AN_ISSUE_LINK)

def click_report_an_issue_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(REPORT_AN_ISSUE_LINK)
    find_element_and_perform_action(REPORT_AN_ISSUE_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_contact_us_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(CONTACT_US_LINK)
    return check_element_exists(CONTACT_US_LINK)

def click_contact_us_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(CONTACT_US_LINK)
    find_element_and_perform_action(CONTACT_US_LINK, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_help_and_guidance_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(HELP_AND_GUIDANCE_LINK)
    return check_element_exists(HELP_AND_GUIDANCE_LINK)

def click_help_and_guidance_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(HELP_AND_GUIDANCE_LINK)
    find_element_and_perform_action(HELP_AND_GUIDANCE_LINK, "click")

def click_logout_button():
    ensure_log_out_nav_element_exists()
    find_element_and_perform_action(LOGOUT_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    time.sleep(5)

def click_navbar_toggler():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(NAV_BAR_TOGGLER)
    find_element_and_perform_action(NAV_BAR_TOGGLER, "click")

def click_nav_link_bar_toggler():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(NAV_LINK_BAR_TOGGLER)
    find_element_and_perform_action(NAV_LINK_BAR_TOGGLER, "click")

def check_logout_button_exists():
    ensure_log_out_nav_element_exists()
    return check_element_exists(LOGOUT_NAV_ELEMENT, True)

def check_navbar_toggle_exists_without_waiting():
    ensure_log_out_nav_element_exists()
    return check_element_exists(NAV_BAR_TOGGLER, False)

def check_navbar_toggle_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(NAV_BAR_TOGGLER)
    return check_element_exists(NAV_BAR_TOGGLER, True)

def check_nav_link_bar_toggle_exists_without_waiting():
    ensure_log_out_nav_element_exists()
    return check_element_exists(NAV_LINK_BAR_TOGGLER, False)

def check_nav_link_bar_toggle_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(NAV_LINK_BAR_TOGGLER)
    return check_element_exists(NAV_LINK_BAR_TOGGLER, True)

def check_logout_button_exists_without_waiting():
    ensure_log_out_nav_element_exists()
    return check_element_exists(LOGOUT_NAV_ELEMENT, False)

def click_profile_nav_link(email):
    # ensure_log_out_nav_element_exists()
    ensure_log_out_nav_element_exists()
    element = ("role", "link", email)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_reports_nav_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(REPORTS_NAV_ELEMENT)

def click_reports_nav_link():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(REPORTS_NAV_ELEMENT)
    find_element_and_perform_action(REPORTS_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CREATE_REPORT_BUTTON)

def check_vaccines_nav_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(VACCINES_NAV_ELEMENT)

def click_vaccines_nav_link():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(VACCINES_NAV_ELEMENT)
    find_element_and_perform_action(VACCINES_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_VACCINE_BUTTON)

def check_manage_users_nav_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(MANAGE_USERS_NAV_ELEMENT)

def click_manage_users_nav_link():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(MANAGE_USERS_NAV_ELEMENT)
    find_element_and_perform_action(MANAGE_USERS_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)

def check_record_vaccinations_nav_link_exists():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    return check_element_exists(RECORD_VACCINATIONS_NAV_ELEMENT)

def click_record_vaccinations_nav_link():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    find_element_and_perform_action(RECORD_VACCINATIONS_NAV_ELEMENT, "click")

def click_find_a_patient_nav_link():
    ensure_log_out_nav_element_exists()
    wait_for_element_to_appear(FIND_A_PATIENT_NAV_ELEMENT)
    find_element_and_perform_action(FIND_A_PATIENT_NAV_ELEMENT, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(SEARCH_BUTTON)
