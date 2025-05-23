import time
from init_helpers import *

PAGE_LOADING_ELEMENT = ("role", "status")
REACTIVATE_BUTTON = ("role", "button", "Reactivate")
REACTIVATE_HEADING_TEXT_ELEMENT = ("role", "heading", "Reactivate")

def ensure_reactivate_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(REACTIVATE_HEADING_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(REACTIVATE_HEADING_TEXT_ELEMENT)

def check_reactivate_button_exists():
    ensure_reactivate_heading_element_exists()
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    return check_element_exists(REACTIVATE_BUTTON)

def click_reactivate_button():
    ensure_reactivate_heading_element_exists()
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    time.sleep(2)
    find_element_and_perform_action(REACTIVATE_BUTTON, "click")

def check_reactivate_message_text_exists(name, email_address):
    ensure_reactivate_heading_element_exists()
    wait_for_element_to_appear(REACTIVATE_BUTTON)
    time.sleep(2)
    element = ("text", f"Once you have reactivated {name} ({email_address}), they can sign in to NHS Record a vaccination again using their Okta account.")
    return check_element_exists(element)
