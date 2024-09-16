from init_helpers import *
import re

ADD_VACCINE_BUTTON = ("//a[text()='Add vaccine']")
SELECT_SITE_DROPDOWN = ("//select[@name='SiteId']")
VIEW_PRODUCT_BUTTON = ("//a[text()='View Product']")
ADD_BATCH_LINK = ("//a[text()='Add batch']")

def click_add_vaccine_button():
    find_element_and_perform_action(ADD_VACCINE_BUTTON,"click")

def click_first_available_add_batch_link():
    element = "(//a[text()='Add batch'])[1]"
    find_element_and_perform_action(element, "click")

def click_vaccine_type_add_batch_link(site, vaccine_type):
    element = (f"//h1[text() = '{site}']/following-sibling::div//td[text()='{vaccine_type}']/following-sibling::td/a[text()='Add batch']")
    find_element_and_perform_action(element, "click")

def select_site(site):
    find_element_and_perform_action(SELECT_SITE_DROPDOWN, "select_option", site)

def click_site(site):
    element = (f"//caption[text()='{site}']")
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
