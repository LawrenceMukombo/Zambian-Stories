const { spawnSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const candidates = [
  process.env.CODEX_PYTHON,
  'C:\\Users\\Mukombo\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe',
  process.platform === 'win32' ? 'python.exe' : 'python3'
].filter(Boolean);

const python = candidates.find(candidate => path.isAbsolute(candidate) ? fs.existsSync(candidate) : true);
const result = spawnSync(python, [path.join(__dirname, 'build_publish.py'), ...process.argv.slice(2)], { stdio: 'inherit' });
if (result.error) throw result.error;
if ((result.status ?? 1) !== 0) process.exit(result.status ?? 1);
if (!process.argv.includes('--full')) {
  const cover = spawnSync(python, [path.join(__dirname, 'build_wrap_cover.py')], { stdio: 'inherit' });
  if (cover.error) throw cover.error;
  process.exit(cover.status ?? 1);
}
process.exit(0);
