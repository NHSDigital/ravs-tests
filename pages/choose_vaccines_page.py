import time
from init_helpers import *
from test_data.get_values_from_models import get_covid_consent_vaccine_xpath, get_flu_consent_vaccine_xpath, get_rsv_consent_vaccine_xpath, get_pertussis_consent_vaccine_xpath

COVID_RADIOBUTTON = ("label", "COVID-")
FLU_RADIOBUTTON = ("label", "Flu")
RSV_RADIOBUTTON = ("label", "Pertussis")
PERTUSSIS_RADIOBUTTON = ("label", "Respiratory syncytial virus (")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_BUTTON=("role", "button", "continue")
BACK_ELEMENT = ("link", "back")
AGE_BASED_WARNING = ("text", "This vaccine may not be recommended for a person of this age. Please check before proceeding or refer to a prescriber for a Patient Specific Direction.")
MIN_INTERVAL_BASED_WARNING = ("text", "You may have not reached the minimal interval between COVID-19 vaccine doses for this patient. This could depend on the clinical circumstances. For vaccination guidance, visit ")
CHOOSE_VACCINE_HEADING_TEXT_ELEMENT = ("role", "heading", "Choose vaccine")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_choose_vaccine_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(CHOOSE_VACCINE_HEADING_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(CHOOSE_VACCINE_HEADING_TEXT_ELEMENT)

def click_site_radiobutton(site):
    element = ("label", site)
    wait_for_element_to_appear(element)
    find_element_and_perform_action(element, "check")

def click_back_button_choosing_vaccine_for_patient():
    wait_for_element_to_appear(BACK_ELEMENT)
    find_element_and_perform_action(BACK_ELEMENT, "click")

def click_delivery_team_radiobutton(deliveryTeam):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("label", deliveryTeam)
    wait_for_element_to_appear(element)
    if check_element_exists(element, True) == True:
        find_element_and_perform_action(element, "check")
    else:
        print("Delivery team not available at organization")

def click_vaccine_type_radiobutton(vaccine_type):
    element = ("label", vaccine_type, None, True)
    wait_for_element_to_appear(element)
    if check_element_exists(element, True) == True:
        find_element_and_perform_action(element, "check")
    else:
        print("Vaccine type not available")

def click_vaccine_radiobutton(vaccine):
    element = ("label", vaccine)
    wait_for_element_to_appear(element)
    if check_element_exists(element, True) == True:
        find_element_and_perform_action(element, "check")
    else:
        print("Vaccine not available")

def check_back_button_exists():
    return check_element_exists(BACK_ELEMENT, True)

def check_age_based_warning_exists():
    attach_screenshot("age_based_warning")
    return check_element_exists(AGE_BASED_WARNING, True)

def check_age_based_warning_not_exists():
    attach_screenshot("age_based_warning")
    return check_element_not_exists(AGE_BASED_WARNING, True)

def check_minimum_interval_based_warning_exists():
    return check_element_exists(MIN_INTERVAL_BASED_WARNING, False)

def check_covid_radiobutton_exists():
    wait_for_element_to_appear(COVID_RADIOBUTTON)
    return check_element_exists(COVID_RADIOBUTTON, True)

def check_flu_radiobutton_exists():
    wait_for_element_to_appear(FLU_RADIOBUTTON)
    return check_element_exists(FLU_RADIOBUTTON, True)

def click_continue_to_assess_patient_button():
    wait_for_element_to_appear(CONTINUE_BUTTON)
    find_element_and_perform_action(CONTINUE_BUTTON, "click")

def get_selected_delivery_team_radio_button_value_on_choose_vaccine_page():
    selected_value = get_checked_radio_button_text("Delivery team")
    if selected_value != "":
        return selected_value
    else:
        print("No delivery team selection was made.")
        return "Delivery team selection did not persist"

def get_selected_vaccine_radio_button_value_on_choose_vaccine_page():
    selected_value = get_checked_radio_button_text("Vaccine")
    if selected_value != "":
        return selected_value
    else:
        return "Vaccine selection did not persist"

def get_selected_vaccine_product_radio_button_value_on_choose_vaccine_page():
    selected_value = get_checked_radio_button_text("Vaccine product")
    if selected_value != "":
        return selected_value
    else:
        return "Vaccine product selection did not persist"
