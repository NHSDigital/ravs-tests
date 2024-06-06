from init_helpers import *
from test_data.get_values_from_models import get_covid_consent_vaccine_xpath, get_flu_consent_vaccine_xpath

COVID_RADIOBUTTON = ("#VaccineProgramId-1")
FLU_RADIOBUTTON = ("#VaccineProgramId-2")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_BUTTON=("//button[text()='Continue']")
BACK_ELEMENT = ("//a[@href='/patient/1']")

def click_covid_radiobutton():
    find_element_and_perform_action(COVID_RADIOBUTTON, "click")

def click_back_button_choosing_vaccine_for_patient():
    find_element_and_perform_action(BACK_ELEMENT, "click")

def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccinetype):

    element = get_covid_consent_vaccine_xpath(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccinetype):

    element = get_flu_consent_vaccine_xpath(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def check_back_button_exists():
    check_element_exists(BACK_ELEMENT, True)

def check_covid_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)

def click_flu_radiobutton():
    find_element_and_perform_action(FLU_RADIOBUTTON, "click")

def check_flu_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)

def click_save_and_return_button_on_choose_vaccines_screen():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_assess_patient_button():
    find_element_and_perform_action(CONTINUE_BUTTON, "click")
