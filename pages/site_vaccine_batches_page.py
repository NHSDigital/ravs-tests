from init_helpers import *

ADD_BATCH_BUTTON = ("//button[text()='Add batch']")
SELECT_SITE_RADIOBUTTON = ("#SiteId")
BACK_BUTTON_ON_VACCINE_BATCHES_PAGE = ("//a[@href='/site-vaccines']")
COVID_VACCINE_RADIOBUTTON = ("//input[@class='nhsuk-radios__input' and @id='VaccineProgramId' and @value='1']")
FLU_VACCINE_RADIOBUTTON = ("//input[@class='nhsuk-radios__input' and @id='VaccineProgramId' and @value='2']")
CANCEL_ADDING_VACCINE_BATCHES_BUTTON = ("//button[text()='Cancel']")
CONFIRM_VACCINE_BATCHES_CHOICES_BUTTON = ("//button[text()='Confirm choices']")
SELECT_VACCINES_LABEL = ("//legend[text()='Select vaccines']")
FLU_BATCH_NUMBER_INPUT_FIELD = ("#FluBatchNumber")
COVID_BATCH_NUMBER_PREFIX_INPUT_FIELD = ("#CovidBatchNumberPrefix")
COVID_BATCH_NUMBER_SUFFIX_INPUT_FIELD = ("#CovidBatchNumberSuffix")
EXPIRY_DATE_DAY_INPUT_FIELD = ("#ExpiryDate_1")
EXPIRY_DATE_MONTH_INPUT_FIELD = ("#ExpiryDate_2")
EXPIRY_DATE_YEAR_INPUT_FIELD = ("#ExpiryDate_3")
COVID_BATCH_NUMBER_PREFIX_ERROR_LABEL = ("#CovidBatchNumberPrefixIdError")
COVID_BATCH_NUMBER_SUFFIX_ERROR_LABEL = ("#CovidBatchNumberSuffixIdError")
EXPIRY_DAY_INPUT_ERROR_LABEL = ("#ExpiryDate_1IdError")
EXPIRY_MONTH_INPUT_ERROR_LABEL = ("#ExpiryDate_2IdError")
EXPIRY_YEAR_INPUT_ERROR_LABEL = ("#ExpiryDate_3IdError")

def check_required_field_error_appears_for_expiry_month(wait):
    return check_element_exists(EXPIRY_MONTH_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_covid_batch_prefix(wait):
    return check_element_exists(COVID_BATCH_NUMBER_PREFIX_ERROR_LABEL, wait)

def check_required_field_error_appears_for_covid_batch_suffix(wait):
    return check_element_exists(COVID_BATCH_NUMBER_SUFFIX_ERROR_LABEL, wait)

def check_required_field_error_appears_for_expiry_year(wait):
    return check_element_exists(EXPIRY_YEAR_INPUT_ERROR_LABEL, wait)

def check_required_field_error_appears_for_expiry_DAY(wait):
    return check_element_exists(EXPIRY_DAY_INPUT_ERROR_LABEL, wait)

def enter_expiry_date(date):
    day, month, year = date.split('/')
    find_element_and_perform_action(EXPIRY_DATE_DAY_INPUT_FIELD, "input_text",day)
    find_element_and_perform_action(EXPIRY_DATE_MONTH_INPUT_FIELD,"input_text", month)
    find_element_and_perform_action(EXPIRY_DATE_YEAR_INPUT_FIELD, "input_text",year)

def enter_flu_batch_number(batchnumber):
    find_element_and_perform_action(FLU_BATCH_NUMBER_INPUT_FIELD, "input_text",batchnumber)

def enter_covid_batch_number_prefix(batchnumber):
    find_element_and_perform_action(COVID_BATCH_NUMBER_PREFIX_INPUT_FIELD,"input_text", batchnumber)

def enter_covid_batch_number_suffix(batchnumber):
    find_element_and_perform_action(COVID_BATCH_NUMBER_SUFFIX_INPUT_FIELD,"input_text", batchnumber)

def click_back_button_on_vaccine_batches_page():
    find_element_and_perform_action(BACK_BUTTON_ON_VACCINE_BATCHES_PAGE,"click")

def click_select_vaccines_label():
    release_mouse()
    find_element_and_perform_action(SELECT_VACCINES_LABEL, "click")

def click_cancel_adding_vaccine_batches_button():
    find_element_and_perform_action(CANCEL_ADDING_VACCINE_BATCHES_BUTTON,"click")

def click_confirm_vaccine_batch_choices_button():
    find_element_and_perform_action(CONFIRM_VACCINE_BATCHES_CHOICES_BUTTON, "click")

def Click_add_batch_button():
    find_element_and_perform_action(ADD_BATCH_BUTTON, "click")

def check_add_batch_button_exists():
    return check_element_exists(ADD_BATCH_BUTTON, True)

def click_site_radio_button(site):
    element = (f"//label[text()='{site}']/preceding-sibling::input[@id='SiteId']")
    find_element_and_perform_action(element, "click")

def click_covid_vaccine_radiobutton():
    find_element_and_perform_action(COVID_VACCINE_RADIOBUTTON, "click")

def click_flu_vaccine_radiobutton():
    find_element_and_perform_action(FLU_VACCINE_RADIOBUTTON, "click_checkbox")

def click_covid_vaccine_type_radiobutton_on_add_batches_page(vaccinetype):
    xpath_map = {
        "comirnaty original/omicron ba.4-5": "//input[@class='nhsuk-radios__input' and @id='CovidVaccineId' and @value='1']",
        "comirnaty 30 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @id='CovidVaccineId' and @value='2']",
        "comirnaty 10 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @id='CovidVaccineId' and @value='3']",
        "comirnaty 3 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @id='CovidVaccineId' and @value='4']",
        "ppikevax xbb.1.5": "//input[@class='nhsuk-radios__input' and @id='CovidVaccineId' and @value='5']"
    }
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def click_flu_vaccine_type_radiobutton_on_add_batches_page(vaccinetype):
    xpath_map = {
        "fluenz tetra - laiv": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='6']",
        "quadrivalent influenza vaccine - qive": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='7']",
        "quadrivalent influvac sub - unit tetra - qive": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='8']",
        "flucelvax tetra - qivc": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='9']",
        "supemtek - qivr": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='10']",
        "fluad tetra - aqiv": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='12']",
        "cell-based quadrivalent - qivc": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='13']",
        "adjuvanted quadrivalent - aqiv": "//input[@class='nhsuk-radios__input' and @id='FluVaccineId' and @value='14']"
    }
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def check_vaccine_already_added_warning_message_exists(site, vaccine):
    element = (f"//span[text()='{vaccine} has already been added to {site}']")
    return check_element_exists(element, True)

