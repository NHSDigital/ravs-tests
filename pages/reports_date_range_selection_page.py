from init_helpers import *

CREATE_REPORT_BUTTON = ("role", "button", "Create report")
NO_VACCINATION_DATE_TO_REPORT = ("text", "No vaccination data to report")
TODAY_RADIO_BUTTON = ("label", "Today", None, True)
YESTERDAY_RADIO_BUTTON = ("label", "Yesterday")
LAST_7_DAYS_RADIO_BUTTON = ("label", "Last 7 days (includes today)")
LAST_14_DAYS_RADIO_BUTTON = ("label", "Last 14 days (includes today)")
LAST_31_DAYS_RADIO_BUTTON = ("label", "Last 31 days (includes today)")
CUSTOM_DATE_RANGE_RADIO_BUTTON = ("label", "Select a custom date range up to 31 days")
CONTINUE_TO_SELECT_VACCINE_BUTTON = ("role", "button", "Continue")
BACK_TO_REPORTS_HOMEPAGE_BUTTON = ("role", "button", "Back")
SELECT_A_DATE_RANGE_ERROR_MESSAGE_LINK = ("role", "button", "Please select a date range")
SELECT_A_DATE_RANGE_ERROR_MESSAGE_TEXT = ("text", "Error: Please select a date")
FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK = ("role", "button", "From date must be valid")
FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT = ("text", "Error: From date must be valid")
TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK = ("role", "button", "To date must be valid")
TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT = ("text", "Error: To date must be valid")
DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_LINK = ("role", "button", "The date range must be within 31 days")
DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_TEXT = ("text", "Error: The date range must be within 31 days")
PAGE_LOADING_ELEMENT = ("text", "Loading...Loading...")
FROM_DATE_DAY_INPUT_ELEMENT = ("#fromDate-day")
FROM_DATE_MONTH_INPUT_ELEMENT = ("#fromDate-month")
FROM_DATE_YEAR_INPUT_ELEMENT = ("#fromDate-year")
TO_DATE_DAY_INPUT_ELEMENT = ("#toDate-day")
TO_DATE_MONTH_INPUT_ELEMENT = ("#toDate-month")
TO_DATE_YEAR_INPUT_ELEMENT = ("#toDate-year")

def check_create_report_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CREATE_REPORT_BUTTON)
    return check_element_exists(CREATE_REPORT_BUTTON)

def check_no_vaccination_data_to_report_message_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(NO_VACCINATION_DATE_TO_REPORT)
    return check_element_exists(NO_VACCINATION_DATE_TO_REPORT)

def check_create_report_button_enabled():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CREATE_REPORT_BUTTON)
    return check_element_enabled(CREATE_REPORT_BUTTON)

def click_create_report_button():
    wait_for_element_to_appear(CREATE_REPORT_BUTTON)
    find_element_and_perform_action(CREATE_REPORT_BUTTON, "click")

def check_today_radio_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(TODAY_RADIO_BUTTON)
    return check_element_exists(TODAY_RADIO_BUTTON)

def click_today_radio_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(TODAY_RADIO_BUTTON)
    find_element_and_perform_action(TODAY_RADIO_BUTTON, "check")

def check_yesterday_radio_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(YESTERDAY_RADIO_BUTTON)
    return check_element_exists(YESTERDAY_RADIO_BUTTON)

def click_yesterday_radio_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(YESTERDAY_RADIO_BUTTON)
    find_element_and_perform_action(YESTERDAY_RADIO_BUTTON, "check")

def check_last_7_days_radio_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_7_DAYS_RADIO_BUTTON)
    return check_element_exists(LAST_7_DAYS_RADIO_BUTTON)

def click_last_7_days_radio_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_7_DAYS_RADIO_BUTTON)
    find_element_and_perform_action(LAST_7_DAYS_RADIO_BUTTON, "check")

def check_last_14_days_radio_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_14_DAYS_RADIO_BUTTON)
    return check_element_exists(LAST_14_DAYS_RADIO_BUTTON)

def click_last_14_days_radio_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_14_DAYS_RADIO_BUTTON)
    find_element_and_perform_action(LAST_14_DAYS_RADIO_BUTTON, "check")

def check_last_31_days_radio_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_31_DAYS_RADIO_BUTTON)
    return check_element_exists(LAST_31_DAYS_RADIO_BUTTON)

def click_last_31_days_radio_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(LAST_31_DAYS_RADIO_BUTTON)
    find_element_and_perform_action(LAST_31_DAYS_RADIO_BUTTON, "check")

