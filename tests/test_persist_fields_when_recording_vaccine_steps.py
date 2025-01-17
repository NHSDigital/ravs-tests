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

features_directory = get_working_directory() + "features"

@scenario(f'{features_directory}/persist_field_when_recording_a_vaccine.feature', 'Persist fields when recording a vaccination')
def test_persisting_fields_when_recording_a_vaccine(navigate_and_login):
    pass