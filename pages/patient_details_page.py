import re
import time
from init_helpers import *

REPORT_ERRORS_BUTTON = ("//button[text()='Report Errors']")
EXPANDED_COVID_19_BUTTON = ("(//button[@class='accordion-button'])[1]")
COLLAPSED_COVID_19_BUTTON = ("(//button[@class='accordion-button collapsed'])[1]")
EXPANDED_FLU_BUTTON = ("(//button[@class='accordion-button'])[2]")
COLLAPSED_FLU_BUTTON = ("(//button[@class='accordion-button collapsed'])[2]")
EXPANDED_RSV_BUTTON = ("(//button[@class='accordion-button'])[3]")
COLLAPSED_RSV_BUTTON = ("(//button[@class='accordion-button collapsed'])[3]")
EXPANDED_PERTUSSIS_BUTTON = ("(//button[@class='accordion-button'])[4]")
COLLAPSED_PERTUSSIS_BUTTON = ("(//button[@class='accordion-button collapsed'])[4]")
CHECK_IN_AND_RETURN_BUTTON=("//button[text()='Check in and return']")
CHOOSE_VACCINE_BUTTON=("role", "button", "Choose Vaccine")
PATIENT_DID_NOT_SHOW_BUTTON=("//button[text()='Patient did not show']")
BACK_BUTTON_ON_PATIENT_DETAILS_PAGE = ("link", "Back")
SHOW_ALL_BUTTON_COVID_RECORDS = ("(//h2[contains(text(), 'COVID-19')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_FLU_RECORDS = ("(//h2[contains(text(), 'Flu')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_RSV_RECORDS = ("(//h2[contains(text(), 'Respiratory syncytial virus (RSV)')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
SHOW_ALL_BUTTON_PERTUSSIS_RECORDS = ("(//h2[contains(text(), 'Pertussis')])[1]/ancestor::div[@class='mb-2']//button[contains(text(), 'Show all')]")
EDIT_HISTORY_BUTTON = ("xpath", "//span[text()='Edit']")
DELETE_HISTORY_BUTTON = ("xpath", "//span[text()='Delete']")
VACCINE_SUMMARY_LIST_ROWS_ELEMENTS = ("xpath", "//dl[@class='nhsuk-summary-list mb-1']")
COVID_HISTORY_ELEMENT = ("xpath", "//div[text()='COVID-19']")
FLU_HISTORY_ELEMENT = ("xpath", "//div[text()='Flu']")
RSV_HISTORY_ELEMENT = ("xpath", "(//div[text()='Respiratory syncytial virus (RSV)'])[1]")
PERTUSSIS_HISTORY_ELEMENT = ("xpath", "//div[text()='Pertussis']")
PAGE_LOADING_ELEMENT = ("role", "status")
VACCINATION_HISTORY_NOT_AVAILABLE = ("role", "heading", "No vaccination history available")
PATIENT_NAME_ELEMENT = ("xpath", "//dt[text()='Name']/following-sibling::dd")
PATIENT_NHS_NUMBER_ELEMENT = ("xpath", "//dt[text()='NHS number']/following-sibling::dd")
PATIENT_DATE_OF_BIRTH_ELEMENT = ("xpath", "//dt[text()='Date of birth']/following-sibling::dd")
PATIENT_GENDER_ELEMENT = ("xpath", "//dt[text()='Gender']/following-sibling::dd")
PATIENT_PHONE_NUMBER_ELEMENT = ("xpath", "//dt[text()='Phone number']/following-sibling::dd")
PATIENT_ADDRESS_ELEMENT = ("xpath", "//dt[text()='Address']/following-sibling::dd")
PATIENT_DETAILS_TEXT_HEADING_ELEMENT = ("role", "heading", "Patient details", True)

def ensure_patient_details_heading_element_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(PATIENT_DETAILS_TEXT_HEADING_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(PATIENT_DETAILS_TEXT_HEADING_ELEMENT)

def get_patient_name_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_NAME_ELEMENT, "get_text")

def get_patient_nhs_number_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_NHS_NUMBER_ELEMENT, "get_text")

def get_patient_date_of_birth_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_DATE_OF_BIRTH_ELEMENT, "get_text")

def get_patient_gender_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_GENDER_ELEMENT, "get_text")

def get_patient_phone_number_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_PHONE_NUMBER_ELEMENT, "get_text")

def get_patient_address_value_in_patient_details_screen():
    ensure_patient_details_heading_element_exists()
    return find_element_and_perform_action(PATIENT_ADDRESS_ELEMENT, "get_text")

def check_vaccine_history_not_available_label_element_exists():
    ensure_patient_details_heading_element_exists()
    time.sleep(2)
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    return check_element_exists(VACCINATION_HISTORY_NOT_AVAILABLE)

def check_covid_history_element_exists():
    ensure_patient_details_heading_element_exists()
    return check_element_exists(COVID_HISTORY_ELEMENT)

def check_flu_history_element_exists():
    ensure_patient_details_heading_element_exists()
    return check_element_exists(FLU_HISTORY_ELEMENT)

def check_rsv_history_element_exists():
    ensure_patient_details_heading_element_exists()
    return check_element_exists(RSV_HISTORY_ELEMENT)

def check_pertussis_history_element_exists():
    ensure_patient_details_heading_element_exists()
    return check_element_exists(PERTUSSIS_HISTORY_ELEMENT)

