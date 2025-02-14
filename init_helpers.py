import os
import re
import shutil
from helpers.apiHelper import ApiHelper
from helpers.datetimeHelper import DatetimeHelper
from helpers.playwrightHelper import PlaywrightHelper
from helpers.mockdatabaseHelper import MockDatabaseHelper
import pytest
from playwright.sync_api import sync_playwright
import allure
import logging
from _pytest.main import Session

playwright_helper_instance = None
mockdatabase_helper_instance = None
api_helper_instance = None
datetime_helper_instance = None
chrome_binary_path = None
config = None

def get_working_directory():
    if "api" in os.getcwd():
        working_dir = os.path.join(os.getcwd(), "../../source/")
    elif "source" in os.getcwd():
        working_dir = os.path.join(os.getcwd(), "/")
    else:
        working_dir = os.path.join(os.getcwd(), "")
    print("Working directory is : " + working_dir)
    return working_dir

def get_mobile_devices():
    with sync_playwright() as p:
        return {
            "iPhone_12": p.devices["iPhone 12"],
            "iPhone_11": p.devices["iPhone 11"],
            "Pixel_5": p.devices["Pixel 5"],
            "Pixel_4": p.devices["Pixel 4"]
        }

def initialize_helpers():
    global api_helper_instance, datetime_helper_instance, playwright_helper_instance, mockdatabase_helper_instance, config

    working_directory = get_working_directory()
    mock_data_file = os.path.join(working_directory, "mock_data", "mock_patients.json")

    if playwright_helper_instance is None:
        playwright_helper_instance = PlaywrightHelper(working_directory, config)

    if api_helper_instance is None:
        api_helper_instance = ApiHelper()

    if datetime_helper_instance is None:
        datetime_helper_instance = DatetimeHelper()

    if mockdatabase_helper_instance is None:
        mockdatabase_helper_instance = MockDatabaseHelper(mock_data_file)

def load_config_from_env():
    config = {
        "test_environment": os.environ.get("TEST_ENVIRONMENT", "qa"),
        "headless_mode": os.environ.get("HEADLESS_MODE",""),
        "browser": os.environ.get("BROWSER", "chrome"),
        "device": os.environ.get("DEVICE", "iphone_12"),
        "timeout_seconds": int(os.environ.get("TIMEOUT_SECONDS", 1)),
        "credentials": {
            "ravs_password": os.environ.get("RAVS_PASSWORD", "")
        }
    }
    return config

def sanitize_filename(filename):
    """
    Remove or replace illegal characters in filenames for cross-platform compatibility.
    For example, Windows does not allow: \\ / : * ? " < > |
    """
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)

    # Remove leading/trailing spaces and periods (invalid in some OS)
    sanitized = sanitized.strip().strip('.')

    return sanitized[:200]

def attach_screenshot(filename):
    logging.basicConfig(level=logging.DEBUG)

    working_dir = get_working_directory()

    # Dynamically generate the filename
    if config["browser"] == "mobile":
        filename = f'{config["test_environment"]}_{config["browser"]}_{config["device"]}_{get_browser_version()}_{filename}.png'
    else:
        filename = f'{config["test_environment"]}_{config["browser"]}_{get_browser_version()}_{filename}.png'

    # Sanitize the filename
    filename = sanitize_filename(filename)

    # Define the directory
    directory = os.path.join(working_dir, 'data', 'attachments')
    full_path = os.path.join(directory, filename)

    # Ensure the directory exists
    try:
        # Check if directory exists, create it if not
        if not os.path.exists(directory):
            logging.debug(f"Directory does not exist, creating it: {directory}")
            os.makedirs(directory, exist_ok=True)

        # Confirm that directory creation was successful
        if os.path.exists(directory):
            logging.debug(f"Directory verified: {directory}")
        else:
            logging.error(f"Failed to create directory: {directory}")
            return  # Abort if directory creation failed

        # Capture the screenshot
        logging.debug(f"Saving screenshot to: {full_path}")
        screenshot = capture_screenshot(full_path)

        # Check if screenshot was captured and file exists
        if screenshot and os.path.exists(full_path):
            allure.attach.file(full_path, name=filename, attachment_type=allure.attachment_type.PNG)
            logging.debug(f"Screenshot attached at: {full_path}")
        else:
            logging.error(f"Screenshot capture failed or file not found at: {full_path}")
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {e}")


