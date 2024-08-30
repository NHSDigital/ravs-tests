from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.add_vaccines_page import *
from pages.settings_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.vaccines_add_batch_page import *
from pages.vaccines_choose_site_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def shared_data():
    return {}

@scenario(f"{features_directory}/add_batches.feature", "Add vaccine batches page should launch")
def test_add_vaccine_batches_page_should_launch(site, care_model, navigate_and_login):
    pass

@scenario(f"{features_directory}/add_batches.feature", "Add batch to vaccine")
def test_batch_already_added_to_site_warning_should_appear():
    pass

@given("I am logged into the RAVS app")
def logged_into_ravs_app(site, care_model):
    # set_vaccinator_location(site, care_model)
    pass

@given("I am on the RAVS home page")
def logged_into_homepage(login_and_navigate_to_homepage):
    pass

@when("I am on the vaccines page")
def i_am_on_the_vaccines_page():
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_vaccines_nav_link()

@when("I click add batch link")
def i_click_add_batch_link():
    click_add_batch_link()

@when(parse("I select {site}, {vaccine}, {vaccinetype} and enter {batchprefix}, {batchsuffix}"))
def i_select_site_vaccine_and_vaccinetype_for_batch(site, vaccine, vaccinetype, batchprefix, batchsuffix, shared_data):
    click_site_radio_button(site)
    if "covid" in vaccine.lower():
        click_covid_vaccine_radiobutton()
        click_covid_vaccine_type_radiobutton_on_add_batches_page(vaccinetype)
    elif "flu" in vaccine.lower():
        click_flu_vaccine_radiobutton()
        click_flu_vaccine_type_radiobutton_on_add_batches_page(vaccinetype)
    shared_data["site"] = site
    shared_data["vaccine"] = vaccine
    shared_data["vaccinetype"] = vaccinetype
    if "covid" in shared_data["vaccine"].lower():
        enter_covid_batch_number_prefix(batchprefix)
        enter_covid_batch_number_suffix(batchsuffix)
    elif "flu" in shared_data["vaccine"].lower():
        enter_flu_batch_number(batchprefix)
    attach_screenshot("entered_batch_number")

@when(parse("I enter {batch_number}"))
def i_enter_batchprefix_and_batchsuffix(batch_number):
    click_add_batch_link()
    enter_batch_number_prefix_and_suffix(batch_number)
    attach_screenshot("entered_batch_number")

# @when(parse("I enter {expirydate}"))
# def i_enter_expiryDate(expirydate, shared_data):
#     expirydate = format_date(str(get_date_value(expirydate)), config["browser"])
#     enter_expiry_date(expirydate)
#     shared_data["expiryDate"] = expirydate
#     attach_screenshot("entered_expiry_date")

@when("I click Add batch button")
def i_click_add_batch_button():
    click_add_batch_button()
    attach_screenshot("clicked_add_batch_button")

@when("I click confirm choices button")
def i_click_confirm_choices_button():
    click_confirm_vaccine_batch_choices_button()
    attach_screenshot("clicked_confirm_choices_button")

@when("I click confirm button")
def i_click_confirm_button():
    click_confirm_button()
    attach_screenshot("clicked_confirm_choices_button")

@then("the batch is already added to site warning should appear")
def batch_already_added_warning_should_exist():
    attach_screenshot("batch_already_added_warning_message_exists")
    assert check_batch_already_exists_error_is_displayed() == True

@then("the add batch page should be launched")
def add_batch_page_should_launch():
    attach_screenshot("add_batch_page_should_launch")
    assert check_add_batch_title_exists(True) == True

@when(parse("I view product for the {vaccine_type} on {site}"))
def view_product_for_site_and_vaccine_type(vaccine_type, site):
    click_view_product(site, vaccine_type)
