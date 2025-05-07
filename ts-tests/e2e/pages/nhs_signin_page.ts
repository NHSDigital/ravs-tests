import { playwrightHelperInstance } from '../init_helpers';

const SIGN_IN_BUTTON_ELEMENT = { type: 'role', value: 'button', name: 'Sign in' };
const KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT = { type: 'text', value: 'Keep me signed in' };
const EMAIL_INPUT_ELEMENT = { type: 'label', value: 'Email' };
const PASSWORD_INPUT_ELEMENT = { type: 'label', value: 'Password' };
const ALERT_TEXT_EMAILADDRESS = { type: 'xpath', value: "//p[contains(@id, 'input-container-error')]" };
const ALERT_TEXT_PASSWORD = { type: 'xpath', value: "//p[contains(@id, 'input-container-error')]" };
const ERROR_UNABLE_TO_SIGN_IN = { type: 'text', value: 'Unable to sign in' };
const FOUND_SOME_ERRORS = { type: 'text', value: 'We found some errors. Please review the form and make corrections.' };
const LOGOUT_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Log out' };
const PAGE_LOADING_ELEMENT = { type: 'role', value: 'status' };
const NHS_SIGN_IN_HEADING_ELEMENT = { type: 'role', value: 'heading', name: 'NHS Sign In' };

export async function ensureSignInHeadingElementExists(): Promise<void> {
    if (!(await playwrightHelperInstance!.checkElementExists(NHS_SIGN_IN_HEADING_ELEMENT))) {
        await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
        await playwrightHelperInstance!.waitForElementToAppear(NHS_SIGN_IN_HEADING_ELEMENT);
    }
}

export async function navigateToNhsSigninPage(url: string): Promise<void> {
    await playwrightHelperInstance!.navigateToUrl(url);
}

export async function checkSigninButtonExists(): Promise<boolean> {
    await ensureSignInHeadingElementExists();
    return await playwrightHelperInstance!.checkElementExists(SIGN_IN_BUTTON_ELEMENT);
}

export async function clickNhsSigninButton(): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(SIGN_IN_BUTTON_ELEMENT, 'click');
}

export async function enterEmailAddress(emailAddress: string): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(EMAIL_INPUT_ELEMENT, 'input_text', emailAddress);
}

export async function clearEmailAddress(): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(EMAIL_INPUT_ELEMENT, 'clear');
}

export async function clearPassword(): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(PASSWORD_INPUT_ELEMENT, 'clear');
}

export async function enterPassword(password: string): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(PASSWORD_INPUT_ELEMENT, 'input_text', password);
}

export async function clickKeepMeSignedIn(): Promise<void> {
    await ensureSignInHeadingElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT, 'click');
}

export async function checkPasswordErrorAlertExists(): Promise<boolean> {
    await playwrightHelperInstance!.waitForElementToAppear(KEEP_ME_SIGNED_IN_CHECKBOX_ELEMENT);
    await playwrightHelperInstance!.waitForElementToAppear(ALERT_TEXT_PASSWORD);
    return await playwrightHelperInstance!.checkElementExists(ALERT_TEXT_PASSWORD);
}

export async function checkEmailAddressErrorAlertExists(): Promise<boolean> {
    await playwrightHelperInstance!.waitForElementToAppear(ALERT_TEXT_EMAILADDRESS);
    return await playwrightHelperInstance!.checkElementExists(ALERT_TEXT_EMAILADDRESS);
}

export async function checkFoundSomeErrorsAlertExists(): Promise<boolean> {
    await playwrightHelperInstance!.waitForElementToAppear(FOUND_SOME_ERRORS);
    return await playwrightHelperInstance!.checkElementExists(FOUND_SOME_ERRORS);
}

export async function getPasswordMissingErrorText(): Promise<string | null> {
    await playwrightHelperInstance!.waitForElementToAppear(ALERT_TEXT_PASSWORD);
    return await playwrightHelperInstance!.findElementAndPerformAction(ALERT_TEXT_PASSWORD, 'get_text') as string;
}

export async function getEmailAddressMissingErrorText(): Promise<string | null> {
    await playwrightHelperInstance!.waitForElementToAppear(ALERT_TEXT_EMAILADDRESS);
    return await playwrightHelperInstance!.findElementAndPerformAction(ALERT_TEXT_EMAILADDRESS, 'get_text') as string;
}

export async function checkUnableToSignInErrorExists(): Promise<boolean> {
    await playwrightHelperInstance!.waitForElementToAppear(ERROR_UNABLE_TO_SIGN_IN);
    return await playwrightHelperInstance!.checkElementExists(ERROR_UNABLE_TO_SIGN_IN);
}
