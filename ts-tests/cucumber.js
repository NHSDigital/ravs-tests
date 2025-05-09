let common = [
  './e2e/features/*.feature',
  '--require-module ts-node/register',
  '--require ./e2e/steps/*.ts',
  '--format progress-bar',
  '--publish-quiet',
  `--format-options '{"snippetInterface": "synchronous"}'`,
  '--timeout 10000'
].join(' ');

module.exports = {
  default: common
}
