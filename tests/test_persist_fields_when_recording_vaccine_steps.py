import copy
import json
from pytest import Parser
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.vaccinator_location_page import *
from pages.settings_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_page import *
from pages.choose_vaccines_page import *
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

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/persist_field_when_recording_a_vaccine.feature')

@when("I change the delivery team on the choose vaccine page")
def change_delivery_team_choose_vaccine(shared_data):
    click_delivery_team_radiobutton(shared_data["new_site"])
    assert get_selected_vaccine_radio_button_value_on_choose_vaccine_page() == shared_data["chosen_vaccine"]
    attach_screenshot("vaccine_selection_should_persist")
    assert str(get_selected_vaccine_product_radio_button_value_on_choose_vaccine_page()).replace("Active batches available", "").strip() == shared_data["chosen_vaccine_type"]
    attach_screenshot("vaccine_product_selection_should_persist")
    click_continue_to_assess_patient_button()
    get_is_patient_eligible_value_on_assessing_the_patient_page() == "Is patient eligible selection did not persist"
    attach_screenshot("assessment_patient_eligible_value_should_not_persist")

@when("I change the vaccination product on the choose vaccine page")
def change_vaccine_product_choose_vaccine(shared_data):
    click_vaccine_radiobutton(shared_data["chosen_vaccine_new"])
    assert get_selected_delivery_team_radio_button_value_on_choose_vaccine_page().lower() == shared_data["site"].lower()
    attach_screenshot("site_selection_should_persist")
    assert str(get_selected_vaccine_product_radio_button_value_on_choose_vaccine_page()).replace("Active batches available", "").strip() == "Vaccine product selection did not persist"
    attach_screenshot("vaccine_product_selection_should_not_persist")
    click_vaccine_type_radiobutton(shared_data["chosen_vaccine_type_new"])
    click_continue_to_assess_patient_button()
    get_is_patient_eligible_value_on_assessing_the_patient_page() == "Is patient eligible selection did not persist"
    attach_screenshot("assessment_patient_eligible_value_should_not_persist")

@when("I change the vaccination product type on the choose vaccine page")
def change_vaccine_product_choose_vaccine(shared_data):
    assert get_selected_delivery_team_radio_button_value_on_choose_vaccine_page().lower() == shared_data["site"].lower()
    attach_screenshot("site_selection_should_persist")
    assert get_selected_vaccine_radio_button_value_on_choose_vaccine_page() == shared_data["chosen_vaccine"]
    attach_screenshot("vaccine_product_selection_should_persist")
    assert str(get_selected_vaccine_product_radio_button_value_on_choose_vaccine_page()).replace("Active batches available", "").strip() == shared_data["chosen_vaccine_type"]
    attach_screenshot("vaccine_product_selection_should_persist")
    click_vaccine_type_radiobutton(shared_data["chosen_vaccine_type_new"])
    click_continue_to_assess_patient_button()
    get_is_patient_eligible_value_on_assessing_the_patient_page() == "Is patient eligible selection did not persist"
    attach_screenshot("assessment_patient_eligible_value_should_not_persist")

@then("the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must not persist on the assessment screen")
def consent_values_should_not_persist(shared_data):
    assert get_assessment_date_value() == ""
    attach_screenshot("assessment_date_value_did_not_persist")
    assert get_legal_mechanism_value_on_assessing_the_patient_page()== "Legal mechanism selection did not persist"
    attach_screenshot("legal_mechanism_value_did_not_persist")
    assert get_assessing_clinician_value_on_assessing_the_patient_page() == ""
    attach_screenshot("assessing_clinician_value_did_not_persist")
    assert get_assessment_outcome_value_on_assessing_the_patient_page() == "Assessment outcome selection did not persist"
    attach_screenshot("assessing_outcome_value_did_not_persist")
    eligibility_type = shared_data.get('eligibility_type_new', None) or shared_data['eligibility_type']
    assess_patient_with_details_and_click_continue_to_consent(shared_data['eligible_decision'], eligibility_type, shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], None, shared_data['eligibility_assessment_date'], shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'],shared_data['eligibility_assessment_no_vaccine_given_reason'])

@then("the patient's consent answer, consent given by, consenting clinician, selection must not persist on the consent screen")
def consent_values_must_not_persist(shared_data):
    assert get_patient_consent_value_on_consent_page() == "Patient consent selection did not persist"
    attach_screenshot("patient_consent_value_did_not_persist")
    if shared_data['legal_mechanism'] != "Patient Group Direction (PGD)":
        assert get_consenting_clinician_details_on_consent_page() == ""
    else:
        assert get_consenting_clinician_details_on_consent_page() == shared_data['eligibility_assessing_clinician']
    attach_screenshot("consent_clinician_value_did_not_persist")
    name_of_person_consenting = "Automation tester"
    relationship_to_patient = "RAVS tester"
    if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
        shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']
    else:
        if "Aspire pharmacy".lower() in shared_data["site"].lower():
            shared_data['consent_clinician_details'] = get_consenting_clinician_fhh39(shared_data["index"])
        else:
            shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
    shared_data["no_consent_reason"] = get_no_consent_reason(shared_data["index"])
    record_consent_details_and_click_continue_to_vaccinate(shared_data['consent_decision'],shared_data['consent_given_by'], name_of_person_consenting, relationship_to_patient, shared_data['consent_clinician_details'], shared_data['legal_mechanism'], shared_data["no_consent_reason"])

@then("the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should not persist")
def vaccinated_values_must_not_persist(shared_data):
    assert get_is_patient_vaccinated_value_on_vaccinated_page() == "Patient vaccinated value did not persist"
    attach_screenshot("patient_vaccinated_value_should_not_persist")
    assert get_vaccination_date() == ""
    attach_screenshot("vaccinated_date_value_did_not_persist")
    assert get_vaccination_care_model_value_on_vaccinated_page() == "Care model value did not persist"
    attach_screenshot("care_model_value_did_not_persist")
    if shared_data['legal_mechanism'] != "Patient Group Direction (PGD)":
        assert get_vaccinator_value_on_vaccinated_page() == ""
    else:
        assert get_vaccinator_value_on_vaccinated_page() == shared_data['vaccinator']
    attach_screenshot("vaccinator_value_did_not_persist")
