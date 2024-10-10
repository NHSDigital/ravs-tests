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

def click_site_radiobutton(site):
    element = ("label", site)
    click_element(element)

def click_back_button_choosing_vaccine_for_patient():
    click_element(BACK_ELEMENT)

def click_delivery_team_radiobutton(deliveryTeam):
    element = ("label", deliveryTeam)
    if check_if_element_exists(element, True) == True:
        check_element(element)
    else:
        print("Delivery team not available at organization")

def click_vaccine_type_radiobutton(vaccine_type):
    element = ("label", vaccine_type)
    if check_if_element_exists(element, True) == True:
        check_element(element)
    else:
        print("Vaccine type not available")

def click_vaccine_radiobutton(vaccine):
    element = ("label", vaccine)
    if check_if_element_exists(element, True) == True:
        check_element(element)
    else:
        print("Vaccine not available")

def check_back_button_exists():
    return check_if_element_exists(BACK_ELEMENT, True)

def check_age_based_warning_exists():
    time.sleep(2)
    wait_for_element_to_appear(AGE_BASED_WARNING)
    return check_if_element_exists(AGE_BASED_WARNING, True)

def check_minimum_interval_based_warning_exists():
    return check_if_element_exists(MIN_INTERVAL_BASED_WARNING, False)

def check_covid_radiobutton_exists():
    return check_if_element_exists(COVID_RADIOBUTTON, True)

def check_flu_radiobutton_exists():
    return check_if_element_exists(FLU_RADIOBUTTON, True)

def click_continue_to_assess_patient_button():
    click_element(CONTINUE_BUTTON)
