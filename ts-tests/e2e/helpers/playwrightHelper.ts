import {
  chromium,
  firefox,
  webkit,
  devices,
  Browser,
  BrowserContext,
  LaunchOptions,
  Route,
} from 'playwright';
import { Page, Locator } from '@playwright/test';
import * as fs from 'fs';
import * as path from 'path';
import { URL } from 'url';

export enum SupportedBrowser {
  CHROMIUM = 'chromium',
  FIREFOX = 'firefox',
  WEBKIT = 'webkit',
  EDGE = 'edge',
}

const maxRetries = 3;
const retryDelay = 1000;

export class BasePlaywrightHelper {
  private browser: Browser | null = null;
  private context: BrowserContext | null = null;
  private page: Page | null = null;
  private config: Record<string, any>;
  private workingDirectory: string;


  constructor(config: Record<string, any>, workingDirectory: string) {
    this.config = config;
    this.workingDirectory = workingDirectory;
  }

  async launchBrowser(
    browserType: SupportedBrowser,
    headless: boolean = true,
    options: LaunchOptions = {}
  ) {
    try {
      const timeout = 1000;
      switch (browserType) {
        case 'chromium':
          this.browser = await chromium.launch({ headless, timeout, ...options });
          break;
        case 'firefox':
          this.browser = await firefox.launch({ headless, timeout, ...options });
          break;
        case 'webkit':
          this.browser = await webkit.launch({ headless, timeout, ...options });
          break;
        case 'edge':
          this.browser = await chromium.launch({
            channel: 'msedge',
            headless,
            timeout,
            ...options,
          });
          break;
        default:
          throw new Error(`Unsupported browser type: ${browserType}`);
      }
      this.context = await this.browser.newContext();
      this.page = await this.context.newPage();
      return this.browser
    } catch (error) {
      console.error(`Error launching ${browserType}:`, error);
    }
  }

public async getPage(): Promise<Page> {
    if (!this.page || this.page.isClosed()) {
        if (!this.browser) {
            throw new Error('❌ Browser is not initialized. Call launchBrowser() first.');
        }

        console.log('🌐 Reinitializing context and page...');

        // Reuse existing context if available, otherwise create a new one
        if (!this.context || this.context?.pages().every(p => p.isClosed())) {
            this.context = await this.browser.newContext();
            console.log('✅ New context created.');
        }

        // Create a fresh page within the existing context
        this.page = await this.context.newPage();
        console.log('✅ Page reinitialized.');
    }

    return this.page;
}


  public getBrowser(): Browser {
    if (!this.browser) {
      throw new Error('❌ Browser is not initialized. Call launchBrowser() first.');
    }
    return this.browser;
  }

public getContext(): BrowserContext | null {
  if (!this.page) {
    throw new Error('❌ Page is not initialized. Call launchBrowser() first.');
  }
  return this.page.context();
}

  async launchMobileBrowser(deviceName: string, headless: boolean = true) {
    try {
      const device = devices[deviceName];
      if (!device) throw new Error(`Device ${deviceName} not found.`);
      this.browser = await chromium.launch({ headless });
      this.context = await this.browser.newContext({
        ...device,
        locale: 'en-GB',
      });
      this.page = await this.context.newPage();
    } catch (error) {
      console.error(`Error launching mobile browser for ${deviceName}:`, error);
    }
  }

async navigateToUrl(url: string, timeout: number = 1000): Promise<void> {
  if (!this.page || this.page.isClosed()) {
    console.error("⚠️ Page is not initialized or is closed.");
    return;
  }

  try {
    console.log(`🌐 Navigating to ${url}...`);

    // Navigate to the URL
    await this.page.goto(url, { waitUntil: 'networkidle' });

    console.log(`✅ Successfully navigated to ${url}`);
  } catch (error: any) {
    console.error(`❌ Failed to navigate to ${url} within ${timeout / 1000}s:`, error);
    if (error.name === 'TimeoutError') {
      console.error(`⚠️ Timeout while navigating to ${url}. Consider increasing the timeout.`);
    }
    throw error; // Rethrow the error to fail the test properly
  }
}

  async captureScreenshot(filename: string): Promise<string | null> {
    if (this.page) {
      const filepath = path.join(filename);
      try {
        await this.page.screenshot({ path: filepath });
        return filepath;
      } catch (error) {
        console.error('Error capturing screenshot:', error);
      }
    }
    return null;
  }

