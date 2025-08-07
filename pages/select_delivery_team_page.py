from init_helpers import *

WHICH_TEAM_ARE_YOU_WORKING_WITH_TEXT_ELEMENT = ("role", "heading", "Which team are you working with?")
CONTINUE_TO_VACCINATOR_SCREEN = ("role", "button", "Continue")
SELECT_A_TEAM_ERROR_MESSAGE_LINK = ("role", "link", "Select a team")
SELECT_A_TEAM_ERROR_MESSAGE_TEXT = ("text", "Error: Select a team")

def ensure_which_team_are_you_working_with_label_is_visible():
    if not check_element_exists(WHICH_TEAM_ARE_YOU_WORKING_WITH_TEXT_ELEMENT):
        wait_for_element_to_appear(WHICH_TEAM_ARE_YOU_WORKING_WITH_TEXT_ELEMENT)

def check_which_team_are_you_working_with_label_exists():
    return check_element_exists(WHICH_TEAM_ARE_YOU_WORKING_WITH_TEXT_ELEMENT)

def click_team_radio_button(team):
    element = ("role", "radio", team)
    find_element_and_perform_action(element, "click")

def check_select_a_team_error_message_link_exists():
    return check_element_exists(SELECT_A_TEAM_ERROR_MESSAGE_LINK)

def check_select_a_team_error_message_text_exists():
    return check_element_exists(SELECT_A_TEAM_ERROR_MESSAGE_TEXT)

def click_select_a_team_error_message_link():
    find_element_and_perform_action(SELECT_A_TEAM_ERROR_MESSAGE_LINK, "click")

def click_continue_to_select_vaccinator_screen():
    find_element_and_perform_action(CONTINUE_TO_VACCINATOR_SCREEN, "click")
