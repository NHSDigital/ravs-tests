from init_helpers import *

CONTINUE_BUTTON=("//button[text()='Continue']")

def click_continue_button():
    find_element_and_perform_action(CONTINUE_BUTTON, "click")

def click_vaccine_radiobutton(vaccine):
    element = (f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{vaccine.lower()}')]/preceding-sibling::input[@name='VaccineProgramId']")
    find_element_and_perform_action(element, "click")

def click_vaccine_type_radiobutton(vaccine_type):
    element = (f"//label[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{vaccine_type.lower()}')]/preceding-sibling::input[@name='VaccineId']")
    find_element_and_perform_action(element, "click")

    