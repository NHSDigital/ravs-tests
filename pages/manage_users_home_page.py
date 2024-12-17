from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
ADD_USER_BUTTON = ("role", "button", "Add user")

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

def check_change_user_details_link_exists(user):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("label", f"Change details for {user}")
    return check_element_exists(element)

def click_view_deactivated_users_link(count):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("role", "link", f"View {count} deactivated users")
    find_element_and_perform_action(element, "click")

def check_view_deactivated_users_link_exists(count):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(ADD_USER_BUTTON)
    element = ("role", "link", f"View {count} deactivated users")
    check_element_exists(element)
