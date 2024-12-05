import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
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

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    data = {}
    yield data
    data.clear()

@scenario(f'{features_directory}/record_a_vaccine_for_patient_with_nhs_number.feature', 'Record a vaccine with nhs number')
def test_record_a_vaccine_with_nhs_number(navigate_and_login):
    pass

@scenario(f'{features_directory}/record_a_vaccine_for_patient_with_nhs_number.feature', 'Record a maternity vaccine with nhs number')
def test_record_a_maternity_vaccine_with_nhs_number(navigate_and_login):
    pass # All test steps are in conftest.py
