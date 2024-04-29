import os
from helpers.apiHelper import ApiHelper
from helpers.datetimeHelper import DatetimeHelper
from helpers.playwrightHelper import PlaywrightHelper
import pytest
from playwright.sync_api import sync_playwright
import allure

playwright_helper_instance = None
api_helper = None
datetime_helper = None
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
    global api_helper, datetime_helper, playwright_helper_instance, config

    working_directory = get_working_directory()
   
    if playwright_helper_instance is None:
        playwright_helper_instance = PlaywrightHelper(working_directory, config)  

    if api_helper is None:
        api_helper = ApiHelper()

    if datetime_helper is None:
        datetime_helper = DatetimeHelper()        

def load_config_from_env():
    config = {
        "test_environment": os.environ.get("TEST_ENVIRONMENT", "qa"),
        "headless_mode": os.environ.get("HEADLESS_MODE",""),
        "browser": os.environ.get("BROWSER", "chrome"),
        "device": os.environ.get("DEVICE", "iphone_12"),
        "timeout_seconds": int(os.environ.get("TIMEOUT_SECONDS", 10)),
        "credentials": {
            "ravs_password": os.environ.get("RAVS_PASSWORD", "")
        }
    }
    return config      

def attach_screenshot(filename):
    if config["browser"] == "mobile":
        filename = config["browser"].upper() + "_" + config["device"] + "_" + get_browser_version() + "_" + filename + "_"
    else:
        filename = config["browser"].upper() + "_" + get_browser_version() + "_" + filename + "_"
    screenshot = capture_screenshot(filename)
    allure.attach.file(screenshot, name=f"{filename}", attachment_type=allure.attachment_type.PNG)

config = load_config_from_env()

mobile_devices = get_mobile_devices()

@pytest.fixture(scope="session", autouse=True)
def initialize_session():
    initialize_helpers()

@pytest.fixture(scope="session")
def playwright_helper():
    return playwright_helper_instance

@pytest.fixture(scope="function")
def api_helper():
    return api_helper

@pytest.fixture(scope="function")
def datetime_helper():
    return datetime_helper

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

def wait_for_page_to_load(timeout=10):
    playwright_helper_instance.wait_for_page_to_load(timeout)

def check_element_exists(element, wait=False):
    try:
        return playwright_helper_instance.check_element_exists(element, wait)
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def scroll_into_view(element):
    return playwright_helper_instance.scroll_into_view(element)

def wait_for_element_to_appear(selector):
    playwright_helper_instance.wait_for_element_to_appear(selector)

def clear_element(element):
    return playwright_helper_instance.clear_element(element)

def capture_screenshot(filename):
    return playwright_helper_instance.capture_screenshot(filename)

def find_element_and_perform_action(element, action, inputValue=None):
    return playwright_helper_instance.find_element_and_perform_action(element, action, inputValue)

def release_mouse():
    return playwright_helper_instance.release_mouse()