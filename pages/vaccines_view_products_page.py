from datetime import datetime
from init_helpers import *
import re
from pages.home_page import click_vaccines_nav_link

ADD_BATCH_LINK = ("(//a[text()='Add batch'])[1]")
REACTIVATE_BATCH_CONFIRMATION_BUTTON = ("//button[text()='Reactivate']")

def click_add_batch_link():
    find_element_and_perform_action(ADD_BATCH_LINK, "click")

def check_batch_number_and_expiry_date_exists(batch_number, expiry_date, wait):
    formatted_expiry_date = date_format_with_name_of_month_shortened(expiry_date)
    element = (f"//tr[td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']"
               f" and td[normalize-space(text()) = '{formatted_expiry_date}']]")
    return check_element_exists(element, wait)

def check_batch_number_is_active_with_date(batch_number, expiry_date, wait):
    click_vaccines_nav_link()
    formatted_expiry_date = date_format_with_name_of_month(expiry_date)
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']"
               f"/following-sibling::td['{formatted_expiry_date}']"
               f"/following-sibling::td/strong[not(contains(., 'Inactive'))]")
    return check_element_exists(element, wait)

def click_reactivate_batch_link(batch_number):
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']/following-sibling::td/a[text()='Reactivate batch']")
    find_element_and_perform_action(element, "click")

def click_reactivate_batch_confirmation_button():
    if check_element_exists(REACTIVATE_BATCH_CONFIRMATION_BUTTON):
        find_element_and_perform_action(REACTIVATE_BATCH_CONFIRMATION_BUTTON, "click")
