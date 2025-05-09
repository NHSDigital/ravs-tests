let common = [
  './e2e/features/*.feature',
  '--require-module ts-node/register',
  '--require ./e2e/steps/*.ts',
  '--format progress-bar',
  '--publish-quiet',
  `--format-options '{"snippetInterface": "synchronous"}'`
].join(' ');

module.exports = {
  default: common,
  parallel: 4,
  publishQuiet: true,
  failFast: true,
  worldParameters: {},
  timeout: 1000
};
