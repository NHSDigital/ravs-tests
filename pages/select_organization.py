from init_helpers import *

continue_to_home_page_button = ("role", "button", "Continue")

def click_continue_to_home_page_button():
    if check_element_exists(continue_to_home_page_button):
        find_element_and_perform_action(continue_to_home_page_button, "click")

def select_site(site):
    element = ("role", "radio", site)
    if check_element_exists(element):
        find_element_and_perform_action(element, "click")
