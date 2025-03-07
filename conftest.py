from faker import Faker
import pytest
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.check_and_confirm_vaccinated_record_page import *
from pages.confirm_page import *
from pages.create_a_patient_page import *
from pages.delete_vaccination_page import *
from pages.settings_page import *
from pages.site_vaccine_batches_page import *
from pages.vaccines_page import *
from pages.site_vaccine_batches_confirm_page import *
from pages.site_vaccines_check_and_confirm_page import *
from pages.home_page import *
from pages.login_page import *
from pages.nhs_signin_page import *
from pages.appointments_page import *
from pages.patient_details_page import *
from pages.find_a_patient_page import *
from pages.choose_vaccines_page import *
from pages.assess_patient_page import *
from pages.vaccinator_location_page import *
from pages.record_consent_page import *
from pages.record_vaccinated_page import *
from pages.vaccines_choose_site_page import *
from pages.vaccines_choose_vaccine_page import *
from pages.site_vaccines_add_batch_page import *
from pages.vaccines_view_products_page import *
from pages.select_organization import *
from init_helpers import *
from datetime import datetime, timedelta
from allure_commons.types import LabelType
import logging
from test_data.get_values_from_models import *

fake = Faker('en_GB')

@pytest.fixture(scope='function', autouse=True)
def report_browser_version(request):
    browser_version = get_browser_version()
    allure.dynamic.label(LabelType.TAG, browser_version)
    if config["browser"] == "mobile":
        logging.info(config["browser"].upper() + f" browser version for " + config["device"] + f" is : {browser_version}")
    else:
        logging.info(config["browser"].upper() + f" browser version is : {browser_version}")

def format_nhs_number(nhs_number):
    # Use regular expressions to insert spaces in the phone number
    formatted_number = re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1 \2 \3", nhs_number)
    return formatted_number

# Fixture for site parameter
@pytest.fixture(params=["NEELIMA HOUSE", "ALBERT HOUSE", "ST JOHN'S HOUSE"])
def site(request):
    return request.param

# Fixture for care_model parameter
@pytest.fixture(params=["Vaccination Centre", "Hospital Hub", "Care Home", "Home Of Housebound Patient", "Off-site Outreach Event", "Community pharmacy"])
def care_model(request):
    return request.param

# Fixture for covid vaccination types parameter
@pytest.fixture(params=["Comirnaty Original/Omicron BA.4-5", "Comirnaty 30 Omicron XBB.1.5", "Comirnaty 3 Omicron XBB.1.5", "Comirnaty 10 Omicron XBB.1.5", "Spikevax XBB.1.5"])
def covid_vaccine_type(request):
    return request.param

# Fixture for navigating and logging in
@pytest.fixture(scope='function')
def navigate_and_login(request, navigate_to_ravs):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    click_login_button()
    emailAddress = "neelima.guntupalli1@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()

def navigate_and_login_as_community_pharmacist(site):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
            attach_screenshot("clicked_navbar_toggler")
    if check_logout_button_exists_without_waiting():
        click_logout_button()
        attach_screenshot("clicked_logout_button")
    url = get_app_url(config["test_environment"])
    navigate_to_ravs_login_page(url)
    attach_screenshot("navigated_to_ravs_login_page")
    click_login_button()
    if site.lower() == "Leeds pharmacy".lower():
        emailAddress = "neelima.guntupalli1+community_pharmacy@nhs.net"
    elif "Aspire pharmacy".lower()  or "fhh39".lower() in site.lower():
        emailAddress = "neelima.guntupalli1+fhh39@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()

# Fixture for navigating and logging in
@pytest.fixture(scope='function')
def navigate_and_login_as_recorder(request, navigate_to_ravs):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    click_login_button()
    emailAddress = "neelima.guntupalli1+recorder_automated@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()
    select_site("Leeds Pharmacy")
    click_continue_to_home_page_button()

# Fixture for navigating and logging in as administrator
@pytest.fixture(scope='function')
def navigate_and_login_as_administrator(request, navigate_to_ravs):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    click_login_button()
    emailAddress = "neelima.guntupalli1+admin_automated@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()
    select_site("Leeds Pharmacy")
    click_continue_to_home_page_button()

# Fixture for navigating and logging in as lead administrator
@pytest.fixture(scope='function')
def navigate_and_login_as_lead_administrator(request, navigate_to_ravs):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    click_login_button()
    emailAddress = "neelima.guntupalli1@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()

# Fixture for navigating to RAVS
@pytest.fixture(scope='function')
def navigate_to_ravs(request):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
            attach_screenshot("clicked_navbar_toggler")
    if check_logout_button_exists_without_waiting():
        click_logout_button()
        attach_screenshot("clicked_logout_button")
    url = get_app_url(config["test_environment"])
    navigate_to_ravs_login_page(url)
    attach_screenshot("navigated_to_ravs_login_page")
    return True

# Fixture for logging in and navigating to find a patient
@pytest.fixture(scope='function')
def login_and_navigate_to_find_a_patient(request, navigate_to_ravs):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    click_login_button()
    emailAddress = "neelima.guntupalli1@nhs.net"
    enter_email_address(emailAddress)
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    click_nhs_signin_button()
    click_find_a_patient_nav_link()

# Fixture for logging in and finding a patient by NHS number
@pytest.fixture(scope='function')
def login_and_find_a_patient_by_nhs_number(request, login_and_navigate_to_find_a_patient, nhs_number):
    enter_nhs_number(nhs_number)
    click_search_for_patient_button()

# Fixture for navigating to appointments open first patient and clicking choose vaccine
@pytest.fixture(scope='function')
def goto_appointments_open_first_patient_and_click_choose_vaccine(request, login_and_navigate_to_appointments_open_first_patient):
    click_choose_vaccine_button()

# Fixture for logging out
@pytest.fixture(scope='function')
def logout(request, navigate_and_login):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists():
            click_navbar_toggler()
            attach_screenshot("clicked_navbar_toggler")
    click_logout_button()
    attach_screenshot("clicked_log_out_button")

def click_find_a_patient_and_search_with_nhs_number(nhs_number):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_find_a_patient_nav_link()
    enter_nhs_number(nhs_number)
    click_search_for_patient_button()
    attach_screenshot("entered_nhs_number_as" + nhs_number + "_and_clicked_search_for_patient_button")

def click_find_a_patient_top_nav_bar():
    click_find_a_patient_nav_link()
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_manage_users_top_nav_bar():
    click_manage_users_nav_link()
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_on_patient_search_result_and_click_choose_vaccine(name, vaccine):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    immunisation_history_records = get_count_of_immunisation_history_records(vaccine)
    attach_screenshot("immunisation_history_records_count_is_" + str(immunisation_history_records))
    click_choose_vaccine_button()
    attach_screenshot("clicked_choose_vaccine_button")
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    attach_screenshot("clicked_on_patient_" + name + "_and_clicked_choose_vaccine_button")
    return immunisation_history_records

def choose_vaccine_and_vaccine_type_for_patient(site, vaccine, vaccine_type):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    click_delivery_team_radiobutton(site)
    attach_screenshot("clicked_delivery_team")
    click_vaccine_radiobutton(vaccine)
    attach_screenshot("clicked_vaccine")
    click_vaccine_type_radiobutton(vaccine_type)
    attach_screenshot("clicked_vaccine_type")
    click_continue_to_assess_patient_button()
    attach_screenshot("selected_vaccine_" + vaccine + "_and_" + vaccine_type + "_and_clicked_continue_button")

def choose_vaccine_and_vaccine_type_only(site, vaccine, vaccine_type):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    click_delivery_team_radiobutton(site)
    attach_screenshot("clicked_delivery_team")
    click_vaccine_radiobutton(vaccine)
    attach_screenshot("clicked_vaccine")
    click_vaccine_type_radiobutton(vaccine_type)
    attach_screenshot("selected_vaccine_" + vaccine + "_and_" + vaccine_type)

