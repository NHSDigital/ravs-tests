from init_helpers import *

PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")

def check_deactivated_user_exists_in_list(user_email_address):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("cell", user_email_address, True)
    wait_for_element_to_appear(element)
    return check_element_exists(element)

def click_reactivate_user_link(user_email_address):
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    element = ("xpath", f'//td[@class="nhsuk-table__cell" and text()="{user_email_address}"]/following-sibling::td[@class="nhsuk-table__cell"]/a[text()="Reactivate"]')
    find_element_and_perform_action(element, "click")
