import time
from init_helpers import *
from pages.patient_details_page import CHOOSE_VACCINE_BUTTON

PATIENT_NAME_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Name']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_DOB_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Date of birth']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ADDRESS_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Address']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_NHS_NUMBER_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='NHS number']/following-sibling::dd[@class='nhsuk-summary-list__value']")
VACCINATOR_ORGANISATION_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Organisation']/following-sibling::dd[@class='nhsuk-summary-list__value']")
VACCINATOR_SITE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Site']/following-sibling::dd[@class='nhsuk-summary-list__value']")
VACCINATOR_CARE_MODEL_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Care model']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CHOSEN_VACCINE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Please select which vaccine the patient wants to receive.']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CHOSEN_VACCINE_TYPE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccine']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBLE_FOR_VACCINE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Is the patient eligible for the vaccine?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ELIGIBLE_FOR_VACCINE_ANSWER_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Is the patient eligible for the vaccine?']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_ELIGIBILITY_TYPE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Eligibility type']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ELIGIBILITY_TYPE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Eligibility type']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_ELEGIBILITY_ASSESSING_CLINICIAN_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessing clinician']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ELIGIBILITY_ASSESSING_CLINICIAN_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Eligibility type']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_ELEGIBILITY_ASSESSMENT_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_DATE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment date']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_ELEGIBILITY_ASSESSMENT_OUTCOME_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment outcome']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_OUTCOME_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment outcome']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__value'])[1]")
CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_BUTTON = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change'])[1]")
PATIENT_CONSENT_GIVEN_VALUE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Does the patient or someone on their behalf consent to the vaccination?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_CONSENT_GIVEN_VALUE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Does the patient or someone on their behalf consent to the vaccination?']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_CONSENT_GIVEN_BY_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent given by']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_CONSENT_GIVEN_BY_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent given by']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_CONSENT_NAME_OF_PERSON_CONSENTING_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Name of the person consenting']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_CONSENT_NAME_OF_PERSON_CONSENTING_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Name of the person consenting']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_CONSENT_PERSON_CONSENTING_RELATIONSHIP_TO_PARENT_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Relationship to patient']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_CONSENT_PERSON_CONSENTING_RELATIONSHIP_TO_PATIENT_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Relationship to patient']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_CONSENT_RECORDED_BY_CLINICIAN_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent clinician']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_CONSENT_RECORDED_BY_CLINICIAN_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent clinician']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATED_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Have you vaccinated the patient?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATED_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Have you vaccinated the patient?']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccination date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_DATE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccination date']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_VACCINE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccine']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_VACCINE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccine']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_ROUTE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccination route']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_ROUTE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccination route']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_BATCH_NUMBER_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Batch number']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_BATCH_NUMBER_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Batch number']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_BATCH_EXPIRY_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Batch expiry date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_BATCH_EXPIRY_DATE_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Batch expiry date']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_DOSE_AMOUNT_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Dose amount']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_DOSE_AMOUNT_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Dose amount']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_PRESCRIBING_METHOD_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Prescribing method']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_PRESCRIBING_METHOD_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Prescribing method']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_VACCINATOR_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccinator']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_PATIENT_VACCINATION_VACCINATOR_BUTTON = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccinator']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change']")
PATIENT_VACCINATION_COMMENTS_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__value'])[2]")
CHANGE_PATIENT_VACCINATION_COMMENTS_BUTTON = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__actions']/button[text()='Change'])[2]")
CONFIRM_DETAILS_AND_SAVE_BUTTON = ("//button[text()='Confirm details and save']")
CANCEL_CONFIRM_DETAILS_BUTTON = ("//button[text()='Cancel']")
BACK_ON_CONFIRM_DETAILS_PAGE_BUTTON = ("//a[contains(@href, '/vaccination/add')]")

def click_change_patient_eligible_answer_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBLE_FOR_VACCINE_ANSWER_BUTTON, "click")

def click_change_patient_eligibility_type_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBILITY_TYPE_BUTTON, "click")

def click_change_patient_eligibility_assessing_clinician_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBILITY_ASSESSING_CLINICIAN_BUTTON, "click")

def click_change_patient_eligibility_assessment_date_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_DATE_BUTTON, "click")

def click_change_patient_eligibility_assessment_outcome_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_OUTCOME_BUTTON, "click")

def click_change_patient_eligibility_assessment_comments_button():
    find_element_and_perform_action(CHANGE_PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_BUTTON, "click")

def click_change_patient_consent_given_answer_button():
    find_element_and_perform_action(CHANGE_PATIENT_CONSENT_GIVEN_VALUE_BUTTON, "click")

def click_change_patient_consent_given_by_button():
    find_element_and_perform_action(CHANGE_PATIENT_CONSENT_GIVEN_BY_BUTTON, "click")

def click_change_patient_consent_given_by_name_of_person_button():
    find_element_and_perform_action(CHANGE_CONSENT_NAME_OF_PERSON_CONSENTING_BUTTON, "click")

def click_change_patient_consenting_relationship_to_patient_button():
    find_element_and_perform_action(CHANGE_CONSENT_PERSON_CONSENTING_RELATIONSHIP_TO_PATIENT_BUTTON, "click")

