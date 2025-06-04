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
from pages.streamlining_patient_details_page import *
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
        attach_screenshot("click_vaccinator_me_radio_button")
    else:
        set_clinician_details(shared_data, shared_data["site"])
        formatted = shared_data["vaccinator"].replace(" - ", " (") + ")"
        click_vaccinator_radio_button(formatted)
        attach_screenshot(f"clicked_{formatted}_radio_button")
        click_continue_to_choose_vaccine_screen()
    attach_screenshot("clicked_continue_to_choose_vaccine_screen")

@given(parse("I select vaccine - {chosen_vaccine}"))
def I_set_vaccine(chosen_vaccine):
    click_vaccine_radio_button(chosen_vaccine)
    attach_screenshot(f"clicked_{chosen_vaccine}_radio_button")

@given("I select vaccine product")
def I_set_vaccine_product(shared_data):
    vaccine_product = get_vaccination_type(shared_data["index"], shared_data["chosen_vaccine"])
    click_vaccine_product_radio_button(vaccine_product)
    attach_screenshot(f'clicked_{vaccine_product}_radio_button')
    shared_data["vaccine_product"] = vaccine_product
    click_continue_to_choose_batch_screen()
    attach_screenshot("clicked_continue_to_choose_batch_screen")

@given(parse("I select batch"))
def I_select_batch(shared_data):
    shared_data["batch_number_to_select"] = shared_data["batch_number"] + shared_data["batch_expiry_date"]
    shared_data["batch_expiry_date"] = date_format_with_name_of_month(shared_data["batch_expiry_date"])
    click_batch_radio_button(shared_data["batch_number"], shared_data["batch_expiry_date"])
    attach_screenshot(f'clicked_{shared_data["batch_number"]}_radio_button')
    click_continue_to_choose_eligibility_screen()
    attach_screenshot("clicked_continue_to_choose_eligibility_screen")

@given(parse("I select patient's eligibility for the vaccine"))
def I_select_eligibility(shared_data):
    shared_data["eligibility"] = get_new_eligibility_type(shared_data["index"], shared_data["chosen_vaccine"])
    click_eligibility_radio_button(shared_data["eligibility"])
    attach_screenshot(f'click_{shared_data["eligibility"]}_radio_button')
    click_continue_to_choose_vaccination_location_screen()
    attach_screenshot("clicked_continue_to_choose_vaccination_location_screen")

@given(parse("I select the location where vaccination was given"))
def I_select_vaccination_location(shared_data):
    shared_data["vaccination_location"] = get_vaccination_location(shared_data["index"])
    click_vaccination_location_radio_button(shared_data["vaccination_location"])
    attach_screenshot(f'clicked_{shared_data["vaccination_location"]}_radio_button')
    if shared_data["vaccination_location"].lower() == "care home":
        enter_and_select_care_home_details("WHITESTONES CARE HOME")
        attach_screenshot("entered__whitestones_care_home_details")
    click_continue_to_find_patient_by_nhs_number_screen()
    attach_screenshot("clicked_continue_to_find_patient_by_nhs_number_screen")

@given(parse("I enter the patient's NHS number - {nhs_number}"))
def I_enter_patients_nhs_number(shared_data, nhs_number):
    enter_patient_nhs_number(nhs_number)
    attach_screenshot(f"entered_{nhs_number}")
    shared_data["patient_nhs_number"] = nhs_number
    click_continue_to_patient_details_screen()
    attach_screenshot("clicked_continue_to_patient_details_screen")

@given(parse("I should be directed to the patient history page and show {name}, {nhs_number}, {date_of_birth} and {address} details"))
def I_should_be_directed_to_patient_history_screen(shared_data, name, nhs_number, date_of_birth, address):
    assert check_patient_details_heading_exists(name)
    attach_screenshot(f"patient_{name}_details_exist")
    assert get_patient_name_value_in_patient_details_screen().lower() == name.lower()
    if "nhs_number" == "9449304033":
        nhs_number = "9734250221"
        shared_data["patient_nhs_number"] = "9734250221"
    elif nhs_number == "9467361590":
        nhs_number = "3508118053"
        shared_data["patient_nhs_number"] = "3508118053"
    assert get_patient_nhs_number_value_in_patient_details_screen() == format_nhs_number(nhs_number)
    assert get_patient_date_of_birth_value_in_patient_details_screen() == date_format_with_age_for_streamlining(date_of_birth)
    if address != "None":
        assert normalize_address(get_patient_address_value_in_patient_details_screen()) == normalize_address(address)
    else:
        assert get_patient_address_value_in_patient_details_screen() == None

@given("I click continue to select injection site")
def I_click_continue_injection_site_selection_screen():
    click_continue_to_select_injection_site_screen()
    attach_screenshot("clicked_continue_to_select_injection_site_screen")

@given("I select where the injection was given")
def I_select_injection_location(shared_data):
    shared_data["injection_location"] = get_vaccination_site(shared_data["index"])
    click_injection_location_radio_button(shared_data["injection_location"])
    attach_screenshot(f'clicked_{shared_data["injection_location"]}_radio_button')
    click_continue_to_check_and_confirm_screen()
    attach_screenshot("clicked_continue_to_check_and_confirm_screen")

