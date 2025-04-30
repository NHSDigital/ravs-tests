from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
CONFIRM_AND_SEND_BUTTON = ("role", "button", "Confirm and send")
CHANGE_NAME_LINK = ("role", "button", "Change name")
CHANGE_EMAIL_ADDRESS_LINK = ("role", "button", "Change email address")
CHANGE_CLINICAL_STATUS_LINK = ("role", "button", "Change clinical")
CHANGE_PERMISSION_LEVEL_LINK = ("role", "button", "Change permission level")
ACTIVATE_YOUR_OKTA_ACCOUNT_TEXT = ("text", "You’ll receive a ‘Welcome to Okta’ email (from noreply@okta.com). Please activate the link within 7 days.")
LOGIN_TO_RAVS_TEXT = ("text", "Once you’ve activated your Okta account, log in to www.ravs.england.nhs.uk using your Okta username and password.")
HELPDESK_EMAIL_TEXT = ("text", "Email: ravs.support@england.")
HELPDESK_TELEPHONE_TEXT = ("text", "Telephone: 0121 611 0187 (select option 3)")
HELPDESK_TIMES_TEXT = ("text", "Monday to Friday: 8am to 6pm. Weekends: 8am to 4 pm")
CHECK_AND_ADD_USER_TEXT_ELEMENT = ("role", "heading", "Check and add user")

def ensure_check_and_add_user_test_element_exists():
    if not check_element_exists(CHECK_AND_ADD_USER_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CHECK_AND_ADD_USER_TEXT_ELEMENT)

def check_confirm_and_send_button_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CONFIRM_AND_SEND_BUTTON)

def click_confirm_and_send_button():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CONFIRM_AND_SEND_BUTTON, "click")

def check_change_name_link_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CHANGE_NAME_LINK)

def click_change_name_link():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CHANGE_NAME_LINK, "click")

def check_change_email_address_link_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CHANGE_EMAIL_ADDRESS_LINK)

def click_change_email_address_link():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CHANGE_EMAIL_ADDRESS_LINK, "click")

def check_change_clinical_status_link_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CHANGE_CLINICAL_STATUS_LINK)

def click_change_clinical_status_link():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CHANGE_CLINICAL_STATUS_LINK, "click")

def check_change_permission_level_link_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(CHANGE_PERMISSION_LEVEL_LINK)

def click_change_permission_level_link():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    find_element_and_perform_action(CHANGE_PERMISSION_LEVEL_LINK, "click")

def check_activate_your_okta_account_message_text_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(ACTIVATE_YOUR_OKTA_ACCOUNT_TEXT)

def check_login_to_ravs_message_text_exists():
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    return check_element_exists(LOGIN_TO_RAVS_TEXT)

def click_change_detail_link(detail):
    ensure_check_and_add_user_test_element_exists()
    wait_for_element_to_appear(CONFIRM_AND_SEND_BUTTON)
    if detail == "name":
        click_change_name_link()
    elif detail == "email_address":
        click_change_email_address_link()
    elif detail == "permission_level":
        click_change_permission_level_link()
    elif detail == "clinician_status":
        click_change_clinical_status_link()

def get_users_name():
    ensure_check_and_add_user_test_element_exists()
    element = ("xpath", "//dt[text()='Name']/following-sibling::dd[@class='nhsuk-summary-list__value']")
    wait_for_element_to_appear(element)
    return find_element_and_perform_action(element, "get_text")

def get_users_email_address():
    ensure_check_and_add_user_test_element_exists()
    element = ("xpath", "//dt[text()='Email address']/following-sibling::dd[@class='nhsuk-summary-list__value']")
    wait_for_element_to_appear(element)
    return find_element_and_perform_action(element, "get_text")

def get_users_clinician_status():
    ensure_check_and_add_user_test_element_exists()
    element = ("xpath", "//dt[text()='Clinical']/following-sibling::dd[@class='nhsuk-summary-list__value']")
    wait_for_element_to_appear(element)
    return find_element_and_perform_action(element, "get_text")

def get_users_permission_level():
    ensure_check_and_add_user_test_element_exists()
    element = ("xpath", "//dt[text()='Permission level']/following-sibling::dd[@class='nhsuk-summary-list__value']")
    wait_for_element_to_appear(element)
    return find_element_and_perform_action(element, "get_text")