def click_change_patient_consent_recorded_by_clinician_button():
    find_element_and_perform_action(CHANGE_CONSENT_RECORDED_BY_CLINICIAN_BUTTON, "click")

def click_change_patient_vaccinated_answer_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATED_BUTTON, "click")

def click_change_patient_vaccination_date_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_DATE_BUTTON, "click")

def click_change_patient_vaccination_vaccine_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_VACCINE_BUTTON, "click")

def click_change_patient_vaccination_route_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_ROUTE_BUTTON, "click")

def click_change_patient_vaccination_batch_number_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_BATCH_NUMBER_BUTTON, "click")

def click_change_patient_vaccination_batch_expiry_date_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_BATCH_EXPIRY_DATE_BUTTON, "click")

def click_change_patient_vaccination_vaccinator_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_VACCINATOR_BUTTON, "click")

def click_change_patient_vaccination_comments_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_COMMENTS_BUTTON, "click")

def click_change_patient_vaccination_prescribing_method_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_PRESCRIBING_METHOD_BUTTON, "click")

def click_change_patient_vaccination_dose_amount_button():
    find_element_and_perform_action(CHANGE_PATIENT_VACCINATION_DOSE_AMOUNT_BUTTON, "click")

def click_confirm_details_and_save_button():
    find_element_and_perform_action(CONFIRM_DETAILS_AND_SAVE_BUTTON, "click")
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)

def check_confirm_details_and_save_button_exists():
    return check_element_exists(CONFIRM_DETAILS_AND_SAVE_BUTTON)

def click_back_button_on_check_and_confirm_vaccination_screen():
    find_element_and_perform_action(BACK_ON_CONFIRM_DETAILS_PAGE_BUTTON, "click")

def click_cancel_confirm_details_button():
    find_element_and_perform_action(CANCEL_CONFIRM_DETAILS_BUTTON, "click")

def get_patient_name_value():
    return find_element_and_perform_action(PATIENT_NAME_LABEL_ELEMENT, "get_text")

def get_patient_dob_value():
    return find_element_and_perform_action(PATIENT_DOB_LABEL_ELEMENT, "get_text")

def get_patient_address_value():
    return find_element_and_perform_action(PATIENT_ADDRESS_LABEL_ELEMENT, "get_text")

def get_patient_nhs_number_value():
    return find_element_and_perform_action(PATIENT_NHS_NUMBER_LABEL_ELEMENT, "get_text")

def get_vaccinator_organisation_value():
    return find_element_and_perform_action(VACCINATOR_ORGANISATION_LABEL_ELEMENT, "get_text")

def get_vaccinator_site_value():
    return find_element_and_perform_action(VACCINATOR_SITE_LABEL_ELEMENT, "get_text")

def get_vaccinator_care_model_value():
    return find_element_and_perform_action(VACCINATOR_CARE_MODEL_LABEL_ELEMENT, "get_text")

def get_patient_chosen_vaccine_value():
    return find_element_and_perform_action(PATIENT_CHOSEN_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_vaccine_type_chosen_vaccine_value():
    return find_element_and_perform_action(PATIENT_CHOSEN_VACCINE_TYPE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_for_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELIGIBLE_FOR_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_type_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_TYPE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessing_clinician_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELEGIBILITY_ASSESSING_CLINICIAN_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_date_value():
    return find_element_and_perform_action(PATIENT_ELEGIBILITY_ASSESSMENT_DATE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_outcome_value():
    return find_element_and_perform_action(PATIENT_ELEGIBILITY_ASSESSMENT_OUTCOME_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_comments_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_LABEL_ELEMENT, "get_text")

def get_patient_consented_given_value():
    return find_element_and_perform_action(PATIENT_CONSENT_GIVEN_VALUE_LABEL_ELEMENT, "get_text")

def get_patient_consent_given_by_value():
    return find_element_and_perform_action(PATIENT_CONSENT_GIVEN_BY_LABEL_ELEMENT, "get_text")

def get_patient_consent_given_by_person_name_value():
    return find_element_and_perform_action(PATIENT_CONSENT_NAME_OF_PERSON_CONSENTING_LABEL_ELEMENT, "get_text")

def get_patient_consent_given_by_person_relationship_to_patient_value():
    return find_element_and_perform_action(PATIENT_CONSENT_PERSON_CONSENTING_RELATIONSHIP_TO_PARENT_LABEL_ELEMENT, "get_text")

def get_patient_consent_recorded_by_clinician_value():
    return find_element_and_perform_action(PATIENT_CONSENT_RECORDED_BY_CLINICIAN_LABEL_ELEMENT, "get_text")

def get_patient_vaccinated_value():
    return find_element_and_perform_action(PATIENT_VACCINATED_LABEL_ELEMENT, "get_text")

def get_patient_vaccinated_date_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_DATE_LABEL_ELEMENT, "get_text")

def get_patient_vaccinated_chosen_vaccine_date_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_route_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_ROUTE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_batch_number_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_BATCH_NUMBER_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_batch_expiry_date_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_BATCH_EXPIRY_DATE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_dose_amount_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_DOSE_AMOUNT_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_prescribing_method_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_PRESCRIBING_METHOD_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_vaccinator_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_comments_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_COMMENTS_LABEL_ELEMENT, "get_text")