from datetime import datetime
from init_helpers import *
import re
from pages.home_page import click_vaccines_nav_link

ADD_BATCH_LINK = ("(//a[text()='Add batch'])[1]")
REACTIVATE_BATCH_CONFIRMATION_BUTTON = ("//button[text()='Reactivate']")
PAGE_LOADING_ELEMENT = ("role", "status")

def ensure_add_batch_link_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(ADD_BATCH_LINK):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(ADD_BATCH_LINK)

def ensure_reactivate_batch_confirmation_button_is_visible():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(REACTIVATE_BATCH_CONFIRMATION_BUTTON):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(REACTIVATE_BATCH_CONFIRMATION_BUTTON)

def click_add_batch_link():
    ensure_add_batch_link_is_visible()
    find_element_and_perform_action(ADD_BATCH_LINK, "click")

def check_batch_number_and_expiry_date_exists(batch_number, expiry_date, wait):
    ensure_add_batch_link_is_visible()
    formatted_expiry_date = date_format_with_name_of_month_shortened(expiry_date)
    element = (f"//tr[td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}'] and td[normalize-space(text()) = '{formatted_expiry_date}']]")
    return check_element_exists(element, wait)

def check_batch_number_is_active_with_date(batch_number, expiry_date, wait):
    click_vaccines_nav_link()
    ensure_add_batch_link_is_visible()
    formatted_expiry_date = date_format_with_name_of_month(expiry_date)
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']/following-sibling::td['{formatted_expiry_date}']/following-sibling::td/strong[not(contains(., 'Inactive'))]")
    return check_element_exists(element, wait)

def click_reactivate_batch_link(batch_number, batch_expiry_date):
    ensure_reactivate_batch_confirmation_button_is_visible()
    date = date_format_with_name_of_month(batch_expiry_date)
    element = (f"//tr[td[contains(text(), '{batch_number}')] and td[contains(text(), '{date}')]]//a[contains(@id, 'reactivateBatchId')]")
    find_element_and_perform_action(element, "click")

def click_reactivate_batch_confirmation_button():
    ensure_reactivate_batch_confirmation_button_is_visible()
    if check_element_exists(REACTIVATE_BATCH_CONFIRMATION_BUTTON):
        find_element_and_perform_action(REACTIVATE_BATCH_CONFIRMATION_BUTTON, "click")
