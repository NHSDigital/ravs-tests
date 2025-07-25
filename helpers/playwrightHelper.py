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
from urllib.parse import urlparse

_cached_playwright = None

def get_sync_playwright():
    global _cached_playwright
    if _cached_playwright is None:
        _cached_playwright = sync_playwright().start()
    return _cached_playwright
class BasePlaywrightHelper:
    def __init__(self, working_directory, config):
        self.working_directory = working_directory
        self.screenshots_dir = "screenshots"
        self._browser_started = False
        self.config = config
        if not os.path.exists(self.screenshots_dir):
            os.makedirs(self.screenshots_dir)
        self.playwright = get_sync_playwright()
        self.browser = None
        self.context = None
        self.page = None

    def get_or_create_page(self):
        if not self.page or self.page.is_closed():
            self.page = self.context.new_page()
        return self.page

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
            self.page = self.get_or_create_page()
        except Exception as e:
            print(f"Error launching Chromium: {e}")

    def launch_edge(self, headless_mode, slow_mo=0):
        try:
            self.browser = self.playwright.chromium.launch(channel="msedge",headless=headless_mode, slow_mo=slow_mo, args=["--fullscreen"])
            self.context = self.browser.new_context()
            self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
            self.page = self.get_or_create_page()
        except Exception as e:
                print(f"Error launching Edge: {e}")

    def launch_safari(self, headless_mode):
        try:
            self.browser = self.playwright.webkit.launch(headless=headless_mode, args=["--fullscreen"])
            self.context = self.browser.new_context()
            self.page = self.get_or_create_page()
        except Exception as e:
                print(f"Error launching Safari: {e}")

    def launch_chrome(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode, args=["--fullscreen", "--disable-gpu", "--no-sandbox"])
            self.context = self.browser.new_context()
            self.page = self.get_or_create_page()
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
            locale = "en-GB"

            if "iphone_12" == device_name.lower():
                device_settings = self.playwright.devices["iPhone 12"]
            elif "iphone_11" == device_name.lower():
                device_settings = self.playwright.devices["iPhone 11"]
            elif "pixel_5" == device_name.lower():
                device_settings = self.playwright.devices["Pixel 5"]
            else:
                device_settings = self.playwright.devices["Galaxy S9+"]

            if "iphone" in device_name.lower() or "pixel" in device_name.lower():
                self.browser = self.playwright.webkit.launch(headless=headless_mode)
            else:
                self.browser = self.playwright.chromium.launch(channel='chromium', headless=headless_mode)

            device_settings = {
                k: v for k, v in device_settings.items()
                if k not in ["is_mobile", "viewport", "device_scale_factor"]
            }

            self.context = self.browser.new_context(
                **device_settings,
                locale=locale,
            )

            self.page = self.get_or_create_page()
            self.page.set_viewport_size(device_settings["viewport"])

        except Exception as e:
            print(f"Error launching mobile browser for {device_name}: {e}")

    def capture_screenshot(self, full_path):
        try:
            # self.page.wait_for_timeout(500)
            self.page.screenshot(path=full_path)
        except Exception as error:
            if "Timeout" in str(error):
                print('Screenshot taking timed out, ignoring...')
                return None
            else:
                raise error
        return full_path

    def add_cookie(self, url, cookie, value):
        self.page.goto(url)
        domain = urlparse(url).netloc
        self.context.add_cookies([
                {
                    "name": cookie,
                    "value": value,
                    "domain": domain,
                    "path": "/"
                }
            ])

    def get_browser_version(self):
        if self.browser:
            print(self.browser.version)
            return self.browser.version
        else:
            return None

    def close_browser(self):
        try:
            if self.context:
                trace_path = os.path.join(self.working_directory, "trace.zip")
                try:
                    self.context.tracing.stop(path=trace_path)
                    print(f"Trace saved to {trace_path}")
                except Exception as trace_error:
                    print(f"An error occurred while stopping tracing: {trace_error}")

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

    def wait_for_page_to_load(self, timeout=5):
        try:
            time.sleep(1)
            self.page.wait_for_load_state('load', timeout=timeout * 1000)
            self.page.wait_for_selector('body', timeout=timeout * 1000)
            self.page.wait_for_function(
                "() => [...document.querySelectorAll('*')].every(el => el.isConnected)",
                timeout=timeout * 1000
            )
        except Exception as e:
            print(f"Page did not fully load or elements not attached within {timeout} seconds. Proceeding anyway.")

    def find_elements(self, selector):
        return self.page.query_selector_all(selector)

    def get_element(self, locator_or_element, wait=False, timeout=5000):
        """Utility method to get an element with optional waiting."""
        try:
            if isinstance(locator_or_element, str):
                if wait:
                    self.page.wait_for_selector(locator_or_element, state="visible", timeout=timeout * 1000)
                    element = self.page.locator(locator_or_element)

                    if not element.is_visible():
                        print(f"Element '{locator_or_element}' found, but it is not visible.")
                        return None
                else:
                    element = self.page.locator(locator_or_element)
            else:
                element = locator_or_element

            return element
        except Exception as e:
            print(f"Error retrieving element '{locator_or_element}': {e}")
            return None

    def wait_for_element_to_appear(self, locator_or_element, timeout=10000, poll_interval=0.1):
        """Waits for an element to be visible, polling every 0.1s, failing fast if missing."""
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            try:
                element = self.get_element(locator_or_element, wait=True)
                if element and element.is_visible():
                    print(f"✅ Element '{locator_or_element}' appeared.")
                    return element
            except Exception:
                pass
            time.sleep(poll_interval)
        print(f"⚠️ Fast-fail: Element '{locator_or_element}' did not appear.")
        return None

    def wait_for_element_to_disappear(self, locator_or_element, timeout=10000, poll_interval=0.1):
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            try:
                element = self.get_element(locator_or_element, wait=True)
                if not element or not element.is_visible():
                    print(f"✅ Element '{locator_or_element}' disappeared.")
                    return True
            except Exception:
                print(f"⚠️ Exception occurred while checking '{locator_or_element}', assuming it's gone.")
                return True
            time.sleep(poll_interval)
        print(f"⚠️ Timeout: Element '{locator_or_element}' did not disappear within {timeout} ms.")
        return False

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
            if self.page.query_selector("body"):
                self.page.wait_for_selector("body", timeout=5000)
                return "responsive"
            else:
                if self.page.query_selector("html"):
                    return "partially_loaded"
                else:
                    return "no_content"
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
                    self.wait_for_page_to_load(timeout=5)
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
            if not os.path.isabs(download_dir):
                download_dir = os.path.join(os.getcwd(), download_dir)

            os.makedirs(download_dir, exist_ok=True)

            self.page.on("download", lambda download: download.save_as(os.path.join(download_dir, download.suggested_filename)))

            with self.page.expect_download(timeout=timeout * 1000) as download_info:
                self.find_element_and_perform_action(locator_or_element, action)

            download = download_info.value
            downloaded_file_path = download.path()

            print(f"Download completed: {downloaded_file_path}")
            return downloaded_file_path

        except Exception as e:
            print(f"Error during download: {e}")
            raise

    def get_checked_radio_button_text(self, name):
        try:
            legend_selector = f'//legend[contains(normalize-space(), "{name}")]'
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

    def javascript_click(self, element):
        element_handle = element.element_handle()
        self.page.evaluate("element => element.click()", element_handle)

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
            screenshot_name = "".join(c if c.isalnum() else "_" for c in str(locator_or_element)) or "element_action"

        self.wait_for_page_to_load(10)
        time.sleep(0.5)

        # DEFAULT_WAIT_TIMEOUT = 10000
        retries = 0

        while retries < max_retries:
            try:
                element = self.get_element(locator_or_element, wait=True)
                if not element:
                    time.sleep(3)
                    if not element:
                        print(f"[FAIL FAST] Element not found for action: {action}. Skipping further retries.")
                    return None

                if not element.is_visible():
                    print(f"[FAIL FAST] Element found but not visible for action: {action}. Waiting briefly to confirm...")
                    time.sleep(3)
                    if not element.is_visible():
                        print(f"[FAIL FAST] Still not visible. Skipping further retries.")
                        return None

                self.disable_smooth_scrolling()
                self.wait_for_element_to_appear(element)

                if action.lower() in ["input_text", "type_text", "select_option"] and inputValue is None:
                    raise ValueError(f"`inputValue` required for action '{action}' but not provided.")

                element.scroll_into_view_if_needed()

                action_map = {
                    "click": lambda: self._click_element(element),
                    "check": lambda: self._check_element(element),
                    "uncheck": lambda: self._uncheck_element(element),
                    "select_option": lambda: self._select_option(element, inputValue),
                    "get_options": lambda: self._get_options(element),
                    "clear": lambda: self._clear_element(element),
                    "input_text": lambda: self._input_text(element, inputValue),
                    "type_text": lambda: self._type_text(element, inputValue),
                    "get_text": lambda: self._get_text(element),
                    "get_value": lambda: self._get_value(element),
                    "scroll_to": lambda: self._scroll_to_element(element),
                    "get_selected_option": lambda: self._get_selected_option(element),
                }

                if action.lower() not in action_map:
                    print(f"Unsupported action: {action}")
                    return

                result = action_map[action.lower()]()
                return result
            except TimeoutError:
                print(f"Timeout waiting for element to perform {action}. Retrying... ({retries+1}/{max_retries})")
            except Exception as e:
                print(f"Exception: {e} during {action} on element. Retrying... ({retries+1}/{max_retries})")

            retries += 1
            time.sleep(retry_delay)

        print(f"Action '{action}' failed after {max_retries} retries.")

    def is_element_really_visible(self, element):
        try:
            return element.bounding_box() is not None
        except:
            return False

    def _click_element(self, element, timeout=5000):
        element.click()
        print("Clicked the element successfully.")

    def _check_element(self, element):
        if not element.is_checked():
            element.check()
            print("Checkbox checked.")
        else:
            print("Checkbox already checked.")

    def _uncheck_element(self, element):
        if element.is_checked():
            element.uncheck()
            print("Checkbox un-checked.")
        else:
            print("Checkbox already un-checked.")

    def _select_option(self, element, inputValue):
        if isinstance(inputValue, int):
            element.select_option(index=inputValue)
            print(f"Selected option by index '{inputValue}'.")
        else:
            element.select_option(value=inputValue)
            print(f"Selected option by value '{inputValue}'.")


    def _get_options(self, element):
        options = element.evaluate("(el) => Array.from(el.options).map(option => option.text)")
        print(f"Options: {options}")
        return options

    def _clear_element(self, element):
        element.fill('')
        print(f"Cleared text from the element.")

    def _input_text(self, element, inputValue):
        if element.text_content() != '':
            element.clear()
        element.fill(inputValue)
        print(f"Entered text '{inputValue}'.")

    def _type_text(self, element, inputValue):
        if element.text_content() != '':
            element.clear()
        element.type(inputValue, delay=50)
        print(f"Typed text '{inputValue}'.")

    def _get_text(self, element):
        text = element.text_content()
        if not text:
            text = element.get_attribute("value")
        print(f"Text from element: '{text}'")
        return text

    def _get_value(self, element):
        value = element.get_attribute("value")
        print(f"Value from element: '{value}'")
        return value

    def _scroll_to_element(self, element):
        element.scroll_into_view_if_needed()
        print("Scrolled to the element.")

    def _get_selected_option(self, element):
        selected_option = element.locator("option:checked")
        if selected_option.count() > 0:
            text = selected_option.text_content()
            value = selected_option.get_attribute("value")
            print(f"Selected option text: '{text}', value: '{value}'")
            return text
        else:
            print("No option is currently selected.")
            return None

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

    def get_element_by_type(self, locator_type_or_selector, locator_value=None, name=None, exact=False, parent_locator=None):
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
        elif locator_type_or_selector == "radio":
            return self.page.get_by_role("radio", name=locator_value, exact=exact)
        elif locator_type_or_selector == "title":
            return self.page.get_by_title(locator_value, exact=exact)
        elif locator_type_or_selector == "row":
            return self.page.get_by_role("row", name=locator_value, exact=exact)
        elif locator_type_or_selector == "cell":
            return self.page.get_by_role("cell", name=locator_value, exact=exact)
        elif locator_type_or_selector == "id":
            return self.page.locator(f"#{locator_value}")
        elif locator_type_or_selector == "nested_role":
            parent_locator = self.page.locator(parent_locator)
            return parent_locator.get_by_role(locator_value, name=name, exact=exact)
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
            current_url = self.page.url
            axe = Axe()
            results = axe.run(self.page)
            violations = results['violations']

            if violations:
                violations_json = json.dumps(violations, indent=4)
                allure.attach(
                                violations_json,
                                name=f"Accessibility Violations for {current_url}",
                                attachment_type=allure.attachment_type.JSON
                            )
                print(f"Accessibility Violations for {current_url}: {violations_json}")
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

    def start_browser_if_needed(self):
            if self._browser_started:
                return

            browser_name = self.config["browser"].lower()
            headless_mode = self.config["headless_mode"].lower() == "true"

            try:
                if browser_name == "chromium":
                    self.launch_chromium(headless_mode)
                elif browser_name == "chrome":
                    self.launch_chrome(headless_mode)
                elif browser_name == "firefox":
                    self.launch_firefox(headless_mode)
                elif browser_name == "safari":
                    self.launch_safari(headless_mode)
                elif "edge" in browser_name:
                    self.launch_edge(headless_mode)
                elif browser_name == "mobile":
                    self.launch_mobile_browser(self.config["device"], headless_mode)
                else:
                    raise ValueError(f"Unsupported browser: {browser_name}")
                self._browser_started = True
            except Exception as e:
                print(f"Error launching browser: {e}")

class PlaywrightHelper(BasePlaywrightHelper):
    def __init__(self, working_directory, config):
        super().__init__(working_directory, config)

        self.config = config
        self._browser_started = False

        # try:
        #     browser_name = config["browser"].lower()
        #     headless_mode = config["headless_mode"].lower() == "true"
        #     if browser_name == "chromium":
        #         self.launch_chromium(headless_mode)
        #     if browser_name == "chrome":
        #         self.launch_chrome(headless_mode)
        #     elif browser_name == "firefox":
        #         self.launch_firefox(headless_mode)
        #     elif browser_name == "safari":
        #         self.launch_safari(headless_mode)
        #     elif "edge" in browser_name:
        #         self.launch_edge(headless_mode)
        #     elif browser_name == "mobile":
        #         self.launch_mobile_browser(config["device"], headless_mode)
        #     else:
        #         print(f"Unsupported browser: {browser_name}")
        # except Exception as e:
        #     print(f"Error launching browser: {e}")
