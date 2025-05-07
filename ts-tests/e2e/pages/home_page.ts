import { playwrightHelperInstance } from '../init_helpers';

export const FIND_A_PATIENT_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Find a patient' };
export const VACCINES_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Vaccines' };
export const REPORTS_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Reports' };
export const MANAGE_USERS_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Manage users' };
export const RECORD_VACCINATIONS_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Record vaccinations' };
export const NHS_LOGO_NAV_ELEMENT = { type: 'role', value: 'link', name: 'NHS Logo Record a vaccination' };
export const LOGOUT_NAV_ELEMENT = { type: 'role', value: 'link', name: 'Log out' };
export const NAV_BAR_TOGGLER = { type: 'xpath', value: "//button[@class='navbar-toggler']" };
export const NAV_LINK_BAR_TOGGLER = { type: 'xpath', value: "//button[@class='navbar-toggler p-2']" };
export const FEEDBACK_LINK = { type: 'role', value: 'link', name: 'feedback (opens in a new tab)' };
export const REPORT_AN_ISSUE_LINK = { type: 'role', value: 'link', name: 'Report an issue' };
export const ADD_VACCINES_LINK = { type: 'role', value: 'link', name: 'Add vaccines' };
export const ADD_USERS_LINK = { type: 'role', value: 'link', name: 'Add users' };
export const FIND_A_PATIENT_LINK = { type: 'nested_role', value: 'link', name: 'Find a patient', exact: true, parentSelector: '#maincontent' };
export const CONTACT_US_LINK = { type: 'role', value: 'link', name: 'Contact us' };
export const HELP_AND_GUIDANCE_LINK = { type: 'role', value: 'link', name: 'Help and guidance' };
export const USER_GUIDE_LINK = { type: 'role', value: 'link', name: 'User guide (opens in new tab)' };
export const TERMS_OF_USE_LINK = { type: 'role', value: 'link', name: 'Terms of use' };
export const COOKIES_LINK = { type: 'role', value: 'link', name: 'Cookies' };
export const ACCESSIBILITY_STATEMENT_LINK = { type: 'role', value: 'link', name: 'Accessibility statement' };
export const ADD_USER_BUTTON = { type: 'role', value: 'button', name: 'Add user' };
export const SEARCH_BUTTON = { type: 'role', value: 'button', name: 'Search' };
export const ADD_VACCINE_BUTTON = { type: 'role', value: 'button', name: 'Add vaccine' };
export const CREATE_REPORT_BUTTON = { type: 'role', value: 'button', name: 'Create report' };
export const PAGE_LOADING_ELEMENT = { type: 'role', value: 'status' };
export const TODAY_VACCINATION_COUNT = { type: 'id', value: 'today-vaccinations' };
export const WEEK_VACCINATION_COUNT = { type: 'id', value: 'week-vaccinations' };
export const MONTH_VACCINATION_COUNT = { type: 'id', value: 'month-vaccinations' };
export const CREATE_A_REPORT_LINK = { type: 'role', value: 'link', name: 'create a report' };
export const TOTAL_VACCINATIONS_TEXT_ELEMENT = { type: 'role', value: 'heading', name: 'Total vaccinations' };

export async function ensureLogOutNavElementExists(): Promise<void> {
    if (!(await playwrightHelperInstance!.checkElementExists(LOGOUT_NAV_ELEMENT))) {
        await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
        await playwrightHelperInstance!.waitForElementToAppear(LOGOUT_NAV_ELEMENT);
    }
}

export async function checkFeedbackLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'feedback (opens in a new tab)' });
}

export async function checkAccessibilityStatementLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Accessibility statement' });
}

export async function checkTermsOfUseLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Terms of use' });
}

export async function checkUserGuideLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'User guide (opens in new tab)' });
}

export async function clickAccessibilityStatementLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Accessibility statement' }, 'click');
}

export async function clickUserGuideLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'User guide (opens in new tab)' }, 'click');
}

export async function clickTermsOfUseLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Terms of use' }, 'click');
}

export async function checkAddVaccinesLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Add vaccines' });
}

export async function checkAddUsersLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Add users' });
}

export async function checkFindAPatientLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'nested_role', value: 'link', name: 'Find a patient', parent: '#maincontent' });
}

export async function clickAddVaccinesLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Add vaccines' }, 'click');
}

