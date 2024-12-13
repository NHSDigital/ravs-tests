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
