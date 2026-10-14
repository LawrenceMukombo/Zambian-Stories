/**
 * Stories from the Baobab Tree - Traditional EPUB / 3D Flipbook Reader
 * Features:
 * - Multi-page story pagination (splits long stories across multiple comfortable reading pages)
 * - 3D physical book page flip engine with synthesized paper rustle sound
 * - Clean typeset book layout: running heads, page numbers, drop caps, no clutter
 * - Interactive Table of Contents with working close button and direct chapter links
 * - Offline text-to-speech audio reader and customizable themes/font sizes
 */

const S = window.KALULU_STORIES || [];
const F = window.BAOBAB_FRONT || {};
const Q = window.BAOBAB_QUIZZES || {};

const bookContainer = document.querySelector('#book-container');
const leftContent = document.querySelector('#left-page-content');
const rightContent = document.querySelector('#right-page-content');
const leftPageNumEl = document.querySelector('#left-page-number');
const rightPageNumEl = document.querySelector('#right-page-number');
const runningChapter = document.querySelector('#running-chapter');
const chapterTitleEl = document.querySelector('#current-chapter-title');
const pageScrubber = document.querySelector('#page-scrubber');
const spreadIndicator = document.querySelector('#spread-indicator');
const progressIndicator = document.querySelector('#progress-indicator');
const flippingLeaf = document.querySelector('#flipping-leaf');
const ttsBtn = document.querySelector('#btn-read-aloud');
const ttsIcon = document.querySelector('#tts-icon');
const ttsLabel = document.querySelector('#tts-label');

let currentSpread = 0;
let isFlipping = false;
let isReadingAloud = false;
let currentUtterance = null;
let currentParaIndex = -1;
let readableParas = [];

const CATEGORIES = [
  { title: 'Kalulu the Hare Stories', icon: '&#128007;', description: 'All adventures featuring Kalulu, gathered into one collection.', ids: [1,2,3,4,5,6,26,27,28,29,30,31,32] },
  { title: 'Classic Zambian Children&#8217;s Stories', icon: '&#127795;', description: 'Animal tales, journeys and traditional moral stories.', ids: [7,8,9,10,11,12,13,14,15] },
  { title: 'Jelita and Mulenga Stories', icon: '&#127891;', description: 'Original school adventures about honesty, teamwork and discovery.', ids: [16,17,18,19] },
  { title: 'Children of Northwestern Province', icon: '&#127757;', description: 'Original stories featuring Chisola, Bernice, Chawana, Vumbi, Wana, Chishomyo and Chiwape.', ids: [20,21,22,23,24,25] },
  { title: 'Other Folktales Retold by Parvathi Raman', icon: '&#128218;', description: 'Traditional tales from the credited 1979 source collection.', ids: [33,34,35,36,37,38,39,40] },
  { title: 'Why the Lion Roars and Other Animal Stories', icon: '&#129409;', description: 'Animal origin tales from the credited G. N. Lansdown collection.', ids: [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60] }
];