  async addCookie(url: string, name: string, value: string) {
    if (this.context) {
      const domain = new URL(url).hostname;
      await this.context.addCookies([{ name, value, domain, path: '/' }]);
    }
  }

  async getBrowserVersion(): Promise<string | null> {
    const version = this.browser?.version()
    console.log("Browser version: ", version)
    return this.browser ? this.browser.version() : null;
  }

  async closeBrowser() {
    try {
      if (this.context) {
        const tracePath = path.join(this.workingDirectory, 'trace.zip');
        try {
          await this.context.tracing.stop({ path: tracePath });
          console.log(`Trace saved to ${tracePath}`);
        } catch (traceError) {
          console.error(`An error occurred while stopping tracing: ${traceError}`);
        }

        await this.context.close();
      }

      if (this.browser) {
        await this.browser.close();
      }

      console.log('Browser closed successfully.');
    } catch (error) {
      console.error(`An error occurred while closing the browser: ${error}`);
    }
  }

  async findElements(selector: string) {
    return this.page ? await this.page.$$(selector) : [];
  }

  async waitForElement(selector: string, timeout = 1000) {
    if (this.page) {
      try {
        await this.page.waitForSelector(selector, { timeout });
        return await this.page.$(selector);
      } catch (error) {
        console.warn(`Element ${selector} not found within ${timeout}ms.`);
      }
    }
    return null;
  }

async checkElementExists(element: { type: string, value: string, name?: string, exact?: boolean; parent?: string }): Promise<boolean> {
    try {
        const { type, value, name, exact } = element;
        const elementLocator = this.getElementByType(type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id', value, name, exact);
        return elementLocator !== null;
    } catch (error) {
        console.error(`Error occurred while checking if element exists: ${error}`);
        return false; // Returning false as the element was not found or there was an error
    }
}

  async getCheckedRadioButtonText(name: string): Promise<string | undefined> {
    if (this.page) {
      const radioButtons = await this.page.locator(`input[name="${name}"]:checked`);
      const checkedButton = await radioButtons.first();
      if (checkedButton) {
        const label = await checkedButton.locator('..').locator('label');
        const labelText = await label.textContent();
        return labelText ?? undefined;
      }
    }
    return undefined;
  }

  async checkElementEnabled(selector: string): Promise<boolean> {
    const element = await this.getElement(selector);
    return element ? await element.isEnabled() : false;
  }

  async checkElementChecked(selector: string): Promise<boolean> {
    const element = await this.getElement(selector);
    return element ? await element.isChecked() : false;
  }

  async getElement(locatorOrElement: string | Locator): Promise<Locator> {
    if (typeof locatorOrElement === 'string' && this.page) {
      return this.page.locator(locatorOrElement);
    }
    if (
      locatorOrElement &&
      typeof locatorOrElement === 'object' &&
      typeof (locatorOrElement as any).isVisible === 'function'
    ) {
      return locatorOrElement as Locator;
    }

    throw new Error('Invalid argument: locatorOrElement must be a string or Locator.');
  }

  async waitForElementToAppear(elementDefinition: { type: string; value: string; name?: string; exact?: boolean }, timeout: number = 1000, pollInterval: number = 100): Promise<Locator | null> {
  const startTime = Date.now();
  while (Date.now() - startTime < timeout) {
    try {
      const locator = this.getElementByType(
        elementDefinition.type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
        elementDefinition.value,
        elementDefinition.name,
        elementDefinition.exact ?? false
      );
      const element = await this.getElement(locator);
      if (element && await element.isVisible()) {
        console.log(`✅ Element '${elementDefinition.value}' appeared.`);
        return element;
      }
    } catch (e) {
      console.warn(`⚠️ Error while waiting for element '${elementDefinition.value}': ${e}`);
    }
    await new Promise(resolve => setTimeout(resolve, pollInterval));
  }
  console.log(`⚠️ Element '${elementDefinition.value}' did not appear within the timeout.`);
  return null;
}


  async waitForElementToDisappear(elementDefinition: { type: string; value: string; name?: string; exact?: boolean }, timeout: number = 1000, pollInterval: number = 100): Promise<boolean> {
    const startTime = Date.now();
    while (Date.now() - startTime < timeout) {
      try {
        const locator = this.getElementByType(
          elementDefinition.type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
          elementDefinition.value,
          elementDefinition.name,
          elementDefinition.exact ?? false
        );
        const element = await this.getElement(locator);
        if (!element || !(await element.isVisible())) {
          console.log(`✅ Element '${elementDefinition}' disappeared.`);
          return true;
        }
      } catch (e) {
        console.log(`⚠️ Exception occurred while checking '${elementDefinition}', assuming it's gone.`);
        return true;
      }
      await new Promise(resolve => setTimeout(resolve, pollInterval)); // Polling interval
    }

    console.log(`⚠️ Timeout: Element '${elementDefinition.value}' did not disappear within ${timeout} ms.`);
    return false;
  }

  async isPageResponsive(): Promise<boolean> {
    if (this.page) {
      try {
        await this.page.waitForSelector('body', { timeout: 1000 });
        return true;
      } catch {
        return false;
      }
    }
    return false;
  }

  async handleUnresponsivePage(): Promise<boolean> {
    if (this.page) {
      try {
        await this.page.reload({ waitUntil: 'networkidle' });
        await this.page.waitForLoadState();
        return true;
      } catch (error) {
        console.error('Error reloading page:', error);
        return false;
      }
    }
    return false;
  }
  getMockDatabaseHelper(workingDirectory: string): any {
    const mockDataFile = path.join(workingDirectory, 'mock_data', 'mock_patients.json');
    if (!fs.existsSync(mockDataFile)) {
      throw new Error(`Mock data file not found: ${mockDataFile}`);
    }
    return JSON.parse(fs.readFileSync(mockDataFile, 'utf-8')); // Simulate DB as JSON object
  }

  async javascriptClick(element: Locator) {
    if (!this.page) throw new Error('Page is not initialized. Did you launch the browser?');
    const handle = await element.elementHandle();
    if (handle) {
      await this.page.evaluate((el) => {
        if ('click' in el) (el as HTMLElement).click();
      }, handle);
    }
  }

  async mockApiResponse(workingDirectory: string) {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }

    const endpointPattern = '**/FHIR/R4/Patient/**';
    const db = this.getMockDatabaseHelper(workingDirectory);

    await this.page.route(endpointPattern, async (route: Route) => {
      const url = route.request().url();
      const nhsNumber = new URL(url).searchParams.get('nhsNumber');

      if (!nhsNumber) {
        console.warn(`No NHS number found in request: ${url}`);
        return route.continue();
      }

      const patient = db.patients.find((p: any) => p.nhs_number === nhsNumber);

      if (patient) {
        const fullName = patient.name.split(' ');
        const response = {
          PdsPatient: {
            PatientId: patient.id,
            NhsNumber: patient.nhs_number,
            FirstName: fullName[0],
            LastName: fullName[1] || '',
            DateOfBirth: patient.dob,
            GenderId: 1,
            Gender: null,
            Telephone: null,
            Address: patient.address,
            Postcode: 'DN18 5DW',
            GpCode: null,
            TooManyReturnedResults: false,
            PatientExists: true,
            IsDeceased: false,
            PdsPatientDto: null,
            Vaccinations: null,
            SecurityCode: 0,
            AuditTypeId: null,
            AuditDateTime: null,
            AuditUserId: null,
            AuditIpAddress: null
          },
          RavsPatient: {
            ...patient,
            PatientExists: false,
            IsDeceased: false,
            Address: null,
            Postcode: null
          }
        };
        await route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify(response)
        });
      } else {
        await route.fulfill({
          status: 404,
          contentType: 'application/json',
          body: JSON.stringify({ error: 'Patient not found' })
        });
      }
    });
    await this.page.route('**/FHIR/R4/Patient/**', route => route.abort());
  }

