import re
import time
from init_helpers import *

REPORT_ERRORS_BUTTON = ("//button[text()='Report Errors']")
EXPANDED_COVID_19_BUTTON = ("(//button[@class='accordion-button'])[1]")
COLLAPSED_COVID_19_BUTTON = ("(//button[@class='accordion-button collapsed'])[1]")
EXPANDED_FLU_BUTTON = ("(//button[@class='accordion-button'])[2]")
COLLAPSED_FLU_BUTTON = ("(//button[@class='accordion-button collapsed'])[2]")
CHECK_IN_AND_RETURN_BUTTON=("//button[text()='Check in and return']")
CHOOSE_VACCINE_BUTTON=("//button[text()='Choose Vaccine']")
PATIENT_DID_NOT_SHOW_BUTTON=("//button[text()='Patient did not show']")
BACK_BUTTON = ("//a[@href='/appointment']")
VACCINATION_HISTORY_LABEL = ("//h3[text()='Vaccination History']")
SHOW_ALL_BUTTON_COVID_RECORDS = ("(//button[contains(text(), 'Show all')])[1]")
SHOW_ALL_BUTTON_FLU_RECORDS = ("(//button[contains(text(), 'Show all')])[2]")
EDIT_HISTORY_BUTTON = ("//span[text()='Edit']")
DELETE_HISTORY_BUTTON = ("//span[text()='Delete']")
VACCINE_SUMMARY_LIST_ROWS_ELEMENTS = ("//dl[@class='nhsuk-summary-list mb-1']")

def get_count_of_immunisation_history_records(chosen_vaccine):
    time.sleep(5)
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)

    if "covid" in chosen_vaccine.lower():
        SHOW_ALL_BUTTON = SHOW_ALL_BUTTON_COVID_RECORDS
    else:
        SHOW_ALL_BUTTON = SHOW_ALL_BUTTON_FLU_RECORDS

    if check_element_exists(SHOW_ALL_BUTTON):
        show_all_button_text = find_element_and_perform_action(SHOW_ALL_BUTTON, "get_text")
        match = re.search(r'\((\d+)\)', show_all_button_text)
        
        if match:
            count = int(match.group(1))
            print("Immunisation history record count is:", count)
            return count
        else:
            print("No immunisation history records found.")
            return 0 
    else:
        print("Show all button not found. Assuming no records exist.")
        return 0  

def get_immunisation_history_details_of_vaccine(index):
    wait_for_element_to_appear(CHOOSE_VACCINE_BUTTON)
    element_selector = f"(//dl[@class='nhsuk-summary-list mb-1'])[{index}]"
    vaccine_summary_list_rows_elements = find_elements(element_selector)
    return vaccine_summary_list_rows_elements

def get_vaccine_program_details(history_index):
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
    
def get_vaccine_location_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)
    
    if vaccine_summary_list_rows_elements:
        location = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(4) .nhsuk-summary-list__value').inner_text()
        return location
    else:
        return None
    
def get_vaccine_data_source_details(history_index):
    vaccine_summary_list_rows_elements = get_immunisation_history_details_of_vaccine(history_index)
    
    if vaccine_summary_list_rows_elements:
        data_source = vaccine_summary_list_rows_elements[0].query_selector('.nhsuk-summary-list__row:nth-child(5) .nhsuk-summary-list__value').inner_text()
        return data_source
    else:
        return None
def check_vaccination_history_label_exists():
    return check_element_exists(VACCINATION_HISTORY_LABEL, True)

def click_show_all_covid_history_button():
    find_element_and_perform_action(SHOW_ALL_BUTTON_COVID_RECORDS, "click")

def click_show_all_flu_history_button():
    find_element_and_perform_action(SHOW_ALL_BUTTON_FLU_RECORDS, "click")

def click_delete_history_button(vaccine):
    if vaccine.lower() == "covid-19":
        element = "(//span[text()='Delete'])[1]"
    else:
        element = "(//span[text()='Delete'])[2]"
    find_element_and_perform_action(element, "click")

def click_edit_history_button(vaccine):
    if vaccine.lower() == "covid-19":
        element = "(//span[text()='Edit'])[1]"
    else:
        element = "(//span[text()='Edit'])[2]"
    find_element_and_perform_action(element, "click")

def click_report_errors_button():
    find_element_and_perform_action(REPORT_ERRORS_BUTTON, "click")

def click_expand_covid_history():
    find_element_and_perform_action(COLLAPSED_COVID_19_BUTTON, "click")

def click_collapse_covid_history():
    find_element_and_perform_action(EXPANDED_COVID_19_BUTTON, "click")    

def click_expand_flu_history():
    find_element_and_perform_action(COLLAPSED_FLU_BUTTON, "click")

def click_check_in_and_return_button():
    find_element_and_perform_action(CHECK_IN_AND_RETURN_BUTTON, "click")    

def click_choose_vaccine_button():
    find_element_and_perform_action(CHOOSE_VACCINE_BUTTON, "click")        

def click_patient_did_not_show_button():
    find_element_and_perform_action(PATIENT_DID_NOT_SHOW_BUTTON, "click")         

def click_back_button():
    find_element_and_perform_action(BACK_BUTTON, "click")       

def check_choose_vaccine_button_exists():
    wait_for_page_to_load()
    return check_element_exists(CHOOSE_VACCINE_BUTTON, True)