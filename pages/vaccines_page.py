import time
from init_helpers import *
import re

from pages.site_vaccines_add_batch_page import *

add_vaccine_button = ("role", "button", "Add vaccine")
site_search_input_element = ("placeholder", "Enter 3 or more characters to search")
continue_to_add_batch_page_button = ("role", "Continue")
view_product_button = "//a[text()='View Product']"
add_batch_link = "//a[text()='Add batch']"
filter_by_site_dropdown = ("label", "Select site")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def click_view_product_link(vaccine):
    click_link_in_row(vaccine, 0)

def click_first_available_view_product_link():
    xpath = "(//tr[@role='row']//a[contains(text(),'View product')])[1]"
    find_element_and_perform_action(("xpath", xpath), "click")

def check_add_vaccine_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(add_vaccine_button)
    return check_element_exists(add_vaccine_button)

def click_add_vaccine_button():
    find_element_and_perform_action(add_vaccine_button, "click")

def click_continue_to_add_batch_page_button():
    find_element_and_perform_action(continue_to_add_batch_page_button, "click")

def filter_by_site(site):
    find_element_and_perform_action(filter_by_site_dropdown, "select_option", site)

def click_view_vaccine_product_link(vaccine):
    click_link_in_row(vaccine, 0)

def click_add_batch_for_vaccine_link(vaccine):
    click_link_in_row(vaccine, 1)

def click_first_available_add_batch_link():
    element = "(//a[text()='Add batch'])[1]"
    find_element_and_perform_action(element, "click")

def search_for_site(site):
    element  = get_element_by_type("site_search_input_element")
    find_element_and_perform_action(element, "input_text", site)

def click_site_in_search_results_dropdown(site):
    element = get_element_by_type("text", site)
    find_element_and_perform_action(element, "click")

def to_title_case(text):
    return ' '.join(word.capitalize() for word in text.split())

def check_vaccine_batch_exists_with_same_number_and_expiry_date_and_is_active(site, vaccine, vaccine_type, batch_number, batch_expiry_date):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if vaccine.lower() == "covid-19":
        vaccine = "COVID-19"

    site = to_title_case(site)
    vaccine_element = (f"//table[caption[text()='{site}']]//tr[td[text()='{vaccine}'] and td[text()='{vaccine_type}']]")
    if check_element_exists(vaccine_element, True):
        print(f"DEBUG: Found vaccine element for {site}, {vaccine}, {vaccine_type}")

        view_vaccine_element = (
            f"//table[caption[normalize-space(text())='{site}']]"
            f"//tr[td[normalize-space(text())='{vaccine}'] and td[normalize-space(text())='{vaccine_type}']]"
            f"//td[normalize-space(text())='{vaccine_type}']/following-sibling::td//a[normalize-space(text())='View']"
        )

        javascript_click(view_vaccine_element)
        attach_screenshot("clicked_view_vaccine_element")

        batch_expiry_date = date_format_with_name_of_month(batch_expiry_date)
        batch_number_with_expiry_date_element = f"//td[text()='{batch_number}']/following-sibling::td[text()='{batch_expiry_date}']/following-sibling::td/strong[text()='Active']"

        print(f"DEBUG: Checking batch element: {batch_number_with_expiry_date_element}")

        wait_for_element_to_appear(batch_number_with_expiry_date_element)
        result = check_element_exists(batch_number_with_expiry_date_element, True)
        attach_screenshot("checked_batch_number_with_expiry_date_element_exists")
        print(f"DEBUG: Batch element exists -> {result}")
        return result

    print(f"DEBUG: Vaccine element not found, checking again: {vaccine_element}")
    return check_element_exists(vaccine_element, True)

def get_pack_size_value_vaccines_page(batch_number, batch_expiry_date, pack_size):
    batch_expiry_date = date_format_with_name_of_month(batch_expiry_date)
    element = (f"//tr[td[text()='{batch_number}'] and td[3][text()='{batch_expiry_date}'] and td[4]/strong[text()='Active']]/td[2]")
    wait_for_element_to_appear(element)
    if check_element_exists(element):
        return find_element_and_perform_action(element, "get_text")
    else:
        edit_element = (f"//tr[td[1][normalize-space()='{batch_number}'] and td[2][normalize-space()='{batch_expiry_date}'] and td[3]/strong[normalize-space()='Active']]/td[5]//a[normalize-space()='Edit']")
        find_element_and_perform_action(edit_element, "click")
        select_pack_size(pack_size)
        click_save_changes_to_vaccine_details_button()
        return pack_size

def check_vaccine_has_been_added(site, vaccine, wait):
    if vaccine.lower() == "covid-19":
        vaccine = "COVID-19"
    element = (f"//caption[text() = '{site}']/following-sibling::tbody//td[text()='{vaccine}']")
    return check_element_exists(element, wait)

def check_vaccine_type_has_been_added(site, vaccine, vaccine_type, wait):
    element = (f"//h1[text() = '{site}']/following-sibling::div//h2[text()='{vaccine}']/following-sibling::table//td[text()='{vaccine_type}']")
    return check_element_exists(element, wait)

def click_view_product(site, vaccine_type):
    element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='View product']")
    find_element_and_perform_action(element, "click")
