# Stories from the Baobab Tree

This project has two deliberately separate modes:

- The local reader contains all 60 stories for private review and testing.
- The Amazon build contains only the ten stories explicitly identified as original (IDs 16-25).

Stories 26-60 state that permission is not recorded. Stories 1-15 need a completed provenance review. Do not upload those sections commercially until the rights file is complete.

## Test locally

1. Run `npm run preview`.
2. Open `http://localhost:8080`.
3. Run `npm test` for content and asset checks.

## Build Amazon files

Run `npm run build`. Outputs are written to `dist/`:

- `stories-from-the-baobab-tree-original.epub` for Kindle eBook review.
- `stories-from-the-baobab-tree-original-6x9.pdf` for a 6 x 9 inch, no-bleed paperback interior.
- `publication-preflight.json` records scope, dimensions, page count, and remaining manual checks.

Always inspect the EPUB in Kindle Previewer and the PDF in KDP Print Previewer. The paperback wraparound cover must be made after the final page count and paper/ink choices are fixed.

## Build the complete 60-story edition

Run `npm run build:full`. This produces `complete` EPUB and PDF files containing every Kalulu story and every other collection. The complete edition remains subject to the permissions warning recorded in its preflight report.
