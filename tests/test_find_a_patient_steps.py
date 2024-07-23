from pytest_bdd import given, when, then, scenario, scenarios
from pytest_bdd.parsers import parse
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

scenarios(f'{features_directory}/find_a_patient.feature')
         
# @scenario(f'{features_directory}/find_a_patient.feature', 'Search for an NHS number with fewer than 10 characters')
# def test_search_for_nhs_number_with_fewer_than_10_chars():
#     pass

# @scenario(f'{features_directory}/find_a_patient.feature', 'Entering and then clearing the NHS Number shows an error to enter the NHS number')
# def test_enter_clear_nhs_number_error():
#     pass

def select_site_and_care_model(site, care_model):
  site = "ST JOHN'S HOUSE"
  care_model = "Vaccination Centre"
  select_site(site)
  select_care_model(care_model)
  click_continue_to_record_a_vaccination_homepage()
  if config["browser"] == "mobile":
      if check_navlink_bar_toggle_exists():
          click_navlinkbar_toggler()
  click_find_a_patient_nav_link()

@when("I click the find a patient navigation link")
def i_click_the_find_a_patient_nav_link():
    if config["browser"] == "mobile":
      if check_navlink_bar_toggle_exists():
            click_navlinkbar_toggler()
    click_find_a_patient_nav_link()

@given('I am on the PDS search page')
def given_im_on_pds_search_page(login_and_navigate_to_find_a_patient):
  pass

@given('I am on the find a patient by nhs number page')
def given_im_on_the_find_a_patient_by_nhs_number_page(navigate_and_login):
    select_site_and_care_model(site, care_model)
    click_search_by_nhs_number_link()

@given('I am on the find a patient by pds details page')
def given_im_on_the_find_a_patient_by_pds_details_page(navigate_and_login):
  select_site_and_care_model(site, care_model)
  click_search_by_demographics_link()

@when('I click the search button')
def i_click_the_search_button():
  click_search_for_patient_button()

@when('I click the find a patient navigation link')
def i_click_the_search_button():
  click_search_for_patient_button()

@given(parse('I enter nhs number {nhsNumber}'))
def step_i_enter_nhs_number(nhsNumber):
    enter_nhs_number(nhsNumber)

@when('I clear the nhs number')
def step_i_clear_the_nhs_number_input_field():
    enter_nhs_number('')

@then(parse('I can see an nhs number error message {errorMessage}'))
def error_message_appears_for_nhs_number(errorMessage):
  attach_screenshot("error_message_appears_for_nhs_number")
  assert errorMessage in get_nhs_number_error_message_text()

@then('the alert messages should appear for first name, surname, and date of birth')
def the_alert_messages_should_appear_forename_surname_dob_gender_postcode():
  attach_screenshot("alert_messages_should_appear_for_missing_fields")
  assert "Enter the first name" in get_first_name_error_message_text()
  assert "Enter the last name" in get_last_name_error_message_text()
  assert "Enter the date of birth" in get_dob_error_message_text()

@then(parse("I should be directed to the patient's information page and show {name}, {nhsNumber}, {dateofbirth} and {address} details"))
def patient_information_page_should_be_available(name, nhsNumber, dateofbirth, address):
    attach_screenshot("patient_information_page_should_be_visible")
    if name.lower() != "Not found".lower():
      assert check_patient_nhs_number_search_result_exists(nhsNumber, True) == True
      assert check_patient_name_search_result_exists(name, True) == True
      assert check_patient_dob_search_result_exists(dateofbirth, True) == True
      assert check_patient_address_search_result_exists(address, True) == True
    else:
       assert check_patient_not_found_message_exists(format_nhs_number(nhsNumber), True) == True
       assert check_create_new_patient_button_exists(True) == True
