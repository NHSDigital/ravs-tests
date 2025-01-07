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
from pages.manage_users_change_user_details_page import *
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
    shared_data["first_deactivated_users_name"] = get_first_deactivated_users_name().split(' (')[0]
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

@when("I click the change user details link")
def I_click_change_user_details_link(shared_data):
    full_name = get_first_users_name()
    if full_name:
        shared_data["user_clinician_status_before_change"] = get_first_users_clinician_status()
        shared_data["user_name_before_change"] = get_first_users_name().split(' (')[0]
        shared_data["user_email_address_before_change"] = get_first_users_email_address()
        shared_data["user_permission_level_before_change"] = get_first_users_permission_level()
        shared_data["user_active_status_before_change"] = get_first_users_active_status()
        shared_data["first_users_name"] = full_name.split(' (')[0]
        if '(' in full_name and ')' in full_name:
                shared_data["first_users_clinician_status"] = full_name.split('(')[1].strip(')')
        else:
                shared_data["first_users_clinician_status"] = None
        attach_screenshot("before_clicking_first_users_change_details_link")
        logging.info("before_clicking_first_users_change_details_link")
        click_first_users_change_details_link()
    else:
        shared_data["first_users_name"] = None
        shared_data["first_users_clinician_status"] = None
    attach_screenshot("clicked_first_users_change_details_link")
    logging.info("clicked_first_users_change_details_link")

@then("the change user details page should be displayed")
def the_change_user_details_page_should_be_displayed(shared_data):
    assert check_users_name_is_displayed(shared_data["first_users_name"]) == True
    assert check_continue_to_change_user_details_button_exists() == True
    attach_screenshot("checked_change_user_details_page_is_displayed")
    logging.info("checked_change_user_details_page_is_displayed")

@when(parse("I change the user's {detail}"))
def change_users_detail(shared_data, detail):
    shared_data["detail"] = detail
    if detail == "clinician":
        if shared_data["user_clinician_status_before_change"] is not None:
            click_change_to_no_registered_clinician_radio_button()
            shared_data["user_clinician_status_after_change"] = ""
        else:
            click_change_to_yes_registered_clinician_radio_button()
            shared_data["user_clinician_status_after_change"] = "clinician"
    else:
        if shared_data["user_permission_level_before_change"].lower() != detail:
            click_change_to_permission_level_radio_button(detail)
            shared_data["user_permission_level_after_change"] = detail
        else:
            click_change_to_permission_level_radio_button("Recorder")
            shared_data["user_permission_level_after_change"] = "Recorder"
        attach_screenshot("users_details_are_changed")

@when("I click continue to save the changed detail")
def click_continue_to_save_changed_detail():
    click_continue_to_change_user_details_user_button()
    attach_screenshot("clicked_continue_to_change_user_details_user_button")
    logging.info("clicked_continue_to_change_user_details_user_button")

@then("the user's new details should be visible in the user management table")
def assert_users_new_details_are_updated(shared_data):
    if shared_data["detail"] == "clinician":
        attach_screenshot("before_asserting_clinician_status")
        if shared_data["user_clinician_status_before_change"] is not None:
            assert get_first_users_clinician_status() is None
            click_first_users_change_details_link()
            click_change_to_yes_registered_clinician_radio_button()
            click_continue_to_change_user_details_user_button()
        else:
            assert get_first_users_clinician_status().lower() == shared_data["user_clinician_status_after_change"]
            click_first_users_change_details_link()
            click_change_to_no_registered_clinician_radio_button()
            click_continue_to_change_user_details_user_button()
    else:
        attach_screenshot("before_asserting_permission_level")
        assert get_first_users_permission_level().lower() == shared_data["user_permission_level_after_change"].lower()
        click_first_users_change_details_link()
        click_change_to_permission_level_radio_button(shared_data["user_permission_level_before_change"])
        click_continue_to_change_user_details_user_button()
    attach_screenshot("reset_user_details_to_before_test_after_asserting")

