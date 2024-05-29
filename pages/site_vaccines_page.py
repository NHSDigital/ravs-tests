from init_helpers import *

ADD_VACCINES_BUTTON = ("//button [text()='Add vaccines']")
ADD_BATCHES_BUTTON = ("//button [text()='Add batches']")
SELECT_SITE_DROPDOWN = ("//select[@name='SiteId']")
BACK_BUTTON_ON_VACCINES_PAGE = ("//a[@href='/settings']")
CONFIRM_CHOICES_BUTTON = ("//button[text()='Confirm choices']")
CANCEL_BUTTON = ("//button[text()='Cancel']")

def click_back_button_on_vaccines_page():
    find_element_and_perform_action(BACK_BUTTON_ON_VACCINES_PAGE, "click")

def click_confirm_vaccine_choices_button():
    find_element_and_perform_action(CONFIRM_CHOICES_BUTTON, "click")

def click_cancel_vaccine_choices_button():
    find_element_and_perform_action(CANCEL_BUTTON, "click")

def Click_add_vaccines_button():
    find_element_and_perform_action(ADD_VACCINES_BUTTON,"click")

def Check_add_vaccines_button_exists():
    check_element_exists(ADD_VACCINES_BUTTON, True)

def Click_add_batches_button():
    find_element_and_perform_action(ADD_BATCHES_BUTTON, "click")

def select_site(site):
    find_element_and_perform_action(SELECT_SITE_DROPDOWN, "select_option", site)

def click_site(site):
    element = (f"//caption[text()='{site}']")
    find_element_and_perform_action(element, "click")

def check_vaccine_has_been_added(vaccine, site, wait):
    element = (f"//strong[text()='{site}']/parent::span/preceding-sibling::a[contains(., '{vaccine}')]")
    return check_element_exists(element, wait)

def get_batches_count_for_vaccine_in_a_site(vaccine,site):
    element = (f"//strong[text()='{site}']/parent::span/preceding-sibling::a[contains(., '{vaccine}')]/following::span[text()='Batches']")
    return find_element_and_perform_action(element, "get_text")

def get_batches_count_for_vaccine_in_a_site(vaccine,site):
    element = (f"//strong[text()='{site}']/parent::span/preceding-sibling::a[contains(., '{vaccine}')]/following::span[text()='Batches']")
    return find_element_and_perform_action(element, "get_text")

def check_no_batches_added_for_vaccine_in_a_site(vaccine,site, wait):
    element = (f"//strong[text()='{site}']/parent::span/preceding-sibling::a[contains(., '{vaccine}')]/following::span[text()='Batches']/following::strong[text()=' NO BATCHES ADDED']")
    return check_element_exists(element, wait)
