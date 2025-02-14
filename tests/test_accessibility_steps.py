from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.home_page import *
from pages.login_page import *
from pages.nhs_signin_page import *
import logging
from conftest import *
from init_helpers import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/accessibility.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given("I access RAVS")
def access_ravs(navigate_to_ravs):
    pass

@then('the RAVS sign in page should be accessible')
def check_accessibility():
    attach_screenshot("user_should_be_logged_out")
    violations = get_accessibility_violations()
    assert len(violations or []) == 0, f"Accessibility violations found: {violations}"

@when(parse('I access the page {page}'))
def access_page(page, shared_data):
    attach_screenshot("user_should_be_logged_in")
    if page != "dashboard":
        navigate_to_url(page)
    else:
        shared_data["page"] = ""

@then(parse("the page {page} should be accessible"))
def page_should_be_accessible(page, shared_data):
    violations = get_accessibility_violations()
    assert len(violations or []) == 0, f"Accessibility violations found: {violations}"
