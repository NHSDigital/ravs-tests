import { Given, When, Then } from '@cucumber/cucumber';
import * as InitHelpers from '../init_helpers';
import { navigateToRavsLoginPage, checkLoginButtonExists, clickLoginButton } from '../pages/login_page';
import * as nhsSigninPage from '../pages/nhs_signin_page';
import * as homePage from '../pages/home_page'
import assert from 'assert';

interface SharedData {
  emailAddress?: string;
  password?: string;
}

const sharedData: SharedData = {};
const config = InitHelpers.loadConfigFromEnv();
console.log('Loaded Config: ', config);
const appUrl = InitHelpers.getAppUrl(config.test_environment);
console.log('appUrl: ', appUrl);

Given('I access the ravs web app', async function () {
  if (!appUrl) {
    throw new Error('appUrl is undefined or invalid');
  }
    await navigateToRavsLoginPage(appUrl);
});

Then('the login button should be visible', async function () {
    await InitHelpers.attachScreenshot('login_should_be_visible');
    const loginButtonExists = await checkLoginButtonExists();
    assert(loginButtonExists, 'Login button is not visible');
});

Then('the NHS sign in page should be visible', async function () {
    await InitHelpers.attachScreenshot('nhs_sign_in_button_should_be_visible');
    const signinButtonExists = await nhsSigninPage.checkSigninButtonExists();
    assert(signinButtonExists, 'NHS signin button is not visible');
});

// 🥒 When Steps
When('I click on the log in button', async function () {
    await clickLoginButton();
    await InitHelpers.attachScreenshot('clicked_login_button');
});

When(/^I provide the (.+) and (.+)$/, async function (emailAddress: string, password: string) {
    if (emailAddress === 'None') {
        await nhsSigninPage.clearEmailAddress();
        await nhsSigninPage.clearPassword();
        await nhsSigninPage.enterPassword(password);
    } else if (password === 'None') {
        await nhsSigninPage.clearPassword();
        await nhsSigninPage.clearEmailAddress();
        await nhsSigninPage.enterEmailAddress(emailAddress);
    } else if (emailAddress.includes('long_email_address')) {
        emailAddress = InitHelpers.generateRandomString(65) + '@nhs.net';
        await nhsSigninPage.enterEmailAddress(emailAddress);
        await nhsSigninPage.enterPassword(password);
    } else if (password.includes('long_password')) {
        password = InitHelpers.generateRandomString(65);
        await nhsSigninPage.enterEmailAddress(emailAddress);
        await nhsSigninPage.enterPassword(password);
    } else if (emailAddress.toLowerCase().includes('valid') && !emailAddress.toLowerCase().includes('invalid')) {
        emailAddress = emailAddress.replace('-valid', '').trim();
        const validPassword = config.credentials.ravs_password;
        if (!validPassword) throw new Error("Please provide RAVs password as environment variable");
        await nhsSigninPage.enterEmailAddress(emailAddress);
        await nhsSigninPage.enterPassword(validPassword);
    } else {
        await nhsSigninPage.enterEmailAddress(emailAddress);
        await nhsSigninPage.enterPassword(password);
    }

    await InitHelpers.attachScreenshot('entered_emailAddress_and_password');
    sharedData.emailAddress = emailAddress;
    sharedData.password = password;
});

When('the NHS sign in button is clicked', async function () {
    await nhsSigninPage.clickNhsSigninButton();
    await InitHelpers.attachScreenshot('clicked_nhs_signin_button');
});

Then(/^sign in should (.+)$/, async function (status: string) {
    await InitHelpers.attachScreenshot('sign_in_should_' + status.toLowerCase());

    if (status.toLowerCase() === 'fail') {
        if (sharedData.password === 'None' && !sharedData.emailAddress?.toLowerCase().includes('valid')) {
            await InitHelpers.attachScreenshot('check_password_error_alert_exists');
            assert(await nhsSigninPage.checkPasswordErrorAlertExists(), 'Password error alert not found');
            assert.strictEqual(await nhsSigninPage.getPasswordMissingErrorText(), 'This field cannot be left blank');
        } else if (sharedData.emailAddress === 'None' && !sharedData.emailAddress?.toLowerCase().includes('valid')) {
            await nhsSigninPage.clickNhsSigninButton();
            await InitHelpers.attachScreenshot('clicked_nhs_signin_button_and_check_error_alerts_exist');
            assert(await nhsSigninPage.checkEmailAddressErrorAlertExists(), 'Email address error alert not found');
            assert(await nhsSigninPage.checkFoundSomeErrorsAlertExists(), 'General error alert not found');
            assert.strictEqual(await nhsSigninPage.getEmailAddressMissingErrorText(), 'This field cannot be left blank');
        } else if (sharedData.emailAddress?.includes('long_email_address')) {
            await InitHelpers.attachScreenshot('check_emailAddress_error_alert_exists');
            assert(await nhsSigninPage.checkEmailAddressErrorAlertExists(), 'Email address error alert not found');
            assert.strictEqual(await nhsSigninPage.getEmailAddressMissingErrorText(), 'This field cannot be left blank');
        } else if (sharedData.emailAddress?.includes('valid') && status.toLowerCase() === 'pass') {
            await InitHelpers.attachScreenshot('logout_button_should_exist');
            assert(await homePage.checkLogoutButtonExists(), 'Logout button not found');
            await homePage.clickLogoutButton();
            await InitHelpers.attachScreenshot('clicked_logout_button');
        } else {
            await InitHelpers.attachScreenshot('check_unable_to_sign_in_error_exists');
            assert(await nhsSigninPage.checkUnableToSignInErrorExists(), 'Unable to sign in error not found');
        }
    }
});
