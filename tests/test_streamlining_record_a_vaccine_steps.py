import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
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

@given(parse("I select batch"))
def I_select_batch(shared_data):
    shared_data["batch_number_to_select"] = shared_data["batch_number"] + shared_data["batch_expiry_date"]
    click_batch_radio_button(shared_data["batch_number"])
