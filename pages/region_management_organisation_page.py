import time
from init_helpers import *

YOU_HAVE_INVITED_TEXT_ELEMENT = ("text", "You have invited this organisation to create an NHS Record a vaccination service account.")
PAGE_LOADING_ELEMENT = ("role", "status")
DEACTIVATE_ORGANISATION_LINK = ("role", "link", "Deactivate Organisation")
ADD_ANOTHER_USER_BUTTON = ("role", "button", "Add another user")
BACK_TO_ALL_ORGANISATIONS_PAGE_LINK = ("role", "link", "Back to all organisations")

def ensure_you_have_invited_this_organisation_label_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    if not check_element_exists(YOU_HAVE_INVITED_TEXT_ELEMENT):
        wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
        wait_for_element_to_appear(YOU_HAVE_INVITED_TEXT_ELEMENT)

def check_deactivate_organisation_link_exists():
    check_element_exists(DEACTIVATE_ORGANISATION_LINK, wait=True)

def click_deactivate_organisation_link():
    wait_for_element_to_appear(DEACTIVATE_ORGANISATION_LINK)
    find_element_and_perform_action(DEACTIVATE_ORGANISATION_LINK, "click")

def click_add_another_user_button():
    wait_for_element_to_appear(ADD_ANOTHER_USER_BUTTON)
    find_element_and_perform_action(ADD_ANOTHER_USER_BUTTON, "click")

def check_add_another_user_button_exists():
    check_element_exists(ADD_ANOTHER_USER_BUTTON, wait=True)

def click_deactivate_organisation_link():
    wait_for_element_to_appear(DEACTIVATE_ORGANISATION_LINK)
    find_element_and_perform_action(DEACTIVATE_ORGANISATION_LINK, "click")

def check_back_to_all_organisations_link_exists():
    check_element_exists(BACK_TO_ALL_ORGANISATIONS_PAGE_LINK, wait=True)

def click_back_to_all_organisations_link():
    wait_for_element_to_appear(BACK_TO_ALL_ORGANISATIONS_PAGE_LINK)
    find_element_and_perform_action(BACK_TO_ALL_ORGANISATIONS_PAGE_LINK, "click")
