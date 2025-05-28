import time
from init_helpers import *

VACCINATION_SAVED_LABEL_ELEMENT = ("role", "heading", "Vaccination saved")
NEXT_VACCINATION_LINK_ELEMENT = ("role", "link", "Next vaccination")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_vaccination_saved_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    time.sleep(1)
    if not check_element_exists(VACCINATION_SAVED_LABEL_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(VACCINATION_SAVED_LABEL_ELEMENT)

def check_vaccination_saved_label_exists():
    ensure_vaccination_saved_visible()
    return check_element_exists(VACCINATION_SAVED_LABEL_ELEMENT)

def check_next_vaccination_link_exists():
    ensure_vaccination_saved_visible()
    return check_element_exists(NEXT_VACCINATION_LINK_ELEMENT)

def click_next_vaccination_link():
    ensure_vaccination_saved_visible()
    find_element_and_perform_action(NEXT_VACCINATION_LINK_ELEMENT, "click")

def check_patients_record_saved_text_exists(name):
    ensure_vaccination_saved_visible()
    element = ("text", f"{name}'s record will be sent to their GP.")
    return check_element_exists(element)

def check_patients_record_link_exists(name):
    ensure_vaccination_saved_visible()
    element = ("role", "link", f"{name}'s record")
    return check_element_exists(element)

def click_patients_record_link(name):
    ensure_vaccination_saved_visible()
    element = ("role", "link", f"{name}'s record")
    find_element_and_perform_action(element, "click")