const ORDER = CATEGORIES.flatMap(c => c.ids);
const storyById = id => S.find(x => x.id === id);
const esc = t => String(t ?? '').replace(/[&<>\"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '\"': '&quot;' }[c]));

function coverPath(id) {
  let ext = id > 40 ? 'svg' : (id > 25 ? 'png' : 'jpg');
  return `assets/covers/story-${String(id).padStart(2, '0')}.${ext}?v=20261014f`;
}

// In-Page Contextual Scenes to visualize key moments across all 60 stories
const STORY_CONTEXTUAL_SCENES = {
  1: { src: 'assets/story-01.svg?v=20261014f', caption: 'Kalulu outwits the gathered animals at the great feast' },
  2: { src: 'assets/story-02.svg?v=20261014f', caption: 'Hyena discovers Kalulu\'s clever deception in the bush' },
  3: { src: 'assets/story-03.svg?v=20261014f', caption: 'Kalulu leaps safely across the backs of the river crocodiles' },
  4: { src: 'assets/story-04.svg?v=20261014f', caption: 'Kalulu outsmarting the cunning farmer\'s snare trap' },
  5: { src: 'assets/story-05.svg?v=20261014f', caption: 'The great tug-of-war between the elephant and hippopotamus' },
  6: { src: 'assets/story-06.svg?v=20261014f', caption: 'Leopard searching in vain for the quick-footed hare' },
  7: { src: 'assets/covers/corrected-07.png?v=20261014f', caption: 'Chimuka standing firm and brave against the school bully' },
  8: { src: 'assets/covers/corrected-08.png?v=20261014f', caption: 'The children embarking on their long journey to Tanzania' },
  9: { src: 'assets/covers/corrected-09.png?v=20261014f', caption: 'Arriving across the northern borders at twilight' },
  10: { src: 'assets/covers/corrected-10.png?v=20261014f', caption: 'Searching deep in the bush for the farmer\'s lost calf' },
  11: { src: 'assets/covers/corrected-11.png?v=20261014f', caption: 'Elders sharing timeless ancestral wisdom around the fire' },
  12: { src: 'assets/covers/corrected-12.png?v=20261014f', caption: 'Safely crossing the flooded river during heavy rains' },
  13: { src: 'assets/covers/corrected-13.png?v=20261014f', caption: 'Harvesting sweet wild honey from the hollow trunk of the baobab' },
  14: { src: 'assets/covers/corrected-14.png?v=20261014f', caption: 'The sacred bird revealing truth to the village chief' },
  15: { src: 'assets/covers/corrected-15.png?v=20261014f', caption: 'Working side by side to build the new village school' },
  16: { src: 'assets/covers/original-16.png?v=20261014f', caption: 'Jelita and Mulenga helping at the bustling community market' },
  17: { src: 'assets/covers/original-17.png?v=20261014f', caption: 'Jelita and Mulenga\'s science discovery walk through nature' },
  18: { src: 'assets/covers/original-18.png?v=20261014f', caption: 'Finding the ancient pathway along the Zambezi riverbanks' },
  19: { src: 'assets/covers/original-19.png?v=20261014f', caption: 'Celebrating school excellence and teamwork at the assembly' },
  20: { src: 'assets/covers/northwestern-20.png?v=20261014f', caption: 'Chisola and Bernice gathering wild forest fruit near Solwezi' },
  21: { src: 'assets/covers/northwestern-21.png?v=20261014f', caption: 'Chawana and Vumbi crossing the historic Kabompo footbridge' },
  22: { src: 'assets/covers/northwestern-22.png?v=20261014f', caption: 'Wana observing the honeyguide bird in the open woodland' },
  23: { src: 'assets/covers/northwestern-23.png?v=20261014f', caption: 'Chishomyo practicing traditional bamboo basket weaving' },
  24: { src: 'assets/covers/northwestern-24.png?v=20261014f', caption: 'Chiwape exploring the sacred Mukenge riverbanks' },
  25: { src: 'assets/covers/northwestern-25.png?v=20261014f', caption: 'The village community gathering for the traditional harvest festival' },
  26: { src: 'assets/covers/story-26.svg?v=20261014f', caption: 'Kalulu encountering the mysterious clay man in the orchard' },
  27: { src: 'assets/covers/story-27.svg?v=20261014f', caption: 'Kalulu and the enchanted cooking pot during the dry season' },
  28: { src: 'assets/covers/story-28.svg?v=20261014f', caption: 'Chameleon matching pace with the swift hare' },
  29: { src: 'assets/covers/story-29.svg?v=20261014f', caption: 'Kalulu riding triumphantly upon the lion\'s back' },
  30: { src: 'assets/covers/story-30.svg?v=20261014f', caption: 'The great council of waterbirds at the marsh' },
  31: { src: 'assets/covers/story-31.svg?v=20261014f', caption: 'Kalulu finding refuge beneath the baobab as the bush burns' },
  32: { src: 'assets/covers/story-32.svg?v=20261014f', caption: 'The village healer inspecting the medicine bundle' },
  33: { src: 'assets/covers/story-33.svg?v=20261014f', caption: 'The chief setting the test of wisdom and courage' },
  34: { src: 'assets/covers/story-34.svg?v=20261014f', caption: 'The enchanted rhythm of the drum sounding through the trees' },
  35: { src: 'assets/covers/story-35.svg?v=20261014f', caption: 'The magic calabash overflowing with grain and bounty' },
  36: { src: 'assets/covers/story-36.svg?v=20261014f', caption: 'The three brothers following the golden guinea-fowl' },
  37: { src: 'assets/covers/story-37.svg?v=20261014f', caption: 'The hunter listening to the secret language of the animals' },
  38: { src: 'assets/covers/story-38.svg?v=20261014f', caption: 'The talking baobab tree echoing across the Luangwa valley' },
  39: { src: 'assets/covers/story-39.svg?v=20261014f', caption: 'The hidden pool discovered in the limestone caves' },
  40: { src: 'assets/covers/story-40.svg?v=20261014f', caption: 'The wise elder settling the dispute between the two fishermen' },
  41: { src: 'assets/covers/story-41.svg?v=20261014f', caption: 'The furious swarm of bees attacking the honey-covered lion' },
  42: { src: 'assets/covers/story-42.svg?v=20261014f', caption: 'Crocodile holding fast to Ostrich\'s head while Ostrich pulls back' },
  43: { src: 'assets/covers/story-43.svg?v=20261014f', caption: 'Chickens continually scratching the dusty ground searching for the needle' },
  44: { src: 'assets/covers/story-44.svg?v=20261014f', caption: 'Frog burning his throat on the scalding porridge by the pond' },
  45: { src: 'assets/covers/story-45.svg?v=20261014f', caption: 'Hyena laughing boastfully across the vast golden plains' },
  46: { src: 'assets/covers/story-46.svg?v=20261014f', caption: 'Hare sipping the glistening morning dewdrops from the green leaves' },
  47: { src: 'assets/covers/story-47.svg?v=20261014f', caption: 'Hippo plunging into the river waters after losing his golden horns' },
  48: { src: 'assets/covers/story-48.svg?v=20261014f', caption: 'Hyena limping away in pain after being outsmarted by Hare' },
  49: { src: 'assets/covers/story-49.svg?v=20261014f', caption: 'The joyful assembly of birds singing melodic songs among the branches' },
  50: { src: 'assets/covers/story-50.svg?v=20261014f', caption: 'Fish finding sanctuary and freedom in the cool river currents' },
  51: { src: 'assets/covers/story-51.svg?v=20261014f', caption: 'Porcupine raising a protective fan of sharp black-and-white quills' },
  52: { src: 'assets/covers/story-52.svg?v=20261014f', caption: 'The wise horned owl gliding silently beneath the crescent moon' },
  53: { src: 'assets/covers/story-53.svg?v=20261014f', caption: 'Tortoise walking safely beneath his carved protective shell' },
  54: { src: 'assets/covers/story-54.svg?v=20261014f', caption: 'Cat eating the unguarded meat from the table while Dog barks below' },
  55: { src: 'assets/covers/story-55.svg?v=20261014f', caption: 'The mighty elephant startled by the brave little mouse at his feet' },
  56: { src: 'assets/covers/story-56.svg?v=20261014f', caption: 'Giraffe reaching high into the baobab canopy for tender leaves' },
  57: { src: 'assets/covers/story-57.svg?v=20261014f', caption: 'Leopard resting upon the acacia branch with his new spotted coat' },
  58: { src: 'assets/covers/story-58.svg?v=20261014f', caption: 'Monkeys swinging and conversing high in the forest treetops' },
  59: { src: 'assets/covers/story-59.svg?v=20261014f', caption: 'Pulu the bushbuck and Ngolo the zebra grazing together in loyal friendship' },
  60: { src: 'assets/covers/story-60.svg?v=20261014f', caption: 'The gentle collared dove bearing a velvet black ring of peace' }
};

function getContextualScene(storyId) {
  return STORY_CONTEXTUAL_SCENES[storyId] || null;
}

// --- Local Storage Progress & State ---
const STORAGE_KEY = 'baobab-learning-v1';
function loadState() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
  } catch (e) {
    return {};
  }
}

let state = Object.assign({
  read: [],
  quiz: {},
  words: {},
  matches: {},
  theme: 'paper',
  fontSize: 'md',
  sound: true
}, loadState());

state.read = state.read || [];
state.quiz = state.quiz || {};
state.words = state.words || {};
state.matches = state.matches || {};

function saveState() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch (e) {}
}

// --- Synthesized Physical Page Turn Sound ---
let audioCtx = null;
function getAudioCtx() {
  if (!audioCtx && (window.AudioContext || window.webkitAudioContext)) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

function playPaperSound() {
  if (!state.sound) return;
  try {
    const ctx = getAudioCtx();
    if (!ctx) return;
    const now = ctx.currentTime;
    const bufferSize = Math.floor(ctx.sampleRate * 0.16);
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    const noise = ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(1300, now);
    filter.frequency.exponentialRampToValueAtTime(650, now + 0.15);
    filter.Q.value = 1.8;

    const gain = ctx.createGain();
    gain.gain.setValueAtTime(0.09, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);

    noise.start(now);
  } catch (e) {}
}

function playSuccessChime() {
  if (!state.sound) return;
  try {
    const ctx = getAudioCtx();
    if (!ctx) return;
    const notes = [523.25, 659.25, 783.99, 1046.50];
    notes.forEach((freq, idx) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.value = freq;
      const start = ctx.currentTime + idx * 0.06;
      gain.gain.setValueAtTime(0.07, start);
      gain.gain.exponentialRampToValueAtTime(0.001, start + 0.2);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(start);
      osc.stop(start + 0.2);
    });
  } catch (e) {}
}

