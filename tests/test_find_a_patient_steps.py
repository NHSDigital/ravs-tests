from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.find_a_patient_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    return {}

@scenario(f'{features_directory}/find_a_patient.feature', 'Find a patient page should launch')
def test_find_a_patient_page_should_launch(site, care_model, navigate_and_login):
    pass

@scenario(f'{features_directory}/find_a_patient.feature', 'Search by NHS number')
def test_search_by_nhs_number():
    pass

@scenario(f'{features_directory}/find_a_patient.feature', 'Search without entering nhs number')
def test_search_without_entering_nhs_number():
    pass

@scenario(f'{features_directory}/find_a_patient.feature', 'Search without entering patient details')
def test_search_without_entering_patient_details():
    pass

@given("I am logged into the RAVS app")
def logged_into_ravs_app(site, care_model):
    set_vaccinator_location(site, care_model)

@when("I click the find a patient navigation link")
def i_click_the_find_a_patient_nav_link():
    if config["browser"] == "mobile":
      if check_navlink_bar_toggle_exists():
            click_navlinkbar_toggler()
    click_find_a_patient_nav_link()

@then('the find a patient page should be displayed')
def the_pds_search_section_should_be_displayed():
    attach_screenshot("find_a_patient_page_should_be_displayed")
    assert check_search_for_patient_button_visible()

@given('I am on the PDS search page')
def given_im_on_pds_search_page(login_and_navigate_to_find_a_patient):
  pass

@given('I am on the find a patient by nhs number page')
def given_im_on_the_find_a_patient_by_nhs_number_page(navigate_and_login):
    site = "ST JOHN'S HOUSE"
    care_model = "Vaccination Centre"
    select_site(site)
    select_care_model(care_model)
    click_continue_to_record_a_vaccination_homepage()
    if config["browser"] == "mobile":
        if check_navlink_bar_toggle_exists():
            click_navlinkbar_toggler()
    click_find_a_patient_nav_link()

@given('I am on the find a patient by pds details page')
def given_im_on_the_find_a_patient_by_pds_details_page(navigate_and_login):
  site = "ST JOHN'S HOUSE"
  care_model = "Vaccination Centre"
  select_site(site)
  select_care_model(care_model)
  click_continue_to_record_a_vaccination_homepage()
  if config["browser"] == "mobile":
      if check_navlink_bar_toggle_exists():
          click_navlinkbar_toggler()
  click_find_a_patient_nav_link()
  click_search_by_pds_tab()

@when('I click the search button')
def i_click_the_search_button():
  click_search_for_patient_button()

@when('I click the find a patient navigation link')
def i_click_the_search_button():
  click_search_for_patient_button()

@when(parse('I enter a valid {nhsNumber}'))
def i_enter_valid_nhs_number(nhsNumber, shared_data):
    enter_NHSNumber(nhsNumber)

@then('the alert message should appear for nhs number')
def the_alert_messages_should_appear_nhs_number():
  attach_screenshot("required_alerts_should_appear_for_nhsNumber")
#   assert check_required_field_error_appears_for_nhsNumber(False) == True

@then('the alert messages should appear for Forename, Surname, Date Of Birth, Gender and Postcode')
def the_alert_messages_should_appear_forename_surname_dob_gender_postcode():
  attach_screenshot("alert_messages_should_appear_for_missing_fields")
  assert check_required_field_error_appears_for_forename(False) == True
  assert check_required_field_error_appears_for_surname(False) == True
  assert check_required_field_error_appears_for_dob(False) == True

@then(parse("I should be directed to the patient's information page and show {name}, {nhsNumber}, {dateofbirth} and {address} details"))
def patient_information_page_should_be_available(name, nhsNumber, dateofbirth, address):
    attach_screenshot("patient_information_page_should_be_visible")
    if name.lower() != "Not found".lower():
      assert check_patient_nhsnumber_search_result_exists(nhsNumber, True) == True
      assert check_patient_name_search_result_exists(name, True) == True
      assert check_patient_dob_search_result_exists(dateofbirth, True) == True
      assert check_patient_address_search_result_exists(address, True) == True
    else:
       assert check_patient_not_found_message_exists(format_nhs_number(nhsNumber), True) == True
       assert check_create_new_patient_button_exists(True) == True
