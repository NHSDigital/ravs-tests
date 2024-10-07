from init_helpers import *
import re

ADD_BATCH_LINK = ("(//a[text()='Add batch'])[1]")

def click_add_batch_link():
    find_element_and_perform_action(ADD_BATCH_LINK, "click")

def check_batch_number_exists(batch_number, wait):
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']")
    return check_element_exists(element, wait)

def check_batch_number_is_active(batch_number, wait):
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']/following-sibling::td/strong[not(contains(.,'Inactive'))]")
    return check_element_exists(element, wait)

def click_reactivate_batch_link(batch_number):
    element = (f"//td[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') = '{batch_number.lower()}']/following-sibling::td/a[text()='Reactivate batch']")
    find_element_and_perform_action(element, "click")
