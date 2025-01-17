import warnings
from pytest_bdd import given, when, then, scenario, scenarios
from pytest_bdd.parsers import parse
from pages.vaccinator_location_page import *
from pages.find_a_patient_page import *
from pages.create_a_patient_page import *
from pages.confirm_page import *
import logging
from init_helpers import *
from conftest import *
from faker import Faker
import random

warnings.filterwarnings("ignore", category=UserWarning, module='faker')

features_directory = get_working_directory() + "features"
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

logging.getLogger('faker').setLevel(logging.CRITICAL)
logging.getLogger('faker.factory').setLevel(logging.CRITICAL)
logging.getLogger('faker.providers').setLevel(logging.CRITICAL)

fake = Faker('en_GB')

@scenario(f'{features_directory}/find_a_patient.feature', 'Find a patient page should launch')
def test_find_a_patient_page_should_launch(navigate_and_login):
    pass

scenarios(f'{features_directory}/find_a_patient.feature')

@given('I am on the find a patient by pds details page')
def given_im_on_the_find_a_patient_by_pds_details_page(navigate_and_login):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_find_a_patient_nav_link()
    click_search_by_demographics_link()

def step_select_site_and_care_model(site, care_model):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_find_a_patient_nav_link()

@when("I click the find a patient navigation link")
def step_i_click_the_find_a_patient_nav_link():
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_find_a_patient_nav_link()

@then('the alert message should appear for nhs number')
def the_alert_messages_should_appear_nhs_number():
    attach_screenshot("required_alerts_should_appear_for_nhsNumber")

@given("I am logged into the RAVS app")
def logged_into_ravs_app():
    pass

@given('I am on the PDS search page')
def step_given_im_on_pds_search_page(login_and_navigate_to_find_a_patient):
    pass

@given('I am on the find a patient by nhs number page')
def step_i_am_on_the_find_a_patient_by_nhs_number_page(login_and_navigate_to_find_a_patient):
    pass

@given('I am on the find a patient by demographics page')
def step_given_i_am_on_the_find_a_patient_by_demographics_page(login_and_navigate_to_find_a_patient):
    click_search_by_demographics_link()

@then('I am on the find a patient by local records page')
@given('I am on the find a patient by local records page')
def step_given_i_am_on_the_find_a_patient_by_local_records_page(login_and_navigate_to_find_a_patient):
    click_search_by_local_records_link()

@given('I click the find a patient by local records link')
@then('I click the find a patient by local records link')
def step_click_the_find_a_patient_by_local_records_link():
    click_search_by_local_records_link()
    attach_screenshot("clicked_search_by_local_records_link")

@given('I am on the create a new patient page')
def step_given_i_am_on_the_find_a_patient_by_local_records_page(login_and_navigate_to_find_a_patient):
    click_search_by_local_records_link()
    attach_screenshot("clicked_search_by_local_records_link")

@then('the find a patient page should be displayed')
def the_pds_search_section_should_be_displayed():
    attach_screenshot("find_a_patient_page_should_be_displayed")
    assert check_search_for_patient_button_visible()

@given('I click the search button')
@when('I click the search button')
def step_click_search_button():
    click_search_for_patient_button()
    attach_screenshot("clicked_search_for_patient_button")

@given('I click the create a new patient button')
@when('I click the create a new patient button')
def step_click_create_a_new_patient_button():
    click_create_a_new_patient_button()
    attach_screenshot("clicked_create_a_new_patient_button")

@when('I click the check and confirm button')
def step_click_check_and_confirm_button():
    click_check_and_confirm_button()
    attach_screenshot("clicked_check_and_confirm_button")

@when('I click the confirm and save button')
def step_click_confirm_and_save_button():
    click_confirm_and_save_button()
    attach_screenshot("clicked_confirm_and_save_button")

@when('I click the search button')
def step_i_click_the_search_button():
    click_search_for_patient_button()

@when(parse('I enter a valid {nhsNumber}'))
@given(parse('I enter {nhsNumber} as the nhs number'))
def step_i_enter_nhs_number(nhsNumber):
    enter_nhs_number(nhsNumber)