function toggleFlipSound() {
  state.sound = !state.sound;
  saveState();
  const btn = document.querySelector('#btn-sound-toggle');
  if (btn) btn.innerHTML = state.sound ? '&#128266; Page Flip Sound: On' : '&#128263; Page Flip Sound: Off';
  if (state.sound) playPaperSound();
}

// --- MULTI-PAGE STORY PAGINATION ENGINE ---
// Splits stories across multiple comfortable, readable pages.
// Avoids vertical scrolling inside pages and gives a genuine book experience.

let ALL_SPREADS = [];
let CHAPTER_SPREAD_MAP = {}; // storyId -> spreadIndex
let SPREAD_CHAPTER_MAP = {}; // spreadIndex -> storyId

function paginateStoryIntoPages(story) {
  const pages = [];
  const body = story.body || [];
  
  // Page 1 of Story: Title, Illustration, and first 2-3 paragraphs (~600 chars)
  let chars = 0;
  let idx = 0;
  const firstPageItems = [];
  while (idx < body.length && (firstPageItems.length < 2 || (chars < 650 && firstPageItems.length < 4))) {
    const item = body[idx];
    firstPageItems.push(item);
    chars += (item.text || '').length;
    idx++;
  }

  pages.push({
    type: 'story-start',
    storyId: story.id,
    title: story.title,
    chapter: story.chapter,
    items: firstPageItems,
    illustration: coverPath(story.id)
  });

  // Middle narrative pages: ~900-1100 chars per page
  while (idx < body.length) {
    const pageItems = [];
    let pageChars = 0;
    while (idx < body.length && (pageItems.length < 3 || (pageChars < 1050 && pageItems.length < 6))) {
      const item = body[idx];
      pageItems.push(item);
      pageChars += (item.text || '').length;
      idx++;
    }

    // Check if this is the final page of the story
    const isFinal = (idx >= body.length);
    const contextualImage = (!isFinal && pages.length === 1) ? getContextualScene(story.id) : null;
    pages.push({
      type: isFinal ? 'story-end' : 'story-body',
      storyId: story.id,
      title: story.title,
      chapter: story.chapter,
      items: pageItems,
      contextualImage: contextualImage,
      lesson: isFinal ? story.lesson : null,
      story: isFinal ? story : null
    });
  }

  // Ensure story has an end page with the moral lesson and activities if not already added
  const hasEnd = pages.some(p => p.type === 'story-end');
  if (!hasEnd) {
    pages.push({
      type: 'story-end',
      storyId: story.id,
      title: story.title,
      chapter: story.chapter,
      items: [],
      lesson: story.lesson,
      story: story
    });
  }

  return pages;
}