config = load_config_from_env()

mobile_devices = get_mobile_devices()

@pytest.fixture(scope="session")
def shared_data():
    """
    Provide a session-scoped shared_data dictionary to share data across tests.
    """
    return {}

@pytest.fixture(scope="session", autouse=True)
def initialize_session(shared_data):
    initialize_helpers()
    yield
    after_all()
    shared_data.clear()
    quit_browser()

@pytest.fixture(scope="session")
def playwright_helper():
    return playwright_helper_instance

@pytest.fixture(scope="session")
def api_helper():
    return api_helper_instance

@pytest.fixture(scope="session")
def datetime_helper():
    return datetime_helper_instance

def get_app_url(test_environment):
    if test_environment is not None and "dev" in test_environment:
        return "https://www.ravs-dev.england.nhs.uk"
    elif test_environment is not None and "qa" in test_environment:
        return "https://www.ravs-qa.england.nhs.uk"
    else:
        raise ValueError(f"Unknown test environment: {test_environment}")

def navigate_to_url(url):
    playwright_helper_instance.navigate_to_url(url)

def get_total_scenarios_to_run(config, tags=None):
    """
    Calculate the total number of scenarios to run based on tags.
    Args:
        config: pytest Config object.
        tags: List of tags to filter scenarios.
    Returns:
        int: Total number of scenarios to be run.
    """
    session = Session.from_config(config)
    session.perform_collect()  # Collect all test items

    # Filter scenarios
    scenarios = [
        item for item in session.items
        if "pytest_bdd_scenario" in item.keywords  # Filter pytest-bdd scenarios
    ]

    if tags:
        scenarios = [
            scenario for scenario in scenarios
            if any(tag in scenario.keywords for tag in tags)  # Check if tags match
        ]

    total_scenarios = len(scenarios)
    print(f"Total scenarios to be run: {total_scenarios}")
    return total_scenarios

def after_all():
    # Add anything you want to happen after all the tests have completed here
    env = os.environ.get("TEST_ENVIRONMENT", "qa")
    product = "RAVS"
    properties_dict = {"PRODUCT": product, "ENV": env}
        # if PULL_REQUEST_ID:
        #     pull_request_id = PULL_REQUEST_ID.lower()
        #     if "pr-" in pull_request_id:
        #         env = os.path.join("PULL-REQUEST", PULL_REQUEST_ID)
        #         pull_request_link = os.path.join(
        #             select_repository_base_url(product),
        #             "pull",
        #             PULL_REQUEST_ID.upper().replace("PR-", ""),
        #         )
        #         properties_dict = {
        #             "PRODUCT": product,
        #             "ENV": env,
        #             "PULL-REQUEST": pull_request_link,
        #         }

    working_dir = get_working_directory()
    file_path = os.path.join(working_dir, 'allure-results', 'environment.properties')
    write_properties_file(file_path, properties_dict)

def write_properties_file(file_path, properties_dict):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if os.path.exists(file_path):
            os.remove(file_path)
        with open(file_path, "w") as file:
            for key, value in properties_dict.items():
                file.write(f"{key}={value}\n")
    except Exception as e:
        logging.debug(f"Failed to create environment properties file {file_path}: {e}")
        print(f"Error writing to {file_path}: {e}")

def quit_browser():
    playwright_helper_instance.quit_browser()

def get_accessibility_violations():
    return playwright_helper_instance.get_accessibility_violations()

def get_current_url():
    return playwright_helper_instance.get_current_url()

