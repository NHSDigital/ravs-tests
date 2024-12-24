from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
REACTIVATE_BUTTON = ("role", "button", "Reactivate")

def check_reactivate_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    return check_element_exists(REACTIVATE_BUTTON)

def click_reactivate_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    find_element_and_perform_action(REACTIVATE_BUTTON, "click")

def check_reactivate_message_text_exists(name, email_address):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    element = ("text", f"Once you have reactivated {name} ({email_address}), they can sign in to NHS Record a vaccination again using their Okta account.")
    return check_element_exists(element)
