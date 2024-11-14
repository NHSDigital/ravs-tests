from asyncio import sleep
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
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
def logged_into_ravs_app(navigate_and_login):
    pass

@when("I click the reports navigation link")
def I_click_reports_nav_link():
    click_reports_nav_link()
    attach_screenshot("reports_navigation_link_clicked")
    logging.info("logged_in_and_reports_navigation_link_clicked")

@then("the reports page should be displayed")
def the_reports_page_should_be_displayed():
    assert check_create_report_button_exists() == True
    attach_screenshot("reports_page_loads_and_create_report_button_is_visible")
    logging.info("reports_page_loads_and_create_report_button_is_visible")

@when("I click the create report button")
def I_click_create_report_button():
    click_create_report_button()
    attach_screenshot("create_report_button_is_clicked")
    logging.info("logged_in_and_reports_navigation_link_clicked")

@then("the choose dates page should be displayed")
def the_choose_dates_page_should_be_displayed():
    assert check_today_radio_button_exists() == True
    attach_screenshot("choose_dates_range_page_should_be_displayed")
    logging.info("choose_dates_range_page_should_be_displayed")


@given(parse('I am logged into the RAVS app with the {username}'))
def logged_into_ravs_app_with_username(username):
    navigate_and_login_with_username(username)

@then("the `No vaccination data to report on` message should be displayed")
def the_choose_dates_page_should_be_displayed():
    assert check_no_vaccination_data_to_report_message_exists() == True
    attach_screenshot("no_vaccination_data_to_report_message_exists")
    logging.info("no_vaccination_data_to_report_message should be visible")

@then("the Create report button should be disabled")
def the_choose_dates_page_should_be_displayed():
    assert check_create_report_button_enabled() == False
    attach_screenshot("Create report button should be disabled")
    logging.info("Create report button should be disabled")
