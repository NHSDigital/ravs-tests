import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.add_vaccines_page import *
from pages.settings_page import *
from pages.site_vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.check_and_confirm_vaccinated_record_page import *
from pages.patient_details_page import *
from pages.delete_vaccination_page import *
import logging
from init_helpers import *
from conftest import *
from helpers.datetimeHelper import *

features_directory = get_working_directory() + "features"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope='function')
def shared_data():
    data = {}

    yield data
    data.clear()

@scenario(f'{features_directory}/record_a_vaccine_for_patient_with_nhs_number.feature', 'Record a vaccine with nhs number')
def test_record_a_vaccine_with_nhs_number(navigate_and_login):
    pass

@given(parse("I login to RAVS and get patient details from {data_file}"))
def step_login_to_ravs(data_file, shared_data):
    file_path = os.path.join(get_working_directory(), "tests", "test_data", data_file)
    with open(file_path, 'r') as file:
        loaded_data = json.load(file)
        shared_data.update(copy.deepcopy(loaded_data))
    return shared_data

@given("set the vaccinator details")
def step_set_vaccinator_details(shared_data):
    select_site(shared_data["vaccinator_site"])
    select_care_model(shared_data.get("vaccinator_care_model"))
    click_continue_to_record_a_vaccination_homepage()

@given("I search for a patient with the NHS number in the find a patient screen")
def step_search_for_patient(shared_data):
    nhs_number = shared_data["nhs_number"]
    click_find_a_patient_and_search_with_nhsnumber(nhs_number)

@given("I open the patient record and click choose vaccine button")
def step_search_for_patient(shared_data):
    chosen_vaccine = shared_data["chosen_vaccine"]
    immunisation_history_records_count_before_vaccination = click_on_patient_search_result_and_click_choose_vaccine(shared_data['patient_name'], chosen_vaccine)
    shared_data["immunisation_history_records_count_before_vaccination"] = immunisation_history_records_count_before_vaccination

@when("I choose the vaccine and vaccine type and click continue")
def step_choose_vaccine_and_vaccine_type(shared_data):
    choose_vaccine_and_vaccine_type_for_patient(shared_data['chosen_vaccine'], shared_data['chosen_vaccine_type'])

@when("I assess the patient's eligibility with the details and click continue to record consent screen button")
def step_assess_eligibility_and_click_continue_record_consent_screen(shared_data):
    patient_eligible_decision = shared_data['eligible_decision']
    patient_eligibility_type = shared_data['eligibility_type']
    patient_eligibility_assessing_clinician = shared_data['eligibility_assessing_clinician']
    patient_eligibility_assessment_date = format_date(str(get_date_value(shared_data['eligibility_assessment_date'])), config["browser"])
    shared_data['eligibility_assessment_date'] = patient_eligibility_assessment_date
    patient_eligibility_assessment_outcome=shared_data['eligibility_assessment_outcome']
    patient_eligibility_assessment_no_vaccine_given_reason = shared_data['eligibility_assessment_no_vaccine_given_reason']
    patient_eligibility_assessment_comments = shared_data['assessment_comments']
    assess_patient_with_details_and_click_continue_to_consent(patient_eligible_decision, patient_eligibility_type, patient_eligibility_assessing_clinician, patient_eligibility_assessment_date, patient_eligibility_assessment_outcome, patient_eligibility_assessment_comments,patient_eligibility_assessment_no_vaccine_given_reason)

@when("I record consent with the details and click continue to vaccinate button")
def step_record_consent_and_click_continue_to_vaccinate_screen(shared_data):
    if shared_data["eligibility_assessment_outcome"].lower() == "Give vaccine".lower():
        patient_consent_decision = shared_data['consent_decision']
        patient_consent_given_by = shared_data['consent_given_by']
        name_of_person_consenting = shared_data['name_of_person_consenting']
        relationship_to_patient = shared_data['relationship_to_patient']
        consent_clinician_details= shared_data['consent_clinician_details']
        no_consent_reason = shared_data["no_consent_reason"]
        record_consent_details_and_click_continue_to_vaccinate(patient_consent_decision,patient_consent_given_by, name_of_person_consenting, relationship_to_patient, consent_clinician_details, no_consent_reason)

@when("I enter vaccination details and click Continue to Check and confirm screen")
def step_enter_vaccination_details_and_continue_to_check_and_confirm_screen(shared_data):
    if shared_data["consent_decision"].lower() == "Yes".lower():
        vaccinated_decision = shared_data["vaccinated_decision"]
        vaccinated_date = format_date(str(get_date_value(shared_data["vaccination_date"])), config["browser"])
        shared_data["vaccination_date"] = vaccinated_date
        chosen_vaccine = shared_data["chosen_vaccine"]
        vaccinated_type2 = shared_data["vaccine_type2"]
        vaccination_route = shared_data["vaccination_route"]
        batch_number = shared_data["batch_number"]
        batch_number_to_select = shared_data["batch_number_to_select"]
        batch_expiry_date = shared_data["batch_expiry_date"]
        dose_amount = shared_data["dose_amount"]
        prescribing_method = shared_data["prescribing_method"]
        vaccinator = shared_data["vaccinator"]
        vaccination_comments = shared_data["vaccination_comments"]
        no_vaccination_reason = shared_data["no_vaccination_reason"]
        enter_vaccine_details_and_click_continue_to_check_and_confirm(vaccinated_decision, vaccinated_date, chosen_vaccine, vaccinated_type2, vaccination_route, batch_number, batch_number_to_select, batch_expiry_date, dose_amount, prescribing_method, vaccinator, vaccination_comments, no_vaccination_reason)
        attach_screenshot("entered_vaccination_details")

@then("I need to be able to see the patient details on the check and confirm screen")
def step_see_patient_details_on_check_and_confirm_screen(shared_data):
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower():
        attach_screenshot("check_and_confirm_screen_before_assertion")
        assert get_patient_name_value() == shared_data["patient_name"]
        assert get_patient_address_value() == shared_data["address"]
        assert get_patient_vaccination_dose_amount_value() == shared_data["dose_amount"]
        assert get_patient_vaccine_type_chosen_vaccine_value() == shared_data["chosen_vaccine_type"]
        assert get_patient_vaccinated_chosen_vaccine_value() == shared_data["vaccine_type2"]
        assert standardize_date_format(get_patient_eligibility_assessment_date_value()) == shared_data['eligibility_assessment_date']
        assert standardize_date_format(get_patient_vaccinated_date_value()) == shared_data['vaccination_date']
        assert shared_data["date_of_birth"] in get_patient_dob_value()
        attach_screenshot("check_and_confirm_screen_after_assertion")

@then("when I click confirm and save button, the immunisation history of the patient should be updated in the patient details page")
def click_confirm_and_save_button_immunisation_history_should_be_updated(shared_data):
    attach_screenshot("patient_details_screen_with_immunisation_history")
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower():
        click_confirm_details_and_save_button()
        if "covid" in shared_data["chosen_vaccine"].lower():
            index = 1
        else:
            index = 2

        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
        assert get_vaccine_program_details(index) == shared_data["chosen_vaccine"]
        assert standardize_date_format(get_vaccine_date_details(index)) == standardize_date_format(shared_data["vaccination_date"])
        click_delete_history_button(shared_data["chosen_vaccine"])
        attach_screenshot("delete_history_button_clicked")
        click_delete_vaccination_button()
        attach_screenshot("delete_vaccination_button_clicked")
        time.sleep(10)
        shared_data.clear()
    else:
        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) == int(shared_data["immunisation_history_records_count_before_vaccination"])
        shared_data.clear()
