import time
from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
ADD_USER_BUTTON = ("role", "button", "Add user")
DEACTIVATED_USERS_LINK = ("xpath", "//a[@href='/manage-users/deactivated-users']")
MANAGE_USERS_HEADING_ELEMENT = ("role", "heading", "Manage users")

def ensure_manage_users_heading_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(MANAGE_USERS_HEADING_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        time.sleep(3)
        wait_for_element_to_appear(MANAGE_USERS_HEADING_ELEMENT)

def check_add_user_button_exists():
    wait_for_element_to_appear(ADD_USER_BUTTON)
    return check_element_exists(ADD_USER_BUTTON)

def click_add_user_button():
    wait_for_element_to_appear(ADD_USER_BUTTON)
    find_element_and_perform_action(ADD_USER_BUTTON, "click")

def click_change_user_details_link(user):
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("label", f"Change details for {user}")
    find_element_and_perform_action(element, "click")

def get_first_users_name():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[1])[1]')
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        return None

def get_first_users_clinician_status():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[1])[1]')
    wait_for_element_to_appear(element)
    full_name = find_element_and_perform_action(element, "get_text")
    if '(' in full_name and ')' in full_name:
                return full_name.split('(')[1].strip(')')
    else:
        return None

def get_first_users_email_address():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[2])[1]')
    wait_for_element_to_appear(element)
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        return None

def get_first_users_permission_level():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[3])[1]')
    wait_for_element_to_appear(element)
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        return None

def get_first_users_active_status():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[4])[1]')
    wait_for_element_to_appear(element)
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        return None

def click_first_users_change_details_link():
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    element = ("xpath", '(//button[text()="Change"])[1]')
    if check_element_exists(element):
        return find_element_and_perform_action(element, "click")
    else:
        return None

def check_change_user_details_link_exists(user):
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("label", f"Change details for {user}")
    return check_element_exists(element)

def click_view_deactivated_users_link():
    wait_for_element_to_appear(ADD_USER_BUTTON)
    find_element_and_perform_action(DEACTIVATED_USERS_LINK, "click")

def check_view_deactivated_users_link_exists(count):
    wait_for_element_to_appear(ADD_USER_BUTTON)
    return check_element_exists(DEACTIVATED_USERS_LINK)