function buildAllSpreads() {
  ALL_SPREADS = [];
  CHAPTER_SPREAD_MAP = {};
  SPREAD_CHAPTER_MAP = {};

  let currentBookPage = 1;

  // SPREAD 0: Book Cover & Frontispiece
  ALL_SPREADS.push({
    type: 'cover',
    title: 'Cover & Frontispiece',
    chapterRunning: 'Stories from the Baobab Tree',
    leftNum: '',
    rightNum: '',
    leftHtml: `
      <div style="height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding: 24px;">
        <div style="font-size:3.5rem; margin-bottom:12px;">&#127795;</div>
        <h3 style="font-size:1.4rem; color:var(--accent); margin:0 0 10px;">Wisdom Beneath the Branches</h3>
        <p style="font-style:italic; max-width:320px; line-height:1.7; opacity:0.85;">
          "A person who does not travel thinks their mother is the only cook."
        </p>
        <small style="margin-top:14px; opacity:0.65;">— Traditional African Proverb</small>
        <div style="margin-top:36px; padding:12px 18px; border:1px dashed var(--page-border); border-radius:8px; font-size:0.85rem;">
          <strong>60 Stories &middot; 6 Collections</strong><br>
          Illustrated Zambian & African Folktales
        </div>
      </div>
    `,
    rightHtml: `
      <div class="book-cover-page">
        <div>
          <span class="cover-badge">Zambian Reader Edition</span>
          <h1 class="cover-title">Stories from the Baobab Tree</h1>
          <p class="cover-subtitle">A Collection of African Tales Inspired by Classic Zambian School Readers</p>
        </div>
        <div class="cover-art-frame">
          <img src="assets/covers/story-01.jpg" alt="Baobab Book Cover">
        </div>
        <div>
          <p class="cover-author">Compiled by Lawrence Mukombo</p>
          <button class="tool-btn" style="background:var(--accent); color:#fff; font-size:0.95rem; padding:8px 24px; margin-top:6px;" onclick="flipNext()">
            Open Book &#10148;
          </button>
        </div>
      </div>
    `
  });

  // SPREAD 1: Title & Publication Notice
  ALL_SPREADS.push({
    type: 'front',
    title: 'Title & Copyright',
    chapterRunning: 'Publication Notice',
    leftNum: 'i',
    rightNum: 'ii',
    leftHtml: `
      <div style="padding: 24px 10px; text-align:center;">
        <h1 style="font-size:2rem; color:var(--accent); margin: 20px 0 6px;">Stories from the Baobab Tree</h1>
        <p style="font-size:1.05rem; font-style:italic; margin-bottom:30px;">A Collection of African Tales Inspired by Classic Zambian School Readers</p>
        <hr style="border:0; border-top:1px solid var(--page-border); width:60%; margin:20px auto;">
        <p style="font-weight:700; text-transform:uppercase; letter-spacing:0.06em; margin-top:30px;">Compiled and Arranged by</p>
        <h3 style="font-size:1.3rem; margin:6px 0;">Lawrence Mukombo</h3>
        <p style="font-size:0.88rem; color:var(--ink-muted); margin-top:40px;">Published in Zambia &middot; Digital Interactive Edition</p>
      </div>
    `,
    rightHtml: `
      <div style="padding: 10px 6px; font-size:0.86rem; line-height:1.65;">
        <h3 style="color:var(--accent); font-size:1.05rem; margin-top:0;">Rights and Permissions Notice</h3>
        <p>Copyright in each individual story remains with its respective original author, publisher, storyteller, or rights holder. Lawrence Mukombo claims no ownership of underlying folk works.</p>
        <p><strong>Original Section:</strong> Chapters 16–19 (Jelita & Mulenga) and 20–25 (Children of Northwestern Province) are newly created original stories prepared specifically for this edition.</p>
        <p><strong>Credited Sources:</strong> Chapters 26–40 reproduce stories retold by Parvathi Raman (1979). Chapters 41–60 reproduce tales from G. N. Lansdown (1960).</p>
      </div>
    `
  });

  // SPREAD 2: Dedication & Acknowledgements
  ALL_SPREADS.push({
    type: 'front',
    title: 'Dedication & Acknowledgements',
    chapterRunning: 'Dedication',
    leftNum: 'iii',
    rightNum: 'iv',
    leftHtml: `
      <div style="height:100%; display:flex; flex-direction:column; justify-content:center; text-align:center; padding: 20px;">
        <div style="font-size:2.8rem; color:var(--accent); margin-bottom:12px;">&#10084;&#65039;</div>
        <h2 style="font-size:1.6rem; color:var(--accent); margin:0 0 16px;">Dedication</h2>
        <p style="font-size:1.15rem; line-height:1.75; font-style:italic;">
          Dedicated with love to<br>
          <strong style="font-size:1.3rem; color:var(--ink);">Chawana Mukombo</strong>,<br>
          my daughter.
        </p>
        <p style="font-size:0.95rem; line-height:1.7; max-width:320px; margin: 16px auto 0; opacity:0.85;">
          May these stories encourage you to grow in wisdom, courage, kindness, honesty, and respect for others.
        </p>
      </div>
    `,
    rightHtml: `
      <div style="padding: 10px 6px;">
        <div style="font-size:2.4rem; color:var(--accent); text-align:center;">&#128591;</div>
        <h2 style="font-size:1.4rem; color:var(--accent); text-align:center; margin:0 0 16px;">Acknowledgements</h2>
        <p style="font-size:0.92rem; line-height:1.7;">Grateful acknowledgement is given to the original storytellers, authors, publishers, educators, cultural custodians, and communities through whom these stories have been preserved and shared.</p>
        <p style="font-size:0.92rem; line-height:1.7;">This collection was compiled to celebrate oral storytelling, encourage young readers, and preserve values carried through African school-reader traditions.</p>
      </div>
    `
  });

  // Table of Contents Spread Indices (will be backfilled once story pages are computed)
  const tocSpreadIndex1 = ALL_SPREADS.length;
  ALL_SPREADS.push(null); // Placeholder for TOC 1-30
  const tocSpreadIndex2 = ALL_SPREADS.length;
  ALL_SPREADS.push(null); // Placeholder for TOC 31-60

  // PAGINATE ALL 60 STORIES
  S.forEach(story => {
    const storyPages = paginateStoryIntoPages(story);
    const startSpreadIndex = ALL_SPREADS.length;
    CHAPTER_SPREAD_MAP[story.id] = startSpreadIndex;

    // Pair story pages into 2-page spreads (Left and Right)
    for (let p = 0; p < storyPages.length; p += 2) {
      const spreadIdx = ALL_SPREADS.length;
      SPREAD_CHAPTER_MAP[spreadIdx] = story.id;

      const leftP = storyPages[p];
      const rightP = (p + 1 < storyPages.length) ? storyPages[p + 1] : null;

      const leftPageNumber = String(currentBookPage++);
      const rightPageNumber = String(currentBookPage++);

      const leftHtml = renderPageContent(leftP, story);
      const rightHtml = rightP 
        ? renderPageContent(rightP, story) 
        : renderStoryCompanionPage(story);

      ALL_SPREADS.push({
        type: 'story',
        storyId: story.id,
        title: story.title,
        chapterRunning: `Chapter ${story.id}: ${story.title}`,
        leftNum: leftPageNumber,
        rightNum: rightPageNumber,
        leftHtml,
        rightHtml
      });
    }
  });

  // Backfill Table of Contents Spreads now that all chapter page numbers are known
  ALL_SPREADS[tocSpreadIndex1] = {
    type: 'toc',
    title: 'Table of Contents (Part 1)',
    chapterRunning: 'Contents: Chapters 1–30',
    leftNum: 'v',
    rightNum: 'vi',
    leftHtml: `<div class="book-toc-page"><h2>Table of Contents</h2>${renderTOCRange(1, 15)}</div>`,
    rightHtml: `<div class="book-toc-page"><h2>Table of Contents (Cont.)</h2>${renderTOCRange(16, 30)}</div>`
  };

  ALL_SPREADS[tocSpreadIndex2] = {
    type: 'toc',
    title: 'Table of Contents (Part 2)',
    chapterRunning: 'Contents: Chapters 31–60',
    leftNum: 'vii',
    rightNum: 'viii',
    leftHtml: `<div class="book-toc-page"><h2>Table of Contents (Cont.)</h2>${renderTOCRange(31, 45)}</div>`,
    rightHtml: `<div class="book-toc-page"><h2>Table of Contents (Cont.)</h2>${renderTOCRange(46, 60)}</div>`
  };

  // SPREAD: Sources & About the Compiler
  ALL_SPREADS.push({
    type: 'back',
    title: 'Sources & About the Compiler',
    chapterRunning: 'About the Compiler',
    leftNum: String(currentBookPage++),
    rightNum: String(currentBookPage++),
    leftHtml: `
      <div style="padding: 10px 4px; font-size:0.86rem; line-height:1.65;">
        <h2 style="font-size:1.3rem; color:var(--accent); margin-top:0;">Sources and Permissions</h2>
        <p><strong>Chapters 26–40:</strong> Parvathi Raman, <em>Kalulu the Hare and Other Zambian Folk-Tales</em> (Arthur H. Stockwell Ltd., 1979; ISBN 0 7223 1219-9).</p>
        <p><strong>Chapters 41–60:</strong> G. N. Lansdown, <em>Why the Lion Roars and Other Animal Stories from Africa</em> (Macmillan & Co Ltd., 1960; Luvale translation by Chitokoloki Mission, Balovale).</p>
        <p><strong>Chapters 16–25:</strong> Original contemporary fiction written by Lawrence Mukombo (Jelita & Mulenga adventures and Children of Northwestern Province).</p>
      </div>
    `,
    rightHtml: `
      <div style="padding: 10px 4px; font-size:0.88rem; line-height:1.7;">
        <div style="font-size:2.4rem; color:var(--accent); text-align:center;">&#128100;</div>
        <h2 style="font-size:1.3rem; color:var(--accent); text-align:center; margin:0 0 12px;">About the Compiler</h2>
        <p><strong>Lawrence Mukombo</strong> compiled and typeset this collection to encourage young readers and celebrate values of kindness, honesty, and quick thinking.</p>
        <dl style="margin:20px 0; font-size:0.85rem;">
          <div style="margin:6px 0;"><strong>Country:</strong> Zambia</div>
          <div style="margin:6px 0;"><strong>Email:</strong> lawrencemukombo2@gmail.com</div>
          <div style="margin:6px 0;"><strong>Phone:</strong> +260 963 328807</div>
        </dl>
      </div>
    `
  });

  // SPREAD: Back Cover
  ALL_SPREADS.push({
    type: 'backcover',
    title: 'Back Cover',
    chapterRunning: 'The Baobab Tree',
    leftNum: '',
    rightNum: '',
    leftHtml: `
      <div style="height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding: 24px;">
        <div style="font-size:3rem; margin-bottom:12px;">&#127795;</div>
        <h3 style="color:var(--accent); margin:0 0 12px;">The End of the Book</h3>
        <p style="font-size:0.95rem; line-height:1.7; max-width:300px; font-style:italic;">
          "Knowledge is like a baobab tree; no one person can embrace it alone."
        </p>
        <small style="margin-top:20px; opacity:0.75;">You have completed your journey beneath the branches.</small>
        <button class="tool-btn" style="margin-top:28px;" onclick="goToSpread(0)">
          &#8634; Read Again from Beginning
        </button>
      </div>
    `,
    rightHtml: `
      <div class="book-cover-page" style="background:var(--cover-leather); color:#ede5d3; border-color:#d97706;">
        <div>
          <h2 style="color:#f59e0b; margin:10px 0 6px;">Stories from the Baobab Tree</h2>
          <p style="font-size:0.88rem; color:#d1d5db; max-width:320px; line-height:1.6; margin:0 auto;">
            Sixty enduring African folktales, humorous trickster adventures of Kalulu the Hare, and original school stories.
          </p>
        </div>
        <div style="padding:14px; border:1px dashed #d97706; border-radius:8px; max-width:300px; font-size:0.82rem; line-height:1.5;">
          Suitable for family reading, classroom storytelling, and young scholars of all ages.
        </div>
        <div style="font-size:0.75rem; letter-spacing:0.08em; opacity:0.8;">
          ZAMBIAN FOLK STORIES &middot; 2026 EDITION
        </div>
      </div>
    `
  });
}

