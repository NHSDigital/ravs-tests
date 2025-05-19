import os
import re
import shutil
import logging
from helpers.apiHelper import ApiHelper
from helpers.datetimeHelper import DatetimeHelper
from helpers.playwrightHelper import PlaywrightHelper
from helpers.mockdatabaseHelper import MockDatabaseHelper
import pytest
from playwright.sync_api import sync_playwright
import allure
from _pytest.main import Session

# Singleton instances
playwright_helper_instance = None
mockdatabase_helper_instance = None
api_helper_instance = None
datetime_helper_instance = None
chrome_binary_path = None
config = None
_device_cache = None

def get_playwright_helper():
    global playwright_helper_instance
    if playwright_helper_instance is None:
        playwright_helper_instance = PlaywrightHelper(get_working_directory(), config)
    return playwright_helper_instance

def get_working_directory():
    cwd = os.getcwd()
    if "api" in cwd:
        working_dir = os.path.join(cwd, "../../source/")
    elif "source" in cwd:
        working_dir = os.path.join(cwd, "/")
    else:
        working_dir = os.path.join(cwd, "")
    print("Working directory is : " + working_dir)
    return working_dir

def get_mobile_devices():
    global _device_cache
    if _device_cache is None:
        with sync_playwright() as p:
            _device_cache = {
                "iPhone_12": p.devices["iPhone 12"],
                "iPhone_11": p.devices["iPhone 11"],
                "Pixel_5": p.devices["Pixel 5"],
                "Pixel_4": p.devices["Pixel 4"]
            }
    return _device_cache

def initialize_helpers():
    global api_helper_instance, datetime_helper_instance, mockdatabase_helper_instance, config

    if api_helper_instance is None:
        api_helper_instance = ApiHelper()

    if datetime_helper_instance is None:
        datetime_helper_instance = DatetimeHelper()

    if mockdatabase_helper_instance is None:
        mock_data_file = os.path.join(get_working_directory(), "mock_data", "mock_patients.json")
        mockdatabase_helper_instance = MockDatabaseHelper(mock_data_file)

def load_config_from_env():
    return {
        "test_environment": os.environ.get("TEST_ENVIRONMENT", "qa"),
        "headless_mode": os.environ.get("HEADLESS_MODE", ""),
        "browser": os.environ.get("BROWSER", "chrome"),
        "device": os.environ.get("DEVICE", "iphone_12"),
        "timeout_seconds": int(os.environ.get("TIMEOUT_SECONDS", 10)),
        "credentials": {
            "ravs_password": os.environ.get("RAVS_PASSWORD", "")
        }
    }

def sanitize_filename(filename):
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename).strip().strip('.')
    return sanitized[:200]

def attach_screenshot(filename):
    logging.basicConfig(level=logging.DEBUG)

    working_dir = get_working_directory()
    directory = os.path.join(working_dir, 'data', 'attachments')
    os.makedirs(directory, exist_ok=True)

    if config["browser"] == "mobile":
        filename = f'{config["test_environment"]}_{config["browser"]}_{config["device"]}_{get_browser_version()}_{filename}.png'
    else:
        filename = f'{config["test_environment"]}_{config["browser"]}_{get_browser_version()}_{filename}.png'

    full_path = os.path.join(directory, sanitize_filename(filename))

    try:
        screenshot = capture_screenshot(full_path)
        if screenshot and os.path.exists(full_path):
            allure.attach.file(full_path, name=filename, attachment_type=allure.attachment_type.PNG)
            logging.debug(f"Screenshot attached at: {full_path}")
        else:
            logging.error(f"Screenshot capture failed or file not found at: {full_path}")
    except Exception as e:
        logging.error(f"Failed to capture screenshot: {e}")

def resolve_element(element):
    if isinstance(element, (tuple, list)):
        return get_playwright_helper().get_element_by_type(*element)
    return get_playwright_helper().get_element_by_type(element)

@pytest.fixture(scope="session")
def shared_data():
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
    return get_playwright_helper()

@pytest.fixture(scope="session")
def api_helper():
    return api_helper_instance

@pytest.fixture(scope="session")
def datetime_helper():
    return datetime_helper_instance

def get_app_url(test_environment):
    if "dev" in test_environment.lower():
        return "https://www.ravs-dev.england.nhs.uk"
    elif "qa" in test_environment.lower():
        return "https://www.ravs-qa.england.nhs.uk"
    else:
        raise ValueError(f"Unknown test environment: {test_environment}")

def navigate_to_url(url):
    get_playwright_helper().navigate_to_url(url)

def check_element_exists(element, wait=False):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().check_element_exists(resolved_element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_enabled(element, wait=False):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().check_element_enabled(resolved_element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_checked(element, wait=False):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().check_element_checked(resolved_element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def check_element_by_locator_enabled(element, wait=False):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().check_element_by_locator_enabled(resolved_element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def after_all():
    env = os.environ.get("TEST_ENVIRONMENT", "qa")
    product = "RAVS"
    properties_dict = {"PRODUCT": product, "ENV": env}

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

def quit_browser():
    get_playwright_helper().quit_browser()

def get_browser_version():
    return get_playwright_helper().get_browser_version()

def capture_screenshot(filename):
    return get_playwright_helper().capture_screenshot(filename)

def click_link_in_row(row_name, link_index):
    return get_playwright_helper().click_link_in_row(row_name, link_index)

def javascript_click(element):
    element = resolve_element(element)
    return get_playwright_helper().javascript_click(element)

def find_element_and_perform_action(element, action, inputValue=None):
    element = resolve_element(element)
    wait_until_spinner_disappears()
    return get_playwright_helper().find_element_and_perform_action(element, action, inputValue)

def wait_until_spinner_disappears():
    SPINNER_ELEMENT = ("role", "status")
    return wait_for_element_to_disappear(SPINNER_ELEMENT)

def wait_for_element_to_appear(element, timeout=10):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().wait_for_element_to_appear(resolved_element, timeout)
    except Exception as e:
        pytest.fail(f"An error occurred while waiting for element to appear: {e}")

def wait_for_element_to_disappear(element, timeout=10):
    try:
        resolved_element = resolve_element(element)
        return get_playwright_helper().wait_for_element_to_disappear(resolved_element, timeout)
    except Exception as e:
        pytest.fail(f"An error occurred while waiting for element to disappear: {e}")

config = load_config_from_env()

mobile_devices = get_mobile_devices()
