from init_helpers import *

COVID_RADIOBUTTON = ("#VaccineProgramId-1") 
FLU_RADIOBUTTON = ("#VaccineProgramId-2") 
SAVE_AND_RETURN_BUTTON=("//button[text()='Save and return']")
CONTINUE_BUTTON=("//button[text()='Continue']")
BACK_ELEMENT = ("//a[@href='/patient/1']")

def click_covid_radiobutton():
    find_element_and_perform_action(COVID_RADIOBUTTON, "click")

def click_back_button_choosing_vaccine_for_patient():
    find_element_and_perform_action(BACK_ELEMENT, "click")    

def click_covid_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccinetype):
    xpath_map = {
        "comirnaty original/omicron ba.4-5": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='1']",
        "comirnaty 30 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='2']",
        "comirnaty 10 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='3']",
        "comirnaty 3 omicron xbb.1.5": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='4']",
        "ppikevax xbb.1.5": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='5']"
    }    
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")
    

def click_flu_vaccine_type_radiobutton_choose_vaccine_for_patient_on_consent_page(vaccinetype):
    xpath_map = {
        "fluenz tetra - laiv": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='6']",
        "quadrivalent influenza vaccine - qive": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='7']",
        "quadrivalent influvac sub - unit tetra - qive": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='8']",
        "flucelvax tetra - qivc": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='9']",
        "supemtek - qivr": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='10']",
        "fluad tetra - aqiv": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='12']",
        "cell-based quadrivalent - qivc": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='13']",
        "adjuvanted quadrivalent - aqiv": "//input[@class='nhsuk-radios__input' and @name='ConsentVaccineId' and @value='14']"                     
    }    
    element = xpath_map.get(vaccinetype.lower())
    if element:
        find_element_and_perform_action(element, "click")
    else:
        print("Invalid vaccine type")


def check_back_button_exists():
    check_element_exists(BACK_ELEMENT, True)    

def check_covid_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)    
    
def click_flu_radiobutton():
    find_element_and_perform_action(FLU_RADIOBUTTON, "click")    

def check_flu_radiobutton_exists():
    return check_element_exists(COVID_RADIOBUTTON, True)      

def click_save_and_return_button_on_choose_vaccines_screen():
    find_element_and_perform_action(SAVE_AND_RETURN_BUTTON, "click")        

def click_continue_to_assess_patient_button():
    find_element_and_perform_action(CONTINUE_BUTTON, "click")            