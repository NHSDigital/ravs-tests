from asyncio import sleep
import csv
from logging.handlers import RotatingFileHandler
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse
from pages.login_page import *
from pages.home_page import *
from pages.nhs_signin_page import *
from pages.reports_check_and_confirm_page import *
from pages.reports_creating_report_page import *
from pages.reports_data_selection_page import *
from pages.reports_date_range_selection_page import *
import logging
from init_helpers import *
from conftest import *
from pages.reports_site_selection_page import *
from pages.reports_vaccine_selection_page import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/reports.feature')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Or any other level like INFO, WARNING, etc.

# Create a rotating file handler to log to tox.log
log_handler = RotatingFileHandler('tox.log', maxBytes=1024*1024, backupCount=3)  # Log rotation (optional)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add the handler to the logger
logger.addHandler(log_handler)

def validate_report_headers(file_path, expected_headers):
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            headers = next(reader)

            # Check headers
            if headers == expected_headers:
                logger.info("Headers are valid!")
                logger.info(headers)
                return True, headers
            else:
                logger.info("Headers are invalid!")
                logger.info("Expected Headers:")
                logger.info(expected_headers)
                logger.info("Found Headers:")
                logger.info(headers)

                # Find missing or extra headers
                missing_headers = [h for h in expected_headers if h not in headers]
                extra_headers = [h for h in headers if h not in expected_headers]

                if missing_headers:
                    logger.info("Missing Headers:")
                    logger.info(missing_headers)
                if extra_headers:
                    logger.info("Extra Headers:")
                    logger.info(extra_headers)

                return False, headers

    except Exception as e:
        logger.error(f"An error occurred while validating headers: {e}")
        return False, None

def validate_value_in_header(file_path, header, value):
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Ensure the specified header exists
            if header not in reader.fieldnames:
                logger.error(f"Header '{header}' not found in the report.")
                return False

            # Search for the value under the specified header
            for row in reader:
                if row.get(header) == value:
                    logger.info(f"Value '{value}' found under header '{header}' in the report.")
                    return True

            logger.error(f"Value '{value}' not found under header '{header}' in the report.")
            return False
    except Exception as e:
        logger.error(f"An error occurred while searching for value '{value}' under header '{header}': {e}")
        return False

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # You can add logging setup here if needed
    logger.info("Logging setup complete")
    yield
    logger.info("Test session complete")

@pytest.fixture(scope='function')
def shared_data():
    data = {}
    yield data
    data.clear()

@pytest.mark.reports
@given("I am logged into the RAVS app")
def logged_into_ravs_app(navigate_and_login):
    pass

@when("I click the reports navigation link")
def I_click_reports_nav_link():
    click_reports_nav_link()
    attach_screenshot("reports_navigation_link_clicked")
    logging.info("logged_in_and_reports_navigation_link_clicked")

@then("the reports page should be displayed")
def the_reports_page_should_be_displayed():
    assert check_create_report_button_exists() == True
    attach_screenshot("reports_page_loads_and_create_report_button_is_visible")
    logging.info("reports_page_loads_and_create_report_button_is_visible")

@when("I click the create report button")
def I_click_create_report_button():
    click_create_report_button()
    attach_screenshot("create_report_button_is_clicked")
    logging.info("logged_in_and_create_report_button_clicked")

@then("the choose dates page should be displayed")
def the_choose_dates_page_should_be_displayed():
    assert check_today_radio_button_exists() == True
    attach_screenshot("choose_dates_range_page_should_be_displayed")
    logging.info("choose_dates_range_page_should_be_displayed")

@given(parse('I am logged into the RAVS app with the {username}'))
def logged_into_ravs_app_with_username(username):
    navigate_and_login_with_username(username)

@then("the `No vaccination data to report on` message should be displayed")
def the_no_vaccination_data_to_report_on_message_should_be_displayed():
    assert check_no_vaccination_data_to_report_message_exists() == True
    attach_screenshot("no_vaccination_data_to_report_message_exists")
    logging.info("no_vaccination_data_to_report_message should be visible")

