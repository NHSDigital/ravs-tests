# from init_helpers import *

# VACCINATOR_ORGANISATION_DROPDOWN_ELEMENT = ("#VaccinatorOrganisationId")
# SITE_DROPDOWN_ELEMENT = ("//select[@name='SiteId']")
# CARE_MODEL_DROPDOWN_ELEMENT = ("//select[@name='CareModelId']")
# CONTINUE_BUTTON_ELEMENT = ("//button[@type='submit']")
# CAREHOME_NAME_INPUT_ELEMENT = ("#CareHomeName")
# CAREHOME_ODS_CODE_INPUT_ELEMENT = ("#CareHomeOdsCode")
# CAREHOME_ADDRESS_INPUT_ELEMENT = ("#CareHomeAddress")
# CAREHOME_POSTCODE_INPUT_ELEMENT = ("#CareHomePostcode")
# CAREHOME_ENTER_DETAILS_MANUALLLY_CHECKBOX_ELEMENT = ("#DetailsEnteredManually")

# def select_vaccinator_organisation(vaccinatorOrganisation):
#     find_element_and_perform_action(VACCINATOR_ORGANISATION_DROPDOWN_ELEMENT, "select_option", vaccinatorOrganisation)

# def select_site(site):
#     find_element_and_perform_action(SITE_DROPDOWN_ELEMENT, "select_option", site)
#     attach_screenshot("user_has_selected_site")

# def select_care_model(careModel):
#     find_element_and_perform_action(CARE_MODEL_DROPDOWN_ELEMENT,"select_option", careModel)
#     attach_screenshot("user_has_selected_care_model")

# def enter_carehome_name(name):
#     find_element_and_perform_action(CAREHOME_NAME_INPUT_ELEMENT, "input_text", name)
#     # element_to_click = (f"//li[text()[contains(., '{name}')]]")
#     element_to_click = (f"//strong[text()='{name}']")
#     find_element_and_perform_action(element_to_click, "click")
#     attach_screenshot("user_has_entered_care_home_details")

# def enter_carehome_ods_code(odscode):
#     find_element_and_perform_action(CAREHOME_ODS_CODE_INPUT_ELEMENT, "input_text", odscode)

# def enter_carehome_address(address):
#     find_element_and_perform_action(CAREHOME_ADDRESS_INPUT_ELEMENT, "input_text", address)

# def enter_carehome_postcode(postcode):
#     find_element_and_perform_action(CAREHOME_POSTCODE_INPUT_ELEMENT, "input_text", postcode)

# def click_continue_to_record_a_vaccination_homepage():
#     find_element_and_perform_action(CONTINUE_BUTTON_ELEMENT, "click")
