from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
BACK_TO_MANAGE_USERS_LINK = ("role", "button", "Back to Manage users")
DEACTIVATED_USERS_HEADING = ("role", "heading", "Deactivated users")
DEACTIVATED_USERS_LIST_TABLE = ("xpath", '//table[contains(@class, "nhsuk-table")]')

def check_deactivated_user_exists_in_list(user_email_address):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("cell", user_email_address, True)
    wait_for_element_to_appear(element)
    return check_element_exists(element)

def click_reactivate_user_link(user_email_address):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("xpath", f'//td[@class="nhsuk-table__cell" and text()="{user_email_address}"]/following-sibling::td[@class="nhsuk-table__cell"]/a[text()="Reactivate"]')
    find_element_and_perform_action(element, "click")

def click_back_to_manage_users_link():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_MANAGE_USERS_LINK)
    find_element_and_perform_action(BACK_TO_MANAGE_USERS_LINK, "click")

def check_deactivated_users_list_table_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_MANAGE_USERS_LINK)
    wait_for_element_to_appear(DEACTIVATED_USERS_HEADING)
    return check_element_exists(DEACTIVATED_USERS_LIST_TABLE)

def check_deactivated_users_page_heading_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_MANAGE_USERS_LINK)
    wait_for_element_to_appear(DEACTIVATED_USERS_HEADING)
    return check_element_exists(DEACTIVATED_USERS_HEADING)
