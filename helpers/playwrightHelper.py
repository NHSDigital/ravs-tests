from asyncio.log import logger
import json
import time
from playwright.sync_api import sync_playwright, TimeoutError, Locator
from axe_core_python.sync_playwright import Axe
from requests import request
from init_helpers import *
import pytest
import logging
import platform
from helpers.mockdatabaseHelper import MockDatabaseHelper

class BasePlaywrightHelper:
    def __init__(self, working_directory, config):
        playwright_instance = sync_playwright().start()
        self.working_directory = working_directory
        self.screenshots_dir = "screenshots"
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        self.playwright = playwright_instance
        self.browser = None
        self.context = None
        self.page = None

    def launch_chromium(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(
                headless=headless_mode,
                args=["--fullscreen"]
            )
            self.context = self.browser.new_context(
                geolocation={"latitude": 51.5074, "longitude": -0.1278},  # London, UK
                permissions=["geolocation"],
                locale="en-GB",
                timezone_id="Europe/London"
            )
            self.context.add_cookies([
                {
                    "name": "ravs-cookie-consent",
                    "value": "false",
                    "domain": "www.ravs-dev.england.nhs.uk",
                    "path": "/"
                }
            ])
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Chromium: {e}")

    def launch_edge(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="msedge",headless=headless_mode, args=["--fullscreen"])
            self.context = self.browser.new_context()
            self.context.add_cookies([
                {
                    "name": "ravs-cookie-consent",
                    "value": "false",
                    "domain": "www.ravs-dev.england.nhs.uk",
                    "path": "/"
                }
            ])
            self.page = self.context.new_page()
        except Exception as e:
                print(f"Error launching Edge: {e}")

    def launch_safari(self, headless_mode):
        try:
            self.browser = self.playwright.webkit.launch(headless=headless_mode, args=["--fullscreen"])
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
                print(f"Error launching Safari: {e}")

    def launch_chrome(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode, args=["--fullscreen", "--disable-gpu", "--no-sandbox"])
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Chrome: {e}")

    def launch_firefox(self, headless_mode):
        try:
            self.browser = self.playwright.firefox.launch(headless=headless_mode, args=["--fullscreen"])
            self.page = self.browser.new_page()
            self.context = self.browser.new_context()
        except Exception as e:
            print(f"Error launching Firefox: {e}")

    def launch_mobile_browser(self, device_name, headless_mode):
        try:
            if "iphone_12" == device_name.lower():
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["iPhone 12"])
            elif "iphone_11" == device_name.lower():
                self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["iPhone 11"])
            elif "pixel_5" == device_name.lower():
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["Pixel 5"])
            else:
                self.browser = self.playwright.chromium.launch(channel='chromium', headless=headless_mode)
                self.context = self.browser.new_context(**self.playwright.devices["Galaxy S9+"])

            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching mobile browser for {device_name}: {e}")

    def capture_screenshot(self, full_path):
        try:
            self.page.wait_for_timeout(500)
            self.page.screenshot(path=full_path)
        except Exception as error:
            if "Timeout" in str(error):
                print('Screenshot taking timed out, ignoring...')
                return None
            else:
                raise error
        return full_path

    def get_browser_version(self):
        if self.browser:
            print(self.browser.version)
            return self.browser.version
        else:
            return None

    def close_browser(self):
        try:
            if self.context:
                self.context.close()
            if self.browser:
                self.browser.close()
            print("Browser closed successfully.")
        except Exception as e:
            print(f"An error occurred while closing the browser: {e}")

    def navigate_to_url(self,url):
        print(f"Navigating to URL: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state()

    def wait_for_page_to_load(self, timeout=0.1):
        try:
            self.page.wait_for_load_state('domcontentloaded', timeout=timeout * 1000)
            self.page.wait_for_selector('*', timeout=timeout * 1000)
        except Exception as e:
            print(f"Page did not fully load within {timeout} seconds. Proceeding anyway.")

    def find_elements(self, selector):
        return self.page.query_selector_all(selector)

    def get_element(self, locator_or_element, wait=False, timeout=5):
        """Utility method to get an element with optional waiting."""
        try:
            if isinstance(locator_or_element, str):
                # Wait for selector if specified
                if wait:
                    # Use state='attached' to ensure it's present in the DOM before checking visibility
                    self.page.wait_for_selector(locator_or_element, state="visible", timeout=timeout * 1000)
                    element = self.page.locator(locator_or_element)

                    # Ensure the element is visible and ready for interaction
                    if not element.is_visible():
                        print(f"Element '{locator_or_element}' found, but it is not visible.")
                        return None
                else:
                    element = self.page.locator(locator_or_element)
            else:
                element = locator_or_element  # Assume it is already a Locator

            return element
        except Exception as e:
            print(f"Error retrieving element '{locator_or_element}': {e}")
            return None

    def wait_for_element_to_appear(self, locator_or_element, timeout=10):
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                print(f"Timeout: Element '{locator_or_element}' did not appear.")
                return None

            element = self.get_element(locator_or_element, wait=True)
            if element and element.is_visible():
                print(f"Element with locator '{locator_or_element}' appeared on the page.")
                return element

            time.sleep(0.5)  # Check every 0.5 seconds

    def wait_for_element_to_disappear(self, locator_or_element, timeout=20):
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                print(f"Timeout: Element '{locator_or_element}' did not appear.")
                return None

            element = self.get_element(locator_or_element, wait=True)
            if not element or not element.is_visible():
                print(f"Element with locator '{locator_or_element}' appeared on the page.")
                return True

            time.sleep(0.5)  # Check every 0.5 seconds

    def check_element_exists(self, locator_or_element, wait=False, timeout=5):
        element = self.get_element(locator_or_element, wait=wait, timeout=timeout)
        if element:
            is_visible = element.is_visible()
            print(f"Element visibility check result: {is_visible}")
            if element.is_visible():
                element.scroll_into_view_if_needed()
            return is_visible
        return False

    def check_element_enabled(self, selector, wait=False):
        element = self.get_element(selector, wait=wait)
        if element:
            return element.is_enabled()
        return False

    def check_element_checked(self, selector, wait=False):
        element = self.get_element(selector, wait=wait)
        if element:
            return element.is_checked()
        return False

    def is_page_responsive(self):
        try:
            # Check for a specific element that indicates responsiveness
            self.page.wait_for_selector('#some_element', timeout=2000)  # Adjust the selector
            return True
        except Exception:
            return False

    def check_page_status(self):
        try:
            # Check for common selectors or conditions indicating a responsive page
            if self.page.query_selector("body"):
                self.page.wait_for_selector("body", timeout=5000)  # Wait for the body if present
                return "responsive"
            else:
                # If body is not found, check for other signs of life
                if self.page.query_selector("html"):  # Check if HTML is present
                    return "partially_loaded"
                else:
                    return "no_content"  # No recognizable HTML structure
        except TimeoutError:
            return "unresponsive"
        except Exception as e:
            print(f"Error checking page status: {e}")
            return "error"

    def handle_unresponsive_page(self):
        page_status = self.check_page_status()
        if page_status == "unresponsive":
            print("Page is unresponsive, attempting to reload or take action...")
            retry_limit = 3
            for attempt in range(retry_limit):
                print(f"Retrying page action: Attempt {attempt + 1}")
                try:
                    self.page.reload(wait_until="networkidle")
                    self.wait_for_page_to_load(timeout=15)
                    print("Page reloaded successfully.")
                    return True
                except Exception as e:
                    print(f"Error during reload: {e}")
                    if attempt == retry_limit - 1:
                        print("Retry limit reached. Moving to alternative action.")
            return False

    def click_and_get_download_path(self, locator_or_element, action="click", timeout=30, download_dir="downloads"):
        """
        Clicks an element and waits for a file to be downloaded, then returns the download path.
        The file is saved in a custom directory to prevent deletion after the test.
        This works cross-platform (Windows and Linux).
        """
        try:
            # Ensure the custom download directory exists
            if not os.path.isabs(download_dir):  # Make sure the download_dir is an absolute path
                download_dir = os.path.join(os.getcwd(), download_dir)  # Use current working directory as base

            os.makedirs(download_dir, exist_ok=True)

            # Set the download behavior in Playwright to download files to the specified directory
            self.page.on("download", lambda download: download.save_as(os.path.join(download_dir, download.suggested_filename)))

            # Use Playwright's download expectation
            with self.page.expect_download(timeout=timeout * 1000) as download_info:
                self.find_element_and_perform_action(locator_or_element, action)

            # Get the download object
            download = download_info.value
            downloaded_file_path = download.path()

            print(f"Download completed: {downloaded_file_path}")
            return downloaded_file_path

        except Exception as e:
            print(f"Error during download: {e}")
            raise

    def get_checked_radio_button_text(self, name):
        try:
            legend_selector = f'//legend[text()="{name}"]'
            self.page.wait_for_selector(legend_selector, timeout=5000)

            fieldset = self.page.query_selector(legend_selector).evaluate_handle(
                'element => element.closest("fieldset")'
            )
            selected_radio = fieldset.query_selector('input[type="radio"]:checked')

            if not selected_radio:
                print("No radio button is selected.")
                return ""

            radio_id = selected_radio.get_attribute("id")

            label_selector = f'//label[@for="{radio_id}"]'
            label = self.page.query_selector(label_selector)

            if label:
                selected_text = label.text_content().strip()
                print(f"Selected radio button text: {selected_text}")
                return selected_text
            else:
                print(f"Label not found for radio button ID: {radio_id}")
                return ""
        except Exception as e:
            print(f"Error checking if radio button is selected: {e}")
            return False

    def get_mock_database_helper(self, working_directory):
        """Returns an instance of MockDatabaseHelper, initializing with mock data."""
        mock_data_file = os.path.join(working_directory, "mock_data", "mock_patients.json")
        if not os.path.exists(mock_data_file):
            raise FileNotFoundError(f"Mock data file not found: {mock_data_file}")
        return MockDatabaseHelper(mock_data_file)

    def mock_api_response(self, working_directory):
        endpoint_pattern = "**/api/patient/nhsNumberSearch*"
        endpoint_pattern = "https://api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/**"
        logger.info(f"Setting up mock for API: {endpoint_pattern}")

        def handler(route):
            """Intercept API requests and return mock data."""
            request_url = route.request.url
            logger.info(f"API Request Detected: {request_url}")

            if "nhsNumber=" in request_url:
                nhs_number = request_url.split("nhsNumber=")[-1]
            else:
                nhs_number = None

            logger.info(f"Extracted NHS number: {nhs_number}")

            if not nhs_number:
                logger.warning(f"No NHS number found in request: {request_url}")
                route.continue_()
                return

            mock_db = self.get_mock_database_helper(working_directory)
            patient = mock_db.fetch_one("SELECT * FROM patients WHERE nhs_number = ?", (nhs_number,))

            if patient:
                patient_id = int(patient[0])
                nhs_number = patient[2]
                full_name = patient[1].split()
                first_name = full_name[0]
                last_name = full_name[1] if len(full_name) > 1 else ""
                dob = patient[3]
                address = patient[4]
                postcode = "DN18 5DW"

                response_body = json.dumps({
                    "PdsPatient": {
                        "PatientId": patient_id,
                        "NhsNumber": nhs_number,
                        "FirstName": first_name,
                        "LastName": last_name,
                        "DateOfBirth": dob,
                        "GenderId": 1,
                        "Gender": None,
                        "Telephone": None,
                        "Address": address,
                        "Postcode": postcode,
                        "GpCode": None,
                        "TooManyReturnedResults": False,
                        "PatientExists": True,
                        "IsDeceased": False,
                        "PdsPatientDto": None,
                        "Vaccinations": None,
                        "SecurityCode": 0,
                        "AuditTypeId": None,
                        "AuditDateTime": None,
                        "AuditUserId": None,
                        "AuditIpAddress": None
                    },
                    "RavsPatient": {
                        "PatientId": patient_id,
                        "NhsNumber": nhs_number,
                        "FirstName": first_name,
                        "LastName": last_name,
                        "DateOfBirth": dob,
                        "GenderId": 1,
                        "Gender": None,
                        "Telephone": None,
                        "Address": None,
                        "Postcode": None,
                        "GpCode": None,
                        "TooManyReturnedResults": False,
                        "PatientExists": False,
                        "IsDeceased": False,
                        "PdsPatientDto": None,
                        "Vaccinations": None,
                        "SecurityCode": 0,
                        "AuditTypeId": None,
                        "AuditDateTime": None,
                        "AuditUserId": None,
                        "AuditIpAddress": None
                    }
                })
                logger.info(f"Mocking API response for NHS Number {nhs_number}: {response_body}")

                route.fulfill(status=200, content_type="application/json", body=response_body)
            else:
                logger.warning(f"No mock data found for NHS Number: {nhs_number}")
                route.fulfill(status=404, content_type="application/json", body='{"error": "Patient not found"}')

        self.page.route(endpoint_pattern, handler)
        self.page.route("https://api.service.nhs.uk/personal-demographics/FHIR/R4/Patient/**", lambda route: route.abort())

    def find_element_and_perform_action(self, locator_or_element, action, inputValue=None, screenshot_name=None, max_retries=3, retry_delay=2):
        if not screenshot_name:
            if isinstance(locator_or_element, str):
                screenshot_name = "".join(c if c.isalnum() else "_" for c in locator_or_element)
            else:
                screenshot_name = "element_action"

        self.wait_for_page_to_load()

        retries = 0
        while retries < max_retries:
            try:
                element = self.get_element(locator_or_element, wait=True)

                if not element:
                    print(f"Element not found for action: {action}")
                    return

                self.disable_smooth_scrolling()
                self.wait_for_element_to_appear(element)

                if element.is_visible():
                    element.scroll_into_view_if_needed()

                    # Perform action based on the specified type
                    if action.lower() == "click":
                        if element.is_enabled():
                            element.click()
                            print(f"Clicked the element successfully.")
                        else:
                            print(f"Element is either not visible or not enabled.")
                    elif action.lower() == "check":
                        if not element.is_checked():
                            element.check()
                            print("Checkbox checked successfully.")
                        elif element.is_checked():
                            print("Checkbox is already checked.")
                    elif action.lower() == "uncheck":
                        if element.is_checked():
                            element.uncheck()
                            print("Checkbox un-checked successfully.")
                        elif not element.is_checked():
                            print("Checkbox is already un-checked.")
                    elif action.lower() == "select_option":
                        if isinstance(inputValue, int):
                            element.select_option(index=inputValue)
                            print(f"Selected option by index '{inputValue}' successfully.")
                        else:
                            element.select_option(value=inputValue)
                            print(f"Selected option by label '{inputValue}' successfully.")
                    elif action.lower() == "clear":
                        element.fill('')
                        print(f"Cleared text from the element: {element}.")
                    elif action.lower() == "input_text":
                        if inputValue is None:
                            raise ValueError("`inputValue` cannot be None for 'input_text' action.")
                        if element.is_visible():
                            if element.text_content() != '':
                                element.clear()  # Clear existing text if necessary
                            element.fill(inputValue)
                            print(f"Entered text '{inputValue}' successfully.")
                    elif action.lower() == "get_text":
                        text = element.text_content()
                        if text == "":
                            text = element.get_attribute("value")
                        print(f"Text from the element: {text}")
                        return text
                    elif action.lower() == "get_value":
                        text = element.get_attribute("value")
                        print(f"Text from the element: {text}")
                        return text
                    elif action.lower() == "scroll_to":
                        element.scroll_into_view_if_needed()
                        print(f"Scrolled to {element}")
                    elif action.lower() == "get_selected_option":
                        selected_option = element.locator("option:checked")
                        if selected_option.count() > 0:
                            text = selected_option.text_content()
                            value = selected_option.get_attribute("value")
                            print(f"Selected option text: '{text}', value: '{value}'")
                            return text
                        else:
                            print("No option is currently selected.")
                            return None
                    elif action.lower() == "type_text":
                        if inputValue is None:
                            raise ValueError("`inputValue` cannot be None for 'type_text' action.")
                        if element.text_content() != '':
                            element.clear()  # Clear existing text
                        element.type(inputValue, delay=50)
                        print(f"Typed text '{inputValue}' successfully.")
                    else:
                        print(f"Unsupported action: {action}")

                    return  # If the action was successful, exit the method.

                else:
                    print(f"Element is not visible.")
                    retries += 1
                    if retries < max_retries:
                        print(f"Retrying... ({retries}/{max_retries})")
                        time.sleep(retry_delay)
                    else:
                        print("Element was not visible after retries.")
                        return

            except TimeoutError:
                print(f"Timeout waiting for element to perform {action}. Retrying...")
                retries += 1
                if retries < max_retries:
                    time.sleep(retry_delay)
                else:
                    print(f"Timeout occurred after {max_retries} retries. Aborting action.")
                    return
            except Exception as e:
                print(f"Exception: {e} during {action} on element. Retrying...")
                retries += 1
                if retries < max_retries:
                    time.sleep(retry_delay)
                else:
                    print(f"Failed to perform action {action} after {max_retries} retries.")
                    return

        # If we reached here, it means the action couldn't be performed after max retries
        print(f"Action '{action}' failed after {max_retries} retries.")
        def wait_for_selector_to_disappear(self, selector, timeout=5):
            try:
                self.page.wait_for_selector(selector, state='hidden', timeout=timeout)
                print(f"Element {selector} disappeared from the page.")
            except Exception as e:
                print(f"Error waiting for element {selector} to disappear: {e}")

    def check_element_by_locator_enabled(self, element, wait=False):
        try:
            return element.is_enabled()
        except Exception as e:
            print(f"Element - {element} not found: {e}")
            return False

    def scroll_into_view(self, selector):
        element=self.page.locator(selector)
        element.scroll_into_view_if_needed()

    def scroll_element_by_locator_into_view(self, element):
        element.scroll_into_view_if_needed()

    def clear_element(self, selector):
        try:
            element=self.page.locator(selector)
            element.clear()
            print(f"Cleared text from the {selector} successfully.")
        except Exception as e:
            print(f"Exception: {e}. Element - {selector} not found.")

    def release_mouse(self):
        self.page.mouse.move(100, 100)
        self.page.mouse.down()
        self.page.mouse.up()

    def get_element_by_type(self, locator_type_or_selector, locator_value=None, name=None, exact=False):
        # If locator_type_or_selector is just a string, return it as a selector
        if isinstance(locator_type_or_selector, Locator):
            return locator_type_or_selector  # Directly return the Locator object

    # If locator_type_or_selector is just a string and locator_value is None, treat it as a selector
        if isinstance(locator_type_or_selector, str) and locator_value is None:
            return self.page.locator(locator_type_or_selector)   # Return the string directly

        # Handle known locator types
        if locator_type_or_selector == "role":
            return self.page.get_by_role(locator_value, name=name, exact=exact)
        elif locator_type_or_selector == "text":
            return self.page.get_by_text(locator_value, exact=exact)
        elif locator_type_or_selector == "label":
            return self.page.get_by_label(locator_value, exact=exact).nth(0)
        elif locator_type_or_selector == "placeholder":
            return self.page.get_by_placeholder(locator_value)
        elif locator_type_or_selector == "xpath":
            return self.page.locator(locator_value)
        elif locator_type_or_selector == "link":
            return self.page.get_by_role("link", name=locator_value, exact=exact)
        elif locator_type_or_selector == "title":
            return self.page.get_by_title(locator_value, exact=exact)
        elif locator_type_or_selector == "row":
            return self.page.get_by_role("row", name=locator_value, exact=exact)
        elif locator_type_or_selector == "cell":
            return self.page.get_by_role("cell", name=locator_value, exact=exact)
        elif locator_type_or_selector == "id":
            return self.page.locator(f"#{locator_value}")
        else:
            # Log a warning for unsupported locator types
            print(f"Warning: Unsupported locator type '{locator_type_or_selector}'. Assuming it is a selector.")
            return locator_value  # Return locator_value assuming it's valid

    def click_cell_in_row(self, row_name: str, cell_index: int):
        row_element = self.get_element_by_type("row", row_name)
        cell_element = row_element.get_by_role("cell").nth(cell_index)
        self.find_element_and_perform_action(cell_element, "click")

    def click_link_in_row(self, row_name: str, link_index: int):
        row_element = self.get_element_by_type("row", row_name)
        cell_element = row_element.get_by_role("link").nth(link_index)
        self.find_element_and_perform_action(cell_element, "click")

    def disable_smooth_scrolling(self):
        self.page.add_init_script("""
            window.HTMLElement.prototype.scrollIntoView = () => {};
            window.scrollTo = () => {};
        """)
        self.page.evaluate("() => { window.HTMLElement.prototype.scrollIntoView = function() {} }")

    def get_current_url(self):
        return self.page.url()

    def get_accessibility_violations(self):
        try:
            current_url = self.get_current_url(self.page)

            self.page.goto(current_url)

            axe = self.page.accessibility
            results = axe.check()
            violations = results['violations']

            if violations:
                print(f"Accessibility Violations for {current_url}: {violations}")
            else:
                print(f"No accessibility violations found for {current_url}.")

            return violations

        except Exception as e:
            print(f"Exception during accessibility testing: {e}")
            return None

    def quit_browser(self):
        try:
            if self.page:
                self.page.close()
            if self.browser:
                self.browser.close()
            if self.playwright:
                self.playwright.stop()
        except Exception as e:
            print(f"An error occurred during browser cleanup: {e}")

class PlaywrightHelper(BasePlaywrightHelper):
    def __init__(self, working_directory, config):
        super().__init__(working_directory, config)

        try:
            browser_name = config["browser"].lower()
            headless_mode = config["headless_mode"].lower() == "true"
            if browser_name == "chromium":
                self.launch_chromium(headless_mode)
            if browser_name == "chrome":
                self.launch_chrome(headless_mode)
            elif browser_name == "firefox":
                self.launch_firefox(headless_mode)
            elif browser_name == "safari":
                self.launch_safari(headless_mode)
            elif "edge" in browser_name:
                self.launch_edge(headless_mode)
            elif browser_name == "mobile":
                self.launch_mobile_browser(config["device"], headless_mode)
            else:
                print(f"Unsupported browser: {browser_name}")
        except Exception as e:
            print(f"Error launching browser: {e}")