def check_select_a_custom_date_range_up_to_31_days_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CUSTOM_DATE_RANGE_RADIO_BUTTON)
    return check_element_exists(CUSTOM_DATE_RANGE_RADIO_BUTTON)

def click_select_a_custom_date_range_up_to_31_days_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CUSTOM_DATE_RANGE_RADIO_BUTTON)
    find_element_and_perform_action(CUSTOM_DATE_RANGE_RADIO_BUTTON, "check")

def enter_from_date(date):
    day, month, year = date.split('/')
    wait_for_element_to_appear(FROM_DATE_DAY_INPUT_ELEMENT)
    find_element_and_perform_action(FROM_DATE_DAY_INPUT_ELEMENT, "input_text",day)
    find_element_and_perform_action(FROM_DATE_MONTH_INPUT_ELEMENT,"input_text", month)
    find_element_and_perform_action(FROM_DATE_YEAR_INPUT_ELEMENT, "input_text",year)

def enter_to_date(date):
    day, month, year = date.split('/')
    wait_for_element_to_appear(TO_DATE_DAY_INPUT_ELEMENT)
    find_element_and_perform_action(TO_DATE_DAY_INPUT_ELEMENT, "input_text",day)
    find_element_and_perform_action(TO_DATE_MONTH_INPUT_ELEMENT,"input_text", month)
    find_element_and_perform_action(TO_DATE_YEAR_INPUT_ELEMENT, "input_text",year)

def check_select_a_date_range_error_message_text_exists():
    wait_for_element_to_appear(SELECT_A_DATE_RANGE_ERROR_MESSAGE_TEXT)
    return check_element_exists(SELECT_A_DATE_RANGE_ERROR_MESSAGE_TEXT)

def check_select_a_date_range_error_message_link_exists():
    wait_for_element_to_appear(SELECT_A_DATE_RANGE_ERROR_MESSAGE_LINK)
    return check_element_exists(SELECT_A_DATE_RANGE_ERROR_MESSAGE_LINK)

def click_select_a_date_range_error_message_link():
    wait_for_element_to_appear(SELECT_A_DATE_RANGE_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(SELECT_A_DATE_RANGE_ERROR_MESSAGE_LINK, "click")

def check_from_date_must_be_valid_error_message_text_exists():
    wait_for_element_to_appear(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT)
    return check_element_exists(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT)

def check_from_date_must_be_valid_error_message_link_exists():
    wait_for_element_to_appear(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)
    return check_element_exists(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)

def click_from_date_must_be_valid_error_message_link():
    wait_for_element_to_appear(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(FROM_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK, "click")

def check_to_date_must_be_valid_error_message_text_exists():
    wait_for_element_to_appear(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT)
    return check_element_exists(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_TEXT)

def check_to_date_must_be_valid_error_message_link_exists():
    wait_for_element_to_appear(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)
    return check_element_exists(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)

def click_to_date_must_be_valid_error_message_link():
    wait_for_element_to_appear(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(TO_DATE_MUST_BE_VALID_ERROR_MESSAGE_LINK, "click")

def check_date_range_must_be_valid_error_message_text_exists():
    wait_for_element_to_appear(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_TEXT)
    return check_element_exists(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_TEXT)

def check_date_range_must_be_valid_error_message_link_exists():
    wait_for_element_to_appear(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_LINK)
    return check_element_exists(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_LINK)

def click_date_range_must_be_valid_error_message_link():
    wait_for_element_to_appear(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_LINK)
    find_element_and_perform_action(DATE_RANGE_SHOULD_BE_WITHIN_31_DAYS_ERROR_MESSAGE_LINK, "click")

def check_continue_to_reports_select_vaccine_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_SELECT_VACCINE_BUTTON)
    return check_element_exists(CONTINUE_TO_SELECT_VACCINE_BUTTON)

def click_continue_to_reports_select_vaccine_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(CONTINUE_TO_SELECT_VACCINE_BUTTON)
    find_element_and_perform_action(CONTINUE_TO_SELECT_VACCINE_BUTTON, "click")

def check_back_to_reports_homepage_button_exists():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_REPORTS_HOMEPAGE_BUTTON)
    return check_element_exists(BACK_TO_REPORTS_HOMEPAGE_BUTTON)

def click_back_to_reports_homepage_button():
    wait_for_element_to_disappear(PAGE_LOADING_ELEMENT)
    wait_for_element_to_appear(BACK_TO_REPORTS_HOMEPAGE_BUTTON)
    find_element_and_perform_action(BACK_TO_REPORTS_HOMEPAGE_BUTTON, "click")
