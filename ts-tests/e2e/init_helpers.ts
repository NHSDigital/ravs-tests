import { Before, After, BeforeAll, AfterAll, setDefaultTimeout } from '@cucumber/cucumber';
import fs from 'fs';
import path from 'path';
import { BasePlaywrightHelper, SupportedBrowser } from './helpers/playwrightHelper';
import { DatetimeHelper } from './helpers/datetimeHelper';
import dotenv from 'dotenv';

if (!process.env.CI) {
  const envFile = `../../.env`;
  dotenv.config({ path: path.resolve(__dirname, envFile) });
  console.log(`🔧 Loaded environment from ${envFile}`);
} else {
  const timeout = process.env.PWDEBUG ? -1 : 60 * 1000;
  setDefaultTimeout(timeout);
  console.log(`🌐 Timeout for CI set to ${timeout / 1000} seconds.`);
  console.log("🔧 Using CI environment variables");
}

declare global {
  var browser: any;
  var page: any;
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
  const page = playwrightHelperInstance.getPage();

  if (!browser || !page) {
    throw new Error("Failed to retrieve browser or page instance.");
  }

  global.browser = browser;
  global.page = page;

  console.log("✅ Helpers initialized successfully.");
  return { browser, page };
}

Before(async function () {
  console.log("🚀 Initializing helpers...");

  const { browser, page } = await initializeHelpers();
  global.browser = browser;
  global.page = page;

  console.log("✅ Helpers initialized and directories prepared.");
});

Before({ tags: '@ignore' }, function () {
  console.log("🚫 Skipping ignored test...");
  return 'skipped';
});

Before({ tags: '@debug' }, function () {
  this.debug = true;
  console.log("🐛 Debug mode enabled for this scenario.");
});

After(async function () {
    if (global.page && typeof global.page.close === 'function') {
      await global.page.close();
    }

    if (this.context) {
      await this.context.close();
    }
  console.log("✅ Scenario cleanup complete.");
});

AfterAll(async function () {
  console.log("🛑 Shutting down browser...");

  try {
    if (global.browser) {
      await global.browser.close();
      global.browser = null;
      global.page = null;
      console.log("✅ Browser closed successfully.");
    }
  } catch (error) {
    console.error(`❌ Error during browser shutdown: ${error}`);
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
      // allure.attachment(fullFilename, fs.readFileSync(fullPath), 'image/png');
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