// --- Render Page Types ---
function renderPageContent(page, story) {
  if (page.type === 'story-start') {
    return `
      <div>
        <span class="chapter-badge">${esc(page.chapter)} &middot; Chapter ${story.id} of 60</span>
        <h2 class="story-title">${esc(page.title)}</h2>
        <img src="${page.illustration}" alt="${esc(page.title)}" class="story-illustration" loading="eager" onerror="if(!this.dataset.retry){this.dataset.retry='1';this.src='assets/covers/story-${String(story.id).padStart(2,'0')}.${story.id > 40 ? 'svg' : (story.id > 25 ? 'png' : 'jpg')}';}">
        
        <div class="story-narrative">
          ${page.items.map((b, idx) => {
            if (b.type === 'subheading') return `<h3 class="subheading-title">${esc(b.text)}</h3>`;
            const isFirst = (idx === 0);
            return `<p class="story-para ${isFirst ? 'story-lead' : ''}">${esc(b.text)}</p>`;
          }).join('')}
        </div>
      </div>
    `;
  }

  if (page.type === 'story-body') {
    const spot = page.contextualImage;
    return `
      <div>
        ${spot ? `
          <figure class="story-spot-figure">
            <img src="${spot.src}" alt="${esc(spot.caption)}" class="story-spot-img" loading="lazy">
            <figcaption class="story-spot-caption">${esc(spot.caption)}</figcaption>
          </figure>
        ` : ''}
        <div class="story-narrative">
          ${page.items.map(b => {
            if (b.type === 'subheading') return `<h3 class="subheading-title">${esc(b.text)}</h3>`;
            return `<p class="story-para">${esc(b.text)}</p>`;
          }).join('')}
        </div>
      </div>
    `;
  }

  if (page.type === 'story-end') {
    const isDone = state.read.includes(story.id);
    return `
      <div>
        <div class="story-narrative">
          ${page.items.map(b => {
            if (b.type === 'subheading') return `<h3 class="subheading-title">${esc(b.text)}</h3>`;
            return `<p class="story-para">${esc(b.text)}</p>`;
          }).join('')}
        </div>

        ${page.lesson ? `
          <div class="lesson-box">
            <h4><span style="font-size:1.1rem;">&#127793;</span> Moral of the Story</h4>
            <p>"${esc(page.lesson)}"</p>
          </div>
        ` : ''}

        <div class="study-section">
          <div class="study-tabs">
            <button class="study-tab-btn active" onclick="switchBookTab(event, 'vocab-${story.id}')">Vocabulary</button>
            <button class="study-tab-btn" onclick="switchBookTab(event, 'match-${story.id}')">Match</button>
            <button class="study-tab-btn" onclick="switchBookTab(event, 'quiz-${story.id}')">Quiz</button>
          </div>

          <div id="tab-vocab-${story.id}" class="tab-panel">
            <div class="mini-words">
              ${story.newWords.map((w, i) => {
                const parts = w.split(/\s+(?:[\u2013\u2014-]|\?)\s+/, 2);
                const wordId = `${story.id}-${i}`;
                return `
                  <div class="mini-word-card ${state.words[wordId] ? 'flipped' : ''}" onclick="flipMiniWord(this, '${wordId}')">
                    <span class="mini-word-term">${esc(parts[0])}</span>
                    <span class="mini-word-def">${esc(parts[1] || '')}</span>
                  </div>
                `;
              }).join('')}
            </div>
          </div>

          <div id="tab-match-${story.id}" class="tab-panel" hidden>
            <div class="book-match-list">
              ${renderBookMatch(story)}
            </div>
          </div>

          <div id="tab-quiz-${story.id}" class="tab-panel" hidden>
            <div class="book-quiz-wrap">
              ${renderBookQuiz(story)}
            </div>
          </div>
        </div>

        <div class="finish-chapter-bar">
          <button id="btn-finish-${story.id}" class="finish-chapter-btn ${isDone ? 'completed' : ''}" onclick="completeChapter(${story.id})">
            ${isDone ? '&#10003; Chapter Completed' : 'Mark Chapter Completed &#10003;'}
          </button>
        </div>
      </div>
    `;
  }

  return '';
}