async findElementAndPerformAction(
  elementDefinition: { type: string; value: string | any; name?: string; exact?: boolean; parent?: string },
  action: string,
  inputValue?: any,
): Promise<any> {
  if (!this.page) {
    throw new Error('❌ Page is not initialized. Call launchBrowser() first.');
  }

  for (let retry = 0; retry < maxRetries; retry++) {
    try {
      let locator;

      if (elementDefinition.value && typeof (elementDefinition.value as any).locator === 'function') {
        locator = elementDefinition.value as Locator;
      } else {
        if (elementDefinition.parent) {
          const parentLocator = this.page.locator(elementDefinition.parent);
          locator = parentLocator.locator(this.getElementByType(
            elementDefinition.type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
            elementDefinition.value,
            elementDefinition.name,
            elementDefinition.exact ?? false
          ));
        } else {
          locator = this.getElementByType(
            elementDefinition.type as 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id',
            elementDefinition.value,
            elementDefinition.name,
            elementDefinition.exact ?? false
          );
        }
      }

      try {
        await locator.waitFor({ state: 'visible', timeout: 1000 });
      } catch (e) {
        console.warn(`⚠️ Element '${elementDefinition.value}' not found or not visible after ${maxRetries} attempts.`);
        return;
      }

      switch (action.toLowerCase()) {
        case 'click':
          await locator.click();
          break;

        case 'check':
          if (!(await locator.isChecked())) await locator.check();
          break;

        case 'uncheck':
          if (await locator.isChecked()) await locator.uncheck();
          break;

        case 'select_option':
          if (typeof inputValue === 'number') {
            await locator.selectOption({ index: inputValue });
          } else if (typeof inputValue === 'string') {
            await locator.selectOption({ value: inputValue });
          } else {
            throw new Error('❌ select_option requires a string or number as inputValue');
          }
          break;

        case 'get_options':
          return await locator.evaluate(el =>
            Array.from((el as HTMLSelectElement).options).map(opt => opt.text)
          );

        case 'clear':
          await locator.fill('');
          break;

        case 'input_text':
          if (!inputValue) throw new Error('❌ input_text requires inputValue');
          await locator.fill(String(inputValue));
          break;

        case 'get_text':
          return await locator.textContent();

        case 'get_value':
          return await locator.getAttribute('value');

        case 'scroll_to':
          await locator.scrollIntoViewIfNeeded();
          break;

        case 'get_selected_option':
          const selected = locator.locator('option:checked');
          return {
            text: await selected.textContent(),
            value: await selected.getAttribute('value')
          };

        case 'type_text':
          if (!inputValue) throw new Error('❌ type_text requires inputValue');
          await locator.type(String(inputValue), { delay: 50 });
          break;

        default:
          console.warn(`⚠️ Unsupported action: ${action}`);
      }

      return;
    } catch (err) {
      console.warn(`⚠️ Error on attempt ${retry + 1}:`, err);
    }
  }
}

