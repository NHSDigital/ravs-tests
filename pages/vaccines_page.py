from init_helpers import *
import re

add_vaccine_button = ("link", "Add vaccine")
site_search_input_element = ("placeholder", "Enter 3 or more characters to search")
continue_to_add_batch_page_button = ("role", "Continue")
view_product_button = "//a[text()='View Product']"
add_batch_link = "//a[text()='Add batch']"
filter_by_site_dropdown = ("label", "Select site")

def click_add_vaccine_button():
    element = get_element_by_type(*add_vaccine_button)
    find_element_with_locator_and_perform_action(element,"click")

def click_continue_to_add_batch_page_button():
    element  = get_element_by_type(*continue_to_add_batch_page_button)
    find_element_with_locator_and_perform_action(element,"click")

def filter_by_site(site):
    element = get_element_by_type(*filter_by_site_dropdown)
    find_element_with_locator_and_perform_action(element,"select_option", site)

def click_first_available_add_batch_link():
    element = "(//a[text()='Add batch'])[1]"
    find_element_and_perform_action(element, "click")

def click_vaccine_type_add_batch_link(site, vaccine_type):
    element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='Add batch']")
    find_element_and_perform_action(element, "click")

def search_for_site(site):
    element  = get_element_by_type("site_search_input_element")
    find_element_with_locator_and_perform_action(element, "input_text", site)

def click_site_in_search_results_dropdown(site):
    element = get_element_by_type("text", site)
    find_element_with_locator_and_perform_action(element, "click")

def check_vaccine_has_been_added(site, vaccine, wait):
    element = (f"//h1[text() = '{site}']/following-sibling::div//h2[text()='{vaccine}']")
    return check_element_exists(element, wait)

def check_vaccine_type_has_been_added(site, vaccine, vaccine_type, wait):
    element = (f"//h1[text() = '{site}']/following-sibling::div//h2[text()='{vaccine}']/following-sibling::table//td[text()='{vaccine_type}']")
    return check_element_exists(element, wait)

def click_view_product(site, vaccine_type):
    element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='View product']")
    find_element_and_perform_action(element, "click")