def check_vaccine_and_batch_exists_in_site_api_request(site, vaccine, vaccineType, batch_number, expirydate):
    pass

@given("I am logged into the RAVS app")
def logged_into_ravs_app(navigate_and_login):
    pass

def check_vaccine_and_batch_exists_in_community_pharmacy(site, vaccine, vaccine_type, batch_number, expiry_date, pack_size):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()

    click_vaccines_nav_link()
    attach_screenshot("clicked_vaccines_nav_link")
    check_site_vaccine_type_has_active_batch(site, vaccine, vaccine_type, batch_number, expiry_date, pack_size)

def check_vaccine_and_batch_exists_in_site(shared_data, site, vaccine, vaccine_type, batch_number, expiry_date, pack_size=None):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
    click_vaccines_nav_link()
    attach_screenshot("clicked_vaccines_nav_link")
    time.sleep(1)
    check_site_vaccine_type_has_active_batch(shared_data, site, vaccine, vaccine_type, batch_number, expiry_date, pack_size)

def check_site_vaccine_type_has_active_batch(shared_data, site, vaccine, vaccine_type, batch_number, expiry_date, pack_size=None):
    # If the site does NOT currently have the vaccine, then add a site vaccine
    # Adding a vaccine also adds a vaccine type and an active batch, so we don't need to do further checks

    exists = check_vaccine_batch_exists_with_same_number_and_expiry_date_and_is_active(site, vaccine, vaccine_type, batch_number, expiry_date)
    if not exists:
    # if not check_vaccine_has_been_added(site, vaccine, True):
        click_vaccines_nav_link()
        add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date, pack_size)
        return True
    elif "pharmacy" in site.lower():
            if shared_data["chosen_vaccine"].lower() == "covid-19" or shared_data["chosen_vaccine"].lower() == "flu":
                pack_size = shared_data["pack_size"]
                shared_data['pack_size'] = get_pack_size_value_vaccines_page(batch_number, expiry_date, pack_size)
                attach_screenshot("pack_size_pharmacy")
    elif not check_batch_number_is_active_with_date(batch_number, expiry_date, True):
        click_reactivate_batch_link(batch_number)
        click_reactivate_batch_confirmation_button()

    return True

    # # If the site has the vaccine, but does NOT currently have the vaccine type, then add a site vaccine
    # # Adding a vaccine type is the same process as adding a vaccine for a site
    # if not check_vaccine_type_has_been_added(site, vaccine, vaccine_type, False):
    #     add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date, pack_size)
    #     return True

    # Open the vaccine type to see the batches.
    # If the batch does NOT currently exist, add a batch
    # This adds an active batch, so we don't need to do further checks
    # click_view_product(site, vaccine_type)
    # if not check_batch_number_and_expiry_date_exists(batch_number, expiry_date, True):
    #     add_vaccine_type_batch(batch_number, expiry_date)
    #     return True

    # If we get this far, the batch does exists but is currently INACTIVE
    # This reactivates the batch


def add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date, pack_size=None):
    # vaccines_page
    click_add_vaccine_button()
    attach_screenshot("clicked_add_vaccine_button")

    # vaccines_choose_site_page
    enter_site_name(site)
    attach_screenshot("entered_site_name")
    select_site_from_list(site)
    attach_screenshot("selected_site_from_list")
    click_continue_to_add_vaccine_button()
    attach_screenshot("clicked_continue_to_add_vaccine_button")

    # choose_vaccine_page
    click_vaccine_radiobutton_on_add_vaccine_screen(vaccine)
    attach_screenshot("clicked_vaccine_radiobutton_on_add_vaccine_screen")
    click_vaccine_type_radiobutton_on_add_vaccine_screen(vaccine_type)
    attach_screenshot("clicked_vaccine_type_radiobutton_on_add_vaccine_screen")
    click_continue_to_add_batch_button()
    attach_screenshot("clicked_continue_to_add_batch_button")

    # vaccines_add_batch_page
    enter_batch_number(batch_number)
    attach_screenshot("entered_batch_number")
    enter_expiry_date(expiry_date)
    attach_screenshot("entered_expiry_date")
    if pack_size is not None:
        select_pack_size(pack_size)
        attach_screenshot("selected_pack_size")
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_continue_to_confirm_batch_details_button")
    if not check_batch_already_exists_error_message_is_displayed():
        click_confirm_add_vaccine_and_batch_button()
        attach_screenshot("clicked_confirm_add_vaccine_and_batch_button")

def add_vaccine_type_batch(batch_number, expiry_date, pack_size = None):
    click_add_batch_link()
    attach_screenshot("clicked_add_batch_link")
    enter_batch_number(batch_number)
    attach_screenshot("entered_batch_number")
    enter_expiry_date(expiry_date)
    attach_screenshot("entered_expiry_date")
    if pack_size is not None:
        select_pack_size(pack_size)
        attach_screenshot("selected_pack_size")
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_continue_to_confirm_batch_details_button")
    click_confirm_add_vaccine_and_batch_button()
    attach_screenshot("clicked_confirm_add_vaccine_and_batch_button")

def assess_patient_with_details_and_click_continue_to_consent(eligible_decision, eligibility_type, staff_role, assessing_clinician, due_date, assessment_date, legal_mechanism, assessment_outcome, assessment_comments, eligibility_assessment_no_vaccine_given_reason=None):
    if eligible_decision.lower() == 'yes':
        click_eligible_yes_radiobutton()
        attach_screenshot("clicked_eligible_yes_radiobutton")

        if check_eligibility_type_is_enabled():
            select_eligibility_type(eligibility_type)
            attach_screenshot("selected_eligibility_type")

        if eligibility_type == "Healthcare workers":
            select_staff_role(staff_role)
            attach_screenshot("selected_staff_role")

        if eligibility_type == "Pregnancy" and due_date:
            enter_due_date(due_date)
            attach_screenshot("entered_due_date")

        attach_screenshot("clicked_eligibility_yes_and_selected_eligibility_type")
    else:
        click_eligible_no_radiobutton()
        attach_screenshot("clicked_patient_not_eligible_radiobutton")

    set_assessment_date(assessment_date)
    attach_screenshot("set_assessment_date")
    click_legal_mechanism(legal_mechanism)
    attach_screenshot("clicked_legal_mechanism")

    logging.debug("Assess clinician to select is: " + assessing_clinician)
    logging.debug("Assess legal mechanism is: " + legal_mechanism)

    select_assessing_clinician_with_name_and_council(assessing_clinician)
    attach_screenshot("selected_assessing_clinician_with_name_and_council")

    if assessment_outcome.lower() == "give vaccine":
        click_give_vaccine_radiobutton()
        attach_screenshot("clicked_patient_give_vaccine_radio_button")
    else:
        click_vaccine_not_given_radiobutton()
        attach_screenshot("clicked_vaccine_not_given_radiobutton")
        select_assessment_no_vaccination_reason(eligibility_assessment_no_vaccine_given_reason)
        attach_screenshot("selected_patient_not_given_reason_vaccine_after_assessing")
        click_save_and_return_button_on_assessment_screen()
        attach_screenshot("clicked_save_and_return_on_assessment_screen")

    enter_comments_for_assessing_patient(assessment_comments)
    attach_screenshot("entered_comments_for_assessing_patient")
    click_continue_to_record_consent_button()
    attach_screenshot("clicked_continue_to_record_consent_button")

