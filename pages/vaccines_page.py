from init_helpers import *
import re


class ElementManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ElementManager._instance is None:
            ElementManager()
        return ElementManager._instance

    def __init__(self):
        if ElementManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ElementManager._instance = self
            self.initialize_elements()

    def initialize_elements(self):
        self.elements = {
            "add_vaccine_button": get_element_by_type("link", "Add vaccine"),
            "site_search_input_element": get_element_by_type("placeholder", "Enter 3 or more characters to search"),
            "continue_to_add_batch_page_button": get_element_by_type("role", "Continue"),
            "view_product_button": "//a[text()='View Product']",
            "add_batch_link": "//a[text()='Add batch']"
        }

    def get_element(self, name):
        return self.elements.get(name)

# def initialize_elements(self):
#     ADD_VACCINE_BUTTON = get_element_by_type("link", "Add vaccine")
#     SITE_SEARCH_INPUT_ELEMENT = get_element_by_type("placeholder", "Enter 3 or more characters to search")
#     CONTINUE_TO_ADD_BATCH_PAGE_BUTTON = get_element_by_type("role", "Continue")
#     VIEW_PRODUCT_BUTTON = ("//a[text()='View Product']")
#     ADD_BATCH_LINK = ("//a[text()='Add batch']")

class vaccines_page:
    def __init__(self):
        self.element_manager = ElementManager.get_instance()

    def click_add_vaccine_button():
        element = ElementManager.get_instance().get_element("add_vaccine_button")
        find_element_with_locator_and_perform_action(element,"click")

    def click_continue_to_add_batch_page_button():
        element  = ElementManager.get_instance().get_element("continue_to_add_batch_page_button")
        find_element_with_locator_and_perform_action(element,"click")

    def click_first_available_add_batch_link():
        element = "(//a[text()='Add batch'])[1]"
        find_element_and_perform_action(element, "click")

    def click_vaccine_type_add_batch_link(site, vaccine_type):
        element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='Add batch']")
        find_element_and_perform_action(element, "click")

    def search_for_site(site):
        element  = ElementManager.get_instance().get_element("site_search_input_element")
        find_element_and_perform_action(element, "input_text", site)

    def click_site_in_search_results_dropdown(site):
        element = get_element_by_type("text", site)
        find_element_and_perform_action(element, "click")

    def check_vaccine_has_been_added(site, vaccine, wait):
        element = (f"//h1[text() = '{site}']/following-sibling::div//h2[text()='{vaccine}']")
        return check_element_exists(element, wait)

    def check_vaccine_type_has_been_added(site, vaccine, vaccine_type, wait):
        element = (f"//h1[text() = '{site}']/following-sibling::div//h2[text()='{vaccine}']/following-sibling::table//td[text()='{vaccine_type}']")
        return check_element_exists(element, wait)

    def click_view_product(site, vaccine_type):
        element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='View product']")
        find_element_and_perform_action(element, "click")