export async function clickAddUsersLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Add users' }, 'click');
}

export async function clickFindAPatientLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'nested_role', value: 'link', name: 'Find a patient', parent: '#maincontent' }, 'click');
}

export async function checkSiteNameExistsInDashboard(site: string): Promise<boolean> {
    await ensureLogOutNavElementExists();
    const element = { type: 'role', value: 'heading', name: site };
    return await playwrightHelperInstance!.checkElementExists(element);
}

export async function getTodayVaccinationsCount(): Promise<string> {
    await ensureLogOutNavElementExists();
    const text = await playwrightHelperInstance!.findElementAndPerformAction(TODAY_VACCINATION_COUNT, 'get_text');
    const count = text.match(/\d+/);
    return count ? count[0] : '0';
}

export async function getWeekVaccinationsCount(): Promise<string> {
    await ensureLogOutNavElementExists();
    const text = await playwrightHelperInstance!.findElementAndPerformAction(WEEK_VACCINATION_COUNT, 'get_text');
    const count = text.match(/\d+/);
    return count ? count[0] : '0';
}

export async function getMonthVaccinationsCount(): Promise<string> {
    await ensureLogOutNavElementExists();
    const text = await playwrightHelperInstance!.findElementAndPerformAction(MONTH_VACCINATION_COUNT, 'get_text');
    const count = text.match(/\d+/);
    return count ? count[0] : '0';
}

export async function checkCreateAReportLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists(CREATE_A_REPORT_LINK);
}

export async function clickFeedbackLinkExists(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'feedback (opens in a new tab)' });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'feedback (opens in a new tab)' }, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function checkReportAnIssueLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Report an issue' });
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Report an issue' });
}

export async function clickReportAnIssueLinkExists(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Report an issue' });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Report an issue' }, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function checkContactUsLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Contact us' });
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Contact us' });
}

export async function clickContactUsLinkExists(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Contact us' });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Contact us' }, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function checkHelpAndGuidanceLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Help and guidance' });
    return await playwrightHelperInstance!.checkElementExists({ type: 'role', value: 'link', name: 'Help and guidance' });
}

export async function clickHelpAndGuidanceLinkExists(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'link', name: 'Help and guidance' });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'role', value: 'link', name: 'Help and guidance' }, 'click');
}

export async function clickLogoutButton(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.findElementAndPerformAction(LOGOUT_NAV_ELEMENT, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function clickNavbarToggler(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'xpath', value: "//button[@class='navbar-toggler']" });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'xpath', value: "//button[@class='navbar-toggler']" }, 'click');
}

export async function clickNavLinkBarToggler(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'xpath', value: "//button[@class='navbar-toggler p-2']" });
    await playwrightHelperInstance!.findElementAndPerformAction({ type: 'xpath', value: "//button[@class='navbar-toggler p-2']" }, 'click');
}

export async function checkLogoutButtonExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists(LOGOUT_NAV_ELEMENT);
}

export async function checkNavbarToggleExistsWithoutWaiting(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'xpath', value: "//button[@class='navbar-toggler']" });
}

export async function checkNavbarToggleExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'xpath', value: "//button[@class='navbar-toggler']" });
    return await playwrightHelperInstance!.checkElementExists({ type: 'xpath', value: "//button[@class='navbar-toggler']" });
}

export async function checkNavLinkBarToggleExistsWithoutWaiting(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists({ type: 'xpath', value: "//button[@class='navbar-toggler p-2']" });
}

export async function checkNavLinkBarToggleExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'xpath', value: "//button[@class='navbar-toggler p-2']" });
    return await playwrightHelperInstance!.checkElementExists({ type: 'xpath', value: "//button[@class='navbar-toggler p-2']" });
}

export async function checkLogoutButtonExistsWithoutWaiting(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    return await playwrightHelperInstance!.checkElementExists(LOGOUT_NAV_ELEMENT);
}

export async function clickProfileNavLink(email: string): Promise<void> {
    await ensureLogOutNavElementExists();
    const element = { type: 'role', value: 'link', name: email };
    await playwrightHelperInstance!.waitForElementToAppear(element);
    await playwrightHelperInstance!.findElementAndPerformAction(element, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function checkReportsNavLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(FIND_A_PATIENT_NAV_ELEMENT);
    return await playwrightHelperInstance!.checkElementExists(REPORTS_NAV_ELEMENT);
}

export async function clickReportsNavLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(REPORTS_NAV_ELEMENT);
    await playwrightHelperInstance!.findElementAndPerformAction(REPORTS_NAV_ELEMENT, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'button', name: 'Create report' });
}

