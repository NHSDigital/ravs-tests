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
from pages.manage_users_home_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/user_management.feature')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_handler = RotatingFileHandler('tox.log', maxBytes=1024*1024, backupCount=3)  # Log rotation (optional)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add the handler to the logger
logger.addHandler(log_handler)

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # You can add logging setup here if needed
    logger.info("Logging setup complete")
    yield
    logger.info("Test session complete")

@pytest.fixture(scope='function')
def shared_data():
    data = {}
    yield data
    data.clear()

@pytest.mark.usermanagement
@given("I am logged into the RAVS app")
def logged_into_ravs_app(navigate_and_login):
    pass

@when("I click the manage users navigation link")
def I_click_manage_users_nav_link():
    click_manage_users_nav_link()
    attach_screenshot("manage_users_navigation_link_clicked")
    logging.info("logged_in_and_manage_users_navigation_link_clicked")

@then("the manage users page should be displayed")
def the_manage_users_page_should_be_displayed():
    assert check_add_user_button_exists() == True
    attach_screenshot("manage_users_page_loads_and_add_user_button_is_visible")
    logging.info("reports_page_loads_and_create_report_button_is_visible")
