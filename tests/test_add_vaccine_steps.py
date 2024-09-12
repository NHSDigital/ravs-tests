from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.add_vaccines_page import *
from pages.settings_page import *
from pages.site_vaccines_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    return {}

@scenario(f'{features_directory}/add_vaccines.feature', 'Add vaccines page should launch')
def test_add_vaccines_page_should_launch(navigate_and_login):
    pass

@scenario(f'{features_directory}/add_vaccines.feature', 'Vaccine already added to site warning should appear')
def test_Vaccine_already_added_to_site_warning_should_appear():
    pass

@given("I am logged into the RAVS app")
def logged_into_ravs_app(site, care_model):
    pass

@given("I am on the RAVS home page")
def logged_into_homepage(login_and_navigate_to_homepage):
    pass

@when("I am on the vaccine settings page")
def i_am_on_vaccine_settings_page():
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_settings_nav_link()
    Click_vaccines_settings()

@when("I click add vaccines button")
def i_click_add_vaccines():
    Click_add_vaccines_button()

@then('the add vaccines page should be launched')
def the_add_vaccines_page_should_launch():
    attach_screenshot("add_vaccines_page_should_launch")
    assert check_add_vaccine_button_exists() == True

@when(parse("I select {site}, {vaccine}, {vaccineType}"))
def i_select_site_vaccine_and_vaccinetype(site, vaccine, vaccineType, shared_data):
    click_site_radio_button(site)
    if "covid" in vaccine.lower():
        click_covid_vaccine_checkbox()
        click_covid_vaccine_type_checkbox(vaccineType)
    elif "flu" in vaccine.lower():
        click_flu_vaccine_checkbox()
        click_flu_vaccine_type_checkbox(vaccineType)
    Click_add_vaccine_button()
    shared_data['site'] = site
    shared_data['vaccineType'] = vaccineType

@then("the vaccine is already added to site warning should appear")
def vaccine_already_added_warning_should_exist(shared_data):
    attach_screenshot("vaccine_already_added_warning_message_exists")
    assert check_vaccine_already_added_warning_message_exists(shared_data['site'], shared_data['vaccineType']) == True
