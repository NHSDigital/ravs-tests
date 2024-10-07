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
    element = get_element_by_type("label", site)
    find_element_with_locator_and_perform_action(element, "check")

# def click_covid_radiobutton():
#     element = get_element_by_type(*COVID_RADIOBUTTON)
#     find_element_with_locator_and_perform_action(element, "check")

# def click_flu_radiobutton():
#     element = get_element_by_type(*FLU_RADIOBUTTON)
#     find_element_with_locator_and_perform_action(element, "check")

# def click_rsv_radiobutton():
#     element = get_element_by_type(RSV_RADIOBUTTON)
#     find_element_with_locator_and_perform_action(element, "check")

# def click_pertussis_radiobutton():
#     element = get_element_by_type(PERTUSSIS_RADIOBUTTON)
#     find_element_with_locator_and_perform_action(element, "check")

def click_back_button_choosing_vaccine_for_patient():
    element = get_element_by_type(BACK_ELEMENT)
    find_element_with_locator_and_perform_action(element, "click")

# def click_consent_vaccine_radiobutton(vaccine):
#     element = (f"//label[contains(text(), '{vaccine}')]/preceding-sibling::input[@name='VaccineProgramId']")
#     find_element_and_perform_action(element, "click")

# def click_consent_vaccine_type_radiobutton(vaccine_type):
#     element = (f"//label[contains(text(), '{vaccine_type}')]/preceding-sibling::input[@name='ConsentVaccineId']")
#     find_element_and_perform_action(element, "click")

def click_delivery_team_radiobutton(deliveryTeam):
    element = get_element_by_type("label", deliveryTeam)
    if element:
        find_element_with_locator_and_perform_action(element, "check")
    else:
        print("Delivery team not available at organization")

def click_vaccine_type_radiobutton(vaccine_type):
    element = get_element_by_type("label", vaccine_type)
    if element:
        find_element_with_locator_and_perform_action(element, "check")
    else:
        print("Vaccine type not available")

def click_vaccine_radiobutton(vaccine):
    element = get_element_by_type("label", vaccine)
    if element:
        find_element_with_locator_and_perform_action(element, "check")
    else:
        print("Vaccine not available")

# def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
#     element = get_covid_consent_vaccine_xpath(vaccine_type.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
#     element = get_flu_consent_vaccine_xpath(vaccine_type.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_rsv_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
#     element = get_rsv_consent_vaccine_xpath(vaccine_type.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_pertussis_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
#     element = get_pertussis_consent_vaccine_xpath(vaccine_type.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

def check_back_button_exists():
    return check_element_by_locator_exists(get_element_by_type(*BACK_ELEMENT), True)

def check_age_based_warning_exists():
    return check_element_by_locator_exists(get_element_by_type(*AGE_BASED_WARNING), False)

def check_minimum_interval_based_warning_exists():
    return check_element_by_locator_exists(get_element_by_type(*MIN_INTERVAL_BASED_WARNING), False)

def check_covid_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)

def check_flu_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)

def click_continue_to_assess_patient_button():
    find_element_with_locator_and_perform_action(get_element_by_type(*CONTINUE_BUTTON), "click")
