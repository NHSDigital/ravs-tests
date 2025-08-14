import time
from init_helpers import *

INVITE_ORG_TEXT_ELEMENT = ("text", "Invite an organisation to create an NHS Record a vaccination service (RAVS) account.")
ONCE_SET_UP_TEXT_ELEMENT = ("text", "Once they's re set up, they can add other users and vaccines.")
PAGE_LOADING_ELEMENT = ("role", "status")
INVITE_AN_ORG_BUTTON = ("role", "button", "Invite an organisation")

def ensure_invite_an_organisation_label_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(INVITE_ORG_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(INVITE_ORG_TEXT_ELEMENT)
        wait_for_element_to_appear(ONCE_SET_UP_TEXT_ELEMENT)

def click_invite_an_organisation_button():
    find_element_and_perform_action(INVITE_ORG_TEXT_ELEMENT, "click")

def click_invited_organisation_name_link(org):
    element = ("role", "cell", org)
    check_element_exists(element)
    find_element_and_perform_action(element, "click")
