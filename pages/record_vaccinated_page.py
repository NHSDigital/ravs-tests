import time
from init_helpers import *
from test_data.get_values_from_models import get_covid_vaccine_xpath, get_flu_vaccine_xpath

YES_VACCINATED_RADIO_BUTTON=("label", "Yes")
NO_VACCINATED_RADIO_BUTTON=("label", "No", True)
VACCINATOR_DROPDOWN_ELEMENT = ("label","Vaccinator")
SAVE_AND_RETURN_BUTTON=("role", "button", "Save and return")
CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON=("role", "button", "Continue")
NO_VACCINATION_REASON_DROPDOWN_ELEMENT = ("label", "No vaccination reason")
VACCINATION_DATE_INPUT_ELEMENT = ("label", "Vaccination Date")
VACCINATION_COMMENTS_ELEMENT = ("label", "Comments (Optional)")
VACCINATION_SITE_DROPDOWN_ELEMENT = ("label", "Vaccination site")
BATCH_NUMBER_DROPDOWN_ELEMENT = ("label", "Batch number")
BATCH_EXPIRY_DATE_READONLY_ELEMENT = ("label", "Batch expiry date")
DOSE_AMOUNT_READONLY_ELEMENT = ("role", "textbox", "Dose amount (ml)")
PACK_SIZE_READONLY_ELEMENT = ("role", "textbox", "Pack size")
VACCINATION_SITE_READONLY_ELEMENT = ("label", "Vaccination site")
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
CAREHOME_NAME_INPUT_ELEMENT = ("#CareHomeName")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def get_batch_expiry_date_value():
    return find_element_and_perform_action(BATCH_EXPIRY_DATE_READONLY_ELEMENT, "get_text")

def get_dose_amount_value():
    return find_element_and_perform_action(DOSE_AMOUNT_READONLY_ELEMENT, "get_text")

def enter_dose_amount_value(dose_amount):
    find_element_and_perform_action(DOSE_AMOUNT_READONLY_ELEMENT, "type", dose_amount)

def get_dose_amount_value():
    return find_element_and_perform_action(DOSE_AMOUNT_READONLY_ELEMENT, "get_text")

def get_pack_size_value():
    return find_element_and_perform_action(PACK_SIZE_READONLY_ELEMENT, "get_text")

def check_pack_size_element_exists():
    return check_element_exists(PACK_SIZE_READONLY_ELEMENT)

def set_vaccination_date(date):
    find_element_and_perform_action(VACCINATION_DATE_INPUT_ELEMENT, "clear")
    find_element_and_perform_action(VACCINATION_DATE_INPUT_ELEMENT, "type_text", date)

def get_vaccination_date():
    return find_element_and_perform_action(VACCINATION_DATE_INPUT_ELEMENT, "get_text")

def enter_vaccination_comments(comments):
    find_element_and_perform_action(VACCINATION_COMMENTS_ELEMENT, "type_text", comments)

def check_yes_vaccinated_radiobutton_exists():
    return check_element_exists(YES_VACCINATED_RADIO_BUTTON, True)

def check_no_to_vaccinated_radiobutton_exists():
    return check_element_exists(NO_VACCINATED_RADIO_BUTTON, True)

def click_yes_vaccinated_radiobutton():
    wait_for_element_to_appear(YES_VACCINATED_RADIO_BUTTON)
    find_element_and_perform_action(YES_VACCINATED_RADIO_BUTTON, "click")

def click_not_vaccinated_radiobutton():
    wait_for_element_to_appear(NO_VACCINATED_RADIO_BUTTON)
    find_element_and_perform_action(NO_VACCINATED_RADIO_BUTTON, "check")

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
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_continue_to_check_and_confirm_vaccination_screen_button():
    wait_for_element_to_appear(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON)
    time.sleep(1)
    find_element_and_perform_action(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON, "click")
    if check_vaccination_date_incorrect_error_message_exists() == True:
        return True
    else:
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def check_continue_to_check_and_confirm_screen_button_exists():
    return check_element_exists(CONTINUE_TO_CHECK_AND_CONFIRM_BUTTON)

def check_vaccination_date_incorrect_error_message_exists():
    return check_element_exists(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_TEXT, False)

def check_vaccination_date_incorrect_error_message_link_exists():
    return check_element_exists(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_LINK, False)

def click_vaccination_date_incorrect_error_message_link():
    return find_element_and_perform_action(VACCINATION_DATE_INCORRECT_ERROR_MESSAGE_LINK, "click")

def check_vaccination_site_missing_error_message_exists():
    return check_element_exists(VACCINATION_SITE_MISSING_ERROR_MESSAGE_TEXT, False)

def check_vaccination_site_missing_error_message_link_exists():
    return check_element_exists(VACCINATION_SITE_MISSING_ERROR_MESSAGE_LINK, False)

def click_vaccination_site_missing_error_message_link():
    return find_element_and_perform_action(VACCINATION_SITE_MISSING_ERROR_MESSAGE_LINK, "click")

def click_care_model_option(care_model):
    element = ("label", care_model)
    if check_element_exists(element, False):
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid care model")

def click_vaccine_type(vaccine_type):
    element = ("label", vaccine_type, None, True)
    if check_element_exists(element) == True:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")

def enter_care_home_details(name):
    find_element_and_perform_action(CAREHOME_NAME_INPUT_ELEMENT, "input_text", name)
    element = ("text", name)
    find_element_and_perform_action(element, "click")

def get_is_patient_vaccinated_value_on_vaccinated_page():
    selected_value = get_checked_radio_button_text("Have you vaccinated the patient?")
    if selected_value != "":
        return selected_value
    else:
        return "Patient vaccinated value did not persist"

def get_vaccination_care_model_value_on_vaccinated_page():
    selected_value = get_checked_radio_button_text("Where is the vaccination taking place?")
    if selected_value != "":
        return selected_value
    else:
        return "Care model value did not persist"

def get_vaccine_product_value_on_vaccinated_page():
    selected_value = get_checked_radio_button_text("Vaccine product")
    if selected_value != "":
        return selected_value
    else:
        return "Vaccine product value did not persist"

def get_vaccinator_value_on_vaccinated_page():
    return find_element_and_perform_action(VACCINATOR_DROPDOWN_ELEMENT, "get_selected_option")

def get_batch_number_on_vaccinated_screen():
    return find_element_and_perform_action(BATCH_NUMBER_DROPDOWN_ELEMENT, "get_selected_option")

def get_vaccination_site_on_vaccinated_screen():
    return find_element_and_perform_action(VACCINATION_SITE_DROPDOWN_ELEMENT, "get_selected_option")
