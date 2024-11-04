from init_helpers import *
from test_data.get_values_from_models import get_covid_vaccine_xpath, get_flu_vaccine_xpath

YES_VACCINATED_RADIO_BUTTON=("label", "Yes")
NO_VACCINATED_RADIO_BUTTON=("label", "No")
VACCINATOR_DROPDOWN_ELEMENT = ("label","Vaccinator")
SAVE_AND_RETURN_BUTTON=("role", "button", "Save and return")
CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON=("role", "button", "Continue")
NO_VACCINATION_REASON_DROPDOWN_ELEMENT = ("label", "No vaccination reason")
VACCINATION_DATE_INPUT_ELEMENT = ("label", "Vaccination Date")
VACCINATION_COMMENTS_ELEMENT = ("label", "Comments (Optional)")
VACCINATION_SITE_DROPDOWN_ELEMENT = ("label", "Vaccination site")
BATCH_NUMBER_DROPDOWN_ELEMENT = ("label", "Batch number")
BATCH_EXPIRY_DATE_READONLY_ELEMENT = ("label", "Batch expiry date")
DOSE_AMOUNT_READONLY_ELEMENT = ("label", "Dose amount (ml)")
VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_TEXT = ("text", "Error: Date cannot be older than a year")
VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_LINK = ("text", "Date cannot be older than a year")
VACCINATED_YES_OR_NO_SELECTION_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select 'Yes' if you have vaccinated the patient, or 'No' if you haven't")
VACCINATED_YES_OR_NO_SELECTION_MISSING_ERROR_MESSAGE_LINK = ("text", "Select 'Yes' if you have vaccinated the patient, or 'No' if you haven't")
VACCINATION_DATE_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select a vaccination date")
VACCINATION_DATE_MISSING_ERROR_MESSAGE_LINK = ("text", "Select a vaccination date")
VACCINATOR_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select the vaccinator")
VACCINATOR_MISSING_ERROR_MESSAGE_LINK = ("text", "Select the vaccinator")
VACCINATION_LOCATION_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select where the vaccination is taking place")
VACCINATION_LOCATION_MISSING_ERROR_MESSAGE_LINK = ("text", "Select where the vaccination is taking place")
VACCINE_IS_REQUIRED_ERROR_MESSAGE_TEXT = ("text", "Error: Vaccine is required")
VACCINE_IS_REQUIRED_ERROR_MESSAGE_LINK = ("text", "Vaccine is required")
VACCINATION_SITE_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select a vaccination site")
VACCINATION_SITE_MISSING_ERROR_MESSAGE_LINK = ("text", "Select a vaccination site")
BATCH_NUMBER_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Select a batch number")
BATCH_NUMBER_MISSING_ERROR_MESSAGE_LINK = ("text", "Select a batch number")
BATCH_NUMBER_EXPIRY_DATE_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Enter a batch expiry date")
BATCH_NUMBER_EXPIRY_DATE_MISSING_ERROR_MESSAGE_LINK = ("text", "Enter a batch expiry date")
BATCH_DOSE_AMOUNT_MISSING_ERROR_MESSAGE_TEXT = ("text", "Error: Dose amount (ml) is required")
BATCH_DOSE_AMOUNT_MISSING_ERROR_MESSAGE_LINK = ("text", "Dose amount (ml) is required")
YELLOW_CARD_MESSAGE_LINK = ("role", "link", "Yellow Card Report (opens a")
POST_VACCINATION_MESSAGE_LINK = ("role", "link", "COVID-19 vaccinations on NHS.")

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

def select_vaccination_location(location):
    element = ("label", location)
    find_element_and_perform_action(element, "check")

def select_vaccination_site(site):
    find_element_and_perform_action(VACCINATION_SITE_DROPDOWN_ELEMENT, "select_option", site)

def select_batch_number(batchNumber):
    find_element_and_perform_action(BATCH_NUMBER_DROPDOWN_ELEMENT, "select_option", batchNumber)

def select_reason_for_no_vaccination(reason):
    find_element_and_perform_action(NO_VACCINATION_REASON_DROPDOWN_ELEMENT, "select_option", reason)

def click_save_and_return_button_on_record_vaccinated_page():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")

def click_continue_to_check_and_confirm_screen_button():
    find_element_and_perform_action(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON, "click")
    if check_vaccination_date_incorrect_error_message_exists() == True:
        return True

def check_continue_to_check_and_confirm_screen_button_exists():
    return check_element_exists(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON)

def check_vaccination_date_incorrect_error_message_exists():
    return check_element_exists(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_TEXT, False)

def check_vaccination_date_incorrect_error_message_link_exists():
    return check_element_exists(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_LINK, False)

def click_vaccination_date_incorrect_error_message_link():
    return find_element_and_perform_action(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_LINK, "click")

def click_care_model_option(care_model):
    element = ("label", care_model)
    if check_element_exists(element, False):
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid care model")

# def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
#     element = get_covid_vaccine_xpath(vaccinetype.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
#     element = f"//input[@name='VaccineId']/following-sibling::label[text()='{vaccinetype}']"
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_rsv_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
#     element = f"//input[@name='VaccineId']/following-sibling::label[text()='{vaccinetype}']"
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_pertussis_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccinetype):
#     element = f"//input[@name='VaccineId']/following-sibling::label[text()='{vaccinetype}']"
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

def click_vaccine_type(vaccine_type):
    element = ("label", vaccine_type)
    if check_element_exists(element) == True:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

