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
from pages.reports_vaccine_selection_page import check_covid_check_box_exists

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
    logging.info("logged_in_and_create_report_button_clicked")

@then("the choose dates page should be displayed")
def the_choose_dates_page_should_be_displayed():
    assert check_today_radio_button_exists() == True
    attach_screenshot("choose_dates_range_page_should_be_displayed")
    logging.info("choose_dates_range_page_should_be_displayed")

@given(parse('I am logged into the RAVS app with the {username}'))
def logged_into_ravs_app_with_username(username):
    navigate_and_login_with_username(username)

@then("the `No vaccination data to report on` message should be displayed")
def the_no_vaccination_data_to_report_on_message_should_be_displayed():
    assert check_no_vaccination_data_to_report_message_exists() == True
    attach_screenshot("no_vaccination_data_to_report_message_exists")
    logging.info("no_vaccination_data_to_report_message should be visible")

@then("the Create report button should be disabled")
def the_create_report_button_should_be_disabled():
    assert check_create_report_button_enabled() == False
    attach_screenshot("Create report button should be disabled")
    logging.info("Create report button should be disabled")

@when(parse('I click the {day} radio button and click Continue'))
def I_click_date_range_button_to_generate_reports(day):
    click_day_range_radio_button(day)
    if day == "Select a custom date range up to 31 days":
        from_date = format_date(str(get_date_value("today-31")), config["browser"])
        enter_from_date(from_date)
        to_date = format_date(str(get_date_value("today")), config["browser"])
        enter_to_date(to_date)
    attach_screenshot("day_range_radio_button_is_clicked_and_date_range_Selected")
    logging.info("day_range_radio_button_is_clicked_and_date_range_Selected")
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")

@then("the choose vaccines page should be displayed")
def the_choose_vaccines_page_should_be_displayed():
    assert check_covid_check_box_exists() == True
    attach_screenshot("Choose vaccines page should be visible")
    logging.info("Choose vaccines page should be visible")

@then("the user should not be able to proceed to choose a vaccine")
def the_user_should_not_be_able_to_proceed_to_choose_a_vaccine():
    assert check_no_date_selected_error_message_link_exists() == True
    assert check_no_date_selected_error_message_text_exists() == True
    attach_screenshot("no_date_selected_error_message_should_exist")
    logging.info("no_date_selected_error_message_should_exist")

@when('I select no date range and click Continue')
def I_select_no_date_range_and_click_continue(shared_data):
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")

@when(parse('I select a invalid date range of {from_date} and {to_date} and click Continue'))
def I_click_date_range_button_to_generate_reports(from_date, to_date, shared_data):
    click_day_range_radio_button("Select a custom date range up to 31 days")
    if (from_date and to_date != 'none'):
        from_date = format_date(str(get_date_value(from_date)), config["browser"])
        to_date = format_date(str(get_date_value(to_date)), config["browser"])
        enter_from_date(from_date)
        enter_to_date(to_date)
        attach_screenshot("day_range_radio_button_is_clicked_and_date_range_Selected")
        logging.info("day_range_radio_button_is_clicked_and_date_range_Selected")
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")
    shared_data["from_date"] = from_date
    shared_data["to_date"] = to_date

@then(parse("the {error_message} should be displayed"))
def the_error_message_for_reports_date_should_be_displayed(shared_data, error_message):
    if shared_data['from_date'] == 'none' and shared_data['to_date'] == 'none':
        assert check_from_date_missing_error_message_link_exists() == True
        assert check_from_date_missing_error_message_link_exists() == True
        assert check_to_date_missing_error_message_link_exists() == True
        assert check_to_date_missing_error_message_link_exists() == True
    if 'today+' in shared_data['from_date'] and 'today' in shared_data['to_date']:
        assert check_from_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_from_date_must_be_in_the_past_error_message_link_exists() == True
    if shared_data['from_date'] =='today' and 'today+' in shared_data['to_date']:
        assert check_to_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_link_exists() == True
    if 'today+' in shared_data['from_date'] and 'today+' in shared_data['to_date']:
        assert check_from_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_from_date_must_be_in_the_past_error_message_link_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_link_exists() == True
    attach_screenshot("Choose vaccines page should be visible")
    logging.info("Choose vaccines page should be visible")