def record_consent_details_and_click_continue_to_vaccinate(consent_decision,  consent_given_by, person_consenting_name, relationship_to_patient,  consent_clinician, legal_mechanism, no_consent_reason=None):
    attach_screenshot("before_selecting_consent_clinician")

    logging.debug("Consent clinician to select is: " + consent_clinician)
    logging.debug("Consent legal mechanism is: " + legal_mechanism)

    if (legal_mechanism) != "Patient Group Direction (PGD)":
        select_consent_clinician_with_name_and_council(consent_clinician)
        attach_screenshot("selected_consent_clinician_with_name_and_council")

    if consent_decision.lower() == 'yes':
        click_yes_to_consent()
        attach_screenshot("clicked_yes_to_consent")
        select_consent_given_by_from_dropdown(consent_given_by)
        attach_screenshot("selected_consent_given_by_from_dropdown")

        if consent_given_by != "Patient (informed consent)":
            enter_person_consenting_details(person_consenting_name)
            attach_screenshot("entered_person_consenting_details")
            enter_relationship_to_patient(relationship_to_patient)
            attach_screenshot("entered_relationship_to_patient")
        click_continue_to_vaccinate_button()
        attach_screenshot("clicked_continue_to_vaccinate_button")
    else:
        click_no_to_consent()
        attach_screenshot("clicked_no_to_consent")

        if no_consent_reason is not None:
            select_reason_for_no_consent(no_consent_reason)
            attach_screenshot("selected_reason_for_no_consent")

        attach_screenshot("patient_decided_to_not_consent")
        click_save_and_return_button_on_record_consent_page()
        attach_screenshot("patient_decided_to_not_consent_saved_and_returned")

def enter_vaccine_details_and_click_continue_to_check_and_confirm(vaccinate_decision, care_model, vaccination_date, vaccine, vaccine_type2, vaccination_site,  batch_number, batch_expiry_date, dose_amount, vaccinator, vaccination_comments, legal_mechanism, select_batch, no_vaccination_reason=None, pack_size=None):
    set_vaccination_date(vaccination_date)
    attach_screenshot("vaccination_date_is_set")
    logging.debug("Vaccination legal mechanism is: " + legal_mechanism)
    logging.debug("Vaccinator to select is: " + vaccinator)
    if (legal_mechanism) != "Patient Group Direction (PGD)":
        select_vaccinator_name_and_council(vaccinator)
        attach_screenshot("selected_vaccinator_name_and_council")
    enter_vaccination_comments(vaccination_comments)
    attach_screenshot("entered_vaccination_comments")
    click_care_model_option(care_model)
    attach_screenshot("clicked_care_model_option")
    if care_model == "Care home":
        enter_care_home_details("WHITESTONES CARE HOME")
        attach_screenshot("entered_care_home_details")
    if vaccinate_decision.lower() == 'yes':
        click_yes_vaccinated_radiobutton()
        attach_screenshot("clicked_yes_vaccinated_radiobutton")
        click_vaccine_type(vaccine_type2)
        attach_screenshot("clicked_vaccine_type")
        select_vaccination_site(vaccination_site)
        attach_screenshot("selected_vaccination_site")
        batch_number_to_select = batch_number.upper() + " - " + batch_expiry_date
        logging.debug("Batch number to select is: " + batch_number_to_select)
        if select_batch:
            select_batch_number(batch_number_to_select)
        attach_screenshot("selected_batch_number")
        assert get_dose_amount_value() == dose_amount
        if pack_size:
            assert get_pack_size_value() == pack_size
        attach_screenshot("entered_dose_amount_value")
        if click_continue_to_check_and_confirm_vaccination_screen_button() == True:
            attach_screenshot("vaccination_date_is_set")
            select_batch_number(batch_number_to_select)
            attach_screenshot("selected_batch_number")
            click_continue_to_check_and_confirm_vaccination_screen_button()
            attach_screenshot("clicked_continue_to_check_and_confirm_screen_button")
    else:
        click_not_vaccinated_radiobutton()
        attach_screenshot("clicked_not_vaccinated_radiobutton")
        if no_vaccination_reason is not None:
            select_reason_for_no_vaccination(no_vaccination_reason)
            attach_screenshot("selected_reason_for_no_vaccination")
            click_save_and_return_button_on_record_vaccinated_page()
            attach_screenshot("clicked_save_and_return_button_on_record_vaccinated_page")
        attach_screenshot("patient_decided_to_not_vaccinate_saved_and_returned")

def enter_vaccine_details_and_click_save_and_return(vaccinate_decision, care_model, vaccination_date, vaccine, vaccine_type2, vaccination_site,  batch_number, batch_expiry_date, dose_amount, vaccinator, vaccination_comments, legal_mechanism, no_vaccination_reason=None):
    set_vaccination_date(vaccination_date)
    attach_screenshot("vaccination_date_is_set")
    logging.debug("Vaccination legal mechanism is: " + legal_mechanism)
    logging.debug("Vaccinator to select is: " + vaccinator)
    if (legal_mechanism) != "Patient Group Direction (PGD)":
        select_vaccinator_name_and_council(vaccinator)
        attach_screenshot("selected_vaccinator_name_and_council")
    enter_vaccination_comments(vaccination_comments)
    attach_screenshot("entered_vaccination_comments")
    click_care_model_option(care_model)
    attach_screenshot("clicked_care_model_option")
    if care_model == "Care home":
        enter_care_home_details("WHITESTONES CARE HOME")
        attach_screenshot("entered_care_home_details")
    if vaccinate_decision.lower() == 'yes':
        click_yes_vaccinated_radiobutton()
        attach_screenshot("clicked_yes_vaccinated_radiobutton")
        click_vaccine_type(vaccine_type2)
        attach_screenshot("clicked_vaccine_type")
        select_vaccination_site(vaccination_site)
        attach_screenshot("selected_vaccination_site")
        batch_number_to_select = batch_number.upper() + " - " + batch_expiry_date
        logging.debug("Batch number to select is: " + batch_number_to_select)
        select_batch_number(batch_number_to_select)
        attach_screenshot("selected_batch_number")
        enter_dose_amount_value(dose_amount)
        attach_screenshot("entered_dose_amount_value")
        if click_continue_to_check_and_confirm_vaccination_screen_button() == True:
            attach_screenshot("vaccination_date_is_set")
            select_batch_number(batch_number_to_select)
            attach_screenshot("selected_batch_number")
            click_continue_to_check_and_confirm_vaccination_screen_button()
            attach_screenshot("clicked_continue_to_check_and_confirm_screen_button")
    else:
        click_not_vaccinated_radiobutton()
        attach_screenshot("clicked_not_vaccinated_radiobutton")
        if no_vaccination_reason is not None:
            select_reason_for_no_vaccination(no_vaccination_reason)
            attach_screenshot("selected_reason_for_no_vaccination")
            click_save_and_return_button_on_record_vaccinated_page()
            attach_screenshot("clicked_save_and_return_button_on_record_vaccinated_page")
        click_save_and_return_button_on_record_vaccinated_page()
        attach_screenshot("patient_decided_to_not_vaccinate_saved_and_returned")

def navigate_and_login_with_username(username):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
                click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
        attach_screenshot("clicked_logout_button")
    url = get_app_url(config["test_environment"])
    navigate_to_ravs_login_page(url)
    attach_screenshot("navigated_to_ravs_login_page")
    click_login_button()
    attach_screenshot("clicked_login_button")
    emailAddress = username
    enter_email_address(emailAddress)
    attach_screenshot("entered_email_address")
    password = config["credentials"]["ravs_password"]
    enter_password(password)
    attach_screenshot("entered_password")
    click_nhs_signin_button()
    attach_screenshot("clicked_nhs_signin_button")

