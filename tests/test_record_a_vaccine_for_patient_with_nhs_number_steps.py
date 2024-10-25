import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.settings_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.check_and_confirm_vaccinated_record_page import *
from pages.patient_details_page import *
from pages.delete_vaccination_page import *
import logging
from init_helpers import *
from conftest import *
from helpers.datetimeHelper import *
from test_data.get_values_from_models import *

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

@scenario(f'{features_directory}/record_a_vaccine_for_patient_with_nhs_number.feature', 'Record a maternity vaccine with nhs number')
def test_record_a_maternity_vaccine_with_nhs_number(navigate_and_login):
    pass

@given(parse("I login to RAVS and set vaccinator details with {site} and {care_model} and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date}"))
def step_login_to_ravs(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["care_model"] = get_care_model(index)

    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(site, chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date)
    return shared_data

@given("I search for a patient with the NHS number in the find a patient screen")
@then("I search for a patient with the NHS number in the find a patient screen")
def step_search_for_patient(shared_data):
    nhs_number = shared_data["nhs_number"]
    click_find_a_patient_and_search_with_nhs_number(nhs_number)

@given(parse("I open the patient record by clicking on patient {name}"))
@then(parse("I open the patient record by clicking on patient {name}"))
def step_search_for_patient(shared_data, name):
    attach_screenshot("before_clicking_patient_name")
    click_on_patient_name(name)
    shared_data["patient_name"] = name

@when(parse("I click choose vaccine button and choose the {chosen_vaccine}, {batch_number} with {batch_expiry_date} and click continue"))
def step_choose_vaccine_and_vaccine_type(shared_data, chosen_vaccine, batch_number, batch_expiry_date):
    # time.sleep(3)
    immunisation_history_records_count_before_vaccination = click_on_patient_search_result_and_click_choose_vaccine(shared_data['patient_name'], chosen_vaccine)
    shared_data["immunisation_history_records_count_before_vaccination"] = immunisation_history_records_count_before_vaccination
    choose_vaccine_and_vaccine_type_for_patient(shared_data['site'], chosen_vaccine, shared_data['chosen_vaccine_type'])

@when(parse("I assess the patient's {eligibility} with the details and date as {assess_date} and click continue to record consent screen button"))
def step_assess_eligibility_and_click_continue_record_consent_screen(shared_data, eligibility, assess_date):
    shared_data['eligible_decision'] = eligibility
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = get_eligibility_type(shared_data["index"], shared_data["chosen_vaccine"])
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    shared_data['eligibility_assessing_clinician'] = get_random_assessing_clinician()
    assess_date = format_date(str(get_date_value(assess_date)), config["browser"])
    shared_data['eligibility_assessment_date'] = assess_date
    shared_data['eligibility_assessment_outcome'] = get_assessment_outcome(0)
    shared_data['eligibility_assessment_no_vaccine_given_reason'] = get_assess_vaccine_not_given_reason(shared_data["index"])
    shared_data['assessment_comments'] = "Assessment comments " + assess_date + shared_data["patient_name"]
    assess_patient_with_details_and_click_continue_to_consent(eligibility, shared_data['eligibility_type'], shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], None, assess_date, shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'],shared_data['eligibility_assessment_no_vaccine_given_reason'])

@when(parse("I assess the pregnant patient's {eligibility} with the details and date as {assess_date} and click continue to record consent screen button"))
def step_assess_eligibility_and_click_continue_record_consent_screen(shared_data, eligibility, assess_date):
    shared_data['eligible_decision'] = eligibility
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = "Pregnancy"
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    shared_data['eligibility_assessing_clinician'] = get_random_assessing_clinician()
    due_date = format_date(str(get_date_value(assess_date)), config["browser"])
    shared_data['eligibility_due_date'] = due_date
    assess_date = format_date(str(get_date_value(assess_date)), config["browser"])
    shared_data['eligibility_assessment_date'] = assess_date
    shared_data['eligibility_assessment_outcome'] = get_assessment_outcome(0)
    shared_data['eligibility_assessment_no_vaccine_given_reason'] = get_assess_vaccine_not_given_reason(shared_data["index"])
    shared_data['assessment_comments'] = "Assessment comments " + assess_date + shared_data["patient_name"]
    assess_patient_with_details_and_click_continue_to_consent(eligibility, shared_data['eligibility_type'], shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], due_date, assess_date, shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'],shared_data['eligibility_assessment_no_vaccine_given_reason'])

@when(parse("I record {consent} with the details and click continue to vaccinate button"))
def step_record_consent_and_click_continue_to_vaccinate_screen(shared_data, consent):
    shared_data['consent_decision'] = consent
    if shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
        shared_data['consent_given_by'] = get_consent_given_by(shared_data["index"])
        name_of_person_consenting = "Automation tester"
        relationship_to_patient = "RAVS tester"
        if shared_data['legal_mechanism'] == "Patient Group Directions (PGD)":
            shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']
        else:
            shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
        shared_data["no_consent_reason"] = get_no_consent_reason(shared_data["index"])
        record_consent_details_and_click_continue_to_vaccinate(shared_data['consent_decision'],shared_data['consent_given_by'], name_of_person_consenting, relationship_to_patient, shared_data['consent_clinician_details'], shared_data['legal_mechanism'], shared_data["no_consent_reason"])

@when(parse("I record {vaccination} details and date as {vaccination_date} and click Continue to Check and confirm screen"))
def step_enter_vaccination_details_and_continue_to_check_and_confirm_screen(shared_data, vaccination, vaccination_date):
    shared_data["vaccinated_decision"] = vaccination
    if shared_data["consent_decision"].lower() == "yes":
        if shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
            shared_data["vaccination_date"] = format_date(str(get_date_value(vaccination_date)), config["browser"])
            chosen_vaccine = shared_data["chosen_vaccine"]
            shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
            shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine_type"]))
            if shared_data['legal_mechanism'] == "Patient Group Directions (PGD)":
                shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
            else:
                shared_data["vaccinator"] = get_vaccinator(shared_data["index"])
            shared_data["vaccination_comments"] = shared_data["chosen_vaccine_type"] + "vaccination given on " + shared_data["vaccination_date"] + " for " + shared_data["patient_name"]
            shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
            enter_vaccine_details_and_click_continue_to_check_and_confirm(shared_data["vaccinated_decision"], shared_data["care_model"], shared_data["vaccination_date"], chosen_vaccine, shared_data["chosen_vaccine_type"], shared_data["vaccination_site"], shared_data["batch_number"], shared_data["batch_expiry_date"], shared_data["dose_amount"], shared_data["vaccinator"], shared_data["vaccination_comments"], shared_data["no_vaccination_reason"])
            attach_screenshot("entered_vaccination_details")

@then(parse("I need to be able to see the patient {name}, {dob}, {address} and vaccination details on the check and confirm screen"))
def step_see_patient_details_on_check_and_confirm_screen(shared_data, name, dob, address):
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower() and shared_data["eligibility_assessment_outcome"].lower() == "Give vaccine".lower():
        attach_screenshot("check_and_confirm_screen_before_assertion")
        assert get_patient_name_value() == shared_data["patient_name"]
        assert get_patient_address_value() == address
        assert get_patient_vaccination_dose_amount_value() == shared_data["dose_amount"]
        assert get_patient_vaccinated_chosen_vaccine_value() == shared_data["chosen_vaccine"]
        assert get_patient_vaccinated_chosen_vaccine_product_value() == shared_data["chosen_vaccine_type"]
        assert get_patient_eligibility_assessment_date_value() == date_format_with_day_of_week(shared_data['eligibility_assessment_date'])
        assert get_patient_vaccinated_date_value() == date_format_with_day_of_week(shared_data['vaccination_date'])
        assert get_patient_dob_value() == date_format_with_age(dob)
        assert get_patient_vaccination_batch_expiry_date_value() == date_format_with_name_of_month(shared_data['batch_expiry_date'])
        assert get_patient_eligibility_assessing_clinician_vaccine_value() == shared_data['eligibility_assessing_clinician']
        assert get_patient_consent_recorded_by_clinician_value() == shared_data['consent_clinician_details']
        assert get_patient_vaccination_vaccinator_value() == shared_data['vaccinator']
        attach_screenshot("check_and_confirm_screen_after_assertion")

@then("when I click confirm and save button, I should see a record saved dialogue")
def click_confirm_and_save_button_record_saved(shared_data):
    attach_screenshot("patient_details_screen_with_immunisation_history")
    click_confirm_details_and_save_button()
    attach_screenshot("before_assert_record_saved")
    assert check_record_saved_element_exists(False)

@then("the immunisation history of the patient should be updated in the patient details page")
def immunisation_history_should_be_updated(shared_data):
    immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
    assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
    click_delete_history_link(shared_data["chosen_vaccine"])
    click_delete_vaccination_button()
    shared_data.clear()

@then("when I click confirm and save button, the immunisation history of the patient should be updated in the patient details page")
def click_confirm_and_save_button_immunisation_history_should_be_updated(shared_data):
    attach_screenshot("patient_details_screen_with_immunisation_history")
    if shared_data["vaccinated_decision"].lower() == "yes" and shared_data["consent_decision"].lower() == "yes" and shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
        click_confirm_details_and_save_button()

        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
        # assert get_vaccine_program_details(index) == shared_data["chosen_vaccine"]
        # click_delete_history_button(shared_data["chosen_vaccine"], index)
        # attach_screenshot("delete_history_button_clicked")
        # click_delete_vaccination_button()
        # attach_screenshot("delete_vaccination_button_clicked")
        # time.sleep(10)
        shared_data.clear()
    else:
        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) == int(shared_data["immunisation_history_records_count_before_vaccination"])
        shared_data.clear()

