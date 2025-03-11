from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.home_page import *
from pages.login_page import *
from pages.nhs_signin_page import *
import logging
from conftest import *
from init_helpers import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/logout.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given("I am logged into the RAVS app")
def given_I_login_to_the_ravs_web_app(shared_data):
    navigate_and_login(shared_data)

@when('I click the logout button')
def click_logout():
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists():
            click_navbar_toggler()
    attach_screenshot("before_clicking_logged_out")
    click_logout_button()

@then('the user should be logged out successfully')
def check_logged_out():
    attach_screenshot("user_should_be_logged_out")
    assert check_login_button_exists()
