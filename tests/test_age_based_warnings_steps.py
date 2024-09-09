from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.home_page import *
from pages.login_page import *
from pages.nhs_signin_page import *
import logging
from conftest import *
from init_helpers import *
from test_data.get_values_from_models import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/age_based_warnings.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    return {}

@given("I am logged into the RAVS app")
def given_I_login_to_the_ravs_web_app(login_and_navigate_to_homepage):
    pass

@when(parse('I search for the patient with NHS number {nhs_number}'))
def step_search_for_patient_with_nhs_number(nhs_number, shared_data):
    enter_nhs_number(nhs_number)
    shared_data["nhs_number"] = nhs_number
    click_search_for_patient_button()

@when(parse('I proceed to record a vaccine for {vaccine_type} for all products'))
def step_proceed_to_record_a_vaccine(vaccine_type, shared_data):
    click_patient_name_link()
    attach_screenshot("clicked_patient_name")
    click_choose_vaccine_button()
    shared_data["vaccine_type"] = vaccine_type

@then(parse('the system should display the warnings {expected_warning_count}'))
def step_warning_messages_should_be_displayed(expected_warning_count, shared_data):
    attach_screenshot("clicked_choose_vaccine_button")
    if shared_data['vaccine_type'] == 'covid':
        vaccine_name = get_vaccine_to_choose_from(0)
        shared_data['vaccine_type'] = vaccine_name
        click_vaccine_radiobutton(vaccine_name)
        warning_count = 0
        comirnaty_original_omicron_ba_age_above_12 = get_vaccination_type(0, vaccine_name)
        comirnaty_30_omicron_xbb_age_above_12 = get_vaccination_type(1, vaccine_name)
        comirnaty_3_omicron_xbb_age_above_6months_to_4 = get_vaccination_type(2, vaccine_name)
        comirnaty_10_omicron_xbb_age_above_5_to_11 = get_vaccination_type(3, vaccine_name)
        spikevax_xbb_age_above_18 = get_vaccination_type(4, vaccine_name)
        vaccine_types = [
        (comirnaty_original_omicron_ba_age_above_12, ["9732091169", "9692237893", "9474335761", "9474335761"]),
        (comirnaty_30_omicron_xbb_age_above_12, ["9732091169", "9692237893", "9474335761"]),
        (comirnaty_3_omicron_xbb_age_above_6months_to_4, ["9474335761", "9450153485", "9470472918", "9473673388"]),
        (comirnaty_10_omicron_xbb_age_above_5_to_11, ["9732091169", "9692237893", "9450153485", "9470472918", "9473673388"]),
        (spikevax_xbb_age_above_18, ["9732091169", "9692237893", "9474335761", "9450153485", "9470472918"]),
    ]

    for index, (vaccine, warning_nhs_numbers) in enumerate(vaccine_types):
        click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine)
        if shared_data["nhs_number"] in warning_nhs_numbers:
            assert check_age_based_warning_exists() is True
            warning_count += 1
        else:
            assert check_age_based_warning_exists() is False

    assert str(warning_count) == expected_warning_count

    warning_count = 0

    click_continue_to_assess_patient_button()
    shared_data["index"] = index
    shared_data['chosen_vaccine'] = shared_data['vaccine_type']
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = get_eligibility_type(shared_data["index"], shared_data['chosen_vaccine'])
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    shared_data['eligibility_assessing_clinician'] = get_assessing_clinician(shared_data["index"])
    assess_date = "today"
    assess_date = format_date(str(get_date_value(assess_date)), config["browser"])
    shared_data['eligibility_assessment_date'] = assess_date
    shared_data['eligibility_assessment_outcome'] = get_assessment_outcome(0)
    shared_data['eligibility_assessment_no_vaccine_given_reason'] = get_assess_vaccine_not_given_reason(shared_data["index"])
    shared_data['assessment_comments'] = "Assessment comments " + assess_date
    assess_patient_with_details_and_click_continue_to_consent("yes", shared_data['eligibility_type'], shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], None ,assess_date, shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'],shared_data['eligibility_assessment_no_vaccine_given_reason'])
    shared_data['consent_decision'] = "yes"
    shared_data['consent_given_by'] = get_consent_given_by(shared_data["index"])
    name_of_person_consenting = "Automation tester"
    relationship_to_patient = "RAVS tester"
    if shared_data['legal_mechanism'] == "Patient Group Directions (PGD)":
        shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']
    else:
        shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
    shared_data["no_consent_reason"] = get_no_consent_reason(shared_data["index"])
    record_consent_details_and_click_continue_to_vaccinate(shared_data['consent_decision'],shared_data['consent_given_by'], name_of_person_consenting, relationship_to_patient, shared_data['consent_clinician_details'], shared_data["no_consent_reason"])
    shared_data["vaccinated_decision"] = "yes"
    shared_data["vaccination_date"] = format_date(str(get_date_value("today")), config["browser"])
    chosen_vaccine = shared_data["chosen_vaccine"]
    shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
    shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine"]))
    if shared_data['legal_mechanism'] == "Patient Group Directions (PGD)":
        shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
    else:
        shared_data["vaccinator"] = get_vaccinator(shared_data["index"])
    shared_data["vaccination_comments"] = shared_data["chosen_vaccine"] + "vaccination given on " + shared_data["vaccination_date"]
    shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
    click_yes_vaccinated_radiobutton()
    for index, (vaccine, warning_nhs_numbers) in enumerate(vaccine_types):
        click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccine)
        if shared_data["nhs_number"] in warning_nhs_numbers:
            assert check_age_based_warning_exists() is True
            warning_count += 1
        else:
            assert check_age_based_warning_exists() is False

    assert str(warning_count) == expected_warning_count

