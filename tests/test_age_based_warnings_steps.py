from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.home_page import *
from pages.login_page import *
from pages.nhs_signin_page import *
import logging
from conftest import *
from init_helpers import *
from test_data.get_values_from_models import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/age_based_warnings.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



