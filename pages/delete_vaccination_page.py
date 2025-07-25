from init_helpers import *
from pages.patient_details_page import CHOOSE_VACCINE_BUTTON

DELETE_VACCINATION_BUTTON=("role", "button", "delete")
CANCEL_VACCINATION_DELETE_BUTTON=("role", "button", "Cancel")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_delete_vaccination_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(DELETE_VACCINATION_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(DELETE_VACCINATION_BUTTON)

def click_delete_vaccination_button():
    ensure_delete_vaccination_button_exists()
    find_element_and_perform_action(DELETE_VACCINATION_BUTTON, "click")
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_cancel_vaccination_delete_button():
    ensure_delete_vaccination_button_exists()
    wait_for_element_to_appear(CANCEL_VACCINATION_DELETE_BUTTON)
    find_element_and_perform_action(CANCEL_VACCINATION_DELETE_BUTTON, "click")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