@then("the Create report button should be disabled")
def the_create_report_button_should_be_disabled():
    assert check_create_report_button_enabled() == False
    attach_screenshot("Create report button should be disabled")
    logging.info("Create report button should be disabled")

@when(parse('I click the {day} radio button and click Continue'))
def I_click_date_range_button_to_generate_reports(day):
    click_day_range_radio_button(day)
    if day == "Select a custom date range up to 31 days":
        from_date = format_date(str(get_date_value("today-31")), config["browser"])
        enter_from_date(from_date)
        to_date = format_date(str(get_date_value("today")), config["browser"])
        enter_to_date(to_date)
    attach_screenshot("day_range_radio_button_is_clicked_and_date_range_Selected")
    logging.info("day_range_radio_button_is_clicked_and_date_range_Selected")
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")

@then("the choose vaccines page should be displayed")
def the_choose_vaccines_page_should_be_displayed():
    assert check_covid_check_box_exists() == True
    attach_screenshot("Choose vaccines page should be visible")
    logging.info("Choose vaccines page should be visible")

@then("the user should not be able to proceed to choose a vaccine")
def the_user_should_not_be_able_to_proceed_to_choose_a_vaccine():
    assert check_no_date_selected_error_message_link_exists() == True
    assert check_no_date_selected_error_message_text_exists() == True
    attach_screenshot("no_date_selected_error_message_should_exist")
    logging.info("no_date_selected_error_message_should_exist")

@when('I select no date range and click Continue')
def I_select_no_date_range_and_click_continue(shared_data):
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")

@when(parse('I select a invalid date range of {from_date} and {to_date} and click Continue'))
def I_click_date_range_button_to_generate_reports(shared_data, from_date, to_date):
    click_day_range_radio_button("Select a custom date range up to 31 days")
    if (from_date != "null" and to_date != "null"):
        from_date = format_date(str(get_date_value(from_date)), config["browser"])
        to_date = format_date(str(get_date_value(to_date)), config["browser"])
        enter_from_date(from_date)
        enter_to_date(to_date)
        attach_screenshot("day_range_radio_button_is_clicked_and_date_range_Selected")
        logging.info("day_range_radio_button_is_clicked_and_date_range_Selected")
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")
    shared_data["from_date"] = from_date
    shared_data["to_date"] = to_date

@then(parse('the error message {error_message} should be displayed'))
def the_error_message_for_reports_date_should_be_displayed(error_message, shared_data):
    if shared_data['from_date'] == None and shared_data['to_date'] == None:
        assert check_from_date_missing_error_message_link_exists() == True
        assert check_from_date_missing_error_message_text_exists() == True
        assert check_to_date_missing_error_message_link_exists() == True
        assert check_to_date_missing_error_message_text_exists() == True
    if 'today+' in shared_data['from_date'] and 'today' in shared_data['to_date']:
        assert check_from_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_from_date_must_be_in_the_past_error_message_link_exists() == True
    if shared_data['from_date'] =='today' and 'today+' in shared_data['to_date']:
        assert check_to_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_link_exists() == True
    if 'today+' in shared_data['from_date'] and 'today+' in shared_data['to_date']:
        assert check_from_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_from_date_must_be_in_the_past_error_message_link_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_text_exists() == True
        assert check_to_date_must_be_in_the_past_error_message_link_exists() == True
    attach_screenshot("Choose vaccines page should be visible")
    logging.info("Choose vaccines page should be visible")

@when('I click the today date range button and click continue')
def I_click_today_date_range_and_click_continue(shared_data):
    click_today_radio_button()
    attach_screenshot("clicked_today_radio_button")
    logging.info("clicked_today_radio_button")
    click_continue_to_reports_select_vaccine_button()
    attach_screenshot("clicked_continue_to_reports_select_vaccine_button")
    logging.info("clicked_continue_to_reports_select_vaccine_button")

