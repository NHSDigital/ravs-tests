import pytest
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
pytest.mark.recordvaccine = pytest.mark.mark(recordvaccine=True)
pytest.mark.addvaccine = pytest.mark.mark(addvaccine=True)
pytest.mark.addbatches = pytest.mark.mark(addbatches=True)

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

@pytest.fixture(scope='function')
def playwright_helper(request):
    helper = PlaywrightHelper(get_working_directory(), config)
    def teardown():
        try:
            helper.quit_browser()
        except Exception as e:
            print(f"An error occurred during teardown: {e}")
            raise

    request.addfinalizer(teardown)
    return helper

# Fixture for site parameter
@pytest.fixture(params=["NEELIMA HOUSE", "FRAZER HOUSE", "PAUL TOWERS"])
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

# Fixture for clicking back button
@pytest.fixture(scope='function')
def click_back_button_recording_consent(request):
    click_back_button()

# Fixture for logging in and navigating to appointments
@pytest.fixture(scope='function')
def login_and_navigate_to_appointments(site, care_model,  navigate_and_login):
    select_site(site)
    select_care_model(care_model)
    if care_model == "Care Home":
        enter_carehome_name("WHITESTONES CARE HOME")
    click_continue_to_record_a_vaccination_homepage()
    click_appointments_nav_link()

def set_vaccinator_location(site, care_model):
    select_site(site)
    select_care_model(care_model)
    if care_model == "Care Home":
        enter_carehome_name("WHITESTONES CARE HOME")
    click_continue_to_record_a_vaccination_homepage()

@pytest.fixture(scope='function')
def login_and_navigate_to_homepage(request, navigate_and_login):
    select_site("NEELIMA HOUSE")
    select_care_model("Vaccination Centre")
    click_continue_to_record_a_vaccination_homepage()

# Fixture for logging in and navigating to appointments open first patient
@pytest.fixture(scope='function')
def login_and_navigate_to_appointments_open_first_patient(request, navigate_and_login):
    attach_screenshot("user_has_logged_in")
    site = "ST JOHN'S HOUSE"
    care_model = "Vaccination Centre"
    select_site(site)
    attach_screenshot("user_has_selected_site")
    select_care_model(care_model)
    if care_model == "Care Home":
        enter_carehome_name("WHITESTONES CARE HOME")
    attach_screenshot("user_has_selected_site")
    attach_screenshot("user_has_selected_care_model")
    click_continue_to_record_a_vaccination_homepage()
    attach_screenshot("user_has_clicked_continue_to_ravs_homepage")
    click_appointments_nav_link()
    current_date = datetime.now()
    fromDate = datetime(2023, 12, 1)
    set_from_date(fromDate)
    click_active_from_date()
    toDate = datetime.today()
    set_to_date(toDate)
    click_active_to_date_today()
    click_first_patient()

# Fixture for logging in and navigating to find a patient
@pytest.fixture(scope='function')
def login_and_navigate_to_find_a_patient(request, login_and_set_vaccinator_location):
    set_vaccinator_location()
    if config["browser"] == "mobile":
        if check_navlink_bar_toggle_exists():
            click_navlinkbar_toggler()
    click_find_a_patient_nav_link()

# Fixture for logging in and finding a patient by NHS number
@pytest.fixture(scope='function')
def login_and_find_a_patient_by_NHS_Number(request, login_and_navigate_to_find_a_patient, nhs_number):
    enter_NHSNumber(nhs_number)
    click_search_for_patient_button()

# Fixture for navigating to find a patient by PDS search page
@pytest.fixture(scope='function')
def login_and_navigate_to_find_a_patient_by_pds_search_page(request):
    set_vaccinator_location()
    click_pds_search_nav_link()

# Fixture for navigating to appointments open first patient and clicking choose vaccine
@pytest.fixture(scope='function')
def goto_appointments_open_first_patient_and_click_choose_vaccine(request, login_and_navigate_to_appointments_open_first_patient):
    click_choose_vaccine_button()

# Fixture for navigating to appointments open first patient and clicking choose covid vaccine
@pytest.fixture(scope='function')
def goto_appointments_open_first_patient_and_click_choose_covid_vaccine(request, goto_appointments_open_first_patient_and_click_choose_vaccine):
    click_covid_radiobutton()

# Fixture for navigating to appointments open first patient and clicking choose seasonal flu vaccine
@pytest.fixture(scope='function')
def goto_appointments_open_first_patient_and_click_choose_seasonal_flu_vaccine(request, goto_appointments_open_first_patient_and_click_choose_vaccine):
    click_flu_radiobutton()

# # Fixture for selecting covid vaccine and going to record consent
# @pytest.fixture(scope='function')
# def select_covid_vaccine_and_goto_record_consent(request, goto_appointments_open_first_patient_and_click_choose_covid_vaccine):
#     click_continue_to_record_consent_button()

# Fixture for logging out
@pytest.fixture(scope='function')
def logout(request, navigate_and_login):
    if config["browser"] == "mobile":
        if check_navbar_toggle_exists():
            click_navbar_toggler()
            attach_screenshot("clicked_navbar_toggler")
    click_logout_button()
    attach_screenshot("clicked_log_out_button")

