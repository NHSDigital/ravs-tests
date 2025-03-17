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

scenarios(f'{features_directory}/bsa_record_a_vaccine.feature')
# All steps are in conftest.py
