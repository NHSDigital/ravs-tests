from init_helpers import *

WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT = ("role", "heading", "Which batch are you using?")
CONTINUE_TO_ELIGIBILITY_SCREEN = ("role", "button", "Continue")
SELECT_BATCH_ERROR_MESSAGE_LINK = ("role", "link", "Select a batch")
SELECT_BATCH_ERROR_MESSAGE_TEXT = ("text", "Error: Select a batch")

def check_which_vaccine_are_you_giving_label_exists():
    wait_for_element_to_appear(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)
    return check_element_exists(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)

def click_batch_radio_button(batch):
    wait_for_element_to_appear(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)
    element = ("role", "radio", batch)
    find_element_and_perform_action(element, "click")

def check_select_batch_error_message_link_exists():
    wait_for_element_to_appear(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)
    return check_element_exists(SELECT_BATCH_ERROR_MESSAGE_LINK)

def check_select_batch_error_message_text_exists():
    wait_for_element_to_appear(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)
    return check_element_exists(SELECT_BATCH_ERROR_MESSAGE_TEXT)

def click_select_vaccine_error_message_link():
    wait_for_element_to_appear(WHICH_BATCH_ARE_YOU_USING_TEXT_ELEMENT)
    find_element_and_perform_action(SELECT_BATCH_ERROR_MESSAGE_LINK, "click")

def click_continue_to_choose_eligibility_screen():
    find_element_and_perform_action(CONTINUE_TO_ELIGIBILITY_SCREEN, "click")
