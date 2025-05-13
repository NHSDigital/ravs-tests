let common = [
  './e2e/features/*.feature',
  '--require-module ts-node/register',
  '--require ./e2e/steps/*.ts',
  '--format progress-bar',
  `--format-options '{"snippetInterface": "synchronous"}'`
].join(' ');

module.exports = {
  default: common,
  workers: 4,
  failFast: true,
  worldParameters: {},
  timeout: 1000
};