async waitForLoadingToDisappear(timeout: number = 1000): Promise<void> {
    try {
        if (this.page) {
            await this.page.waitForLoadState('networkidle', { timeout: 1000 });

            const loadingSelectors = [
                '[role="status"]',
                '.loading',
                '.spinner',
                '.loading-overlay',
                '.overlay'
            ];

            for (const selector of loadingSelectors) {
                const loadingElement = this.page.locator(selector);
                if (await loadingElement.count() > 0) {
                    console.log(`⏳ Waiting for loading element (${selector}) to disappear...`);
                    await loadingElement.waitFor({ state: 'hidden', timeout });
                }
            }
        }
    } catch (error) {
        console.error('❌ Error while waiting for loading element to disappear:', error);
    }
}

  async waitForPageToLoad(timeout: number = 1000, loadState: 'load' | 'domcontentloaded' | 'networkidle' = 'load' ): Promise<void> {
    if (this.page) {
      await this.page.waitForLoadState(loadState, { timeout });
    } else {
      throw new Error('Page is not initialized. Please launch the browser first.');
    }
  }

  async waitForSelectorToDisappear(selector: string, timeout = 1000) {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    try {
      await this.page.waitForSelector(selector, { state: 'hidden', timeout });
    } catch (e) {
      console.warn(`Failed waiting for ${selector} to disappear:`, e);
    }
  }

  async checkElementByLocatorEnabled(element: Locator): Promise<boolean> {
    try {
      return await element.isEnabled();
    } catch {
      return false;
    }
  }

  scrollIntoView(selector: string) {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    this.page.locator(selector).scrollIntoViewIfNeeded();
  }

  scrollElementByLocatorIntoView(element: Locator) {
    element.scrollIntoViewIfNeeded();
  }

  clearElement(selector: string) {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    this.page.locator(selector).fill('');
  }

  releaseMouse() {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    this.page.mouse.move(100, 100);
    this.page.mouse.down();
    this.page.mouse.up();
  }

  getElementByType(
    type: 'role' | 'text' | 'label' | 'placeholder' | 'xpath' | 'link' | 'radio' | 'title' | 'row' | 'cell' | 'id' | 'nested_role',
    value?: string,
    name?: string,
    exact: boolean = false,
    parent?: string
): Locator {
    if (!this.page) {
        throw new Error('Page is not initialized. Call launchBrowser() first.');
    }

    if (type === 'nested_role') {
        if (!value || !parent) throw new Error('Nested role requires both a value and a parent');
        const parentLocator = this.page.locator(parent);
        return parentLocator.getByRole(value as any, { name, exact });
    }

    switch (type) {
        case 'role':
            if (!value) throw new Error(`Role type requires a value (e.g., 'button', 'link')`);
            return this.page.getByRole(value as any, { name, exact });

        case 'text':
            if (!value) throw new Error('Text type requires a value');
            return this.page.getByText(value, { exact });

        case 'label':
            if (!value) throw new Error('Label type requires a value');
            return this.page.getByLabel(value, { exact }).first();

        case 'placeholder':
            if (!value) throw new Error('Placeholder type requires a value');
            return this.page.getByPlaceholder(value);

        case 'xpath':
            if (!value) throw new Error('XPath type requires a value');
            return this.page.locator(value);

        case 'link':
            if (!value) throw new Error('Link type requires a value');
            return this.page.getByRole('link', { name: value, exact });

        case 'radio':
            if (!value) throw new Error('Radio type requires a value');
            return this.page.getByRole('radio', { name: value, exact });

        case 'title':
            if (!value) throw new Error('Title type requires a value');
            return this.page.getByTitle(value, { exact });

        case 'row':
            if (!value) throw new Error('Row type requires a value');
            return this.page.getByRole('row', { name: value, exact });

        case 'cell':
            if (!value) throw new Error('Cell type requires a value');
            return this.page.getByRole('cell', { name: value, exact });

        case 'id':
            if (!value) throw new Error('ID type requires a value');
            return this.page.locator(`#${value}`);

        default:
            throw new Error(`Unsupported locator type: ${type}`);
    }
}

