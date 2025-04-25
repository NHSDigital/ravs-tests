import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.enter_patient_nhs_number_page import *
from pages.select_eligibility_page import *
from pages.select_injection_location_page import *
from pages.select_vaccination_location_page import *
from pages.select_vaccinator_page import *
from pages.select_vaccine_page import *
from pages.select_batch_page import *
from pages.record_vaccinations_check_and_confirm_page import *
import logging
from init_helpers import *
from conftest import *
from helpers.datetimeHelper import *
from pages.vaccination_record_saved_page import *
from test_data.get_values_from_models import *
from faker import Faker

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scenarios(f'{features_directory}/streamlining_recording_a_vaccine.feature')
# All steps are in conftest.py

@given(parse("I set vaccinator as {vaccinator}"))
def I_set_vaccinator(shared_data, vaccinator):
    if vaccinator == "me":
       click_vaccinator_radio_button("Me")
    else:
        set_clinician_details(shared_data, shared_data["site"])
        formatted = shared_data["vaccinator"].replace(" - ", " (") + ")"
        click_vaccinator_radio_button(formatted)
        click_continue_to_choose_vaccine_screen()

@given(parse("I select vaccine - {chosen_vaccine}"))
def I_set_vaccine(chosen_vaccine):
    click_vaccine_radio_button(chosen_vaccine)

@given("I select vaccine product")
def I_set_vaccine_product(shared_data):
    vaccine_product = get_vaccination_type(shared_data["index"], shared_data["chosen_vaccine"])
    click_vaccine_product_radio_button(vaccine_product)
    shared_data["vaccine_product"] = vaccine_product
    click_continue_to_choose_batch_screen()

@given(parse("I select batch"))
def I_select_batch(shared_data):
    shared_data["batch_number_to_select"] = shared_data["batch_number"] + shared_data["batch_expiry_date"]
    click_batch_radio_button(shared_data["batch_number"])
    click_continue_to_choose_eligibility_screen()

@given(parse("I select patient's eligibility for the vaccine"))
def I_select_eligibility(shared_data):
    shared_data["eligibility"] = get_eligibility_type(shared_data["index"], shared_data["chosen_vaccine"])
    click_eligibility_radio_button(shared_data["eligibility"])
    click_continue_to_choose_vaccination_location_screen()

@given(parse("I select the location where vaccination was given"))
def I_select_vaccination_location(shared_data):
    shared_data["vaccination_location"] = get_vaccination_location(shared_data["index"])
    click_vaccination_location_radio_button(shared_data["vaccination_location"])
    if shared_data["vaccination_location"].lower() == "care home":
        enter_care_home_details("WHITESTONES CARE HOME")
    click_continue_to_find_patient_by_nhs_number_screen()

@given(parse("I enter the patient's NHS number - {nhs_number}"))
def I_enter_patients_nhs_number(shared_data, nhs_number):
    enter_patient_nhs_number(nhs_number)
    shared_data["patient_nhs_number"] = nhs_number
    click_continue_to_injection_location_screen()

@given("I select where the injection was given")
def I_select_injection_location(shared_data):
    shared_data["injection_location"] = get_vaccination_site(shared_data["index"])
    click_injection_location_radio_button(shared_data["injection_location"])
    click_continue_to_check_and_confirm_screen()

@given(parse("I confirm patient's name as {name}, date of birth as {date_of_birth}, address as {address} and the given vaccination details"))
def I_confirm_details(shared_data, name, date_of_birth, address):
    assert check_change_patient_nhs_number_link_exists()
    assert check_change_vaccine_link_exists()
    assert check_change_batch_link_exists()
    assert check_change_eligibility_link_exists()
    assert check_change_injection_link_exists()
    assert check_change_location_link_exists()
    assert get_patient_nhs_number_value_in_check_and_confirm_screen() == shared_data["patient_nhs_number"]
    assert get_patient_name_value_in_check_and_confirm_screen() == name
    assert get_patient_address_value_in_check_and_confirm_screen() == address
    assert get_patient_dob_value_in_check_and_confirm_screen() == date_format_with_name_of_month(date_of_birth)
    assert get_patient_vaccination_injection_site_value() == shared_data["injection_location"]
    assert get_patient_eligibility_value() == shared_data["eligibility"]
    assert shared_data["chosen_vaccine"] in get_given_vaccine_value()
    assert shared_data["vaccine_product"] in get_given_vaccine_value()
    assert get_team_value().lower() == shared_data["site"].lower()
    assert get_patient_vaccination_vaccinator_value() == shared_data["vaccinator"].split(" - ")[0]
    assert check_optional_note_text_message_exists()
    assert check_optional_note_text_box_exists()
    assert check_optional_note_text_label_exists()
    shared_data["patient_name"] = name
    shared_data["patient_date_of_birth"] = date_of_birth
    shared_data["patient_address"] = address

@given("I click confirm and save button")
def I_click_confirm_and_save_button():
    click_confirm_and_save_button()

@then("the vaccination should be recorded successfully")
def the_vaccine_should_record_successfully(shared_data):
    assert check_next_vaccination_link_exists()
    assert check_patients_record_link_exists(shared_data["patient_name"])
    assert check_patients_record_saved_text_exists(shared_data["patient_name"])
    click_patients_record_link(shared_data["patient_name"])
    immunisation_history_records_after_recording = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
    attach_screenshot("immunisation_history_records_count_after_recording_vaccination_is_" + str(immunisation_history_records_after_recording))
    assert immunisation_history_records_after_recording > shared_data["immunisation_history_records_count_before_recording"]
