from init_helpers import *

FROM_CALENDAR_ELEMENT = ("(//input[@placeholder='Open Calendar'])[1]") 
TO_CALENDAR_ELEMENT = ("(//input[@placeholder='Open Calendar'])[2]")
SORT_BY_ELEMENT = ("//span[text()='Sort by']")
STATUS_ELEMENT = ("//span[text()='Status']")
VACCINES_ELEMENT = ("//span[text()='Vaccines']")
NO_APPOINTMENTS_ALERT=("//div[text()='No Appointment to show']")
DATEPICKER_ELEMENT = ("//div[@class='rdt dateInput rdtOpen']")
FIRSTPATIENT_LINK_ELEMENT = ("(//a[@href='/patient/1'])[1]")
ACTIVE_FROM_DATE=("(//td[@class='rdtDay rdtActive'])[1]")
ACTIVE_TO_DATE=("(//td[@class='rdtDay rdtActive'])[2]")
ACTIVE_TO_DATE_TODAY=("(//td[@class='rdtDay rdtActive rdtToday'])[1]")

def click_from_calendar():
    find_element_and_perform_action(FROM_CALENDAR_ELEMENT, "click")

def click_to_calendar():
    find_element_and_perform_action(TO_CALENDAR_ELEMENT, "click")

def click_sort_by():
    find_element_and_perform_action(SORT_BY_ELEMENT, "click")    

def click_status():
    find_element_and_perform_action(STATUS_ELEMENT, "click")     

def click_vaccines():
    find_element_and_perform_action(VACCINES_ELEMENT, "click")       

def check_no_appointments_to_show_alert_exists():
    return check_element_exists(NO_APPOINTMENTS_ALERT, True)          

def check_datepicker_element_open():    
    return check_element_exists(DATEPICKER_ELEMENT, True)       

def set_from_date(date):
    formatted_date = date.strftime('%a %d %b %Y')
    find_element_and_perform_action(FROM_CALENDAR_ELEMENT, "input_text", formatted_date)

def set_to_date(date):
    formatted_date = date.strftime('%a %d %b %Y')
    find_element_and_perform_action(TO_CALENDAR_ELEMENT, "input_text", formatted_date)    

def click_active_from_date():
    find_element_and_perform_action(ACTIVE_FROM_DATE, "click")    

def click_active_to_date():
    find_element_and_perform_action(ACTIVE_TO_DATE, "click")   

def click_active_to_date_today():
    find_element_and_perform_action(ACTIVE_TO_DATE_TODAY, "click")           

def click_first_patient():
    find_element_and_perform_action(FIRSTPATIENT_LINK_ELEMENT, "click")     