@given(parse("I login to RAVS and set vaccinator details with {site} and {care_model} and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date}"))
def step_login_to_ravs(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["care_model"] = get_care_model(index)
    if "pharmacy" in site.lower():
        shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])
    else:
        shared_data["pack_size"] = None

    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, site, chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date)
    return shared_data

@given(parse("I login to RAVS and set vaccinator details with {site} and {care_model} and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date} and new delivery team {new_delivery_team}"))
def step_login_to_ravs_check_new_site_batch_exists(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, new_delivery_team, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["new_site"] = new_delivery_team
    shared_data["care_model"] = get_care_model(index)
    if "pharmacy" in site.lower():
        shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])
    else:
        shared_data["pack_size"] = None

    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, shared_data["new_site"], chosen_vaccine, shared_data["chosen_vaccine_type"], batch_number, batch_expiry_date)
    return shared_data

@given(parse("I login to RAVS and set vaccinator details with {site} and {care_model} and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date} and new vaccine product {new_vaccine_product}"))
def step_login_to_ravs_check_new_vaccine_product_batch_exist(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, new_vaccine_product, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["chosen_vaccine_new"] = new_vaccine_product
    shared_data["chosen_vaccine_type_new"] = get_vaccination_type(1, shared_data["chosen_vaccine_new"])
    shared_data["care_model"] = get_care_model(index)
    if "pharmacy" in site.lower():
        shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])
    else:
        shared_data["pack_size"] = None

    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, shared_data["site"], shared_data["chosen_vaccine_new"], shared_data["chosen_vaccine_type_new"], "AUTOMATED-FLU", "19/11/2026")
    return shared_data

@given(parse("I login to RAVS and set vaccinator details with {site} and {care_model} and get patient details for {nhs_number} with option {index} and choose to vaccinate with vaccine details as {chosen_vaccine}, {batch_number} with {batch_expiry_date} and new random vaccine product type"))
def step_login_to_ravs_check_new_vaccine_product_type_batch_exist(site, care_model, nhs_number, index, chosen_vaccine, batch_number, batch_expiry_date, shared_data):
    shared_data["nhs_number"] = nhs_number
    shared_data["index"] = index
    shared_data["chosen_vaccine"] = chosen_vaccine
    shared_data["chosen_vaccine_type"] = get_vaccination_type(index, chosen_vaccine)
    shared_data["batch_number"] = batch_number
    shared_data["site"] = site
    shared_data["chosen_vaccine_new"] = shared_data["chosen_vaccine"]
    shared_data["chosen_vaccine_type_new"] = get_vaccination_type(2, shared_data["chosen_vaccine_new"])
    shared_data["care_model"] = get_care_model(index)
    if "pharmacy" in site.lower():
        shared_data["pack_size"] = get_vaccine_type_pack_size_by_index(shared_data["index"], shared_data["chosen_vaccine_type"])
    else:
        shared_data["pack_size"] = None

    today_str = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today_str, '%d/%m/%Y')
    if datetime.strptime(batch_expiry_date, '%d/%m/%Y') <= today:
        batch_expiry_date = today + timedelta(days=7)
        batch_expiry_date = standardize_date_format(batch_expiry_date)
    shared_data["batch_expiry_date"] = batch_expiry_date
    check_vaccine_and_batch_exists_in_site(shared_data, shared_data["site"], shared_data["chosen_vaccine_new"], shared_data["chosen_vaccine_type_new"], "AUTOMATED-COVID", "19/11/2026")
    return shared_data

@given("I search for a patient with the NHS number in the find a patient screen")
@when("I search for a patient with the NHS number in the find a patient screen")
@then("I search for a patient with the NHS number in the find a patient screen")
def step_search_for_patient(shared_data):
    nhs_number = shared_data["nhs_number"]
    click_find_a_patient_and_search_with_nhs_number(nhs_number)

@given(parse("I see the patient's address {address} and gender {gender}"))
def step_save_address_and_gender_to_shared_data(shared_data, address, gender):
    shared_data["address"] = address
    shared_data["gender"] = gender

@given(parse("I open the patient record by clicking on patient {name}"))
@when(parse("I open the patient record by clicking on patient {name}"))
@then(parse("I open the patient record by clicking on patient {name}"))
def step_search_for_patient(shared_data, name):
    attach_screenshot("before_clicking_patient_name")
    click_on_patient_name_search_result(name)
    attach_screenshot("before_clicking_patient_name")
    shared_data["patient_name"] = name

@given('I create a random patient locally')
def generate_random_patient_locally(shared_data):
    click_find_a_patient_nav_link()
    click_search_by_demographics_link()
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
    first_name = shared_data["first_name"]
    last_name = shared_data["last_name"]
    gender = shared_data["gender"]
    postcode = shared_data["postcode"]
    dob = shared_data["dob"]
    enter_first_name(first_name)
    enter_last_name(last_name)
    enter_dob(dob)
    attach_screenshot("add_mandatory_patient_information")
    click_search_for_patient_button()
    attach_screenshot("clicked_search_for_patient_button")
    click_create_a_new_patient_button()
    time.sleep(2)
    attach_screenshot("clicked_create_a_new_patient_button")
    enter_first_name(first_name)
    enter_last_name(last_name)
    select_gender(gender)
    enter_postcode(postcode)
    enter_dob(dob)
    attach_screenshot("add_mandatory_new_patient_information")
    click_check_and_confirm_button()
    attach_screenshot("clicked_check_and_confirm_button")
    click_confirm_and_save_button()
    attach_screenshot("clicked_confirm_and_save_button")
    patient_added_message = get_patient_added_message(shared_data["first_name"])
    attach_screenshot("patient_added_confirmation_message")
    click_search_by_local_records_link()
    enter_first_name(shared_data["first_name"])
    enter_last_name(shared_data["last_name"])
    select_gender(shared_data["gender"])
    enter_postcode(shared_data["postcode"])
    enter_dob(shared_data["dob"])
    click_search_for_patient_button()
    attach_screenshot("clicked_search_for_patient_button")
    shared_data["patient_name"] = shared_data["first_name"] + " " + shared_data["last_name"]
    click_on_patient_name_search_result(shared_data["patient_name"])

@when(parse("I click choose vaccine button and choose the {chosen_vaccine}, {batch_number} with {batch_expiry_date} and click continue"))
def step_choose_vaccine_and_vaccine_type(shared_data, chosen_vaccine, batch_number, batch_expiry_date):
    time.sleep(1)
    if shared_data["nhs_number"] == "9727840361":
        assert check_vaccine_history_not_available_label_element_exists() == True
    attach_screenshot("checked_vaccine_history_not_available_label_element_exists")
    immunisation_history_records_count_before_vaccination = click_on_patient_search_result_and_click_choose_vaccine(shared_data['patient_name'], chosen_vaccine)
    shared_data["immunisation_history_records_count_before_vaccination"] = immunisation_history_records_count_before_vaccination
    shared_data["chosen_vaccine_vaccinate_page"] = chosen_vaccine
    choose_vaccine_and_vaccine_type_for_patient(shared_data['site'], chosen_vaccine, shared_data['chosen_vaccine_type'])

@when(parse("I click choose vaccine button and choose the {chosen_vaccine}, {chosen_vaccine_type}, {batch_number} with {batch_expiry_date} and click continue"))
def step_choose_vaccine_and_vaccine_type(shared_data, chosen_vaccine, chosen_vaccine_type, batch_number, batch_expiry_date):
    time.sleep(1)
    if shared_data["nhs_number"] == "9727840361":
        assert check_vaccine_history_not_available_label_element_exists() == True
    shared_data['chosen_vaccine_type'] = chosen_vaccine_type
    attach_screenshot("checked_vaccine_history_not_available_label_element_exists")
    immunisation_history_records_count_before_vaccination = click_on_patient_search_result_and_click_choose_vaccine(shared_data['patient_name'], chosen_vaccine)
    shared_data["immunisation_history_records_count_before_vaccination"] = immunisation_history_records_count_before_vaccination
    shared_data["chosen_vaccine_vaccinate_page"] = chosen_vaccine
    choose_vaccine_and_vaccine_type_for_patient(shared_data['site'], chosen_vaccine, shared_data['chosen_vaccine_type'])

