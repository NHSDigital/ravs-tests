from init_helpers import *
from test_data.get_values_from_models import get_flu_add_vaccine_checkbox_xpath, get_covid_add_vaccine_checkbox_xpath

ADD_VACCINE_BUTTON = ("//button[text()='Add vaccine']")
ADD_BATCHES_BUTTON = ("//button[text()='Add batches']")
SELECT_SITE_DROPDOWN = ("//select[@name='SiteId']")
BACK_BUTTON_ON_VACCINES_PAGE = ("(//a[@href='/settings'])[2]")
COVID_VACCINE_CHECK_BOX = ("//input[@class='nhsuk-checkboxes__input' and @name='VaccineProgramIds' and @value='1']")
FLU_VACCINE_CHECK_BOX = ("//input[@class='nhsuk-checkboxes__input' and @name='VaccineProgramIds' and @value='2']")
CANCEL_ADDING_VACCINES_BUTTON = ("//button[text()='Cancel']")
CONFIRM_VACCINE_CHOICES_BUTTON = ("//button[text()='Confirm choices']")
SELECT_VACCINES_LABEL = ("//legend[text()='Select vaccines']")

def click_back_button_on_vaccines_page():
    find_element_and_perform_action(BACK_BUTTON_ON_VACCINES_PAGE, "click")

def click_select_vaccines_label():
    release_mouse()
    find_element_and_perform_action(SELECT_VACCINES_LABEL, "click")

def click_cancel_adding_vaccines_button():
    find_element_and_perform_action(CANCEL_ADDING_VACCINES_BUTTON, "click")

def click_confirm_vaccine_choices_button():
    find_element_and_perform_action(CONFIRM_VACCINE_CHOICES_BUTTON, "click")

def Click_add_vaccine_button():
    if check_add_vaccine_button_exists() and check_add_vaccine_button_enabled():
        find_element_and_perform_action(ADD_VACCINE_BUTTON, "click")

def check_add_vaccine_button_exists():
    return check_element_exists(ADD_VACCINE_BUTTON, True)

def check_add_vaccine_button_enabled():
    return check_element_enabled(ADD_VACCINE_BUTTON, True)

def check_confirm_choices_button_enabled():
    return check_element_enabled(CONFIRM_VACCINE_CHOICES_BUTTON, True)

def click_site_radio_button(site):
    element = (f"//label[text()='{site}']/preceding-sibling::input[@name='SiteId']")
    find_element_and_perform_action(element, "click")

def click_covid_vaccine_checkbox():
    find_element_and_perform_action(COVID_VACCINE_CHECK_BOX, "click_checkbox")

def click_flu_vaccine_checkbox():
    find_element_and_perform_action(FLU_VACCINE_CHECK_BOX, "click_checkbox")

def click_covid_vaccine_type_checkbox(vaccinetype):
    element = get_covid_add_vaccine_checkbox_xpath(vaccinetype.lower())
    if check_element_exists(element):
        find_element_and_perform_action(element, "click_checkbox")
    else:
        print("Invalid vaccine type")


def click_flu_vaccine_type_checkbox(vaccinetype):
    element = get_flu_add_vaccine_checkbox_xpath(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click_checkbox")
    else:
        print("Invalid vaccine type")


def check_vaccine_already_added_warning_message_exists(site, vaccine):
    element = (f"//span[text()='{site} already has {vaccine}']")
    return check_element_exists(element, True)

