# from init_helpers import *
# from test_data.get_values_from_models import get_flu_vaccine_add_batch_radio_button_xpath, get_covid_vaccine_add_batch_radio_button_xpath





# COVID_BATCH_NUMBER_PREFIX_ERROR_LABEL = ("#CovidBatchNumberPrefixIdError")
# COVID_BATCH_NUMBER_SUFFIX_ERROR_LABEL = ("#CovidBatchNumberSuffixIdError")
# EXPIRY_DAY_INPUT_ERROR_LABEL = ("#ExpiryDate_1IdError")
# EXPIRY_MONTH_INPUT_ERROR_LABEL = ("#ExpiryDate_2IdError")
# EXPIRY_YEAR_INPUT_ERROR_LABEL = ("#ExpiryDate_3IdError")
# REACTIVATE_BATCH_CONFIRMATION_BUTTON = ("//button[text()='Reactivate']")

# def click_reactivate_batch_confirmation_button():
#     find_element_and_perform_action(REACTIVATE_BATCH_CONFIRMATION_BUTTON, "click")

# def get_first_active_batch_number_value():
#     xpath = "(//tbody[@class='nhsuk-table__body']//tr[td[@role='cell'][3]//strong[text()='Active']][1]//td[@role='cell'])[1]"
#     wait_for_element_to_appear(("xpath", xpath))
#     full_text = find_element_and_perform_action(("xpath", xpath), "get_text")
#     batch_number = full_text.replace('Batch number', '').strip()
#     return batch_number

# def check_required_field_error_appears_for_expiry_month(wait):
#     return check_element_exists(EXPIRY_MONTH_INPUT_ERROR_LABEL, wait)

# def check_required_field_error_appears_for_covid_batch_prefix(wait):
#     return check_element_exists(COVID_BATCH_NUMBER_PREFIX_ERROR_LABEL, wait)

# def check_required_field_error_appears_for_covid_batch_suffix(wait):
#     return check_element_exists(COVID_BATCH_NUMBER_SUFFIX_ERROR_LABEL, wait)

# def check_required_field_error_appears_for_expiry_year(wait):
#     return check_element_exists(EXPIRY_YEAR_INPUT_ERROR_LABEL, wait)

# def check_required_field_error_appears_for_expiry_DAY(wait):
#     return check_element_exists(EXPIRY_DAY_INPUT_ERROR_LABEL, wait)

# def enter_expiry_date(date):
#     day, month, year = date.split('/')
#     find_element_and_perform_action(EXPIRY_DATE_DAY_INPUT_FIELD, "input_text",day)
#     find_element_and_perform_action(EXPIRY_DATE_MONTH_INPUT_FIELD,"input_text", month)
#     find_element_and_perform_action(EXPIRY_DATE_YEAR_INPUT_FIELD, "input_text",year)

# def enter_flu_batch_number(batchnumber):
#     find_element_and_perform_action(FLU_BATCH_NUMBER_INPUT_FIELD, "input_text",batchnumber)

# def enter_covid_batch_number_prefix(batchnumber):
#     find_element_and_perform_action(COVID_BATCH_NUMBER_PREFIX_INPUT_FIELD,"input_text", batchnumber)

# def enter_covid_batch_number_suffix(batchnumber):
#     find_element_and_perform_action(COVID_BATCH_NUMBER_SUFFIX_INPUT_FIELD,"input_text", batchnumber)

# def click_back_button_on_vaccine_batches_page():
#     find_element_and_perform_action(BACK_BUTTON_ON_VACCINE_BATCHES_PAGE,"click")

# def click_select_vaccines_label():
#     release_mouse()
#     find_element_and_perform_action(SELECT_VACCINES_LABEL, "click")

# def click_cancel_adding_vaccine_batches_button():
#     find_element_and_perform_action(CANCEL_ADDING_VACCINE_BATCHES_BUTTON,"click")

# def click_confirm_vaccine_batch_choices_button():
#     find_element_and_perform_action(CONFIRM_VACCINE_BATCHES_CHOICES_BUTTON, "click")

# def click_add_batch_button():
#     find_element_and_perform_action(ADD_BATCH_BUTTON, "click")

# def check_add_batch_button_exists():
#     return check_element_exists(ADD_BATCH_BUTTON, True)

# def check_add_batch_button_enabled():
#     return check_element_enabled(ADD_BATCH_BUTTON, True)

# def click_site_radio_button(site):
#     element = (f"//label[text()='{site}']/preceding-sibling::input[@name='SiteId']")
#     find_element_and_perform_action(element, "click")

# def click_covid_vaccine_radiobutton():
#     find_element_and_perform_action(COVID_VACCINE_RADIOBUTTON, "click")

# def click_flu_vaccine_radiobutton():
#     find_element_and_perform_action(FLU_VACCINE_RADIOBUTTON, "click_checkbox")

# def click_covid_vaccine_type_radiobutton_on_add_batches_page(vaccinetype):
#     element = get_covid_vaccine_add_batch_radio_button_xpath(vaccinetype.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def click_flu_vaccine_type_radiobutton_on_add_batches_page(vaccinetype):
#     element = get_flu_vaccine_add_batch_radio_button_xpath(vaccinetype.lower())
#     if element:
#         find_element_and_perform_action(element, "click")
#     else:
#         print("Invalid vaccine type")

# def check_vaccine_already_added_warning_message_exists(site, vaccine):
#     element = (f"//span[text()='{site} already has {vaccine}']")
#     return check_element_exists(element, False)