@when(parse("I assess the patient's {eligibility} with the details and date as {assess_date} and click continue to record consent screen button"))
def step_assess_eligibility_and_click_continue_record_consent_screen(shared_data, eligibility, assess_date):
    shared_data['eligible_decision'] = eligibility
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = get_eligibility_type(shared_data["index"], shared_data["chosen_vaccine"])
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    if "Aspire pharmacy".lower() in shared_data["site"].lower():
        shared_data['eligibility_assessing_clinician'] = get_assessing_clinician_fhh39(shared_data["index"])
    else:
        shared_data['eligibility_assessing_clinician'] = get_random_assessing_clinician()
    if shared_data["chosen_vaccine"].lower() == "covid-19":
        date = get_date_value_by_days(assess_date)
    else:
        date = get_date_value_by_months(assess_date)
    assess_date = format_date(str(date), config["browser"])
    shared_data['eligibility_assessment_date'] = assess_date
    shared_data['eligibility_assessment_outcome'] = get_assessment_outcome(0)
    shared_data['eligibility_assessment_no_vaccine_given_reason'] = get_assess_vaccine_not_given_reason(shared_data["index"])
    shared_data['assessment_comments'] = "Assessment comments " + assess_date + shared_data["patient_name"]
    assess_patient_with_details_and_click_continue_to_consent(eligibility, shared_data['eligibility_type'], shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], None, assess_date, shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'],shared_data['eligibility_assessment_no_vaccine_given_reason'])

@when(parse("I assess the pregnant patient's {eligibility} with the details of due date as {due_date} and assessment date as {assess_date} and click continue to record consent screen button"))
def step_assess_eligibility_and_click_continue_record_consent_screen(shared_data, eligibility, due_date, assess_date):
    shared_data['eligible_decision'] = eligibility
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = "Pregnancy"
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    if "Aspire pharmacy".lower() in shared_data["site"].lower():
        shared_data['eligibility_assessing_clinician'] = get_assessing_clinician_fhh39(shared_data["index"])
    else:
        shared_data['eligibility_assessing_clinician'] = get_random_assessing_clinician()
    if shared_data["chosen_vaccine"].lower() == "covid-19":
        date = get_date_value_by_days(due_date)
    else:
        date = get_date_value_by_months(due_date)
    due_date = format_date(str(date), config["browser"])
    shared_data['eligibility_due_date'] = due_date
    if shared_data["chosen_vaccine"].lower() == "covid-19":
        a_date = get_date_value_by_days(assess_date)
    else:
        a_date = get_date_value_by_months(assess_date)
    assess_date = format_date(str(a_date), config["browser"])
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
        if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
            shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']

        else:
            if "Aspire pharmacy".lower() in shared_data["site"].lower():
                shared_data['consent_clinician_details'] = get_consenting_clinician_fhh39(shared_data["index"])
            else:
                shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
        shared_data["no_consent_reason"] = get_no_consent_reason(shared_data["index"])
        record_consent_details_and_click_continue_to_vaccinate(shared_data['consent_decision'],shared_data['consent_given_by'], name_of_person_consenting, relationship_to_patient, shared_data['consent_clinician_details'], shared_data['legal_mechanism'], shared_data["no_consent_reason"])

@when(parse("I record {vaccination} details and date as {vaccination_date} and click Continue to Check and confirm screen"))
def step_enter_vaccination_details_and_continue_to_check_and_confirm_screen(shared_data, vaccination, vaccination_date):
    shared_data["vaccinated_decision"] = vaccination
    if shared_data["consent_decision"].lower() == "yes":
        if shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
            if shared_data["chosen_vaccine"].lower() == "covid-19":
                date = get_date_value_by_days(vaccination_date)
            else:
                date = get_date_value_by_months(vaccination_date)
            shared_data["vaccination_date"] = format_date(str(date), config["browser"])
            chosen_vaccine = shared_data["chosen_vaccine"]
            shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
            shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine_type"]))
            if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
                shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
            else:
                if "Aspire pharmacy".lower() in shared_data["site"].lower():
                    shared_data['vaccinator'] = get_vaccinator_fhh39(shared_data["index"])
                else:
                    shared_data['vaccinator'] = get_vaccinator(shared_data["index"])
            shared_data["vaccination_comments"] = shared_data["chosen_vaccine_type"] + "vaccination given on " + shared_data["vaccination_date"] + " for " + shared_data["patient_name"]
            batch_number_to_select = shared_data["batch_number"].upper() + " - " + shared_data["batch_expiry_date"]
            shared_data["batch_number_selected"] = batch_number_to_select
            shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
            enter_vaccine_details_and_click_continue_to_check_and_confirm(shared_data["vaccinated_decision"], shared_data["care_model"], shared_data["vaccination_date"], chosen_vaccine, shared_data["chosen_vaccine_type"], shared_data["vaccination_site"], shared_data["batch_number"], shared_data["batch_expiry_date"], shared_data["dose_amount"], shared_data["vaccinator"], shared_data["vaccination_comments"], shared_data["legal_mechanism"], True, shared_data["no_vaccination_reason"], shared_data['pack_size'])
            attach_screenshot("entered_vaccination_details")
    logging.info(shared_data)

@when(parse("I record {vaccination} details and date as {vaccination_date} and click Continue to Check and confirm screen without selecting batch number as the vaccine product has only one batch so it should be auto-selected"))
def step_enter_vaccination_details_and_continue_to_check_and_confirm_screen(shared_data, vaccination, vaccination_date):
    shared_data["vaccinated_decision"] = vaccination
    if shared_data["consent_decision"].lower() == "yes":
        if shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
            if shared_data["chosen_vaccine"].lower() == "covid-19":
                date = get_date_value_by_days(vaccination_date)
            else:
                date = get_date_value_by_months(vaccination_date)
            shared_data["vaccination_date"] = format_date(str(date), config["browser"])
            chosen_vaccine = shared_data["chosen_vaccine"]
            shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
            shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine_type"]))
            if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
                shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
            else:
                if "Aspire pharmacy".lower() in shared_data["site"].lower():
                    shared_data['vaccinator'] = get_vaccinator_fhh39(shared_data["index"])
                else:
                    shared_data['vaccinator'] = get_vaccinator(shared_data["index"])
            shared_data["vaccination_comments"] = shared_data["chosen_vaccine_type"] + "vaccination given on " + shared_data["vaccination_date"] + " for " + shared_data["patient_name"]
            shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
            enter_vaccine_details_and_click_continue_to_check_and_confirm(shared_data["vaccinated_decision"], shared_data["care_model"], shared_data["vaccination_date"], chosen_vaccine, shared_data["chosen_vaccine_type"], shared_data["vaccination_site"], shared_data["batch_number"], shared_data["batch_expiry_date"], shared_data["dose_amount"], shared_data["vaccinator"], shared_data["vaccination_comments"], shared_data["legal_mechanism"], False, shared_data["no_vaccination_reason"])
            attach_screenshot("entered_vaccination_details")
    logging.info(shared_data)