@given(parse("I confirm patient's name as {name}, date of birth as {date_of_birth}, address as {address} and the given vaccination details"))
def I_confirm_details(shared_data, name, date_of_birth, address):
    # assert check_change_patient_nhs_number_link_exists()
    # attach_screenshot("checked_change_patient_nhs_number_link_exists")
    assert check_change_vaccine_link_exists()
    attach_screenshot("checked_change_vaccine_link_exists")
    assert check_change_batch_link_exists()
    attach_screenshot("checked_change_batch_link_exists")
    assert check_change_eligibility_link_exists()
    attach_screenshot("checked_change_eligibility_link_exists")
    assert check_change_injection_link_exists()
    attach_screenshot("checked_change_injection_link_exists")
    assert check_change_location_link_exists()
    attach_screenshot("checked_change_location_link_exists")
    assert get_patient_nhs_number_value_in_check_and_confirm_screen() == format_nhs_number(shared_data["patient_nhs_number"])
    attach_screenshot(f'patient_nhs_number_value_in_check_and_confirm_screen_should_be_{shared_data["patient_nhs_number"]}')
    assert get_patient_name_value_in_check_and_confirm_screen() == name
    assert shared_data["batch_number"] in get_patient_vaccination_batch_number_value()
    assert shared_data["batch_expiry_date"] in get_patient_vaccination_batch_number_value()
    assert "Expires" in get_patient_vaccination_batch_number_value()
    attach_screenshot("patient_name_value_in_check_and_confirm_screen_should_be_{name}")
    if address != "None":
        assert normalize_address(get_patient_address_value_in_patient_details_screen()) == normalize_address(address)
    else:
        assert get_patient_address_value_in_check_and_confirm_screen() == None
    attach_screenshot(f"patient_address_value_in_check_and_confirm_screen_should_be_{address}")
    # formatted_date = date_format_with_name_of_month(date_of_birth)
    formatted_date = date_format_with_age_for_streamlining(date_of_birth)
    assert get_patient_dob_value_in_check_and_confirm_screen() == formatted_date
    attach_screenshot(f"patient_dob_value_in_check_and_confirm_screen_should_be_{formatted_date}")
    assert get_patient_vaccination_injection_site_value() == shared_data["injection_location"]
    attach_screenshot(f'patient_vaccination_injection_site_value_should_be_{shared_data["injection_location"]}')
    assert get_patient_eligibility_value() == shared_data["eligibility"]
    attach_screenshot(f'patient_eligibility_value_should_be_{shared_data["eligibility"]}')
    assert shared_data["chosen_vaccine"] in get_given_vaccine_value()
    attach_screenshot(f'given_vaccine_value_should_be_{shared_data["chosen_vaccine"]}')
    assert shared_data["vaccine_product"] in get_given_vaccine_value()
    attach_screenshot(f'get_given_product_vaccine_value_should_be_{shared_data["vaccine_product"]}')
    assert get_team_value().lower() == shared_data["site"].lower()
    attach_screenshot(f'team_value_should_be_{shared_data["site"]}')
    assert get_patient_vaccination_vaccinator_value() == shared_data["vaccinator"].split(" - ")[0]
    attach_screenshot(f'patient_vaccination_vaccinator_value_should_be_{shared_data["vaccinator"].split(" - ")[0]}')
    assert check_optional_note_text_message_exists()
    attach_screenshot("checked_optional_note_text_message_exists")
    assert check_optional_note_text_box_exists()
    attach_screenshot("checked_optional_note_text_box_exists")
    assert check_optional_note_text_label_exists()
    attach_screenshot("checked_optional_note_text_label_exists")
    shared_data["patient_name"] = name
    shared_data["patient_date_of_birth"] = date_of_birth
    shared_data["patient_address"] = address

@given("I click confirm and save button")
def I_click_confirm_and_save_button():
    click_confirm_and_save_button()
    attach_screenshot("clicked_confirm_and_save_button")

@then("the vaccination should be recorded successfully")
def the_vaccine_should_record_successfully(shared_data):
    assert check_next_vaccination_link_exists()
    attach_screenshot("checked_next_vaccination_link_exists")
    assert check_patients_record_link_exists(shared_data["patient_name"])
    attach_screenshot(f'checkED_patients_record_link_exists_{shared_data["patient_name"]}')
    assert check_patients_record_saved_text_exists(shared_data["patient_name"])
    attach_screenshot(f'checked_patients_record_saved_text_exists_{shared_data["patient_name"]}')
    click_patients_record_link(shared_data["patient_name"])
    attach_screenshot(f'clicked_patients_record_link{shared_data["patient_name"]}')
    immunisation_history_records_after_recording = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
    attach_screenshot("immunisation_history_records_count_after_recording_vaccination_is_" + str(immunisation_history_records_after_recording))
    assert immunisation_history_records_after_recording > shared_data["immunisation_history_records_count_before_recording"]
    attach_screenshot(f'{immunisation_history_records_after_recording}_greater_than_{shared_data["immunisation_history_records_count_before_recording"]}')
