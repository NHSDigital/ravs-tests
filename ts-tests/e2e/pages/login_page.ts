import { playwrightHelperInstance } from '../init_helpers';

const LOGIN_BUTTON_ELEMENT = { type: 'role', value: 'button', name: 'Log in' };
const YOU_ARE_NOT_LOGGED_IN_LABEL_ELEMENT = { type: 'text', value: 'You are not logged in.' };
const ACCEPT_COOKIES_ELEMENT = { type: 'role', value: 'button', name: "I'm OK with analytics cookies" };
const PAGE_LOADING_ELEMENT = { type: 'role', value: 'status' };
const LOGOUT_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Log out' };

export async function ensureYouAreNotLoggedInLabelExists(): Promise<void> {
    await playwrightHelperInstance!.checkElementExists(YOU_ARE_NOT_LOGGED_IN_LABEL_ELEMENT);
}

export async function navigateToRavsLoginPage(url: string): Promise<void> {
    await playwrightHelperInstance!.navigateToUrl(url);
    await ensureYouAreNotLoggedInLabelExists();

    // const acceptCookiesExists = await playwrightHelperInstance!.checkElementExists(ACCEPT_COOKIES_ELEMENT);
    // if (acceptCookiesExists) {
    //     await playwrightHelperInstance!.findElementAndPerformAction(ACCEPT_COOKIES_ELEMENT, 'click');
    // }
}

export async function checkLoginButtonExists(): Promise<boolean> {
    await ensureYouAreNotLoggedInLabelExists();
    return await playwrightHelperInstance!.checkElementExists(LOGIN_BUTTON_ELEMENT);
}

export async function clickLoginButton(): Promise<void> {
    await ensureYouAreNotLoggedInLabelExists();
    await playwrightHelperInstance!.findElementAndPerformAction(LOGIN_BUTTON_ELEMENT, 'click');
}
