from init_helpers import *
from pages.patient_details_page import CHOOSE_VACCINE_BUTTON

DELETE_VACCINATION_BUTTON=("//button[text()='Delete']")
CANCEL_VACCINATION_DELETE_BUTTON=("//button[text()='Cancel']")

def click_delete_vaccination_button():
    find_element_and_perform_action(DELETE_VACCINATION_BUTTON, "click")
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)

def click_cancel_vaccination_delete_button():
    find_element_and_perform_action(CANCEL_VACCINATION_DELETE_BUTTON, "click")