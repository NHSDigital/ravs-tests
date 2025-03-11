import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.confirm_page import *
from pages.create_a_patient_page import *
from pages.vaccinator_location_page import *
from pages.settings_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.check_and_confirm_vaccinated_record_page import *
from pages.patient_details_page import *
from pages.delete_vaccination_page import *
import logging
from init_helpers import *
from conftest import *
from helpers.datetimeHelper import *
from test_data.get_values_from_models import *
from faker import Faker

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scenarios(f'{features_directory}/bsa_record_a_vaccine_for_community_pharmacy.feature')

@given(parse("I login to RAVS as a community pharmacist to the {site} and set vaccinator details with {site} and {care_model} as community pharmacy and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date}"))
def step_login_to_ravs_community_pharmacy(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["care_model"] = care_model
    shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])

    navigate_and_login_as_community_pharmacist(site, shared_data)
    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, site, chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date, shared_data["pack_size"])
    return shared_data

@given(parse("I login to RAVS as a branch surgery to the {site} and set vaccinator details with {site} and {care_model} as community pharmacy and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date}"))
def step_login_to_ravs_community_pharmacy(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["care_model"] = care_model
    shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])

    navigate_and_login_as_community_pharmacist(site, shared_data)
    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, site, chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date, shared_data["pack_size"])
    return shared_data

@given(parse("I login to RAVS as a community pharmacist to the {site} and set vaccinator details with {site} and {care_model} as community pharmacy and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {chosen_vaccine_type}, {batch_number} with {batch_expiry_date}"))
def step_login_to_ravs_community_pharmacy(site, care_model, nhs_number, index, chosen_vaccine, chosen_vaccine_type, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = chosen_vaccine_type
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["care_model"] = care_model
    shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])

    navigate_and_login_as_community_pharmacist(site, shared_data)
    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, site, chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date, shared_data["pack_size"])
    return shared_data

@given(parse("I login to RAVS as a community pharmacist to the {site}"))
def step_login_to_ravs_community_pharmacy(site, shared_data):
    shared_data["site"] = site
    navigate_and_login_as_community_pharmacist(site, shared_data)
    click_find_a_patient_nav_link()
    return shared_data
