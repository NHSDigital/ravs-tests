import fs from 'fs';
import path from 'path';
import os from 'os';
import { devices, BrowserContext, Page, chromium, webkit, firefox, Browser} from 'playwright';
import { DatetimeHelper } from './helpers/datetimeHelper';
import { BasePlaywrightHelper } from './helpers/playwrightHelper';
import * as allure from 'allure-js-commons';
import { Locator } from 'playwright';
import test from 'playwright/test';
import { After, Before, BeforeAll, AfterAll } from '@cucumber/cucumber';

const config = loadConfigFromEnv();
const workingDirectory = getWorkingDirectory();

let playwrightHelperInstance: BasePlaywrightHelper;
let datetimeHelperInstance: DatetimeHelper;
let globalPage: Page;

export async function initializeHelpers() {
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();
  if (!playwrightHelperInstance) {
    playwrightHelperInstance = new BasePlaywrightHelper(config, workingDirectory);
    await playwrightHelperInstance.launchBrowser('chromium', false);
  }

  if (!datetimeHelperInstance) {
    datetimeHelperInstance = new DatetimeHelper();
  }

  await playwrightHelperInstance.launchBrowser('chromium', false);  // Example

  return { browser, page };

}

BeforeAll(async function () {
  const { page } = await initializeHelpers();
  globalPage = page;
});

AfterAll(async function () {
  if (playwrightHelperInstance) {
    await playwrightHelperInstance.quitBrowser();
  }
});

export function generateRandomString(length: number = 10): string {
  const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
  let randomString = '';
  for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      randomString += characters[randomIndex];
  }
  return randomString;
}

export function loadConfigFromEnv(): Record<string, any> {
  return {
    test_environment: process.env.TEST_ENVIRONMENT || 'dev',
    headless_mode: process.env.HEADLESS_MODE || '',
    browser: process.env.BROWSER || 'chrome',
    device: process.env.DEVICE || 'iphone_12',
    timeout_seconds: parseInt(process.env.TIMEOUT_SECONDS || '1', 10),
    credentials: {
      ravs_password: process.env.RAVS_PASSWORD || '',
    },
  };
}

export function getWorkingDirectory(): string {
  const cwd = process.cwd();
  if (cwd.includes('api')) return path.resolve(cwd, '../../source/');
  if (cwd.includes('source')) return cwd;
  return cwd;
}

