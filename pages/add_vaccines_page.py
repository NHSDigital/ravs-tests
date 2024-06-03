from init_helpers import *

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
    find_element_and_perform_action(ADD_VACCINE_BUTTON, "click")

def check_add_vaccine_button_exists():
    return check_element_exists(ADD_VACCINE_BUTTON, True)

def check_add_vaccine_button_enabled():
    return check_element_enabled(ADD_VACCINE_BUTTON, True)

def check_confirm_choices_button_enabled():
    return check_element_enabled(CONFIRM_VACCINE_CHOICES_BUTTON, True)

def click_site_radio_button(site):
    element = (f"//label[text()='{site}']/preceding-sibling::input[@id='SiteId']")
    find_element_and_perform_action(element, "click")

def click_covid_vaccine_checkbox():
    find_element_and_perform_action(COVID_VACCINE_CHECK_BOX, "click_checkbox")

def click_flu_vaccine_checkbox():
    find_element_and_perform_action(FLU_VACCINE_CHECK_BOX, "click_checkbox")

def click_covid_vaccine_type_checkbox(vaccinetype):
    xpath_map = {
        "comirnaty original/omicron ba.4-5": "//input[@class='nhsuk-checkboxes__input' and @name='CovidVaccineIds' and @value='1']",
        "comirnaty 30 omicron xbb.1.5": "//input[@class='nhsuk-checkboxes__input' and @name='CovidVaccineIds' and @value='2']",
        "comirnaty 3 omicron xbb.1.5": "//input[@class='nhsuk-checkboxes__input' and @name='CovidVaccineIds' and @value='3']",
        "comirnaty 10 omicron xbb.1.5": "//input[@class='nhsuk-checkboxes__input' and @name='CovidVaccineIds' and @value='4']",
        "spikevax xbb.1.5": "//input[@class='nhsuk-checkboxes__input' and @name='CovidVaccineIds' and @value='5']"
    }
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click_checkbox")
    else:
        print("Invalid vaccine type")


def click_flu_vaccine_type_checkbox(vaccinetype):
    xpath_map = {
        "fluenz tetra - laiv": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='6']",
        "quadrivalent influenza vaccine - qive": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='7']",
        "quadrivalent influvac sub - unit tetra - qive": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='8']",
        "flucelvax tetra - qivc": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='9']",
        "supemtek - qivr": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='10']",
        "fluad tetra - aqiv": "//input[@class='nhsuk-checkboxes__input' and @name='FluVaccineIds' and @value='11']",
        "cell-based quadrivalent - qivc": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='12']",
        "adjuvanted quadrivalent - aqiv": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='13']"
    }
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click_checkbox")
    else:
        print("Invalid vaccine type")


def check_vaccine_already_added_warning_message_exists(site, vaccine):
    element = (f"//span[text()='{site} already has {vaccine}']")
    return check_element_exists(element, True)

