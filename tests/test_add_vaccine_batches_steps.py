from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.settings_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.site_vaccines_add_batch_page import *
from pages.vaccines_choose_site_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scenarios(f"{features_directory}/add_batches.feature")

@when("I am on the vaccines page")
def i_am_on_the_vaccines_page():
    attach_screenshot("logged_into_ravs")
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_vaccines_nav_link()
    attach_screenshot("clicked_vaccines_nav_link")

@when("I click on an available add batch link")
def i_click_first_add_batch_link():
    click_first_available_add_batch_link()
    attach_screenshot("click_first_available_add_batch_link")

@when("I click Add batch button")
def i_click_add_batch_button():
    click_add_batch_button()
    attach_screenshot("clicked_add_batch_button")

@when("I click confirm button")
def i_click_confirm_button():
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_confirm_choices_button")

@when(parse("I view product for the existing {vaccine_type} in an existing {site}"))
def view_product_for_site_and_vaccine_type(shared_data, vaccine_type, site):
    click_view_product(site, vaccine_type)
    attach_screenshot("clicked_view_product_link")

@when(parse("I enter {batch_number} that already exists and {expiry_date}"))
def i_enter_batchnumber_and_expirydate(shared_data, batch_number, expiry_date):
    click_add_batch_button()
    attach_screenshot("clicked_add_batch_button")
    enter_batch_number(batch_number)
    enter_expiry_date(expiry_date)
    attach_screenshot("entered_batch_number")
    click_continue_to_add_batch_button()

@then("the add batch page should be launched")
def add_batch_page_should_launch():
    attach_screenshot("add_batch_page_should_launch")
    assert check_add_batch_title_exists(True) == True

@then("the batch is already added to site warning should appear")
def batch_already_added_warning_should_exist():
    attach_screenshot("batch_already_added_warning_message_exists")
    assert check_batch_already_exists_error_message_is_displayed() == True
    assert check_batch_already_exists_error_message_link_is_displayed() == True

@when('I click continue to confirm batch details page')
def step_when_i_click_continue():
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_continue_to_confirm_batch_details_button")

@then('the error messages and error links should appear highlighting missing required fields')
def step_then_the_error_messages_for_missing_fields_should_appear():
    attach_screenshot(check_enter_batch_number_error_message_is_displayed)
    assert check_enter_batch_number_error_message_is_displayed()
    assert check_enter_batch_number_error_message_link_is_displayed()
    assert check_enter_batch_expiry_date_error_message_is_displayed()
    assert check_enter_batch_expiry_date_error_message_link_is_displayed()

@when('I enter batch expiry date in the past')
def step_when_i_click_continue():
    enter_batch_number("TEST-PAST")
    date = get_date_value_by_days("today-10")
    date = format_date(str(date), config["browser"])
    enter_expiry_date(date)
    click_continue_to_confirm_batch_details_button()
    attach_screenshot(f"entered_batch_expiry_date_in_the_past_{date}")

@then('the error message and error link should appear highlighting batch expiry date is in past')
def step_then_the_error_messages_for_missing_fields_should_appear():
    attach_screenshot("check_expiry_date_cannot_be_in_the_past_error_message_is_displayed")
    assert check_expiry_date_cannot_be_in_the_past_error_message_text_is_displayed()
    assert check_expiry_date_cannot_be_in_the_past_error_message_link_is_displayed()
