const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const context = { window: {} };
vm.createContext(context);
for (const file of ['stories-data.js', 'front-matter.js', 'quiz-data.js']) {
  vm.runInContext(fs.readFileSync(path.join(root, file), 'utf8'), context, { filename: file });
}

const stories = context.window.KALULU_STORIES || [];
const errors = [];
const warnings = [];
const ids = new Set();
for (const story of stories) {
  if (!Number.isInteger(story.id) || ids.has(story.id)) errors.push(`Invalid or duplicate story id: ${story.id}`);
  ids.add(story.id);
  for (const key of ['title', 'chapter', 'lesson']) if (!story[key]) errors.push(`Story ${story.id}: missing ${key}`);
  if (!Array.isArray(story.body) || !story.body.length) errors.push(`Story ${story.id}: missing body`);
  if (!Array.isArray(story.newWords) || !story.newWords.length) errors.push(`Story ${story.id}: missing vocabulary`);
  if (!Array.isArray(story.questions) || !story.questions.length) errors.push(`Story ${story.id}: missing questions`);
  const ext = story.id <= 25 ? 'jpg' : story.id <= 40 ? 'png' : 'svg';
  const cover = path.join(root, 'assets', 'covers', `story-${String(story.id).padStart(2, '0')}.${ext}`);
  if (!fs.existsSync(cover)) errors.push(`Story ${story.id}: missing cover ${path.relative(root, cover)}`);
}
for (let id = 1; id <= 60; id++) if (!ids.has(id)) errors.push(`Missing story id ${id}`);

const originalIds = stories.filter(s => s.id >= 16 && s.id <= 25).map(s => s.id);
if (originalIds.length !== 10) errors.push('Expected the ten original stories (IDs 16-25).');
warnings.push('Commercial build is restricted to original stories 16-25. Rights are not recorded for 26-60, and 1-15 require a completed provenance review.');
warnings.push('Run the EPUB through Kindle Previewer and review the print PDF in KDP Previewer before publishing.');

console.log(`Checked ${stories.length} stories, ${ids.size} unique IDs, and all expected cover paths.`);
for (const warning of warnings) console.warn(`WARNING: ${warning}`);
if (errors.length) {
  for (const error of errors) console.error(`ERROR: ${error}`);
  process.exit(1);
}
console.log('Preflight passed.');