def add_cookie(url, cookie, value):
    return playwright_helper_instance.add_cookie(url, cookie, value)

def get_browser_version():
    return playwright_helper_instance.get_browser_version()

def get_current_url():
    return playwright_helper_instance.get_current_url()

def find_elements(selector):
    return playwright_helper_instance.find_elements(selector)

def wait_for_page_to_load(timeout=3):
    playwright_helper_instance.wait_for_page_to_load(timeout)

def check_element_exists(element, wait=False):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    elif isinstance(element, str):
        element = get_element_by_type(element)
    try:
        return playwright_helper_instance.check_element_exists(element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def get_checked_radio_button_text(name):
    try:
        return playwright_helper_instance.get_checked_radio_button_text(name)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def get_checked_radio_button_text(name):
    try:
        return playwright_helper_instance.get_checked_radio_button_text(name)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_enabled(element, wait=False):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    elif isinstance(element, str):
        element = get_element_by_type(element)
    try:
        return playwright_helper_instance.check_element_enabled(element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_checked(element, wait=False):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    elif isinstance(element, str):
        element = get_element_by_type(element)
    try:
        return playwright_helper_instance.check_element_checked(element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_by_locator_enabled(element, wait=False):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    else:
        element = get_element_by_type(element)
    try:
        return playwright_helper_instance.check_element_by_locator_enabled(element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def scroll_into_view(element):
    return playwright_helper_instance.scroll_into_view(element)

def wait_for_element_to_appear(element):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    else:
        element = get_element_by_type(element)
    return playwright_helper_instance.wait_for_element_to_appear(element)

def wait_for_element_to_disappear(element):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    else:
        element = get_element_by_type(element)
    return playwright_helper_instance.wait_for_element_to_disappear(element)

def capture_screenshot(filename):
    return playwright_helper_instance.capture_screenshot(filename)

def handle_unresponsive_page():
    return playwright_helper_instance.handle_unresponsive_page()

def click_and_get_download_path(element, action, timeout, download_dir='downloads'):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)  # Unpack the tuple/list
    else:
        # If it's a string, treat it as a selector directly
        element = get_element_by_type(element)
    return playwright_helper_instance.click_and_get_download_path(element, action, timeout, 'downloads')

def find_element_and_perform_action(element, action, inputValue=None):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)  # Unpack the tuple/list
    else:
        # If it's a string, treat it as a selector directly
        element = get_element_by_type(element)
    wait_until_page_loading_message_disappears()
    return playwright_helper_instance.find_element_and_perform_action(element, action, inputValue)

def mock_api_response():
    working_directory = get_working_directory()
    return playwright_helper_instance.mock_api_response(working_directory)

def wait_until_page_loading_message_disappears():
    PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
    return wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)

def click_cell_in_row(row_name, cell_index):
    return playwright_helper_instance.click_cell_in_row(row_name, cell_index)

def click_link_in_row(row_name, link_index):
    return playwright_helper_instance.click_link_in_row(row_name, link_index)

def get_element_by_type(locator_type, locator_value=None, name=None, exact=False):
    return playwright_helper_instance.get_element_by_type(locator_type, locator_value, name, exact)

def release_mouse():
    return playwright_helper_instance.release_mouse()

def format_date(date, browser):
    return datetime_helper_instance.format_date(date, browser)

def standardize_date_format(date):
    return datetime_helper_instance.standardize_date_format(date)

def date_format_with_day_of_week(date):
    return datetime_helper_instance.date_format_with_day_of_week(date)

def date_format_with_age(date):
    return datetime_helper_instance.date_format_with_age(date)

def date_format_with_name_of_month(date):
    return datetime_helper_instance.date_format_with_name_of_month(date)

def date_format_with_name_of_month_shortened(date):
    return datetime_helper_instance.date_format_with_name_of_month_shortened(date)

def get_date_value(date):
    return datetime_helper_instance.get_date_value(date)

