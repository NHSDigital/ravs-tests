from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.settings_page import *
from pages.vaccines_page import *
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

@given("I am logged into the RAVS app")
def logged_into_ravs_app():
    pass

@given("I am on the RAVS home page")
def logged_into_homepage(navigate_and_login):
    pass

@when("I am on the vaccines page")
def i_am_on_the_vaccines_page():
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_vaccines_nav_link()

@when("I click add vaccine button")
def i_click_add_vaccine():
    click_add_vaccine_button()

@when(parse("I select {site}, {vaccine}, {vaccine_type}"))
def i_select_site_vaccine_and_vaccinetype(site, vaccine, vaccine_type, shared_data):
    enter_site_name(site)
    select_site_from_list(site)
    click_continue_to_add_vaccine_button()
    click_vaccine_radiobutton(vaccine)
    click_vaccine_type_radiobutton(vaccine_type)
    shared_data['site'] = site
    shared_data['vaccineType'] = vaccine_type

@then("the choose site page should be launched")
def the_choose_site_page_is_launched():
    attach_screenshot("choose_site_page_should_launch")
    assert check_choose_site_title_exists(True) == True
