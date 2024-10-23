import os
import re
from helpers.apiHelper import ApiHelper
from helpers.datetimeHelper import DatetimeHelper
from helpers.playwrightHelper import PlaywrightHelper
import pytest
from playwright.sync_api import sync_playwright
import allure
import logging

playwright_helper_instance = None
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
    global api_helper_instance, datetime_helper_instance, playwright_helper_instance, config

    working_directory = get_working_directory()

    if playwright_helper_instance is None:
        playwright_helper_instance = PlaywrightHelper(working_directory, config)

    if api_helper_instance is None:
        api_helper_instance = ApiHelper()

    if datetime_helper_instance is None:
        datetime_helper_instance = DatetimeHelper()

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

@pytest.fixture(scope="session", autouse=True)
def initialize_session():
    initialize_helpers()
    yield
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

def quit_browser():
    playwright_helper_instance.quit_browser()

def get_current_url():
    return playwright_helper_instance.get_current_url()

def get_browser_version():
    return playwright_helper_instance.get_browser_version()

def get_current_url():
    return playwright_helper_instance.get_current_url()

def find_elements(selector):
    return playwright_helper_instance.find_elements(selector)

def wait_for_page_to_load(timeout=1):
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

def check_element_enabled(element, wait=False):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)
    elif isinstance(element, str):
        element = get_element_by_type(element)
    try:
        return playwright_helper_instance.check_element_enabled(element, wait)
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

def capture_screenshot(filename):
    return playwright_helper_instance.capture_screenshot(filename)

def find_element_and_perform_action(element, action, inputValue=None):
    if isinstance(element, (tuple, list)):
        element = get_element_by_type(*element)  # Unpack the tuple/list
    else:
        # If it's a string, treat it as a selector directly
        element = get_element_by_type(element)
    return playwright_helper_instance.find_element_and_perform_action(element, action, inputValue)

def click_cell_in_row(row_name, cell_index):
    return playwright_helper_instance.click_cell_in_row(row_name, cell_index)

def click_link_in_row(row_name, link_index):
    return playwright_helper_instance.click_link_in_row(row_name, link_index)

def get_element_by_type(locator_type, locator_value=None, name=None):
    return playwright_helper_instance.get_element_by_type(locator_type, locator_value, name)

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

def get_date_value(date):
    return datetime_helper_instance.get_date_value(date)

