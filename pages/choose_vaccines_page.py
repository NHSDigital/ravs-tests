from init_helpers import *
from test_data.get_values_from_models import get_covid_consent_vaccine_xpath, get_flu_consent_vaccine_xpath, get_rsv_consent_vaccine_xpath, get_pertussis_consent_vaccine_xpath

COVID_RADIOBUTTON = ("#VaccineProgramId-1")
FLU_RADIOBUTTON = ("#VaccineProgramId-2")
RSV_RADIOBUTTON = ("#VaccineProgramId-3")
PERTUSSIS_RADIOBUTTON = ("#VaccineProgramId-4")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_BUTTON=("//button[text()='Continue']")
BACK_ELEMENT = ("//a[@href='/patient/1']")
AGE_BASED_WARNING = ("//p[text()='This vaccine may not be recommended for a person of this age. Please check before proceeding or refer to a prescriber for a Patient Specific Direction.']")
MIN_INTERVAL_BASED_WARNING = ("//p[contains(text(), 'You may have not reached the minimal interval between COVID-19 vaccine doses for this patient. This could depend on the clinical circumstances. For vaccination guidance, visit ')and ./a[@href='https://assets.publishing.service.gov.uk/media/65d50a1f2197b2001d7fa70e/Greenbook-chapter-14a-20240220.pdf']]")

def click_covid_radiobutton():
    find_element_and_perform_action(COVID_RADIOBUTTON, "click")

def click_rsv_radiobutton():
    find_element_and_perform_action(RSV_RADIOBUTTON, "click")

def click_pertussis_radiobutton():
    find_element_and_perform_action(PERTUSSIS_RADIOBUTTON, "click")

def click_back_button_choosing_vaccine_for_patient():
    find_element_and_perform_action(BACK_ELEMENT, "click")

def click_vaccine_radiobutton(vaccine):
    element = f"//input[@name='SiteId']/following-sibling::label[text()='{vaccine}']"
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Vaccine not available at site")

def click_delivery_team_radiobutton(deliveryTeam):
    element = f"//input[@name='SiteId']/following-sibling::label[text()='{deliveryTeam}']"
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Delivery team not available at organization")

def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
    element = get_covid_consent_vaccine_xpath(vaccine_type.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
    element = get_flu_consent_vaccine_xpath(vaccine_type.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def click_rsv_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
    element = get_rsv_consent_vaccine_xpath(vaccine_type.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def click_pertussis_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type):
    element = get_pertussis_consent_vaccine_xpath(vaccine_type.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def check_back_button_exists():
    return check_element_exists(BACK_ELEMENT, True)

def check_age_based_warning_exists():
    return check_element_exists(AGE_BASED_WARNING, False)

def check_minimum_interval_based_warning_exists():
    return check_element_exists(MIN_INTERVAL_BASED_WARNING, False)

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
