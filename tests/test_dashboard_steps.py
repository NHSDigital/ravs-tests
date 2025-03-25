from asyncio import sleep
import csv
from logging.handlers import RotatingFileHandler
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.login_page import *
from pages.home_page import *
from pages.nhs_signin_page import *
from pages.reports_check_and_confirm_page import *
from pages.reports_creating_report_page import *
from pages.reports_data_selection_page import *
from pages.reports_date_range_selection_page import *
import logging
from init_helpers import *
from conftest import *
from pages.reports_site_selection_page import *
from pages.reports_vaccine_selection_page import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/dashboard.feature')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_handler = RotatingFileHandler('tox.log', maxBytes=1024*1024, backupCount=3)  # Log rotation (optional)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logger.addHandler(log_handler)

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger.info("Logging setup complete")
    yield
    logger.info("Test session complete")

@then(parse("the {site} name should be visible on the dashboard page"))
def the_site_name_should_be_visible_on_dashboard_page(site):
    assert check_site_name_exists_in_dashboard(site) == True
    attach_screenshot("Site name should be visible in the dashboard")
    logging.info("Site name should be visible in the dashboard")

@then("the today vaccinations count should be 0")
def today_vaccinations_count_Should_be_0():
    assert get_today_vaccinations_count() == "0"
    attach_screenshot("Today vaccinations count should be 0 in the dashboard")
    logging.info("Today vaccinations count should be 0 in the dashboard")

@then("the past 7 days vaccinations count should be 0")
def week_vaccinations_count_Should_be_0():
    assert get_week_vaccinations_count() == "0"
    attach_screenshot("Week vaccinations count should be 0 in the dashboard")
    logging.info("Week vaccinations count should be 0 in the dashboard")

@then("the past month's vaccinations count should be 0")
def month_vaccinations_count_Should_be_0():
    assert get_month_vaccinations_count() == "0"
    attach_screenshot("Month vaccinations count should be 0 in the dashboard")
    logging.info("Month vaccinations count should be 0 in the dashboard")

@then("the create a report link should be visible")
def create_a_report_link_should_be_visible():
    assert check_create_a_report_link_exists() == True
    attach_screenshot("Create a report link should be available in the dashboard")
    logging.info("Create a report link should be available in the dashboard")

@then("the create a report link should not be visible")
def create_a_report_link_should_not_be_visible():
    assert check_create_a_report_link_exists() == False
    attach_screenshot("Create a report link should not be available in the dashboard")
    logging.info("Create a report link should not be available in the dashboard")
