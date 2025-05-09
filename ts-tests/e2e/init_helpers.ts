import fs from 'fs';
import path from 'path';
import { DatetimeHelper } from './helpers/datetimeHelper';
import { BasePlaywrightHelper, SupportedBrowser } from './helpers/playwrightHelper';
import * as allure from 'allure-js-commons';
import { After, Before, BeforeAll, AfterAll } from '@cucumber/cucumber';
import dotenv from 'dotenv';

if (!process.env.CI) {
  const envFile = `../../.env`;
  dotenv.config({ path: path.resolve(__dirname, envFile) });
  console.log(`🔧 Loaded environment from ${envFile}`);
} else {
  console.log("🔧 Using CI environment variables");
}

const config = loadConfigFromEnv();
const workingDirectory = getWorkingDirectory();

let playwrightHelperInstance: BasePlaywrightHelper;
let datetimeHelperInstance: DatetimeHelper;

export async function initializeHelpers() {
  if (!playwrightHelperInstance) {
    playwrightHelperInstance = new BasePlaywrightHelper(config, workingDirectory);
    const browserType = process.env.BROWSER as SupportedBrowser || SupportedBrowser.EDGE;
    const headless = process.env.HEADLESS_MODE === 'true';
    console.log(`🌐 Launching main browser instance with browser type: ${browserType} and headless mode: ${headless ? 'enabled' : 'disabled'}`);
    await playwrightHelperInstance.launchBrowser(browserType, headless);
  }

  if (!datetimeHelperInstance) {
    datetimeHelperInstance = new DatetimeHelper();
  }
    const browser = playwrightHelperInstance.getBrowser();
    const page = playwrightHelperInstance.getPage()

    console.log("✅ Helpers initialized successfully.");
    return { browser, page };
}

BeforeAll(async function () {
  const { browser } = await initializeHelpers();
  console.log("✅ Browser and context initialized.");
});

AfterAll(async function () {
  if (playwrightHelperInstance) {
    await playwrightHelperInstance.quitBrowser();
  }
    const env = process.env.TEST_ENVIRONMENT || 'qa';
    const product = 'RAVS';
    const propertiesDict = { PRODUCT: product, ENV: env };

    const workingDir = getWorkingDirectory();
    const filePath = path.join(workingDir, 'allure-results', 'environment.properties');

    try {
      fs.mkdirSync(path.dirname(filePath), { recursive: true });
      const data = Object.entries(propertiesDict).map(([key, value]) => `${key}=${value}`).join('\n');
      fs.writeFileSync(filePath, data);
      console.log(`✅ Allure environment properties written to ${filePath}`);
    } catch (error) {
      console.error(`❌ Failed to write environment properties: ${error}`);
    }

    console.log('✅ Browser closed and environment properties written.');
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

  try {
    const version = await playwrightHelperInstance?.getBrowserVersion() || 'unknown';

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

    const dir = path.join(baseDir, 'data', 'attachments');
    const fullPath = path.join(dir, fullFilename);  

    console.log("Full Screenshot Path:", fullPath);

    if (!fs.existsSync(dir)) {
      console.log(`Directory does not exist. Creating: ${dir}`);
      fs.mkdirSync(dir, { recursive: true });
    }

    const screenshot = await playwrightHelperInstance?.captureScreenshot(fullPath);

    if (screenshot && fs.existsSync(fullPath)) {
      console.log("Screenshot saved at:", fullPath);
      allure.attachment(fullFilename, fs.readFileSync(fullPath), 'image/png');
    } else {
      console.error("Failed to capture screenshot or file not found:", fullPath);
    }

  } catch (e) {
    console.error(`Error capturing screenshot: ${e}`);
  }
}

export function getAppUrl(): string {
  const testEnvironment = process.env.TEST_ENVIRONMENT || 'dev';
  if (testEnvironment.toLowerCase().includes('dev')) {
    return 'https://www.ravs-dev.england.nhs.uk';
  } else if (testEnvironment.toLowerCase().includes('qa')) {
    return 'https://www.ravs-qa.england.nhs.uk';
  }
  throw new Error(`Unknown test environment: ${testEnvironment}`);
}

export { playwrightHelperInstance, datetimeHelperInstance };
