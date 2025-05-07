import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './e2e/features',
  testMatch: ['**/*.feature'],
  use: {
    headless: false,
    trace: 'on-first-retry',
    screenshot: 'on',
    video: 'retain-on-failure',
  },
  timeout: 60000,
});