@then("the choose sites page should be displayed")
def the_choose_sites_page_should_be_displayed():
    assert check_site_check_box_exists("ALBERT HOUSE") == True
    attach_screenshot("check_choose_sites_page_is_displayed")
    logging.info("check_choose_sites_page_is_displayed")

@when(parse('I select the site {site} and click continue'))
def I_select_vaccinetype_and_click_continue(shared_data, site):
    check_site_check_box(site)
    attach_screenshot("clicked_" + site.lower() + "_check_box_on_reports_page")
    logging.info("clicked_" + site.lower() + "_check_box_on_reports_page")
    click_continue_to_reports_select_data_button()
    attach_screenshot("clicked_continue_to_reports_select_data_button")
    logging.info("clicked_continue_to_reports_select_data_button")

@then("the choose data page should be displayed and all data options should be checked by default")
def the_choose_data_page_should_be_displayed():
    assert check_reports_data_check_box_exists("Patients") == True
    assert check_reports_data_check_box_checked("Patients") == True
    assert check_reports_data_check_box_checked("Staff") == True
    assert check_reports_data_check_box_checked("Site or delivery team") == True
    assert check_reports_data_check_box_checked("Assessment and consent") == True
    assert check_reports_data_check_box_checked("Vaccination") == True
    attach_screenshot("check_choose_data_pages_reports_exists")
    logging.info("check_choose_data_pages_reports_exists")

@then("the check and confirm page should be displayed")
def the_check_and_confirm_page_should_be_displayed():
    assert check_reports_change_data_button_exists() == True
    attach_screenshot("check_reports_change_data_pages_reports_exists")
    logging.info("check_reports_change_data_pages_reports_exists")

@when('I click Confirm and create report button in the check and confirm page')
def I_click_confirm_to_generate_report(shared_data):
    click_continue_to_confirm_and_create_report_button()
    attach_screenshot("clicked_continue_to_confirm_and_create_report_button")
    logging.info("clicked_continue_to_confirm_and_create_report_button")

@then("Creating your page element should be displayed and Download Report button should be visible")
def the_check_and_confirm_page_should_be_displayed():
    assert check_reports_download_report_button_exists() == True
    attach_screenshot("check_reports_change_data_pages_reports_exists")
    logging.info("check_reports_change_data_pages_reports_exists")

@when('I click download report button')
def I_click_confirm_to_generate_report(shared_data):
    shared_data['report_download_path'] = click_reports_download_report_button()
    attach_screenshot("clicked_reports_download_report_button")
    logging.info("clicked_reports_download_report_button")

@then("the report is downloaded successfully")
def the_report_is_downloaded_successfully(shared_data):
    assert os.path.exists(shared_data['report_download_path']), f"Downloaded file not found: {shared_data['report_download_path']}"
    attach_screenshot("check_report_downloaded")
    logger.info("check_report_downloaded_to_" + str(shared_data['report_download_path']))
    expected_headers = [
    "NhsNumber", "PatientName", "Gender", "DateOfBirth", "Address", "Postcode",
    "SiteName", "SiteODS", "OrganisationName", "OrganisationODS", "CareModel",
    "Vaccinated", "NoVaccinationReason", "AssessmentDate", "Consented", "ConsentType",
    "ConsentingPersonName", "ConsentingPersonRelationship", "EligibilityType", "StaffType",
    "AssessmentComments", "VaccinationDate", "Vaccine", "VaccineProduct", "DoseAmount",
    "VaccineRoute", "PrescribingMethod", "BatchNumber", "BatchExpiryDate", "AuditType",
    "DateEntered", "UserEnteringData", "VaccinationComments", "AssessingClinician",
    "VaccinatingClinician", "ConsentingClinician"
]
    is_valid, _ = validate_report_headers(shared_data['report_download_path'], expected_headers)
    assert is_valid, "Report headers are invalid. See logs for details."

