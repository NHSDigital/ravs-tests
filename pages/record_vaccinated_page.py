from init_helpers import *
from test_data.get_values_from_models import get_covid_vaccine_xpath, get_flu_vaccine_xpath

YES_VACCINATED_RADIO_BUTTON=("#VaccinatedYes")
NO_VACCINATED_RADIO_BUTTON=("#VaccinatedNo")
CONSENT_TYPE_DROPDOWN_ELEMENT = ("//select[@name='ConsentTypeId']")
VACCINATOR_DROPDOWN_ELEMENT = ("#VaccinatingClinicianId")
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON=("//button[text()='Continue']")
REQUIRED_ALERT_BUTTON = ("//span[text()='Required']")
NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT = ("#NameOfPersonConsenting")
RELATION_TO_PATIENT_INPUT_ELEMENT = ("#RelationshipToPatient")
RESPONSIBLE_CLINICIAN_INPUT_ELEMENT = ("#ConsentResponsibleClinicianId")
NO_VACCINATION_REASON_DROPDOWN_ELEMENT = ("#NoVaccinationReasonId")
CONSENT_GIVEN_BY_DROPDOWN_ELEMENT = ("#ConsentTypeId")
VACCINATION_DATE_INPUT_ELEMENT = ("#VaccinationDate")
VACCINATION_COMMENTS_ELEMENT = ("#VaccinationComments")
VACCINATION_SITE_DROPDOWN_ELEMENT = ("#VaccinationSiteId")
BATCH_NUMBER_DROPDOWN_ELEMENT = ("#BatchNumber")
BATCH_EXPIRY_DATE_READONLY_ELEMENT = ("#BatchExpiryDate")
DOSE_AMOUNT_READONLY_ELEMENT = ("#DoseAmount")
VACCINATION_DATE_INCORRECT_ERROR = ("#VaccinationDateError")

def get_batch_expiry_date_value():
    return find_element_and_perform_action(BATCH_EXPIRY_DATE_READONLY_ELEMENT, "get_text")

def get_dose_amount_value():
    return find_element_and_perform_action(DOSE_AMOUNT_READONLY_ELEMENT, "get_text")

def enter_dose_amount_value(dose_amount):
    find_element_and_perform_action(DOSE_AMOUNT_READONLY_ELEMENT, "type", dose_amount)

def set_vaccination_date(date):
    find_element_and_perform_action(VACCINATION_DATE_INPUT_ELEMENT, "clear")
    find_element_and_perform_action(VACCINATION_DATE_INPUT_ELEMENT, "type_text", date)

def enter_vaccination_comments(comments):
    find_element_and_perform_action(VACCINATION_COMMENTS_ELEMENT, "type_text", comments)

def check_yes_vaccinated_radiobutton_exists():
    return check_element_exists(YES_VACCINATED_RADIO_BUTTON, True)

def check_no_to_vaccinated_radiobutton_exists():
    return check_element_exists(NO_VACCINATED_RADIO_BUTTON, True)

def click_yes_vaccinated_radiobutton():
    find_element_and_perform_action(YES_VACCINATED_RADIO_BUTTON, "click")

def click_not_vaccinated_radiobutton():
    find_element_and_perform_action(NO_VACCINATED_RADIO_BUTTON, "click")

def select_vaccinator_name_and_council(nameandcouncil):
    if check_element_enabled(VACCINATOR_DROPDOWN_ELEMENT):
        find_element_and_perform_action(VACCINATOR_DROPDOWN_ELEMENT, "select_option", nameandcouncil)

def select_vaccination_site(site):
    find_element_and_perform_action(VACCINATION_SITE_DROPDOWN_ELEMENT, "select_option", site)

def select_batch_number(batchNumber):
    find_element_and_perform_action(BATCH_NUMBER_DROPDOWN_ELEMENT, "click")
    find_element_and_perform_action(BATCH_NUMBER_DROPDOWN_ELEMENT, "select_option", batchNumber)

def select_consent_given_by_from_dropdown(givenBy):
    find_element_and_perform_action(CONSENT_GIVEN_BY_DROPDOWN_ELEMENT, "select_option", givenBy)

def select_consentType(consentType):
    find_element_and_perform_action(CONSENT_TYPE_DROPDOWN_ELEMENT, "select_option", consentType)

def select_reason_for_no_vaccination(reason):
    find_element_and_perform_action(NO_VACCINATION_REASON_DROPDOWN_ELEMENT, "select_option", reason)

def click_save_and_return_button_on_record_vaccinated_page():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_check_and_confirm_screen_button():
    find_element_and_perform_action(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON, "click")
    if check_vaccination_date_incorrect_error_exists() == True:
        return True

def check_continue_to_check_and_confirm_screen_button_exists():
    return check_element_exists(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON)

def check_required_alert_exists(wait):
    return check_element_exists(REQUIRED_ALERT_BUTTON, wait)

def check_name_of_person_consenting_input_element_exists(wait):
    return check_element_exists(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, wait)

def check_vaccination_date_incorrect_error_exists():
    return check_element_exists(VACCINATION_DATE_INCORRECT_ERROR, False)

def check_relation_to_parent_input_element_exists(wait):
    return check_element_exists(RELATION_TO_PATIENT_INPUT_ELEMENT, wait)

def check_clinician_details_input_element_exists(wait):
    return check_element_exists(RESPONSIBLE_CLINICIAN_INPUT_ELEMENT, wait)

def enter_person_consenting_details(person):
    find_element_and_perform_action(NAME_OF_PERSON_CONSENTING_INPUT_ELEMENT, "input_text", person)

def enter_relationship_to_patient(relationship):
    find_element_and_perform_action(RELATION_TO_PATIENT_INPUT_ELEMENT, "input_text", relationship)

def enter_clinician_details(clinician):
    find_element_and_perform_action(RESPONSIBLE_CLINICIAN_INPUT_ELEMENT, "input_text", clinician)

def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
    element = get_covid_vaccine_xpath(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def click_care_model_option(care_model):
    element = f"//input[@name='CareModelId']/following-sibling::label[text()='{care_model}']"
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
    element = f"//input[@name='VaccineId']/following-sibling::label[text()='{vaccinetype}']"
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")