// Companion page for stories ending on an odd page
function renderStoryCompanionPage(story) {
  const isDone = state.read.includes(story.id);
  const nextStoryId = story.id < 60 ? story.id + 1 : null;
  const nextStory = nextStoryId ? storyById(nextStoryId) : null;
  const spot = getContextualScene(story.id);

  return `
    <div style="height:100%; display:flex; flex-direction:column; justify-content:space-between; padding: 10px 4px;">
      <div>
        <span class="chapter-badge">Chapter ${story.id} Reflection</span>
        <h3 style="font-size:1.25rem; color:var(--accent); margin: 6px 0 10px;">"${esc(story.title)}"</h3>
        <p style="font-style:italic; line-height:1.65; font-size:0.92rem; opacity:0.9; margin: 0 0 10px;">
          "${esc(story.lesson)}"
        </p>
      </div>

      ${spot ? `
        <figure class="companion-figure">
          <img src="${spot.src}" alt="${esc(spot.caption)}" class="companion-img" loading="lazy">
          <figcaption class="companion-caption">${esc(spot.caption)}</figcaption>
        </figure>
      ` : ''}

      <div style="text-align:center; padding: 14px; border:1px solid var(--page-border); border-radius:10px; background:color-mix(in srgb, var(--accent) 6%, var(--paper));">
        <div style="font-size:1.6rem; margin-bottom:4px;">&#127795;</div>
        ${nextStory ? `
          <small style="text-transform:uppercase; font-weight:700; color:var(--accent); letter-spacing:0.06em;">Up Next</small>
          <h4 style="margin:4px 0 10px; font-size:1.05rem;">Chapter ${nextStoryId}: ${esc(nextStory.title)}</h4>
          <button class="tool-btn" style="background:var(--accent); color:#fff; padding:6px 18px;" onclick="goToChapter(${nextStoryId})">
            Continue Reading &#10148;
          </button>
        ` : `
          <p style="font-size:0.88rem; margin:0;">You have reached the final chapter of Stories from the Baobab Tree.</p>
        `}
      </div>

      <div style="font-size:0.75rem; color:var(--ink-muted); text-align:center;">
        Stories from the Baobab Tree &middot; Traditional Zambian Reader
      </div>
    </div>
  `;
}

// --- Render Table of Contents in-Book Entries ---
function renderTOCRange(startId, endId) {
  let html = '';
  for (let id = startId; id <= endId; id++) {
    const s = storyById(id);
    if (!s) continue;
    const isDone = state.read.includes(id);
    html += `
      <div class="book-toc-item" onclick="goToChapter(${id})" title="Flip to Chapter ${id}: ${esc(s.title)}">
        <span class="book-toc-title">
          ${isDone ? '<span style="color:#2d7d6e;">&#10003;</span> ' : ''}<strong>${id}.</strong> ${esc(s.title)}
        </span>
        <span class="book-toc-pg">Ch. ${id}</span>
      </div>
    `;
  }
  return html;
}

// --- Interactive Matching & Quiz Components ---
function renderBookMatch(story) {
  const parts = story.newWords.map(w => {
    const p = w.split(/\s+(?:[\u2013\u2014-]|\?)\s+/, 2);
    return { word: p[0], meaning: p[1] || '' };
  });
  const shift = story.id % Math.max(parts.length, 1);
  const shuffled = parts.map((_, i) => i).slice(shift).concat(parts.map((_, i) => i).slice(0, shift));

  return parts.map((x, i) => {
    const id = `${story.id}-${i}`;
    const m = state.matches[id];
    const correct = m && m.correct;
    return `
      <div class="book-match-row ${correct ? 'matched' : ''}" id="book-match-${id}">
        <strong>${esc(x.word)}</strong>
        <select onchange="onBookMatchChange(${story.id}, ${i}, this.value)" ${correct ? 'disabled' : ''}>
          <option value="">Meaning...</option>
          ${shuffled.map(j => `<option value="${j}" ${m && String(m.value) === String(j) ? 'selected' : ''}>${esc(parts[j].meaning)}</option>`).join('')}
        </select>
      </div>
    `;
  }).join('');
}

function onBookMatchChange(storyId, wordIdx, val) {
  if (val === '') return;
  const id = `${storyId}-${wordIdx}`;
  const correct = Number(val) === wordIdx;
  state.matches[id] = { value: Number(val), correct };
  saveState();

  const row = document.querySelector(`#book-match-${id}`);
  if (correct) {
    playSuccessChime();
    if (row) {
      row.classList.add('matched');
      const sel = row.querySelector('select');
      if (sel) sel.disabled = true;
    }
  }
}

function renderBookQuiz(story) {
  if (state.quiz[story.id]) {
    return `<div style="color:#2d7d6e; font-weight:700;">&#10003; Knowledge check passed!</div>`;
  }
  const pool = S.filter(x => x.id !== story.id).map(x => x.lesson).filter(Boolean);
  const opts = [story.lesson];
  for (let i = 0; opts.length < 3 && i < pool.length; i++) {
    const c = pool[(story.id * 3 + i * 5) % pool.length];
    if (!opts.includes(c)) opts.push(c);
  }
  opts.sort();

  return `
    <div id="quiz-block-${story.id}">
      <p style="margin:0 0 6px; font-weight:700;">Which is the true lesson?</p>
      ${opts.map(o => `
        <label class="book-quiz-opt">
          <input type="radio" name="bq-${story.id}" value="${esc(o)}"> <span>${esc(o)}</span>
        </label>
      `).join('')}
      <button class="book-quiz-btn" onclick="checkBookQuiz(${story.id})">Check Answer</button>
      <span id="quiz-feed-${story.id}" style="margin-left:8px; font-weight:700; font-size:0.8rem;"></span>
    </div>
  `;
}

function checkBookQuiz(storyId) {
  const story = storyById(storyId);
  const picked = document.querySelector(`input[name="bq-${storyId}"]:checked`);
  const feed = document.querySelector(`#quiz-feed-${storyId}`);
  if (!picked) {
    if (feed) feed.textContent = 'Pick an option.';
    return;
  }
  if (picked.value === story.lesson) {
    playSuccessChime();
    state.quiz[storyId] = true;
    saveState();
    const block = document.querySelector(`#quiz-block-${storyId}`);
    if (block) {
      block.innerHTML = '<div style="color:#2d7d6e; font-weight:700;">&#10003; Correct! Knowledge check passed</div>';
    }
  } else {
    if (feed) {
      feed.style.color = 'var(--accent)';
      feed.textContent = 'Not quite, try again.';
    }
  }
}

function switchBookTab(evt, tabKey) {
  const parent = evt.target.closest('.study-section');
  if (!parent) return;
  parent.querySelectorAll('.study-tab-btn').forEach(b => b.classList.remove('active'));
  evt.target.classList.add('active');
  parent.querySelectorAll('.tab-panel').forEach(p => p.hidden = true);
  const target = parent.querySelector(`#tab-${tabKey}`);
  if (target) target.hidden = false;
}

function flipMiniWord(el, id) {
  playPaperSound();
  el.classList.toggle('flipped');
  if (!state.words[id]) {
    state.words[id] = true;
    saveState();
  }
}

function completeChapter(storyId) {
  playSuccessChime();
  if (!state.read.includes(storyId)) {
    state.read.push(storyId);
  }
  const btn = document.querySelector(`#btn-finish-${storyId}`);
  if (btn) {
    btn.classList.add('completed');
    btn.innerHTML = '&#10003; Chapter Completed';
  }
  saveState();
  setTimeout(() => flipNext(), 400);
}