export function sanitizeFilename(filename: string): string {
  let sanitized = filename.replace(/[<>:"/\\|?*]/g, '_');
  sanitized = sanitized.trim().replace(/^\.+|\.+$/g, '');
  return sanitized.slice(0, 200);
}

export async function attachScreenshot(filename: string): Promise<void> {
  const workingDir = getWorkingDirectory();
  const browser = config.browser;
  const version = playwrightHelperInstance?.getBrowserVersion() || 'unknown';

  console.log("Working Dir:", workingDir);
  console.log("Browser:", browser);
  console.log("Version:", version);
  console.log("Filename:", filename);

  const baseDir = path.normalize(workingDir);

  const fullFilename = sanitizeFilename(
    browser === 'mobile'
      ? `${config.test_environment}_${browser}_${config.device}_${version}_${filename}.png`
      : `${config.test_environment}_${browser}_${version}_${filename}.png`
  );

  const dir = path.join('data', 'attachments', fullFilename);
  const fullPath = path.join(dir, fullFilename);

  try {
    if (!fs.existsSync(dir)) {
      console.log(`Directory does not exist. Creating: ${dir}`);
      fs.mkdirSync(dir, { recursive: true });
    }
    const screenshot = await playwrightHelperInstance?.captureScreenshot(fullPath);
    if (screenshot && fs.existsSync(fullPath)) {
      allure.attachment(fullFilename, fs.readFileSync(fullPath), 'image/png');
    }
  } catch (e) {
    console.error(`Failed to capture screenshot: ${e}`);
  }
}

export function getAppUrl(testEnvironment: string): string {
  if (testEnvironment.toLowerCase().includes('dev')) {
    return 'https://www.ravs-dev.england.nhs.uk';
  } else if (testEnvironment.toLowerCase().includes('qa')) {
    return 'https://www.ravs-qa.england.nhs.uk';
  }
  throw new Error(`Unknown test environment: ${testEnvironment}`);
}

// export function afterAll(): void {
//   const env = process.env.TEST_ENVIRONMENT || 'qa';
//   const product = 'RAVS';
//   const properties = { PRODUCT: product, ENV: env };
//   const filePath = path.join(getWorkingDirectory(), 'allure-results', 'environment.properties');
//   writePropertiesFile(filePath, properties);
// }

function writePropertiesFile(filePath: string, properties: Record<string, string>): void {
  try {
    fs.mkdirSync(path.dirname(filePath), { recursive: true });
    if (fs.existsSync(filePath)) fs.unlinkSync(filePath);
    const content = Object.entries(properties)
      .map(([key, value]) => `${key}=${value}`)
      .join('\n');
    fs.writeFileSync(filePath, content);
  } catch (e) {
    console.error(`Error writing properties file: ${e}`);
  }
}

export function quitBrowser(): void {
  playwrightHelperInstance?.quitBrowser();
}

export function getCurrentUrl(): string | undefined {
  return playwrightHelperInstance?.getCurrentUrl();
}

export function addCookie(url: string, cookie: string, value: string): void {
  playwrightHelperInstance?.addCookie(url, cookie, value);
}

export async function getBrowserVersion(): Promise<string> {
  const version = await playwrightHelperInstance?.getBrowserVersion();
  return version || 'unknown';
}

export function findElements(selector: string): any {
  return playwrightHelperInstance?.findElements(selector);
}

export function waitForPageToLoad(timeout: number = 3): void {
  playwrightHelperInstance?.waitForPageToLoad(timeout);
}

export async function checkElementExists(element: any, wait: boolean = false): Promise<boolean> {
  return await playwrightHelperInstance?.checkElementExists(element) ?? false;
}

export async function getCheckedRadioButtonText(name: string): Promise<string | undefined> {
  return await playwrightHelperInstance?.getCheckedRadioButtonText(name);
}

export async function checkElementEnabled(element: any): Promise<boolean> {
  return await playwrightHelperInstance?.checkElementEnabled(element) ?? false;
}

export async function checkElementChecked(element: any): Promise<boolean> {
  return await playwrightHelperInstance?.checkElementChecked(element) ?? false;
}

export function scrollIntoView(element: any): void {
  playwrightHelperInstance?.scrollIntoView(element);
}

export function waitForElementToAppear(element: any): void {
  playwrightHelperInstance?.waitForElementToAppear(element);
}

export function waitForElementToDisappear(element: any): void {
  playwrightHelperInstance?.waitForElementToDisappear(element);
}

export function captureScreenshot(filename: string): void {
  playwrightHelperInstance?.captureScreenshot(filename);
}

export function handleUnresponsivePage(): void {
  playwrightHelperInstance?.handleUnresponsivePage();
}

export async function clickAndGetDownloadPath(
  elementDefinition: { type: string; value: string; name?: string; exact?: boolean },
  action: string = 'click',
  timeout: number = 30_000,
  downloadDir: string = 'downloads'
): Promise<string> {
  if (!playwrightHelperInstance) {
    throw new Error("❌ Playwright helper instance is not initialized.");
  }

  try {
    const downloadPath = await playwrightHelperInstance.clickAndGetDownloadPath(
      elementDefinition,
      action,
      timeout,
      downloadDir
    );
    return downloadPath;
  } catch (error) {
    console.error("❌ Error in clickAndGetDownloadPath:", error);
    throw error;
  }
}

export async function findElementAndPerformAction(
  elementDefinition: { type: string; value: string; name?: string; exact?: boolean },
  action: string,
  inputValue?: any
): Promise<void>  {
  if (!playwrightHelperInstance) {
    console.error("❌ Playwright helper instance is not initialized.");
    return;
  }

  try {
    const locator = playwrightHelperInstance.getElementByType(
      elementDefinition.type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
      elementDefinition.value,
      elementDefinition.name,
      elementDefinition.exact ?? false
    );

    playwrightHelperInstance.findElementAndPerformAction(elementDefinition, action, inputValue);
  } catch (error) {
    console.error(`❌ Failed to perform action '${action}' on element:`, elementDefinition, error);
  }
}

export function mockApiResponse(): void {
  const workingDirectory = getWorkingDirectory();
  playwrightHelperInstance?.mockApiResponse(workingDirectory);
}

export function waitUntilPageLoadingMessageDisappears(): void {
  const PAGE_LOADING_ELEMENT = ['role', 'status'];
  waitForElementToDisappear(PAGE_LOADING_ELEMENT);
}

export function waitUntilSpinnerDisappears(): void {
  const SPINNER_ELEMENT = ['role', 'status'];
  waitForElementToDisappear(SPINNER_ELEMENT);
}

export function clickCellInRow(rowName: string, cellIndex: number): void {
  playwrightHelperInstance?.clickCellInRow(rowName, cellIndex);
}

export function javascriptClick(element: any): void {
  waitUntilSpinnerDisappears();
  playwrightHelperInstance?.javascriptClick(element);
}

export function clickLinkInRow(rowName: string, linkIndex: number): void {
  playwrightHelperInstance?.clickLinkInRow(rowName, linkIndex);
}

export function getElementByType(
  locatorType: 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
  locatorValue?: string,
  name?: string,
  exact: boolean = false
): Locator | undefined {
  if (!playwrightHelperInstance) {
    console.error('Playwright helper instance is not initialized.');
    return undefined;
  }

  try {
    return playwrightHelperInstance.getElementByType(locatorType, locatorValue, name, exact);
  } catch (error) {
    console.error("Error getting element by type: ${error}");
    return undefined;
  }
}

export function releaseMouse(): void {
  playwrightHelperInstance?.releaseMouse();
}

export function formatDate(date: string, browser: string): string | undefined {
  return datetimeHelperInstance?.formatDate(date, browser);
}

export function standardizeDateFormat(date: string): string | undefined {
  return datetimeHelperInstance?.standardizeDateFormat(date);
}

export function dateFormatWithDayOfWeek(date: string): string | undefined {
  return datetimeHelperInstance?.dateFormatWithDayOfWeek(date);
}

export function dateFormatWithAge(date: string): string | undefined {
  return datetimeHelperInstance?.dateFormatWithAge(date);
}

export function dateFormatWithNameOfMonth(date: string): string | undefined {
  return datetimeHelperInstance?.dateFormatWithNameOfMonth(date);
}

export function dateFormatWithNameOfMonthShortened(date: string): string | undefined {
  return datetimeHelperInstance?.dateFormatWithNameOfMonthShortened(date);
}

export function getDateValueByMonths(date: string | Date): string | undefined {
  const dateStr = typeof date === 'string' ? date : date.toISOString();
  return datetimeHelperInstance?.getDateValueByMonths(dateStr)?.toString();
}

export function getDateValueByDays(date: string | Date): string | undefined {
  const dateStr = typeof date === 'string' ? date : date.toISOString();
  return datetimeHelperInstance?.getDateValueByDays(dateStr)?.toString();
}

export { playwrightHelperInstance, datetimeHelperInstance };
