import time
from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
ADD_USER_BUTTON = ("role", "button", "Add user")
DEACTIVATED_USERS_LINK = ("xpath", "//a[@href='/manage-users/deactivated-users']")

def check_add_user_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    return check_element_exists(ADD_USER_BUTTON)

def click_add_user_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    find_element_and_perform_action(ADD_USER_BUTTON, "click")

def click_change_user_details_link(user):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("label", f"Change details for {user}")
    find_element_and_perform_action(element, "click")

def get_first_users_name():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    time.sleep(3)
    element = ("xpath", '(//button[text()="Change"]/ancestor::tr/td[1])[1]')
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        return None

def click_first_users_change_details_link():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(DEACTIVATED_USERS_LINK)
    element = ("xpath", '(//button[text()="Change"])[1]')
    if check_element_exists(element):
        return find_element_and_perform_action(element, "click")
    else:
        return None

def check_change_user_details_link_exists(user):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("label", f"Change details for {user}")
    return check_element_exists(element)

def click_view_deactivated_users_link():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    find_element_and_perform_action(DEACTIVATED_USERS_LINK, "click")

def check_view_deactivated_users_link_exists(count):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    return check_element_exists(DEACTIVATED_USERS_LINK)
