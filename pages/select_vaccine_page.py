from init_helpers import *

WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT = ("role", "heading", "Which vaccine are you giving?")
CONTINUE_TO_CHOOSE_BATCH_SCREEN = ("role", "button", "Continue")
SELECT_VACCINE_ERROR_MESSAGE_LINK = ("role", "link", "Select the vaccine")
SELECT_VACCINE_ERROR_MESSAGE_TEXT = ("text", "Error: Select the vaccine")
SELECT_VACCINE_PRODUCT_ERROR_MESSAGE_LINK = ("role", "link", "Select the vaccine product")
SELECT_VACCINE_PRODUCT_ERROR_MESSAGE_TEXT = ("text", "Error: Select the vaccine product")

def check_which_vaccine_are_you_giving_label_exists():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    return check_element_exists(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)

def click_vaccine_radio_button(vaccine):
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    element = ("role", "radio", vaccine)
    find_element_and_perform_action(element, "click")

def click_vaccine_product_radio_button(vaccine_product):
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    element = ("role", "radio", vaccine_product)
    find_element_and_perform_action(element, "click")

def check_select_vaccine_error_message_link_exists():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    return check_element_exists(SELECT_VACCINE_ERROR_MESSAGE_LINK)

def check_select_vaccine_error_message_text_exists():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    return check_element_exists(SELECT_VACCINE_ERROR_MESSAGE_TEXT)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_VACCINE_ERROR_MESSAGE_LINK, "click")

def check_select_vaccine_product_error_message_link_exists():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    return check_element_exists(SELECT_VACCINE_PRODUCT_ERROR_MESSAGE_LINK)

def check_select_vaccine_product_error_message_text_exists():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    return check_element_exists(SELECT_VACCINE_PRODUCT_ERROR_MESSAGE_TEXT)

def click_select_vaccine_product_error_message_link():
    wait_for_element_to_appear(WHICH_VACCINE_ARE_YOU_GIVING_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_VACCINE_PRODUCT_ERROR_MESSAGE_LINK, "click")

def click_continue_to_choose_batch_screen():
    find_element_and_perform_action(CONTINUE_TO_CHOOSE_BATCH_SCREEN, "click")