export async function checkVaccinesNavLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(FIND_A_PATIENT_NAV_ELEMENT);
    return await playwrightHelperInstance!.checkElementExists(VACCINES_NAV_ELEMENT);
}

export async function clickVaccinesNavLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(VACCINES_NAV_ELEMENT);
    await playwrightHelperInstance!.findElementAndPerformAction(VACCINES_NAV_ELEMENT, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'button', name: 'Add vaccine' });
}

export async function checkManageUsersNavLinkExists(): Promise<boolean> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(FIND_A_PATIENT_NAV_ELEMENT);
    return await playwrightHelperInstance!.checkElementExists(MANAGE_USERS_NAV_ELEMENT);
}

export async function clickManageUsersNavLink(): Promise<void> {
    await ensureLogOutNavElementExists();
    await playwrightHelperInstance!.waitForElementToAppear(MANAGE_USERS_NAV_ELEMENT);
    await playwrightHelperInstance!.findElementAndPerformAction(MANAGE_USERS_NAV_ELEMENT, 'click');
    await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
    await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'button', name: 'Add user' });
}

export async function clickRecordVaccinationsNavLink(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.waitForElementToAppear(RECORD_VACCINATIONS_NAV_ELEMENT);
  await playwrightHelperInstance!.findElementAndPerformAction(RECORD_VACCINATIONS_NAV_ELEMENT, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
  await playwrightHelperInstance!.waitForElementToAppear({ type: 'role', value: 'button', name: 'Record vaccination' });
}

export async function checkNhsLogoNavElementExists(): Promise<boolean> {
  await ensureLogOutNavElementExists();
  return await playwrightHelperInstance!.checkElementExists(NHS_LOGO_NAV_ELEMENT);
}

export async function clickNhsLogoNavElement(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(NHS_LOGO_NAV_ELEMENT, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function getTotalVaccinationsHeadingText(): Promise<string> {
  await ensureLogOutNavElementExists();
  const text = await playwrightHelperInstance!.findElementAndPerformAction(TOTAL_VACCINATIONS_TEXT_ELEMENT, 'get_text');
  return text || '';
}

export async function getTodayVaccinationCountText(): Promise<string> {
  await ensureLogOutNavElementExists();
  const text = await playwrightHelperInstance!.findElementAndPerformAction(TODAY_VACCINATION_COUNT, 'get_text');
  return text || '';
}

export async function getWeekVaccinationCountText(): Promise<string> {
  await ensureLogOutNavElementExists();
  const text = await playwrightHelperInstance!.findElementAndPerformAction(WEEK_VACCINATION_COUNT, 'get_text');
  return text || '';
}

export async function getMonthVaccinationCountText(): Promise<string> {
  await ensureLogOutNavElementExists();
  const text = await playwrightHelperInstance!.findElementAndPerformAction(MONTH_VACCINATION_COUNT, 'get_text');
  return text || '';
}

export async function navigateToFeedbackPage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(FEEDBACK_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function navigateToContactUsPage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(CONTACT_US_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function navigateToHelpAndGuidancePage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(HELP_AND_GUIDANCE_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function navigateToAccessibilityStatementPage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(ACCESSIBILITY_STATEMENT_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function navigateToUserGuidePage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(USER_GUIDE_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function navigateToTermsOfUsePage(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(TERMS_OF_USE_LINK, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function logoutFromApp(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(LOGOUT_NAV_ELEMENT, 'click');
  await playwrightHelperInstance!.waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export async function toggleNavbar(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(NAV_BAR_TOGGLER, 'click');
}

export async function toggleNavLinkBar(): Promise<void> {
  await ensureLogOutNavElementExists();
  await playwrightHelperInstance!.findElementAndPerformAction(NAV_LINK_BAR_TOGGLER, 'click');
}

export async function checkLogoutButtonExistsOnProfilePage(): Promise<boolean> {
  await ensureLogOutNavElementExists();
  return await playwrightHelperInstance!.checkElementExists(LOGOUT_NAV_ELEMENT);
}

