from asyncio import sleep
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.login_page import *
from pages.home_page import *
from pages.nhs_signin_page import *
from pages.reports_date_range_selection_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/reports.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    return {}

@pytest.mark.reports
@given("I am logged into the RAVS app")
def logged_into_ravs_app():
    pass

@when("I click the reports navigation link")
def I_click_reports_nav_link(navigate_and_login):
    click_reports_nav_link()
    attach_screenshot("reports_navigation_link_clicked")
    logging.info("logged_in_and_reports_navigation_link_clicked")

@then("the reports page should be displayed")
def the_reports_page_should_be_displayed():
    assert check_create_report_button_exists() == True
    attach_screenshot("reports_page_loads_and_create_report_button_is_visible")
    logging.info("reports_page_loads_and_create_report_button_is_visible")
