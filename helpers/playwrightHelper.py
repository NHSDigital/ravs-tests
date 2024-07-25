import time
from playwright.sync_api import sync_playwright, TimeoutError
from axe_core_python.sync_playwright import Axe
from init_helpers import *
import pytest

class ElementNotFoundException(Exception):
    pass

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
            self.browser = self.playwright.chromium.launch(channel="chrome", headless=headless_mode, args=["--fullscreen"])
            self.context = self.browser.new_context()
            self.page = self.context.new_page()
        except Exception as e:
            print(f"Error launching Safari: {e}")

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

    def capture_screenshot(self, filename):
        screenshot_path = os.path.join(self.screenshots_dir, f'before_action_{filename}.png')
        try:
            self.page.screenshot(path=screenshot_path)
        except Exception as error:
            if "Timeout" in str(error):
                print('Screenshot taking timed out, ignoring...')
                return None
            else:
                raise error
        return screenshot_path

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

    def wait_for_page_to_load(self, timeout=0.2):
        self.page.wait_for_selector('*', timeout=timeout * 100)
        self.page.wait_for_load_state('domcontentloaded', timeout=timeout * 100)

    def find_elements(self, selector):
        return self.page.query_selector_all(selector)

    def wait_for_element_to_appear(self, selector, timeout=20):
        try:
            self.page.wait_for_selector(selector, timeout=timeout, state='visible')
            print(f"Element {selector} appeared on the page.")
        except Exception as e:
            print(f"Error waiting for element {selector} to appear: {e}")

    def wait_for_selector_to_disappear(self, selector, timeout=50):
        try:
            self.page.wait_for_selector(selector, state='hidden', timeout=timeout)
            print(f"Element {selector} disappeared from the page.")
        except Exception as e:
            print(f"Error waiting for element {selector} to disappear: {e}")

    def check_element_exists(self, selector, wait=False):
        try:
            element = self.page.locator(selector)
            if wait == True:
                self.page.wait_for_selector(selector)
            return element.is_visible()
        except Exception as e:
            print(f"Element - {selector} not found: {e}")
            return False

    def check_element_enabled(self, selector, wait=False):
        try:
            element = self.page.locator(selector)
            if wait == True:
                self.page.wait_for_selector(selector)
            return element.is_enabled()
        except Exception as e:
            print(f"Element - {selector} not found: {e}")
            return False

    def scroll_into_view(self, selector):
        element=self.page.locator(selector)
        element.scroll_into_view_if_needed()

    def clear_element(self, selector):
        try:
            element=self.page.locator(selector)
            element.clear()
            print(f"Cleared text from the {selector} successfully.")
        except Exception as e:
            print(f"Exception: {e}. Element - {selector} not found.")
            raise ElementNotFoundException(f"Element not found: {selector}")

    def release_mouse(self):
        self.page.mouse.move(100, 100)
        self.page.mouse.down()
        self.page.mouse.up()

    def find_element_and_perform_action(self, selector, action, inputValue=None):
        selector_filename = "".join(c if c.isalnum() else "_" for c in selector)
        self.capture_screenshot(selector_filename)
        try:
            element=self.page.locator(selector)
            self.page.set_viewport_size({"width": 1500, "height":1500})
            element.scroll_into_view_if_needed()
            if action.lower() == "click":
                if element.is_visible():
                    if element.is_enabled():
                        element.click()
                        print(f"Clicked the {selector} successfully.")
                else:
                    print(f"Element with {selector} is not enabled.")
            elif action.lower() == "input_text":
                text = element.text_content()
                if element.is_visible():
                    if text != '':
                        element.clear()
                    element.fill(inputValue)
                    print(f"Entered text into the {selector} successfully.")
            elif action.lower() == "type_text":
                if element.is_visible():
                    text = element.text_content()
                    if text != '':
                        element.clear()
                    element.type(inputValue)
                    print(f"Entered text into the {selector} successfully.")
            elif action.lower() == "get_text":
                text = element.text_content()
                print(f"Text from the {selector}: {text}")
                return text
            elif action.lower() == "select_option":
                if element.is_visible():
                    element.select_option(inputValue)
                    print(f"Selected option with value '{inputValue}' from the {selector} successfully.")
            elif action.lower() == "click_checkbox":
                if element.is_visible():
                    if not element.is_checked():
                        element.check()
                        print(f"{selector} checkbox checked successfully.")
                    else:
                        print(f"{selector} checkbox is already checked.")
            else:
                print(f"Unsupported action: {action}")
        except TimeoutError:
           print(f"Timeout waiting for selector: {selector} to perform {action}")
        except Exception as e:
            print(f"Exception: {e}. Element not found: {selector}")
            raise ElementNotFoundException(f"Element not found: {selector} to perform {action}")
        self.capture_screenshot(selector_filename)

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