def get_count_of_immunisation_history_records(chosen_vaccine):
    count = 0
    time.sleep(2)
    ensure_patient_details_heading_element_exists()
    time.sleep(2)
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)

    element = (
        "xpath",
        f"//h2[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{chosen_vaccine.lower()}')]/following-sibling::div/p[contains(text(), 'Displaying')]"
    )
    wait_for_element_to_appear(element)
    if check_element_exists(element, True):
        display_text = find_element_and_perform_action(element, "get_text")

        match = re.search(r"Displaying\s1\sof\s(\d+)", display_text)
        count = int(match.group(1))
        print("Immunisation history record count is:", count)
        return count
    else:
        print("No immunisation history records found for this vaccine")
        return 0

def get_immunisation_history_details_of_vaccine(index):
    ensure_patient_details_heading_element_exists()
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    element_selector = f"(//dl[@class='nhsuk-summary-list mb-1'])[{index}]"
    element = ("xpath", element_selector)
    wait_for_element_to_appear(element)
    vaccine_summary_list_rows_elements = find_elements(element_selector)
    return vaccine_summary_list_rows_elements

def get_vaccine_program_details(history_index):
    ensure_patient_details_heading_element_exists()
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)
    if vaccine_summary_list_rows_elements:
        vaccine_program = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(1) .nhsuk-summary-list__value').inner_text()
        return vaccine_program
    else:
        return None

def get_vaccine_date_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)

    if vaccine_summary_list_rows_elements:
        vaccine_date = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(2) .nhsuk-summary-list__value').inner_text()
        return vaccine_date
    else:
        return None

def get_vaccine_product_name_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)

    if vaccine_summary_list_rows_elements:
        product_name = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(3) .nhsuk-summary-list__value').inner_text()
        return product_name
    else:
        return None

def get_vaccine_product_batch_number_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)

    if vaccine_summary_list_rows_elements:
        product_name = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(4) .nhsuk-summary-list__value').inner_text()
        return product_name
    else:
        return None

def get_vaccine_location_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)
    if vaccine_summary_list_rows_elements:
        location = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(5) .nhsuk-summary-list__value').inner_text()
        return location
    else:
        return None

def get_vaccine_data_source_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)

    if vaccine_summary_list_rows_elements:
        data_source = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(6) .nhsuk-summary-list__value').inner_text()
        return data_source
    else:
        return None

def click_show_all_covid_history_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(SHOW_ALL_BUTTON_COVID_RECORDS, "click")

def click_show_all_flu_history_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(SHOW_ALL_BUTTON_FLU_RECORDS, "click")

def click_show_all_rsv_history_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(SHOW_ALL_BUTTON_RSV_RECORDS, "click")

def click_show_all_pertussis_history_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(SHOW_ALL_BUTTON_PERTUSSIS_RECORDS, "click")

def click_delete_history_button(vaccine, index):
    if vaccine.lower() == "covid-19":
        element = f"(//span[text()='Delete'])[{index}]"
    elif vaccine.lower() == "flu":
        element = f"(//span[text()='Delete'])[{index}]"
    elif vaccine.lower() == "respiratory syncytial virus (rsv)":
        element = f"(//span[text()='Delete'])[{index}]"
    elif vaccine.lower() == "pertussis":
        element = f"(//span[text()='Delete'])[{index}]"
    find_element_and_perform_action(element, "click")

def click_delete_history_link(vaccine):
    showAllElement = ()
    element = (f"//h2[contains(text(), '{vaccine}')]/following-sibling::div//a/span[text()='Delete']")
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")

def click_edit_history_button(vaccine, index):
    if vaccine.lower() == "covid-19":
        element = f"(//span[text()='Edit'])[{index}]"
    elif vaccine.lower() == "flu":
        element = f"(//span[text()='Edit'])[{index}]"
    elif vaccine.lower() == "respiratory syncytial virus (rsv)":
        element = f"(//span[text()='Edit'])[{index}]"
    elif vaccine.lower() == "pertussis":
        element = f"(//span[text()='Edit'])[{index}]"
    find_element_and_perform_action(element, "click")

def click_report_errors_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(REPORT_ERRORS_BUTTON, "click")

def click_expand_covid_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(COLLAPSED_COVID_19_BUTTON, "click")

def click_collapse_covid_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(EXPANDED_COVID_19_BUTTON, "click")

def click_expand_flu_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(COLLAPSED_FLU_BUTTON, "click")

def click_collapse_flu_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(EXPANDED_FLU_BUTTON, "click")

def click_expand_rsv_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(COLLAPSED_RSV_BUTTON, "click")

def click_collapse_rsv_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(EXPANDED_RSV_BUTTON, "click")

def click_expand_pertussis_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(COLLAPSED_PERTUSSIS_BUTTON, "click")

def click_collapse_pertussis_history():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(EXPANDED_PERTUSSIS_BUTTON, "click")

def click_check_in_and_return_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(CHECK_IN_AND_RETURN_BUTTON, "click")

def click_choose_vaccine_button():
    ensure_patient_details_heading_element_exists()
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    find_element_and_perform_action(CHOOSE_VACCINE_BUTTON, "click")

def click_patient_did_not_show_button():
    ensure_patient_details_heading_element_exists()
    find_element_and_perform_action(PATIENT_DID_NOT_SHOW_BUTTON, "click")

def click_back_button_on_patient_details_page():
    ensure_patient_details_heading_element_exists()
    wait_for_element_to_appear(BACK_BUTTON_ON_PATIENT_DETAILS_PAGE)
    find_element_and_perform_action(BACK_BUTTON_ON_PATIENT_DETAILS_PAGE, "click")

def check_choose_vaccine_button_exists():
    ensure_patient_details_heading_element_exists()
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    return check_element_exists(CHOOSE_VACCINE_BUTTON, True)
