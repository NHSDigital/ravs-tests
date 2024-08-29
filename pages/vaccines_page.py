from init_helpers import *
import re

ADD_VACCINE_BUTTON = ("//a[text()='Add vaccine']")
SELECT_SITE_DROPDOWN = ("//select[@name='SiteId']")
VIEW_PRODUCT_BUTTON = ("//a[text()='View Product']")
ADD_BATCH_BUTTON = ("//a[text()='Add batch']")

def click_add_vaccine_button():
    find_element_and_perform_action(ADD_VACCINE_BUTTON,"click")

def click_add_batch_button():
    find_element_and_perform_action(ADD_BATCH_BUTTON, "click")

def select_site(site):
    find_element_and_perform_action(SELECT_SITE_DROPDOWN, "select_option", site)

def click_site(site):
    element = (f"//caption[text()='{site}']")
    find_element_and_perform_action(element, "click")

def check_vaccine_has_been_added(vaccine, wait):
    element = (f"//h2[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{vaccine.lower()}')]")
    return check_element_exists(element, wait)

def click_view_product(vaccine_type):
    element = (f"//td[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{vaccine_type.lower()}')]/following-sibling::td/a[text()='View product']")
    find_element_and_perform_action(element, "click")