@then(parse("the report is downloaded successfully and contains the vaccine record for {nhs_number}"))
def the_report_is_downloaded_successfully(shared_data, nhs_number):
    assert os.path.exists(shared_data['report_download_path']), f"Downloaded file not found: {shared_data['report_download_path']}"
    attach_screenshot("check_report_downloaded")
    logger.info("check_report_downloaded_to_" + str(shared_data['report_download_path']))
    expected_headers = [
    "NhsNumber", "PatientName", "Gender", "DateOfBirth", "Address", "Postcode",
    "SiteName", "SiteODS", "OrganisationName", "OrganisationODS", "CareModel",
    "Vaccinated", "NoVaccinationReason", "AssessmentDate", "Consented", "ConsentType",
    "ConsentingPersonName", "ConsentingPersonRelationship", "EligibilityType", "StaffType",
    "AssessmentComments", "VaccinationDate", "Vaccine", "VaccineProduct", "DoseAmount",
    "VaccineRoute", "PrescribingMethod", "BatchNumber", "BatchExpiryDate", "AuditType",
    "DateEntered", "UserEnteringData", "VaccinationComments", "AssessingClinician",
    "VaccinatingClinician", "ConsentingClinician"
]
    is_valid, _ = validate_report_headers(shared_data['report_download_path'], expected_headers)
    assert is_valid, "Report headers are invalid. See logs for details."

    vaccination_date = shared_data.get("vaccination_date")
    vaccinated_decision = shared_data["vaccinated_decision"]
    consent_given_by =  shared_data['consent_given_by']
    eligibility_type = shared_data['eligibility_type']
    patient_name = shared_data['patient_name']

    if vaccination_date:
        # Convert the vaccination date from shared_data to a datetime object
        vaccination_date_obj = datetime.strptime(vaccination_date, "%d/%m/%Y")  # Adjust format as needed
        current_date = datetime.now()
        date_diff = (current_date - vaccination_date_obj).days

        if 0 <= date_diff <= 31:
            # If vaccination date is within the last 31 days, ensure all columns have values
            logger.info(f"Vaccination date '{vaccination_date}' is within the last 31 days. Verifying all columns have values...")

            with open(shared_data['report_download_path'], mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                rows = list(reader)
                last_row = rows[-1] if rows else None

                if last_row:
                    logger.info(f"Validating the latest row for vaccination date: {vaccination_date}...")

                if 0 <= date_diff <= 31:
                    # If vaccination date is within the last 31 days, ensure all columns have values
                    logger.info(f"Vaccination date '{vaccination_date}' is within the last 31 days. Verifying all columns in the last row...")

                    for header in expected_headers:

                        if header == "NoVaccinationReason":
                            if vaccinated_decision.lower() == "yes":
                                assert not last_row[header], (
                                    f"Column 'NoVaccinationReason' should be empty for NHS number {shared_data['nhs_number']} as vaccinated_decision is 'yes'."
                                )
                            else:
                                assert last_row[header], (
                                    f"Missing value in column 'NoVaccinationReason' for NHS number {shared_data['nhs_number']}."
                                )
                        elif header in ["ConsentingPersonName", "ConsentingPersonRelationship"]:
                            if consent_given_by == "Patient (informed consent)":
                                assert not last_row[header], (
                                    f"Column '{header}' should be empty for NHS number {shared_data['nhs_number']} as consent given by patient (informed consent)."
                                )
                            else:
                                assert last_row[header], (
                                    f"Missing value in column '{header}' for NHS number {shared_data['nhs_number']}."
                                )
                        elif header == "StaffType":
                            if eligibility_type == "Healthcare workers":
                                assert last_row[header], (
                                    f"Column 'StaffType' should not be empty for NHS number {shared_data['nhs_number']} as eligibility_type is 'Healthcare workers'."
                                )
                            else:
                                assert not last_row[header], (
                                    f"Column 'StaffType' should be empty for NHS number {shared_data['nhs_number']} as eligibility_type is not 'Healthcare workers'."
                                )
                        else:
                            # For other columns, ensure they are not empty
                            assert last_row[header], (
                                f"Missing value in column '{header}' for NHS number {shared_data['nhs_number']}."
                            )

                    # Validate the presence of the vaccination date in the last row
                    assert last_row["VaccinationDate"] == vaccination_date, (
                        f"Value '{vaccination_date}' not found in the 'VaccinationDate' column of the last row."
                    )

                    # Validate the presence of the NHS number in the last row
                    assert last_row["NhsNumber"] == shared_data["nhs_number"], (
                        f"Value '{shared_data['nhs_number']}' not found in the 'NhsNumber' column of the last row."
                    )

                    assert last_row["PatientName"] == shared_data["patient_name"], (
                        f"Mismatch in 'PatientName': expected '{shared_data['patient_name']}' but found '{last_row['PatientName']}'."
                    )

                else:
                    # If vaccination date is more than 31 days old, ensure the last row does not have this date
                    assert last_row["VaccinationDate"] != vaccination_date, (
                        f"Row with vaccination date '{vaccination_date}' found in the last row, but it should not be present since it's older than 31 days."
                    )

                    logger.info(f"Vaccination date '{vaccination_date}' is correctly not present in the last row of the report.")
        else:
            logger.warning("The report file is empty. No rows to validate.")


@when(parse('I select the vaccine type {vaccineType} and click continue'))
def I_select_vaccinetype_and_click_continue(shared_data, vaccineType):
    click_vaccine_check_box_on_reports_page(vaccineType)
    attach_screenshot("clicked_" + vaccineType.lower() + "_check_box_on_reports_page")
    logging.info("clicked_" + vaccineType.lower() + "_check_box_on_reports_page")
    click_continue_to_reports_select_site_button()
    attach_screenshot("clicked_continue_to_reports_select_site_button")
    logging.info("clicked_continue_to_reports_select_site_button")

@then("the choose sites page should be displayed")
def the_choose_sites_page_should_be_displayed():
    assert check_site_check_box_exists("ALBERT HOUSE") == True
    attach_screenshot("check_choose_sites_page_is_displayed")
    logging.info("check_choose_sites_page_is_displayed")

@when(parse('I click continue on the data page'))
def I_select_data_and_click_continue(shared_data):
    click_continue_to_reports_select_data_button()
    attach_screenshot("clicked_continue_to_reports_select_data_button")
    logging.info("clicked_continue_to_reports_select_data_button")

@then("the report is downloaded successfully")
def the_report_is_downloaded_successfully(shared_data):
    assert os.path.exists(shared_data['report_download_path']), f"Downloaded file not found: {shared_data['report_download_path']}"
    attach_screenshot("check_report_downloaded")
    logger.info("check_report_downloaded_to_" + str(shared_data['report_download_path']))
    expected_headers = [
    "NhsNumber", "PatientName", "Gender", "DateOfBirth", "Address", "Postcode",
    "SiteName", "SiteODS", "OrganisationName", "OrganisationODS", "CareModel",
    "Vaccinated", "NoVaccinationReason", "AssessmentDate", "Consented", "ConsentType",
    "ConsentingPersonName", "ConsentingPersonRelationship", "EligibilityType", "StaffType",
    "AssessmentComments", "VaccinationDate", "Vaccine", "VaccineProduct", "DoseAmount",
    "VaccineRoute", "PrescribingMethod", "BatchNumber", "BatchExpiryDate", "AuditType",
    "DateEntered", "UserEnteringData", "VaccinationComments", "AssessingClinician",
    "VaccinatingClinician", "ConsentingClinician"
]
    is_valid, _ = validate_report_headers(shared_data['report_download_path'], expected_headers)
    assert is_valid, "Report headers are invalid. See logs for details."

@then("the choose data page should be displayed")
def the_choose_data_page_should_be_displayed():
    assert check_reports_data_check_box_exists("Patients") == True
    attach_screenshot("check_choose_data_pages_reports_exists")
    logging.info("check_choose_data_pages_reports_exists")

