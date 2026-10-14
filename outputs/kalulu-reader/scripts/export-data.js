const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const context = { window: {} };
vm.createContext(context);
for (const file of ['stories-data.js', 'front-matter.js']) {
  vm.runInContext(fs.readFileSync(path.join(root, file), 'utf8'), context, { filename: file });
}

const outDir = path.join(root, 'build');
fs.mkdirSync(outDir, { recursive: true });
fs.writeFileSync(path.join(outDir, 'book.json'), JSON.stringify({
  title: 'Stories from the Baobab Tree',
  subtitle: 'Ten Original Zambian Stories for Young Readers',
  creator: 'Lawrence Mukombo',
  language: 'en',
  stories: context.window.KALULU_STORIES,
  front: context.window.BAOBAB_FRONT
}, null, 2));
console.log(`Exported ${context.window.KALULU_STORIES.length} stories to build/book.json`);