async clickCellInRow(rowName: string, cellIndex: number) {
    const row = this.getElementByType('row', rowName);
    const cell = row.locator('role=cell').nth(cellIndex);
    await this.findElementAndPerformAction({ type: 'locator', value: cell}, 'click');
  }

  async clickLinkInRow(rowName: string, linkIndex: number) {
    const row = this.getElementByType('row', rowName);
    const link = row.getByRole('link').nth(linkIndex);
    await this.findElementAndPerformAction({ type: 'role', value: 'link' }, 'click');
  }

  async disableSmoothScrolling() {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    await this.page.addInitScript(`
      window.HTMLElement.prototype.scrollIntoView = () => {};
      window.scrollTo = () => {};
    `);
  }

  getCurrentUrl(): string {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    return this.page.url();
  }

  async clickAndGetDownloadPath(
    elementDefinition: { type: string; value: string; name?: string; exact?: boolean },
    action: string = 'click',
    timeout: number = 30_000,
    downloadDir: string = 'downloads'
  ): Promise<string> {
    if (!this.page) {
      throw new Error('Page is not initialized. Call launchBrowser() first.');
    }
    try {
      if (!path.isAbsolute(downloadDir)) {
        downloadDir = path.join(process.cwd(), downloadDir);
      }

      fs.mkdirSync(downloadDir, { recursive: true });

      const [download] = await Promise.all([
        this.page.waitForEvent('download', { timeout }),
        this.findElementAndPerformAction(elementDefinition, action),
      ]);

      const suggestedFilename = download.suggestedFilename();
      const filePath = path.join(downloadDir, suggestedFilename);
      await download.saveAs(filePath);

      console.log(`Download completed: ${filePath}`);
      return filePath;
    } catch (error) {
      console.error('Error during download:', error);
      throw error;
    }
  }

  public async quitBrowser() {
    try {
      if (this.browser) {
        console.log("Closing the browser...");

        const contexts = this.browser.contexts();
        for (const context of contexts) {
          await context.close();
        }

        await this.browser.close();
        this.browser = null;
        console.log("Browser closed successfully.");
      }
    } catch (error) {
      console.error("Error closing the browser:", error);
    }
  }

}

