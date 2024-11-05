from init_helpers import *

CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON=("role", "button", "Continue")


def click_continue_to_add_batch_button():
    find_element_and_perform_action(CONTINUE_TO_ENTER_BATCH_DETAILS_BUTTON, "click")

def click_vaccine_radiobutton_on_add_vaccine_screen(vaccine):
    # element = (f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{vaccine.lower()}')]/preceding-sibling::input[@name='VaccineProgramId']")
    element = ("label", vaccine.upper())
    find_element_and_perform_action(element, "click")

def click_vaccine_type_radiobutton_on_add_vaccine_screen(vaccine_type):
    # element = (f"//label[contains(text(), '{vaccine_type}')]/preceding-sibling::input[@name='VaccineId']")
    element = ("label", vaccine_type, None, True)
    find_element_and_perform_action(element, "click")