// --- Render Current Spread ---
function renderSpread(spreadIdx) {
  if (spreadIdx < 0) spreadIdx = 0;
  if (spreadIdx >= ALL_SPREADS.length) spreadIdx = ALL_SPREADS.length - 1;

  const data = ALL_SPREADS[spreadIdx];
  if (!data) return;

  leftContent.innerHTML = data.leftHtml;
  rightContent.innerHTML = data.rightHtml;

  // Clean page numbers — NEVER [object HTMLSpanElement]
  leftPageNumEl.textContent = String(data.leftNum || '');
  rightPageNumEl.textContent = String(data.rightNum || '');

  runningChapter.textContent = data.chapterRunning;
  chapterTitleEl.textContent = data.title;

  leftContent.scrollTop = 0;
  rightContent.scrollTop = 0;

  updateIndicators();
}

function updateIndicators() {
  pageScrubber.max = ALL_SPREADS.length - 1;
  pageScrubber.value = currentSpread;

  const chId = SPREAD_CHAPTER_MAP[currentSpread];
  if (currentSpread === 0) {
    spreadIndicator.textContent = 'Cover';
  } else if (currentSpread <= 4) {
    spreadIndicator.textContent = 'Front Matter';
  } else if (chId) {
    spreadIndicator.textContent = `Chapter ${chId} of 60`;
  } else {
    spreadIndicator.textContent = 'Back Matter';
  }

  const pct = Math.round((state.read.length / S.length) * 100) || 0;
  progressIndicator.textContent = `${pct}% completed (${state.read.length}/${S.length} stories)`;
}

// --- 3D Flipping Animation Engine ---
function flipNext() {
  if (isFlipping || currentSpread >= ALL_SPREADS.length - 1) return;
  stopReadAloud();
  isFlipping = true;
  playPaperSound();

  const nextSpread = currentSpread + 1;
  const currentData = ALL_SPREADS[currentSpread];
  const nextData = ALL_SPREADS[nextSpread];

  flippingLeaf.innerHTML = `
    <div class="leaf-face leaf-front">
      <div class="page-running-head"><span class="running-right">${esc(currentData.chapterRunning)}</span></div>
      <div class="page-content">${currentData.rightHtml}</div>
      <div class="page-footer" style="justify-content:flex-end;"><span>${esc(currentData.rightNum)}</span></div>
    </div>
    <div class="leaf-face leaf-back">
      <div class="page-running-head"><span class="running-left">Stories from the Baobab Tree</span></div>
      <div class="page-content">${nextData.leftHtml}</div>
      <div class="page-footer" style="justify-content:flex-start;"><span>${esc(nextData.leftNum)}</span></div>
    </div>
  `;

  flippingLeaf.className = 'flipping-leaf flip-forward';

  setTimeout(() => {
    currentSpread = nextSpread;
    renderSpread(currentSpread);
    updateURL();
  }, 260);

  setTimeout(() => {
    flippingLeaf.className = 'flipping-leaf';
    flippingLeaf.innerHTML = '';
    isFlipping = false;
  }, 530);
}

function flipPrev() {
  if (isFlipping || currentSpread <= 0) return;
  stopReadAloud();
  isFlipping = true;
  playPaperSound();

  const prevSpread = currentSpread - 1;
  const currentData = ALL_SPREADS[currentSpread];
  const prevData = ALL_SPREADS[prevSpread];

  flippingLeaf.innerHTML = `
    <div class="leaf-face leaf-front">
      <div class="page-running-head"><span class="running-left">Stories from the Baobab Tree</span></div>
      <div class="page-content">${currentData.leftHtml}</div>
      <div class="page-footer" style="justify-content:flex-start;"><span>${esc(currentData.leftNum)}</span></div>
    </div>
    <div class="leaf-face leaf-back">
      <div class="page-running-head"><span class="running-right">${esc(prevData.chapterRunning)}</span></div>
      <div class="page-content">${prevData.rightHtml}</div>
      <div class="page-footer" style="justify-content:flex-end;"><span>${esc(prevData.rightNum)}</span></div>
    </div>
  `;

  flippingLeaf.className = 'flipping-leaf flip-backward';

  setTimeout(() => {
    currentSpread = prevSpread;
    renderSpread(currentSpread);
    updateURL();
  }, 260);

  setTimeout(() => {
    flippingLeaf.className = 'flipping-leaf';
    flippingLeaf.innerHTML = '';
    isFlipping = false;
  }, 530);
}

function goToSpread(targetSpread) {
  if (targetSpread < 0 || targetSpread >= ALL_SPREADS.length || targetSpread === currentSpread) return;
  stopReadAloud();
  playPaperSound();
  currentSpread = targetSpread;
  renderSpread(currentSpread);
  updateURL();
}

function goToChapter(storyId) {
  closeBookTOC();
  const targetSpread = CHAPTER_SPREAD_MAP[storyId];
  if (targetSpread !== undefined) {
    goToSpread(targetSpread);
  }
}

function onScrubberInput(val) {
  const target = parseInt(val, 10);
  if (!isNaN(target) && target !== currentSpread) {
    goToSpread(target);
  }
}

// --- URL & Hash Routing ---
function updateURL() {
  const chId = SPREAD_CHAPTER_MAP[currentSpread];
  if (chId) {
    location.hash = `#chapter-${chId}`;
  } else if (currentSpread === 0) {
    location.hash = '#cover';
  } else if (currentSpread <= 4) {
    location.hash = '#toc';
  } else {
    location.hash = '#back';
  }
}

function handleHash() {
  const hash = location.hash.replace(/^#/, '');
  if (hash.startsWith('chapter-')) {
    const ch = parseInt(hash.replace('chapter-', ''), 10);
    if (CHAPTER_SPREAD_MAP[ch] !== undefined) {
      currentSpread = CHAPTER_SPREAD_MAP[ch];
      renderSpread(currentSpread);
      return;
    }
  }
  if (hash === 'toc') {
    currentSpread = 3;
    renderSpread(currentSpread);
    return;
  }
  currentSpread = 0;
  renderSpread(currentSpread);
}
window.addEventListener('hashchange', handleHash);

// --- Keyboard Navigation ---
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
  if (e.key === 'Escape') {
    closeBookTOC();
    return;
  }
  if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {
    e.preventDefault();
    flipNext();
  } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
    e.preventDefault();
    flipPrev();
  } else if (e.key === 'Home') {
    e.preventDefault();
    goToSpread(0);
  } else if (e.key === 'End') {
    e.preventDefault();
    goToSpread(ALL_SPREADS.length - 1);
  }
});