@when(parse("I record {vaccination} details and date as {vaccination_date} and click Save and return button"))
def step_enter_vaccination_details_and_continue_to_check_and_confirm_screen(shared_data, vaccination, vaccination_date):
    shared_data["vaccinated_decision"] = vaccination
    if shared_data["consent_decision"].lower() == "yes":
        if shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
            if shared_data["chosen_vaccine"].lower() == "covid-19":
                date = get_date_value_by_days(vaccination_date)
            else:
                date = get_date_value_by_months(vaccination_date)
            shared_data["vaccination_date"] = format_date(str(date), config["browser"])
            chosen_vaccine = shared_data["chosen_vaccine"]
            shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
            shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine_type"]))
            if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
                shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
            else:
                if "Aspire pharmacy".lower() in shared_data["site"].lower():
                    shared_data['vaccinator'] = get_vaccinator_fhh39(shared_data["index"])
                else:
                    shared_data['vaccinator'] = get_vaccinator(shared_data["index"])
            shared_data["vaccination_comments"] = shared_data["chosen_vaccine_type"] + " vaccination given on " + shared_data["vaccination_date"] + " for " + shared_data["patient_name"]
            shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
            enter_vaccine_details_and_click_save_and_return(shared_data["vaccinated_decision"], shared_data["care_model"], shared_data["vaccination_date"], chosen_vaccine, shared_data["chosen_vaccine_type"], shared_data["vaccination_site"], shared_data["batch_number"], shared_data["batch_expiry_date"], shared_data["dose_amount"], shared_data["vaccinator"], shared_data["vaccination_comments"], shared_data["legal_mechanism"], shared_data["no_vaccination_reason"])
            attach_screenshot("entered_vaccination_details")
    logging.info(shared_data)

@when(parse("I need to be able to see the patient {name}, {dob}, {address} and vaccination details on the check and confirm screen"))
@then(parse("I need to be able to see the patient {name}, {dob}, {address} and vaccination details on the check and confirm screen"))
def step_see_patient_details_on_check_and_confirm_screen(shared_data, name, dob, address):
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower() and shared_data["eligibility_assessment_outcome"].lower() == "Give vaccine".lower():
        attach_screenshot("check_and_confirm_screen_before_assertion")
        if get_patient_name_value_in_check_and_confirm_screen() is not None:
            assert get_patient_name_value_in_check_and_confirm_screen().lower() == shared_data["patient_name"].lower()
            assert get_patient_address_value_in_check_and_confirm_screen().lower() == address.lower()
            shared_data["gender"] = get_patient_gender_value_in_check_and_confirm_screen()
            shared_data["address"] = address
            assert get_patient_vaccination_dose_amount_value() == shared_data["dose_amount"]
            assert get_patient_vaccinated_chosen_vaccine_value().lower() == shared_data["chosen_vaccine"].lower()
            assert get_patient_vaccinated_chosen_vaccine_product_value().lower() == shared_data["chosen_vaccine_type"].lower()
            assert get_patient_eligibility_assessment_date_value() == date_format_with_day_of_week(shared_data['eligibility_assessment_date'])
            assert get_patient_vaccinated_date_value() == date_format_with_day_of_week(shared_data['vaccination_date'])
            expected_dob = date_format_with_age(dob)
            actual_dob = get_patient_dob_value_in_check_and_confirm_screen()
            if "0." in actual_dob:
                print("Warning: Known issue detected RAVS-262 : age displayed as 0.67 instead of expected.")
            else:
                assert actual_dob == expected_dob, f"Expected {expected_dob}, but got {actual_dob}"
            shared_data['dob'] = date_format_with_age(dob)
            assert get_patient_vaccination_batch_expiry_date_value() == date_format_with_name_of_month(shared_data['batch_expiry_date'])
            assert get_patient_eligibility_assessing_clinician_vaccine_value() == shared_data['eligibility_assessing_clinician']
            assert get_patient_consent_recorded_by_clinician_value() == shared_data['consent_clinician_details']
            assert get_patient_vaccination_vaccinator_value() == shared_data['vaccinator']
            attach_screenshot("check_and_confirm_screen_after_assertion")

@when(parse("I need to be able to see the patient {name}, {dob} and vaccination details on the check and confirm screen"))
@then(parse("I need to be able to see the patient {name}, {dob} and vaccination details on the check and confirm screen"))
def step_see_patient_details_on_check_and_confirm_screen(shared_data, name, dob):
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower() and shared_data["eligibility_assessment_outcome"].lower() == "Give vaccine".lower():
        attach_screenshot("check_and_confirm_screen_before_assertion")
        if get_patient_name_value_in_check_and_confirm_screen() is not None:
            assert get_patient_name_value_in_check_and_confirm_screen().lower() == shared_data["patient_name"].lower()
            shared_data["gender"] = get_patient_gender_value_in_check_and_confirm_screen()
            assert get_patient_vaccination_dose_amount_value() == shared_data["dose_amount"]
            assert get_patient_vaccinated_chosen_vaccine_value().lower() == shared_data["chosen_vaccine"].lower()
            assert get_patient_vaccinated_chosen_vaccine_product_value().lower() == shared_data["chosen_vaccine_type"].lower()
            assert get_patient_eligibility_assessment_date_value() == date_format_with_day_of_week(shared_data['eligibility_assessment_date'])
            assert get_patient_vaccinated_date_value() == date_format_with_day_of_week(shared_data['vaccination_date'])
            expected_dob = date_format_with_age(dob)
            actual_dob = get_patient_dob_value_in_check_and_confirm_screen()
            if "0." in actual_dob:
                print("Warning: Known issue detected RAVS-262 : age displayed as 0.67 instead of expected.")
            else:
                assert actual_dob == expected_dob, f"Expected {expected_dob}, but got {actual_dob}"
            shared_data['dob'] = date_format_with_age(dob)
            assert get_patient_vaccination_batch_expiry_date_value() == date_format_with_name_of_month(shared_data['batch_expiry_date'])
            assert get_patient_eligibility_assessing_clinician_vaccine_value() == shared_data['eligibility_assessing_clinician']
            assert get_patient_consent_recorded_by_clinician_value() == shared_data['consent_clinician_details']
            assert get_patient_vaccination_vaccinator_value() == shared_data['vaccinator']
            attach_screenshot("check_and_confirm_screen_after_assertion")

@when(parse("I need to be able to see the patient vaccination details on the check and confirm screen"))
@then(parse("I need to be able to see the patient vaccination details on the check and confirm screen"))
def step_see_patient_details_on_check_and_confirm_screen(shared_data):
    if shared_data["vaccinated_decision"].lower() == "Yes".lower() and shared_data["consent_decision"].lower() == "Yes".lower() and shared_data["eligibility_assessment_outcome"].lower() == "Give vaccine".lower():
        attach_screenshot("check_and_confirm_screen_before_assertion")
        if get_patient_name_value_in_check_and_confirm_screen() is not None:
            assert get_patient_vaccination_dose_amount_value() == shared_data["dose_amount"]
            assert get_patient_vaccinated_chosen_vaccine_value().lower() == shared_data["chosen_vaccine"].lower()
            assert get_patient_vaccinated_chosen_vaccine_product_value().lower() == shared_data["chosen_vaccine_type"].lower()
            assert get_patient_eligibility_assessment_date_value() == date_format_with_day_of_week(shared_data['eligibility_assessment_date'])
            assert get_patient_vaccinated_date_value() == date_format_with_day_of_week(shared_data['vaccination_date'])
            assert get_patient_vaccination_batch_expiry_date_value() == date_format_with_name_of_month(shared_data['batch_expiry_date'])
            assert get_patient_eligibility_assessing_clinician_vaccine_value() == shared_data['eligibility_assessing_clinician']
            assert get_patient_consent_recorded_by_clinician_value() == shared_data['consent_clinician_details']
            assert get_patient_vaccination_vaccinator_value() == shared_data['vaccinator']
            attach_screenshot("check_and_confirm_screen_after_assertion")