@given('I clear the nhs number')
def step_i_clear_the_nhs_number():
    enter_nhs_number('')

@then(parse('I can see an nhs number error message {errorMessage}'))
def step_error_message_appears_for_nhs_number(errorMessage):
    attach_screenshot("error_message_appears_for_nhs_number")
    assert check_nhs_number_error_message_text_exists(errorMessage) is True

@then('the alert messages should appear for Forename, Surname, Date Of Birth, Gender and Postcode')
def the_alert_messages_should_appear_forename_surname_dob_gender_postcode():
    attach_screenshot("alert_messages_should_appear_for_missing_fields")
    assert check_required_field_error_appears_for_forename(False) == True
    assert check_required_field_error_appears_for_surname(False) == True
    assert check_required_field_error_appears_for_dob(False) == True

@then('the alert messages should appear for first name, surname, and date of birth')
def step_the_alert_messages_should_appear_forename_surname_dob_gender_postcode():
    attach_screenshot("alert_messages_should_appear_for_missing_fields")
    assert check_first_name_error_message_text_exists() is True
    assert check_last_name_error_message_text_exists() is True
    assert check_dob_error_message_text_exists() is True

@then(parse('I can see a first name error message {errorMessage}'))
def step_error_message_appears_for_first_name(errorMessage):
    attach_screenshot("error_message_appears_for_first_name")
    assert check_first_name_error_message_text_exists() is True

@then(parse('I can see a last name error message {errorMessage}'))
def step_error_message_appears_for_last_name(errorMessage):
    attach_screenshot("error_message_appears_for_last_name")
    assert check_last_name_error_message_text_exists() is True

@then(parse('I can see a dob error message {errorMessage}'))
def step_error_message_appears_for_dob(errorMessage):
    attach_screenshot("error_message_appears_for_dob")
    assert check_dob_error_message_text_exists() is True

@then(parse('I can see a postcode error message {errorMessage}'))
def step_error_message_appears_for_postcode(errorMessage):
    attach_screenshot("error_message_appears_for_postcode")
    assert check_postcode_invalid_error_message_text_exists() is True

@then(parse("I can see the patient's information in the search results, showing their name: {name}, nhs number: {nhsNumber}, dob: {dob} and address: {address}"))
def step_patient_information_page_should_be_available(name, nhsNumber, dob, address):
    attach_screenshot("patient_information_page_should_be_visible")
    assert check_patient_nhs_number_search_result_exists(nhsNumber, True) == True
    assert check_patient_name_search_result_exists(name, True) == True
    assert check_patient_dob_search_result_exists(dob, True) == True
    assert check_patient_address_search_result_exists(address, True) == True

@then(parse("I should be directed to the patient's information page and show {name}, {nhsNumber}, {dob} and {address} details"))
def patient_information_page_should_be_available(name, nhsNumber, dob, address):
    attach_screenshot("patient_information_page_should_be_visible")
    if name.lower() != "Not found".lower():
        assert check_patient_nhs_number_search_result_exists(nhsNumber, True) == True
        assert check_patient_name_search_result_exists(name, True) == True
        assert check_patient_dob_search_result_exists(dob, True) == True
        assert check_patient_address_search_result_exists(address, True) == True
    else:
        assert check_patient_not_found_for_nhs_number_message_exists(format_nhs_number(nhsNumber), True) == True
        assert check_create_new_patient_button_exists(True) == True

@then("I can see the patient's local record in the search results")
def step_patient_information_page_should_be_available(shared_data):
    attach_screenshot("patient_local_record_should_be_visible")
    name = f'{shared_data["first_name"]} {shared_data["last_name"]}'
    dob = shared_data["dob"]
    postcode = shared_data["postcode"]

    assert check_patient_name_search_result_exists(name, True) == True
    assert check_patient_dob_search_result_exists(dob, True) == True
    assert check_patient_postcode_search_result_exists(postcode, True) == True

