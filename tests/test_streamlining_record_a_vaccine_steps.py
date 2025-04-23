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
import logging
from init_helpers import *
from conftest import *
from helpers.datetimeHelper import *
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
