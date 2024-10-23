import time
from init_helpers import *
from pages.patient_details_page import CHOOSE_VACCINE_BUTTON

PATIENT_NAME_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Name']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_DOB_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Date of birth']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ADDRESS_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Address']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_NHS_NUMBER_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='NHS number']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_GENDER_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Gender']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBLE_FOR_VACCINE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Eligible']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_TYPE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Eligibility type']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_ASSESSING_CLINICIAN_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessing clinician']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_ASSESSMENT_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_ASSESSMENT_OUTCOME_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Assessment outcome']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__value'])[1]")
CHANGE_PATIENT_ASSESSMENT_PAGE_DETAILS_BUTTON = ("//button[text()='Change assess the patient page details']")
PATIENT_CONSENT_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CONSENT_GIVEN_BY_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consent given by']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CONSENT_NAME_OF_PERSON_CONSENTING_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Name of the person consenting']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CONSENT_PERSON_CONSENTING_RELATIONSHIP_TO_PARENT_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Relationship to the patient']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_CONSENT_RECORDED_BY_CLINICIAN_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Consenting clinician']/following-sibling::dd[@class='nhsuk-summary-list__value']")
CHANGE_RECORD_CONSENT_PAGE_DETAILS_BUTTON = ("//button[text()='Change record consent page details']")
PATIENT_VACCINATED_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccinated?']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINATION_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINE_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccine']/following-sibling::dd[@class='nhsuk-summary-list__value'])[1]")
PATIENT_VACCINE_PRODUCT_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Product']/following-sibling::dd[@class='nhsuk-summary-list__value'])[1]")
PATIENT_VACCINE_BATCH_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Batch']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINE_BATCH_EXPIRY_DATE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Expiry date']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINATION_SITE_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Site']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINATION_DOSE_AMOUNT_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Dose amount (ml)']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINATION_VACCINATOR_LABEL_ELEMENT = ("//div[@class='nhsuk-summary-list__row']/dt[text()='Vaccinator']/following-sibling::dd[@class='nhsuk-summary-list__value']")
PATIENT_VACCINATION_COMMENTS_LABEL_ELEMENT = ("(//div[@class='nhsuk-summary-list__row']/dt[text()='Comments']/following-sibling::dd[@class='nhsuk-summary-list__value'])[2]")
CHANGE_VACCINATE_PAGE_DETAILS_BUTTON = ("//button[text()='Change vaccinate page details']")
CONFIRM_DETAILS_AND_SAVE_BUTTON = ("//button[text()='Confirm details and save']")
CANCEL_CONFIRM_DETAILS_BUTTON = ("//button[text()='Cancel']")
BACK_ON_CONFIRM_DETAILS_PAGE_BUTTON = ("//a[contains(@href, '/vaccination/add')]")

def click_change_assess_patient_page_details_button():
    find_element_and_perform_action(CHANGE_PATIENT_ASSESSMENT_PAGE_DETAILS_BUTTON, "click")

def click_change_patient_record_consent_page_details_button():
    find_element_and_perform_action(CHANGE_RECORD_CONSENT_PAGE_DETAILS_BUTTON, "click")

def click_change_patient_vaccinate_page_details_button():
    find_element_and_perform_action(CHANGE_VACCINATE_PAGE_DETAILS_BUTTON, "click")

def click_confirm_details_and_save_button():
    find_element_and_perform_action(CONFIRM_DETAILS_AND_SAVE_BUTTON, "click")
    time.sleep(5)
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

def get_patient_eligibility_for_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELIGIBLE_FOR_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_type_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_TYPE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessing_clinician_vaccine_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_ASSESSING_CLINICIAN_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_date_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_ASSESSMENT_DATE_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_outcome_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_ASSESSMENT_OUTCOME_LABEL_ELEMENT, "get_text")

def get_patient_eligibility_assessment_comments_value():
    return find_element_and_perform_action(PATIENT_ELIGIBILITY_ASSESSMENT_COMMENTS_LABEL_ELEMENT, "get_text")

def get_patient_consented_given_value():
    return find_element_and_perform_action(PATIENT_CONSENT_LABEL_ELEMENT, "get_text")

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

def get_patient_vaccinated_chosen_vaccine_value():
    return find_element_and_perform_action(PATIENT_VACCINE_LABEL_ELEMENT, "get_text")

def get_patient_vaccinated_chosen_vaccine_product_value():
    return find_element_and_perform_action(PATIENT_VACCINE_PRODUCT_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_site_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_SITE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_batch_number_value():
    return find_element_and_perform_action(PATIENT_VACCINE_BATCH_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_batch_expiry_date_value():
    return find_element_and_perform_action(PATIENT_VACCINE_BATCH_EXPIRY_DATE_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_dose_amount_value():
    attach_screenshot("vaccination_dose_amount")
    return find_element_and_perform_action(PATIENT_VACCINATION_DOSE_AMOUNT_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_vaccinator_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_VACCINATOR_LABEL_ELEMENT, "get_text")

def get_patient_vaccination_comments_value():
    return find_element_and_perform_action(PATIENT_VACCINATION_COMMENTS_LABEL_ELEMENT, "get_text")