// --- Table of Contents Modal & Working 'X' Close ---
function openBookTOC() {
  playPaperSound();
  const modal = document.querySelector('#toc-modal');
  const overlay = document.querySelector('#toc-overlay');
  if (modal && overlay) {
    modal.classList.add('open');
    overlay.classList.add('open');
    modal.removeAttribute('hidden');
    overlay.removeAttribute('hidden');
    renderTOCModalList();
    const search = document.querySelector('#toc-search-box');
    if (search) {
      search.value = '';
      setTimeout(() => search.focus(), 120);
    }
  }
}

function closeBookTOC() {
  const modal = document.querySelector('#toc-modal');
  const overlay = document.querySelector('#toc-overlay');
  if (modal) {
    modal.classList.remove('open');
    modal.setAttribute('hidden', '');
  }
  if (overlay) {
    overlay.classList.remove('open');
    overlay.setAttribute('hidden', '');
  }
}

function renderTOCModalList(filter = '') {
  const listEl = document.querySelector('#toc-chapter-list');
  if (!listEl) return;
  const q = filter.trim().toLowerCase();
  let html = `
    <div class="toc-modal-row ${currentSpread === 0 ? 'current' : ''}" onclick="goToSpread(0); closeBookTOC();">
      <span class="toc-modal-row-num">&#128217;</span>
      <span class="toc-modal-row-title"><strong>Front Cover</strong></span>
    </div>
    <div class="toc-modal-row ${currentSpread >= 1 && currentSpread <= 4 ? 'current' : ''}" onclick="goToSpread(3); closeBookTOC();">
      <span class="toc-modal-row-num">&#128214;</span>
      <span class="toc-modal-row-title"><strong>Table of Contents & Dedication</strong></span>
    </div>
  `;

  CATEGORIES.forEach(cat => {
    const matched = cat.ids.map(storyById).filter(Boolean).filter(s => {
      if (!q) return true;
      return s.title.toLowerCase().includes(q) || s.chapter.toLowerCase().includes(q) || s.lesson.toLowerCase().includes(q);
    });

    if (matched.length) {
      html += `
        <div class="toc-cat-group">
          <div class="toc-cat-header">${esc(cat.title)} (${matched.length})</div>
          ${matched.map(s => {
            const spread = CHAPTER_SPREAD_MAP[s.id] || 0;
            const isCurrent = currentSpread === spread;
            const isDone = state.read.includes(s.id);
            return `
              <div class="toc-modal-row ${isCurrent ? 'current' : ''}" onclick="goToChapter(${s.id});" title="Open Chapter ${s.id}: ${esc(s.title)}">
                <span class="toc-modal-row-num">${s.id}</span>
                <span class="toc-modal-row-title">${esc(s.title)}</span>
                ${isDone ? '<span class="toc-modal-row-done">&#10003;</span>' : ''}
              </div>
            `;
          }).join('')}
        </div>
      `;
    }
  });

  listEl.innerHTML = html;
}

function onTOCSearch(val) {
  renderTOCModalList(val);
}

// --- Text-to-Speech (Read Aloud) ---
function stopReadAloud() {
  if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isReadingAloud = false;
  currentParaIndex = -1;
  if (ttsLabel) ttsLabel.textContent = 'Read';
  if (ttsIcon) ttsIcon.innerHTML = '&#128266;';
  if (ttsBtn) ttsBtn.classList.remove('active');
  document.querySelectorAll('.speaking-active').forEach(el => el.classList.remove('speaking-active'));
}

function toggleReadAloud() {
  if (!('speechSynthesis' in window)) {
    alert('Voice narration is not supported on this browser.');
    return;
  }
  if (isReadingAloud) {
    stopReadAloud();
    return;
  }

  const paras = Array.from(document.querySelectorAll('.story-para'));
  if (!paras.length) {
    alert('No story text on this page to read aloud.');
    return;
  }
  readableParas = paras;
  isReadingAloud = true;
  if (ttsLabel) ttsLabel.textContent = 'Stop';
  if (ttsIcon) ttsIcon.innerHTML = '&#9209;';
  if (ttsBtn) ttsBtn.classList.add('active');
  readNextBookPara(0);
}

function readNextBookPara(index) {
  if (!isReadingAloud || index >= readableParas.length) {
    stopReadAloud();
    return;
  }
  currentParaIndex = index;
  document.querySelectorAll('.speaking-active').forEach(el => el.classList.remove('speaking-active'));
  const para = readableParas[index];
  para.classList.add('speaking-active');
  para.scrollIntoView({ behavior: 'smooth', block: 'center' });

  const u = new SpeechSynthesisUtterance(para.textContent);
  u.rate = 0.94;
  u.onend = () => {
    if (isReadingAloud) {
      setTimeout(() => readNextBookPara(index + 1), 300);
    }
  };
  u.onerror = () => stopReadAloud();
  window.speechSynthesis.speak(u);
}

// --- Appearance & Theme Controls ---
function setBookTheme(theme) {
  document.body.classList.remove('theme-paper', 'theme-sepia', 'theme-night');
  document.body.classList.add(`theme-${theme}`);
  state.theme = theme;
  saveState();
  document.querySelectorAll('.theme-swatch').forEach(s => {
    s.classList.toggle('active', s.classList.contains(`${theme}-swatch`));
  });
}

function setBookFontSize(size) {
  document.body.classList.remove('font-sm', 'font-md', 'font-lg', 'font-xl');
  document.body.classList.add(`font-${size}`);
  state.fontSize = size;
  saveState();
  document.querySelectorAll('.size-btn').forEach(b => {
    b.classList.toggle('active', b.textContent.toLowerCase() === (size === 'sm' ? 'a-' : size === 'md' ? 'a' : size === 'lg' ? 'a+' : 'a++'));
  });
}

function toggleAppearanceMenu(e) {
  e.stopPropagation();
  const menu = document.querySelector('#appearance-menu');
  if (menu) {
    menu.hidden = !menu.hidden;
  }
}

document.addEventListener('click', (e) => {
  const menu = document.querySelector('#appearance-menu');
  const btn = document.querySelector('#btn-appearance');
  if (menu && !menu.hidden && !menu.contains(e.target) && !btn.contains(e.target)) {
    menu.hidden = true;
  }
});

// --- Initialization ---
setBookTheme(state.theme || 'paper');
setBookFontSize(state.fontSize || 'md');
const soundBtn = document.querySelector('#btn-sound-toggle');
if (soundBtn) soundBtn.innerHTML = state.sound ? '&#128266; Page Flip Sound: On' : '&#128263; Page Flip Sound: Off';

// Build the multi-page spreads and load route
buildAllSpreads();
handleHash();

if (location.protocol !== 'file:' && 'serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js').then(r => r.update()).catch(() => {});
}