@when("I click confirm and save button, I should see a record saved dialogue")
@then("I click confirm and save button, I should see a record saved dialogue")
def click_confirm_and_save_button_record_saved(shared_data):
    attach_screenshot("patient_details_screen_with_immunisation_history")
    click_confirm_details_and_save_button()
    attach_screenshot("before_assert_record_saved")
    assert check_record_saved_element_exists(False)

@when("the immunisation history of the patient should be updated in the patient details page")
@then("the immunisation history of the patient should be updated in the patient details page")
def immunisation_history_should_be_updated(shared_data):
    attach_screenshot("immunisation_history_records_count_after_vaccination")
    immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
    assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
    click_delete_history_link(shared_data["chosen_vaccine"])
    attach_screenshot("click_delete_history_link")
    click_delete_vaccination_button()
    attach_screenshot("click_delete_vaccination_button")

@then("the immunisation history of the patient should be updated in the patient details page and not be deleted")
def immunisation_history_should_be_updated(shared_data):
    attach_screenshot("immunisation_history_records_count_after_vaccination")
    immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
    if shared_data['vaccinated_decision'].lower() == "yes":
        assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
    else:
        assert int(immunisation_history_records_count_after_vaccination) == int(shared_data["immunisation_history_records_count_before_vaccination"])

@then("I click confirm and save button, the immunisation history of the patient should be updated in the patient details page")
def click_confirm_and_save_button_immunisation_history_should_be_updated(shared_data):
    attach_screenshot("patient_details_screen_with_immunisation_history")
    if shared_data["vaccinated_decision"].lower() == "yes" and shared_data["consent_decision"].lower() == "yes" and shared_data["eligibility_assessment_outcome"].lower() == "give vaccine":
        click_confirm_details_and_save_button()
        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) >= int(shared_data["immunisation_history_records_count_before_vaccination"]) + 1
    else:
        immunisation_history_records_count_after_vaccination = get_count_of_immunisation_history_records(shared_data["chosen_vaccine"])
        assert int(immunisation_history_records_count_after_vaccination) == int(shared_data["immunisation_history_records_count_before_vaccination"])
    attach_screenshot("patient_details_screen_with_immunisation_history")

@when(parse("I start to record the vaccination for a new patient {new_patient_name} with nhs number {new_nhs_number}"))
def start_recording_the_vaccine_for_new_patient(shared_data, new_patient_name, new_nhs_number):
    click_find_a_patient_nav_link()
    attach_screenshot("clicked_find_a_patient_nav_link")
    enter_nhs_number(new_nhs_number)
    attach_screenshot("entered_new_nhs_number: " + new_nhs_number)
    click_search_for_patient_button()
    attach_screenshot("clicked_search_for_patient_button")
    click_on_patient_name_search_result(new_patient_name)
    attach_screenshot("clicked_on_patient_name_search_result")
    click_choose_vaccine_button()

@then("the delivery team, vaccine and vaccine product selection should persist on the choose vaccine page")
def check_values_persist_on_choose_vaccine_screen(shared_data):
    assert get_selected_delivery_team_radio_button_value_on_choose_vaccine_page().lower() == shared_data["site"].lower()
    attach_screenshot("delivery_team_selection_is_persisted")
    assert get_selected_vaccine_radio_button_value_on_choose_vaccine_page() == shared_data["chosen_vaccine"]
    attach_screenshot("vaccine_selection_is_persisted")
    assert str(get_selected_vaccine_product_radio_button_value_on_choose_vaccine_page()).replace("Active batches available", "").strip() == shared_data["chosen_vaccine_type"]
    attach_screenshot("vaccine_product_selection_is_persisted")
    click_continue_to_assess_patient_button()

@then("the patient's eligibility, assessment date, legal mechanism, assessing clinician, assessment outcome selection must persist on the assessment screen")
def the_eligibility_values_should_persist(shared_data):
    click_continue_to_record_consent_button()
    assert check_eligibility_type_missing_error_message_link_exists() == True
    attach_screenshot("eligibility_link_missing_error_message_text_should_exist")
    assert get_is_patient_eligible_value_on_assessing_the_patient_page().lower() == str(shared_data["eligible_decision"]).lower()
    attach_screenshot("assessment_patient_eligible_value_should_persist")
    assert format_date(get_assessment_date_value(), config["browser"]) == shared_data["eligibility_assessment_date"]
    attach_screenshot("assessment_date_value_should_persist")
    assert get_legal_mechanism_value_on_assessing_the_patient_page() == shared_data["legal_mechanism"]
    attach_screenshot("legal_mechanism_value_should_persist")
    assert get_assessing_clinician_value_on_assessing_the_patient_page() == shared_data["eligibility_assessing_clinician"]
    attach_screenshot("assessing_clinician_value_should_persist")
    assert get_assessment_outcome_value_on_assessing_the_patient_page().lower() == str(shared_data["eligibility_assessment_outcome"]).lower()
    attach_screenshot("assessment_outcome_value_should_persist")
    if check_eligibility_type_is_enabled():
        select_eligibility_type(shared_data["eligibility_type"])
        attach_screenshot("selected_eligibility_type")
    click_continue_to_record_consent_button()

@then("the patient's consent answer, consent given by, consenting clinician, selection must persist on the consent screen")
def the_consent_values_should_persist(shared_data):
    assert get_patient_consent_value_on_consent_page().lower() == str(shared_data["eligible_decision"]).lower()
    attach_screenshot("consent_value_should_persist")
    assert get_consenting_clinician_details_on_consent_page() == shared_data["consent_clinician_details"]
    attach_screenshot("consent_clinician_value_should_persist")
    name_of_person_consenting = "Automation tester"
    relationship_to_patient = "RAVS tester"
    if shared_data['consent_given_by'] != "Patient (informed consent)":
        enter_person_consenting_details(name_of_person_consenting)
        attach_screenshot("entered_person_consenting_details")
        enter_relationship_to_patient(relationship_to_patient)
        attach_screenshot("entered_relationship_to_patient")
    if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
        shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']
    else:
        if "Aspire pharmacy".lower() in shared_data["site"].lower():
            shared_data['consent_clinician_details'] = get_consenting_clinician_fhh39(shared_data["index"])
        else:
            shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
    if (legal_mechanism) != "Patient Group Direction (PGD)":
        select_consent_clinician_with_name_and_council(shared_data['consent_clinician_details'] )
        attach_screenshot("selected_consent_clinician_with_name_and_council")
    click_continue_to_vaccinate_button()
    attach_screenshot("clicked_continue_to_vaccinate_button")

@then("the patient's vaccinated answer, vaccine product, vaccinate date, care model, batch number, vaccinator should persist")
def the_vaccinated_values_should_persist(shared_data):
    assert get_is_patient_vaccinated_value_on_vaccinated_page().lower() == shared_data["vaccinated_decision"].lower()
    attach_screenshot("patient_vaccinated_value_must_persist")
    assert format_date(get_vaccination_date(), config["browser"]) == shared_data["vaccination_date"]
    attach_screenshot("vaccination_date_should_persist")
    assert get_vaccination_care_model_value_on_vaccinated_page().lower() == shared_data["care_model"].lower()
    attach_screenshot("care_model_value_should_persist")
    assert get_vaccinator_value_on_vaccinated_page() == shared_data['vaccinator']
    attach_screenshot("vaccinator_value_should_persist")
    if get_is_patient_vaccinated_value_on_vaccinated_page().lower() == "yes":
        assert get_vaccine_product_value_on_vaccinated_page() == shared_data["chosen_vaccine_type"]
        attach_screenshot("vaccine_product_value_should_persist")
        assert get_batch_number_on_vaccinated_screen() == shared_data["batch_number_selected"]
        attach_screenshot("vaccine_product_batch_number_value_should_persist")
        assert get_dose_amount_value() == shared_data["dose_amount"]
        attach_screenshot("vaccine_product_does_amount_value_should_persist")
        assert get_vaccination_site_on_vaccinated_screen() == ""
        attach_screenshot("vaccination_site_value_should_not_persist")
    click_continue_to_check_and_confirm_vaccination_screen_button()
    # assert check_vaccination_site_missing_error_message_exists() == True #commenting because error text does not appear only link appears even when it is the first vaccination after logging in
    assert check_vaccination_site_missing_error_message_link_exists() == True

