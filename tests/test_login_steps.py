from asyncio import sleep
import secrets
import string
from pytest_bdd import given, when, then, scenarios, scenario
from pytest_bdd.parsers import parse, cfparse
from pages.login_page import *
from pages.home_page import *
from pages.nhs_signin_page import *
import logging
from init_helpers import *
from conftest import *

features_directory = get_working_directory() + "features"

scenarios(f'{features_directory}/login.feature')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_random_string(length=10):
    characters = string.ascii_lowercase + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

@pytest.fixture(scope='function')
def shared_data():
    return {}

@pytest.mark.login
@given("I access the ravs web app")
def given_I_access_the_ravs_web_app(navigate_to_ravs):
    pass

@then("the login button should be visible")
def then_the_login_button_should_be_visible():
    attach_screenshot("login_should_be_visible")
    if check_login_button_exists():
        assert True, "Login button is visible"
    else:
        assert False, "Login button is not visible"

@when('I click on the log in button')
def step_click_login_button():
    click_login_button()

@then('the NHS sign in page should be visible')
def step_nhs_sign_in_page_visible():
    attach_screenshot("nhs_sign_in_button_should_be_visible")
    if check_signin_button_exists():
        assert True, "NHS signin button is visible"
    else:
        assert False, "NHS signin button is not visible"    

@when(cfparse("I provide the {emailAddress} and {password}"))
@when("I provide the <emailAddress> and <password>")
def provide_credentials(emailAddress, password, shared_data):
    if emailAddress == "None":
        clear_emailAddress()
        clear_password()
        enter_password(password)
    elif password == "None":
        clear_password()
        clear_emailAddress()
        enter_email_address(emailAddress)
    elif "long_email_address" in emailAddress:   
        emailAddress = generate_random_string(65) + "nhs.net"
        enter_email_address(emailAddress)
        enter_password(password)
    elif "long_password" in password:   
        password = generate_random_string(65)
        enter_email_address(emailAddress)
        enter_password(password)
    elif "valid" in emailAddress.lower() and "invalid" not in emailAddress.lower():
        emailAddress = emailAddress.strip("-valid")
        enter_email_address(emailAddress)
        password=config["credentials"]["ravs_password"]
        if password == "":
            assert False, "Please provide RAVs password as environment variable"
        enter_password(password)    
    else:
        enter_email_address(emailAddress)
        enter_password(password)        
    shared_data['emailAddress'] = emailAddress
    shared_data['password'] = password        

@when("the NHS sign in button is clicked")
def click_nhssignin():
    click_nhs_signin_button()

@then(parse("sign in should {status}"))
@then("sign in should <status>")
def verify_signin_status(status, shared_data):
    attach_screenshot("sign_in_should_" + status)
    data = shared_data
    if status.lower() == "fail":
        if data['password'] == "None" and "valid" not in data["emailAddress"].lower():
            assert check_password_error_alert_exists()
            assert get_password_missing_error_text() == "This field cannot be left blank"
        elif data['emailAddress'] == "None" and "valid" not in data["emailAddress"].lower():
            assert check_emailAddress_error_alert_exists() 
            assert check_found_some_errors_alert_exists()  
            assert get_emailAddress_missing_error_text() == "This field cannot be left blank"      
        elif "long_email_address" in data['emailAddress']:
            assert check_emailAddress_error_alert_exists()   
            assert get_emailAddress_missing_error_text() == "This field cannot be left blank"      
        elif "valid" in data['emailAddress'] and status.lower()=="pass":
            assert check_logout_button_exists() 
            click_logout_button()
        else:
            assert check_unable_to_sign_in_error_exists()