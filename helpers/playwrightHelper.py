import time
from playwright.sync_api import sync_playwright, TimeoutError, Locator
from axe_core_python.sync_playwright import Axe
from init_helpers import *
import pytest
import logging
import platform

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
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Chromium: {e}")

    def launch_edge(self, headless_mode):
        try:
            self.browser = self.playwright.chromium.launch(channel="msedge",headless=headless_mode, args=["--fullscreen"])
            self.context = self.browser.new_context()
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
            mouse_position = self.page.evaluate(
                "() => ({ x: window.pageXOffset, y: window.pageYOffset })"
            )
            logging.debug(f"Scrolling to mouse position: {mouse_position}")
            self.page.evaluate(f"window.scrollTo({mouse_position['x']}, {mouse_position['y']});")
            self.page.wait_for_timeout(500)
            self.page.locator(".header")
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

    def wait_for_element_to_disappear(self, locator_or_element, timeout=10):
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

    def handle_unresponsive_page(self):
        if not self.is_page_responsive():
            print("Page is unresponsive. Attempting to reload or take action.")
            self.page.reload(wait_until="networkidle")
            self.wait_for_page_to_load()

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


    def find_element_and_perform_action(self, locator_or_element, action, inputValue=None, screenshot_name=None):
        # Generate screenshot filename if not provided
        if not screenshot_name:
            if isinstance(locator_or_element, str):
                # Generate a safe filename based on the locator
                screenshot_name = "".join(c if c.isalnum() else "_" for c in locator_or_element)
            else:
                screenshot_name = "element_action"

        self.wait_for_page_to_load()

        # Try to get the element using a helper function
        element = self.get_element(locator_or_element, wait=True)

        if not element:
            print(f"Element not found for action: {action}")
            return

        self.disable_smooth_scrolling()
        self.wait_for_element_to_appear(element)

        try:
            # Perform the action based on the passed `action`
            if action.lower() == "click":
                if element.is_visible() and element.is_enabled():
                    element.click()
                    print(f"Clicked the element successfully.")
                else:
                    print(f"Element is either not visible or not enabled.")
            elif action.lower() == "check":
                if element.is_visible() and not element.is_checked():
                    element.check()
                    print("Checkbox checked successfully.")
                elif element.is_checked():
                    print("Checkbox is already checked.")
            elif action.lower() == "uncheck":
                if element.is_visible() and element.is_checked():
                    element.uncheck()
                    print("Checkbox un-checked successfully.")
                elif not element.is_checked():
                    print("Checkbox is already un-checked.")
            elif action.lower() == "select_option":
                if element.is_visible():
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
                print(f"Text from the element: {text}")
                return text
            elif action.lower() == "type_text":
                if inputValue is None:
                    raise ValueError("`inputValue` cannot be None for 'type_text' action.")
                if element.is_visible():
                    if element.text_content() != '':
                        element.clear()  # Clear existing text
                    element.type(inputValue, delay=50)
                    print(f"Typed text '{inputValue}' successfully.")
            else:
                print(f"Unsupported action: {action}")
        except TimeoutError:
            print(f"Timeout waiting for element to perform {action}")
        except Exception as e:
            print(f"Exception: {e} during {action} on element.")

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
