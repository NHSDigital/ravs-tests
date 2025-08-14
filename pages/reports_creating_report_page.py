from init_helpers import *

CREATING_REPORT_ELEMENT = ("text", "Loading...Loading...")
DOWNLOAD_REPORT_BUTTON = ("role", "button", "Download report")
PAGE_LOADING_ELEMENT = ("role", "status")

def check_reports_download_report_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_disappear(CREATING_REPORT_ELEMENT)
    wait_for_element_to_appear(DOWNLOAD_REPORT_BUTTON)
    return check_element_exists(DOWNLOAD_REPORT_BUTTON)

def click_reports_download_report_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_disappear(CREATING_REPORT_ELEMENT)
    wait_for_element_to_appear(DOWNLOAD_REPORT_BUTTON)
    return click_and_get_download_path(DOWNLOAD_REPORT_BUTTON, "click", 300, "downloads")

