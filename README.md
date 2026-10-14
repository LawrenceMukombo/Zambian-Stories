# Zambian Stories - Stories from the Baobab Tree

An interactive, offline-first digital reader and Android application celebrating traditional Zambian and Central African folk tales, featuring Kalulu the clever hare and beloved folklore legends.

## Highlights

- **Interactive 3D Flipbook Reader**: Traditional two-page EPUB-style book presentation with realistic page flip animation, hardcover styling, spine shadow, and ribbon bookmark.
- **Dynamic Story Pagination**: Automatically paginates long folk tales into readable, comfortable 3–5 paragraph spreads so stories never overflow or scroll awkwardly.
- **Full Illustrated Cover Suite**: Tailored vector illustrations (SVGs) for all 60 stories, including the complete Lansdown Animal Collection (Chapters 41–60).
- **Interactive Reading Features**:
  - Chapter navigation & Table of Contents modal with instant chapter jumping.
  - Interactive vocabulary badges, word matching, and comprehension quizzes.
  - Text-to-speech audio narration with progress indicator.
  - Dark/Light reading mode and font scaling.
  - Reading progress tracking and chapter completion markers.
- **PWA & Offline Capable**: Built with Service Worker caching (`baobab-reader-v17`) for completely offline classroom or remote reading.
- **Cross-Platform Android App**: Native Android wrapper inside `outputs/kalulu-android/`.

## Project Structure

```
folk_tale_stories/
├── outputs/
│   ├── kalulu-reader/          # Interactive Web & PWA Flipbook Reader
│   │   ├── index.html          # 3D Flipbook book shell & reader UI
│   │   ├── style.css           # Book styling, flip keyframes & typography
│   │   ├── app.js              # Reader state machine, pagination & interactive widgets
│   │   ├── sw.js               # Service Worker for offline PWA functionality
│   │   ├── assets/             # Cover illustrations (story-01 to story-60) & icons
│   │   └── data/               # Story manifest, full text & comprehension quizzes
│   └── kalulu-android/         # Android application project (Cordova/Capacitor/WebView)
│       └── www/                # Mirrored web assets for Android distribution
└── work/                       # Data processing, illustration scripts & toolchain
    └── create_illustrations.py # Vector illustration generator for Lansdown stories
```

## Running the Reader Locally

To run the web reader locally:

```bash
cd outputs/kalulu-reader
# Using Python
python -m http.server 8085 --bind 127.0.0.1
```

Then visit `http://127.0.0.1:8085` in your web browser.

## Validation & Preflight

To validate story integrity, unique IDs, and cover art mappings across all 60 chapters:

```bash
cd outputs/kalulu-reader
node scripts/preflight.js
```

## License & Heritage

Preserving and celebrating African oral tradition and indigenous folklore for young readers worldwide.
