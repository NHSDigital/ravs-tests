import pytest
# from pages.add_vaccines_page import *
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
from init_helpers import *
from datetime import datetime, timedelta
from allure_commons.types import LabelType
import logging

# Define marks
pytest.mark.login = pytest.mark.mark(login=True)
pytest.mark.logout = pytest.mark.mark(logout=True)
pytest.mark.smoke = pytest.mark.mark(smoke=True)
pytest.mark.appointments = pytest.mark.mark(appointments=True)
pytest.mark.consent = pytest.mark.mark(consent=True)
pytest.mark.findpatient = pytest.mark.mark(findpatient=True)
pytest.mark.createpatient = pytest.mark.mark(createpatient=True)
pytest.mark.recordvaccine = pytest.mark.mark(recordvaccine=True)
pytest.mark.addvaccine = pytest.mark.mark(addvaccine=True)
pytest.mark.addbatches = pytest.mark.mark(addbatches=True)
pytest.mark.reports = pytest.mark.mark(reports=True)

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


# @pytest.fixture(scope='function')
# def playwright_helper(request):
#     helper = PlaywrightHelper(get_working_directory(), config)
#     def teardown():
#         try:
#             helper.quit_browser()
#         except Exception as e:
#             print(f"An error occurred during teardown: {e}")
#             raise

#     request.addfinalizer(teardown)
#     return helper

# Fixture for site parameter
@pytest.fixture(params=["NEELIMA HOUSE", "ALBERT HOUSE", "ST JOHN'S HOUSE"])
def site(request):
    return request.param

# Fixture for care_model parameter
@pytest.fixture(params=["Vaccination Centre", "Hospital Hub", "Care Home", "Home Of Housebound Patient", "Off-site Outreach Event"])
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

# Fixture for navigating to RAVS
@pytest.fixture(scope='function')
def navigate_to_ravs(request):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists_without_waiting():
            click_navbar_toggler()
    if check_logout_button_exists_without_waiting():
        click_logout_button()
    url = get_app_url(config["test_environment"])
    navigate_to_ravs_login_page(url)
    return True

# Fixture for logging in and navigating to find a patient
@pytest.fixture(scope='function')
def login_and_navigate_to_find_a_patient(request):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()
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

def click_on_patient_name(name):
    click_on_patient_name_search_result(name)
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

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

def check_vaccine_and_batch_exists_in_site(site, vaccine, vaccine_type, batch_number, expiry_date):
    if config["browser"] == "mobile":
        if check_nav_link_bar_toggle_exists():
            click_nav_link_bar_toggler()

    click_vaccines_nav_link()
    attach_screenshot("clicked_vaccines_nav_link")
    check_site_vaccine_type_has_active_batch(site, vaccine, vaccine_type, batch_number, expiry_date)

def check_site_vaccine_type_has_active_batch(site, vaccine, vaccine_type, batch_number, expiry_date):

    # If the site does NOT currently have the vaccine, then add a site vaccine
    # Adding a vaccine also adds a vaccine type and an active batch, so we don't need to do further checks
    if not check_vaccine_has_been_added(site, vaccine, True):
        add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date)
        return True

    # If the site has the vaccine, but does NOT currently have the vaccine type, then add a site vaccine
    # Adding a vaccine type is the same process as adding a vaccine for a site
    if not check_vaccine_type_has_been_added(site, vaccine, vaccine_type, False):
        add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date)
        return True

    # Open the vaccine type to see the batches.
    # If the batch does NOT currently exist, add a batch
    # This adds an active batch, so we don't need to do further checks
    click_view_product(site, vaccine_type)
    if not check_batch_number_and_expiry_date_exists(batch_number, expiry_date, True):
        add_vaccine_type_batch(batch_number, expiry_date)
        return True

    # If we get this far, the batch does exists but is currently INACTIVE
    # This reactivates the batch
    if not check_batch_number_is_active_with_date(batch_number, expiry_date, True):
        click_reactivate_batch_link(batch_number)
        click_reactivate_batch_confirmation_button()

def add_site_vaccine(site, vaccine, vaccine_type, batch_number, expiry_date):
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
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_continue_to_confirm_batch_details_button")

    # vaccines_check_and_confirm_page
    click_confirm_add_vaccine_and_batch_button()
    attach_screenshot("clicked_confirm_add_vaccine_and_batch_button")

def add_vaccine_type_batch(batch_number, expiry_date):
    click_add_batch_link()
    attach_screenshot("clicked_add_batch_link")
    enter_batch_number(batch_number)
    attach_screenshot("entered_batch_number")
    enter_expiry_date(expiry_date)
    attach_screenshot("entered_expiry_date")
    click_continue_to_confirm_batch_details_button()
    attach_screenshot("clicked_continue_to_confirm_batch_details_button")

    # vaccines_check_and_confirm_page
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

def enter_vaccine_details_and_click_continue_to_check_and_confirm(vaccinate_decision, care_model, vaccination_date, vaccine, vaccine_type2, vaccination_site,  batch_number, batch_expiry_date, dose_amount, vaccinator, vaccination_comments, legal_mechanism, no_vaccination_reason=None):
    if vaccinate_decision.lower() == 'yes':
        click_yes_vaccinated_radiobutton()
        attach_screenshot("clicked_yes_vaccinated_radiobutton")

        click_vaccine_type(vaccine_type2)
        attach_screenshot("clicked_vaccine_type")
        set_vaccination_date(vaccination_date)
        attach_screenshot("vaccination_date_is_set")
        click_care_model_option(care_model)
        attach_screenshot("clicked_care_model_option")
        if care_model == "Care home":
            enter_care_home_details("WHITESTONES CARE HOME")
            attach_screenshot("entered_care_home_details")
        logging.debug("Vaccination legal mechanism is: " + legal_mechanism)
        logging.debug("Vaccinator to select is: " + vaccinator)
        if (legal_mechanism) != "Patient Group Direction (PGD)":
            select_vaccinator_name_and_council(vaccinator)
            attach_screenshot("selected_vaccinator_name_and_council")
        enter_vaccination_comments(vaccination_comments)
        attach_screenshot("entered_vaccination_comments")
        select_vaccination_site(vaccination_site)
        attach_screenshot("selected_vaccination_site")
        batch_number_to_select = batch_number.upper() + " - " + batch_expiry_date
        logging.debug("Batch number to select is: " + batch_number_to_select)
        select_batch_number(batch_number_to_select)
        attach_screenshot("selected_batch_number")
        enter_dose_amount_value(dose_amount)
        attach_screenshot("entered_dose_amount_value")

        if click_continue_to_check_and_confirm_screen_button() == True:
            vaccination_date = format_date(vaccination_date, "safari")
            set_vaccination_date(vaccination_date)
            attach_screenshot("vaccination_date_is_set")
            select_batch_number(batch_number_to_select)
            attach_screenshot("selected_batch_number")

            click_continue_to_check_and_confirm_screen_button()
            attach_screenshot("clicked_continue_to_check_and_confirm_screen_button")

    else:
        click_not_vaccinated_radiobutton()
        attach_screenshot("clicked_not_vaccinated_radiobutton")
        if no_vaccination_reason is not None:
            select_reason_for_no_vaccination(no_vaccination_reason)
            attach_screenshot("selected_reason_for_no_vaccination")
            click_save_and_return_button_on_record_vaccinated_page
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
