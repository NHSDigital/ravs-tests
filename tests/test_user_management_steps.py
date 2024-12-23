from asyncio import sleep
import csv
from logging.handlers import RotatingFileHandler
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.login_page import *
from pages.home_page import *
from pages.manage_users_add_user_page import *
from pages.manage_users_deactivate_users_page import *
from pages.manage_users_reactivate_users_page import *
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

@when("I click the add user button")
def I_click_add_user_button():
    click_add_user_button()
    attach_screenshot("add_user_button_clicked")
    logging.info("add_user_button_clicked")

@then("the add user page should be displayed")
def the_add_user_page_should_be_displayed():
    assert check_continue_to_add_user_button_exists() == True
    attach_screenshot("continue_to_add_user_button_is_visible")
    logging.info("continue_to_add_user_button_is_visible")

@when("I click the continue to add user details button")
def I_click_continue_to_add_user_button():
    click_continue_to_add_user_button()
    attach_screenshot("continue_to_add_user_button_clicked")
    logging.info("continue_to_add_user_button_clicked")

@then("the error messages and links should be displayed for the missing fields")
def the_error_messages_and_links_should_be_displayed():
    assert check_enter_first_name_error_message_text_exists() == True
    assert check_enter_first_name_error_message_link_exists() == True
    assert check_enter_last_name_error_message_text_exists() == True
    assert check_enter_last_name_error_message_link_exists() == True
    assert check_enter_email_address_error_message_text_exists() == True
    assert check_enter_email_address_error_message_link_exists() == True
    assert check_select_clinician_error_message_text_exists() == True
    assert check_select_clinician_error_message_link_exists() == True
    assert check_select_permission_level_error_message_text_exists() == True
    assert check_select_permission_level_error_message_link_exists() == True
    attach_screenshot("check_add_user_error_messages_are_visible")
    logging.info("check_add_user_error_messages_are_visible")

@when("I click the deactivated users link")
def I_click_deactivated_users_link():
    click_view_deactivated_users_link()
    attach_screenshot("clicked_view_deactivated_users_link")
    logging.info("clicked_view_deactivated_users_link")

@then("the deactivated users page should be displayed")
def the_deactivated_users_page_should_be_displayed():
    assert check_deactivated_users_page_heading_exists() == True
    assert check_deactivated_users_list_table_exists() == True
    attach_screenshot("checked_deactivated_users_list_table_exists")
    logging.info("checked_deactivated_users_list_table_exists")

@when("I click the reactivate user link")
def I_click_reactivate_user_link(shared_data):
    shared_data["first_deactivated_users_name"] = get_first_deactivated_users_name()
    shared_data["first_deactivated_users_email_address"] = get_first_deactivated_users_email_address()
    click_first_deactivated_users_reactivate_link()
    attach_screenshot("clicked_first_deactivated_users_reactivate_link")
    logging.info("clicked_first_deactivated_users_reactivate_link")

@then("the reactivate user page should be displayed")
def the_reactivate_user_page_should_be_displayed(shared_data):
    assert check_reactivate_button_exists() == True
    assert check_reactivate_message_text_exists(shared_data["first_deactivated_users_name"], shared_data["first_deactivated_users_email_address"]) == True
    attach_screenshot("checked_reactivate_button_exists")
    logging.info("check_reactivate_button_exists")