@given("I am logged into the RAVS app as an administrator")
def logged_into_ravs_as_administrator(navigate_and_login_as_administrator):
    pass

@given("I am logged into the RAVS app as a lead administrator")
def logged_into_ravs_as_lead_administrator(navigate_and_login_as_lead_administrator):
    pass

@given("I am logged into the RAVS app as a recorder")
def logged_into_ravs_as_recorder(navigate_and_login_as_recorder):
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
        if "site" in shared_data:
            click_delivery_team_radiobutton(shared_data["site"])
        else:
            click_delivery_team_radiobutton("ALBERT HOUSE")
        click_vaccine_radiobutton(vaccine_name)
        warning_count = 0
        # comirnaty_original_omicron_ba_age_above_12 = get_vaccination_type(0, vaccine_name)
        spikevax_jn1_age_above_18 = get_vaccination_type(0, vaccine_name)
        comirnaty_30_jn1_age_above_12 = get_vaccination_type(1, vaccine_name)
        comirnaty_10_omicron_jn1_above_5_to_11 = get_vaccination_type(2, vaccine_name)
        comirnaty_3_omicron_jn1_above_6months_to_4 = get_vaccination_type(3, vaccine_name)
        vaccine_types = [
        (comirnaty_30_jn1_age_above_12, ["9732091169", "9692237893", "9474335761", "9474335761"]),
        # (comirnaty_30_omicron_xbb_age_above_12, ["9732091169", "9692237893", "9474335761"]),
        (comirnaty_10_omicron_jn1_above_5_to_11, ["9692237893", "9732091169", "9450153485", "9470472918", "9473673388"]),
        (comirnaty_3_omicron_jn1_above_6months_to_4, ["9450153485", "9474335761", "9470472918", "9473673388"]),
        (spikevax_jn1_age_above_18, ["9732091169", "9692237893", "9474335761", "9450153485", "9470472918"]),
    ]

    for index, (vaccine, warning_nhs_numbers) in enumerate(vaccine_types):
        click_vaccine_type_radiobutton(vaccine)
        attach_screenshot("clicked_vaccine_type_radiobutton")
        if shared_data["nhs_number"] in warning_nhs_numbers:
            assert check_age_based_warning_exists() is True
            attach_screenshot("check_age_based_warning_exists")
            warning_count += 1
        else:
            assert check_age_based_warning_exists() is False
            attach_screenshot("check_age_based_warning_does_not_exist")

    assert str(warning_count) == expected_warning_count

    warning_count = 0

    click_continue_to_assess_patient_button()
    attach_screenshot("clicked_continue_to_assess_patient_button")
    shared_data["index"] = index
    shared_data['chosen_vaccine'] = shared_data['vaccine_type']
    shared_data['legal_mechanism'] = get_legal_mechanism(shared_data["index"])
    shared_data['eligibility_type'] = get_eligibility_type(shared_data["index"], shared_data['chosen_vaccine'])
    shared_data["healthcare_worker"] = get_staff_role(shared_data["index"])
    if "site" in shared_data and "Aspire pharmacy".lower() in shared_data["site"].lower():
        shared_data['eligibility_assessing_clinician'] = get_assessing_clinician_fhh39(shared_data["index"])
    else:
        shared_data['eligibility_assessing_clinician'] = get_assessing_clinician(shared_data["index"])
    assess_date = "today"
    assess_date = format_date(str(get_date_value_by_months(assess_date)), config["browser"])
    shared_data['eligibility_assessment_date'] = assess_date
    shared_data['eligibility_assessment_outcome'] = get_assessment_outcome(0)
    shared_data['eligibility_assessment_no_vaccine_given_reason'] = get_assess_vaccine_not_given_reason(shared_data["index"])
    shared_data['assessment_comments'] = "Assessment comments " + assess_date
    assess_patient_with_details_and_click_continue_to_consent("yes", shared_data['eligibility_type'], shared_data["healthcare_worker"], shared_data['eligibility_assessing_clinician'], None ,assess_date, shared_data['legal_mechanism'], shared_data['eligibility_assessment_outcome'], shared_data['assessment_comments'], shared_data['eligibility_assessment_no_vaccine_given_reason'])
    shared_data['consent_decision'] = "yes"
    shared_data['consent_given_by'] = get_consent_given_by(shared_data["index"])
    name_of_person_consenting = "Automation tester"
    relationship_to_patient = "RAVS tester"
    if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
        shared_data['consent_clinician_details'] = shared_data['eligibility_assessing_clinician']
    else:
        if "site" in shared_data and "Aspire pharmacy".lower() in shared_data["site"].lower():
            shared_data['consent_clinician_details'] = get_consenting_clinician_fhh39(shared_data["index"])
        else:
            shared_data['consent_clinician_details'] = get_consenting_clinician(shared_data["index"])
    shared_data["no_consent_reason"] = get_no_consent_reason(shared_data["index"])
    record_consent_details_and_click_continue_to_vaccinate(shared_data['consent_decision'],shared_data['consent_given_by'], name_of_person_consenting, relationship_to_patient, shared_data['consent_clinician_details'], shared_data["no_consent_reason"])
    shared_data["vaccinated_decision"] = "yes"
    shared_data["vaccination_date"] = format_date(str(get_date_value_by_months("today")), config["browser"])
    chosen_vaccine = shared_data["chosen_vaccine"]
    shared_data["vaccination_site"] = get_vaccination_site(shared_data["index"])
    shared_data["dose_amount"] = str(get_vaccine_dose_amount(shared_data["chosen_vaccine"]))
    if shared_data['legal_mechanism'] == "Patient Group Direction (PGD)":
        shared_data['vaccinator'] = shared_data['eligibility_assessing_clinician']
    else:
        if "site" in shared_data and "Aspire pharmacy".lower() in shared_data["site"].lower():
            shared_data['vaccinator'] = get_vaccinator_fhh39(shared_data["index"])
        else:
            shared_data['vaccinator'] = get_vaccinator(shared_data["index"])
    shared_data["vaccination_comments"] = shared_data["chosen_vaccine"] + "vaccination given on " + shared_data["vaccination_date"]
    shared_data["no_vaccination_reason"] = get_vaccination_not_given_reason(shared_data["index"])
    click_yes_vaccinated_radiobutton()
    attach_screenshot("clicked_yes_vaccinated_radiobutton")
    set_vaccination_date(shared_data["vaccination_date"])
    attach_screenshot("vaccination_date_is_Set")
    for index, (vaccine, warning_nhs_numbers) in enumerate(vaccine_types):
        click_vaccine_type_radiobutton(vaccine)
        attach_screenshot("clicked_vaccine_type_radiobutton")
        if shared_data["nhs_number"] in warning_nhs_numbers:
            attach_screenshot("check_age_based_warning_exists")
            assert check_age_based_warning_exists() is True
            warning_count += 1
        else:
            attach_screenshot("check_age_based_warning_does_not_exist")
            assert check_age_based_warning_exists() is False

    assert str(warning_count) == expected_warning_count