def click_find_a_patient_and_search_with_nhsnumber(nhs_number):
    if config["browser"] == "mobile":
        if check_navlink_bar_toggle_exists():
            click_navlinkbar_toggler()
    click_find_a_patient_nav_link()
    enter_NHSNumber(nhs_number)
    click_search_for_patient_button()
    attach_screenshot("entered_nhs_number_as" + nhs_number + "_and_clicked_search_for_patient_button")

def click_on_patient_search_result_and_click_choose_vaccine(name, vaccine):
    click_on_patient_name_search_result(name)
    immunisation_history_records = get_count_of_immunisation_history_records(vaccine)
    click_choose_vaccine_button()
    attach_screenshot("clicked_on_patient_" + name + "_and_clicked_choose_vaccine_button")
    return immunisation_history_records

def choose_vaccine_and_vaccine_type_for_patient(vaccine, vaccine_type):
    if "covid" in vaccine.lower():
        click_covid_radiobutton()
        click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type)
    elif "flu" in vaccine.lower():
        click_flu_radiobutton()
        click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccine_type)
    click_continue_to_assess_patient_button()
    attach_screenshot("selected_vaccine_" + vaccine + "_and_" + vaccine_type + "_and_clicked_continue_button")

def assess_patient_with_details_and_click_continue_to_consent(eligible_decision, eligibility_type, assessing_clinician, assessment_date, assessment_outcome, assessment_comments, eligibility_assessment_no_vaccine_given_reason=None):
    select_assessing_clinician_with_name_and_council(assessing_clinician)
    enter_comments_for_assessing_patient(assessment_comments)
    set_assessment_date(assessment_date)
    if eligible_decision.lower() == 'yes':
        click_eligible_yes_radiobutton()
        select_eligibility_type(eligibility_type)
        attach_screenshot("clicked_eligibility_yes_and_selected_eligibility_type")
    else:
        click_eligible_no_radiobutton()
        attach_screenshot("clicked_patient_not_eligible_radiobutton")
    if assessment_outcome.lower() == "give vaccine":
        click_give_vaccine_radiobutton()
        attach_screenshot("clicked_patient_give_vaccine_radio_button")
        click_continue_to_record_consent_button()
        attach_screenshot("clicked_continue_to_record_consent_button")
    else:
        click_vaccine_not_given_radiobutton()
        select_assessment_no_vaccination_reason(eligibility_assessment_no_vaccine_given_reason)
        attach_screenshot("select_patient_not_given_vaccine_after_assessing")
        click_save_and_return_button_on_assessment_screen()
        attach_screenshot("clicked_save_and_retrun_on_assessment_screen")

def record_consent_details_and_click_continue_to_vaccinate(consent_decision,  consent_given_by, person_consenting_name, relationship_to_patient,  consent_clinician, no_consent_reason=None):
    attach_screenshot("before_selecting_consent_clinician")
    select_consent_clinician_with_name_and_council(consent_clinician)
    if consent_decision.lower() == 'yes':
        click_yes_to_consent()
        select_consent_given_by_from_dropdown(consent_given_by)
        if consent_given_by != "Patient (informed consent)":
            enter_person_consenting_details(person_consenting_name)
            enter_relationship_to_patient(relationship_to_patient)
        click_continue_to_vaccinate_button()
        attach_screenshot("clicked_continue_to_vaccinate_button")
    else:
        click_no_to_consent()
        if no_consent_reason is not None:
            select_reason_for_no_consent(no_consent_reason)
        attach_screenshot("patient_decided_to_not_consent")
        click_save_and_return_button_on_record_consent_page()
        attach_screenshot("patient_decided_to_not_consent_saved_and_returned")

def enter_vaccine_details_and_click_continue_to_check_and_confirm(vaccinate_decision,  vaccination_date, vaccine, vaccine_type2, vaccination_route,  batch_number, batch_number_to_select, batch_expiry_date, dose_amount, prescribing_method, vaccinator, vaccination_comments, no_vaccination_reason=None):
    select_vaccinator_name_and_council(vaccinator)
    enter_vaccination_comments(vaccination_comments)
    set_vaccination_date(vaccination_date)
    if vaccinate_decision.lower() == 'yes':
        click_yes_vaccinated_radiobutton()
        if "covid" in (vaccine).lower():
            click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccine_type2)
        else:
            click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_vaccinated_page(vaccine_type2)
        select_vaccination_route(vaccination_route)
        select_batch_number(batch_number_to_select)
        enter_dose_amount_value(dose_amount)
        click_prescribing_method(prescribing_method)
        click_continue_to_check_and_confirm_screen_button()
    else:
        click_not_vaccinated_radiobutton()
        if no_vaccination_reason is not None:
            select_reason_for_no_vaccination(no_vaccination_reason)
            click_save_and_return_button_on_record_vaccinated_page
        attach_screenshot("patient_decided_to_not_vaccinate")
        click_save_and_return_button_on_record_vaccinated_page()
        attach_screenshot("patient_decided_to_not_vaccinate_saved_and_returned")