@then(parse("I can see a message that no results are found for the NHS number {nhsNumber}"))
def step_assert_no_results_found_for_nhs_number_message(nhsNumber):
    attach_screenshot("no_results_found_should_be_visible")
    assert check_patient_not_found_for_nhs_number_message_exists(format_nhs_number(nhsNumber), True) == True
    assert check_create_new_patient_button_exists(True) == True

@then("I can see a message that no results are found for the patient")
def step_assert_no_results_found_for_patient_message():
    attach_screenshot("no_results_found_should_be_visible")
    assert check_patient_not_found_message_exists(True) == True

@then("I can see a message that more than one result was found")
def step_assert_multiple_results_found_for_patient_message():
    attach_screenshot("multiple_results_found_should_be_visible")
    assert check_patient_multiple_results_found_message_exists(True) == True

@then("I can see an option to create a new patient")
def step_assert_create_new_patient_button_exists():
    attach_screenshot("check_create_new_patient_button_is_visible")
    assert check_create_new_patient_button_exists(True) == True

@given(parse("I enter the mandatory patient details {firstName}, {lastName}, and {dob}"))
def step_add_mandatory_patient_information(firstName, lastName, dob):
    enter_first_name(firstName)
    enter_last_name(lastName)
    enter_dob(dob)
    attach_screenshot("add_mandatory_patient_information")

@given(parse("I select the gender {gender}"))
def step_select_gender(gender):
    select_gender(gender)
    attach_screenshot("select_gender")

@given(parse("I enter the postcode {postcode}"))
@when(parse("I enter the postcode {postcode}"))
def step_enter_postcode(postcode):
    enter_optional_postcode(postcode)
    attach_screenshot("enter_invalid_postcode")

@given("I generate random data for a new patient")
def step_generate_random_patient_details(shared_data):

    gender = [
        "Female",
        "Male",
        "Other",
        "Unknown"
        ]

    shared_data["first_name"] = fake.first_name()
    shared_data["last_name"] = fake.last_name()
    shared_data["gender"] = random.choice(gender)
    shared_data["postcode"] = fake.postcode()
    dob = fake.date_of_birth()
    day, month, year = str(dob.day), str(dob.month), str(dob.year)
    dob_string = f"{day}/{month}/{year}"
    shared_data["dob"] = dob_string

@given("I enter the new patient details on find by demographics page")
def step_add_mandatory_patient_information(shared_data):
    enter_first_name(shared_data["first_name"])
    enter_last_name(shared_data["last_name"])
    select_optional_gender(shared_data["gender"])
    enter_optional_postcode(shared_data["postcode"])
    enter_dob(shared_data["dob"])
    attach_screenshot("add_mandatory_new_patient_information")

@when("I enter the new patient details")
@given("I enter the new patient details on create a new patient page")
@then("I enter the new patient details")
def step_add_mandatory_patient_information(shared_data):
    enter_first_name(shared_data["first_name"])
    enter_last_name(shared_data["last_name"])
    select_gender(shared_data["gender"])
    enter_postcode(shared_data["postcode"])
    enter_dob(shared_data["dob"])
    attach_screenshot("add_mandatory_new_patient_information")

@then("I can check and confirm the patient information is correct")
def step_patient_information_page_should_be_available(shared_data):
    attach_screenshot("patient_information_is_correct")
    assert shared_data["first_name"] in get_first_name_field_text()
    assert shared_data["last_name"] in get_last_name_field_text()
    assert shared_data["gender"] in get_gender_field_text()
    assert shared_data["postcode"] in get_postcode_field_text()
    assert shared_data["dob"] in get_date_of_birth_field_text()

@then("I can see the patient added confirmation message")
def step_patient_added_message_should_be_available(shared_data):
    patient_added_message = get_patient_added_message(shared_data["first_name"])
    attach_screenshot("patient_added_confirmation_message")
    assert f'{shared_data["first_name"]} {shared_data["last_name"]} with date of birth {shared_data["dob"]} has been added to RAVS' in patient_added_message
