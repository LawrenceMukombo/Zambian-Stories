#!/usr/bin/env python3
"""
EPUB 3.0 and Reader Builder for 'Legends of the Zambezi: Spirits, Giants & Sacred Waters'
Produces:
1. outputs/Legends-of-the-Zambezi.epub (Valid IDPF EPUB 3.0 for Apple Books & e-readers)
2. Interactive 3D Web Flipbook files in outputs/zambezi-reader/
"""

import json
import zipfile
from datetime import datetime
from pathlib import Path

ROOT = Path(r"c:\folk_tale_stories")
WORK_EPUB = ROOT / "work" / "epub-zambezi"
OUTPUTS = ROOT / "outputs"
READER = OUTPUTS / "zambezi-reader"

# Ensure dirs
(WORK_EPUB / "META-INF").mkdir(parents=True, exist_ok=True)
(WORK_EPUB / "OEBPS" / "text").mkdir(parents=True, exist_ok=True)
(WORK_EPUB / "OEBPS" / "images").mkdir(parents=True, exist_ok=True)
(WORK_EPUB / "OEBPS" / "styles").mkdir(parents=True, exist_ok=True)

# Load stories
with open(READER / "stories.json", "r", encoding="utf-8") as f:
    STORIES = json.load(f)

# 1. mimetype (must have no trailing whitespace or newline)
with open(WORK_EPUB / "mimetype", "wb") as f:
    f.write(b"application/epub+zip")

# 2. container.xml
container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""
with open(WORK_EPUB / "META-INF" / "container.xml", "w", encoding="utf-8") as f:
    f.write(container_xml)

# 3. EPUB CSS Styles
epub_css = """
@charset "UTF-8";
@namespace epub "http://www.idpf.org/2007/ops";

body {
    font-family: "Georgia", "Palatino", serif;
    font-size: 1.1em;
    line-height: 1.65;
    color: #2b2118;
    background-color: #faf7f2;
    margin: 5% 8%;
    padding: 0;
}

h1, h2, h3 {
    font-family: "Georgia", serif;
    color: #4a2c11;
    text-align: center;
    font-weight: normal;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h1.book-title {
    font-size: 2.2em;
    font-weight: bold;
    color: #8c4a16;
    margin-top: 1em;
    letter-spacing: 0.05em;
}

h2.chapter-title {
    font-size: 1.8em;
    color: #8c4a16;
    margin-top: 0.5em;
    margin-bottom: 0.2em;
}

p.chapter-badge {
    text-align: center;
    font-size: 0.9em;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #b3591b;
    font-weight: bold;
    margin-bottom: 0.3em;
}

p.chapter-subtitle {
    text-align: center;
    font-style: italic;
    color: #6d5b4e;
    margin-bottom: 1.5em;
}

p.region-tag {
    text-align: center;
    font-size: 0.85em;
    color: #8c786a;
    margin-bottom: 2em;
}

p.first-p::first-letter {
    font-size: 3.2em;
    line-height: 0.85;
    float: left;
    margin: 0.05em 0.15em 0 0;
    color: #b3591b;
    font-weight: bold;
    font-family: "Georgia", serif;
}

p {
    text-indent: 1.2em;
    margin-top: 0;
    margin-bottom: 0.8em;
    text-align: justify;
}

p.first-p {
    text-indent: 0;
}

.illustration-box {
    text-align: center;
    margin: 2em auto;
    max-width: 95%;
}

.illustration-box img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    border: 1px solid #d4c2b2;
}

.caption {
    font-size: 0.88em;
    font-style: italic;
    color: #5c4b3f;
    margin-top: 0.6em;
    text-align: center;
}

.moral-box {
    margin: 2em 0;
    padding: 1.2em 1.5em;
    background: #f3eae0;
    border-left: 4px solid #b3591b;
    border-radius: 4px;
}

.moral-box h4 {
    margin: 0 0 0.5em 0;
    color: #8c4a16;
    font-size: 1em;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.moral-box p {
    text-indent: 0;
    margin: 0;
    font-style: italic;
}

.vocab-box {
    margin: 2em 0;
    padding: 1.2em 1.5em;
    background: #fdfaf6;
    border: 1px solid #e0d0c0;
    border-radius: 6px;
}

.vocab-box h4 {
    margin: 0 0 0.8em 0;
    color: #8c4a16;
    font-size: 1.05em;
}

.vocab-item {
    margin-bottom: 0.8em;
}

.vocab-word {
    font-weight: bold;
    color: #3d2410;
}

.quiz-box {
    margin: 2em 0;
    padding: 1.2em 1.5em;
    background: #f7f3ee;
    border-top: 2px dashed #c4b09e;
    border-bottom: 2px dashed #c4b09e;
}

.quiz-box h4 {
    margin: 0 0 1em 0;
    color: #8c4a16;
}

.question-item {
    margin-bottom: 1.2em;
}

.question-title {
    font-weight: bold;
    margin-bottom: 0.4em;
    text-indent: 0;
}

.option-list {
    margin: 0.3em 0 0.5em 1.5em;
    padding: 0;
    list-style-type: lower-alpha;
}

.option-list li {
    margin-bottom: 0.3em;
}

.explanation {
    font-size: 0.9em;
    color: #59473b;
    font-style: italic;
    text-indent: 0;
}
"""

with open(WORK_EPUB / "OEBPS" / "styles" / "style.css", "w", encoding="utf-8") as f:
    f.write(epub_css.strip())

# 4. Generate Chapter XHTML pages
chapter_manifest = []
chapter_spine = []

# Title Page
title_xhtml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Legends of the Zambezi</title>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body style="text-align: center; padding-top: 15%;">
  <p class="chapter-badge">Zambian Oral Heritage &amp; Folklore</p>
  <h1 class="book-title">LEGENDS OF THE ZAMBEZI</h1>
  <p style="font-size: 1.3em; color: #6d5b4e; font-style: italic; margin-top: 0.5em;">Spirits, Giants &amp; Sacred Waters</p>
  <div style="margin: 3em auto; width: 60px; height: 2px; background: #b3591b;"></div>
  <p style="font-size: 1.1em; color: #3d2410;">Illustrated with Authentic Hand-Drawn Watercolors</p>
  <p style="font-size: 0.95em; color: #8c786a; margin-top: 3em;">Traditional Tales of the BaTonga, Leya, Chishinga, Aushi &amp; Kunda Traditions</p>
</body>
</html>"""
with open(WORK_EPUB / "OEBPS" / "text" / "title.xhtml", "w", encoding="utf-8") as f:
    f.write(title_xhtml)

# Cover page
cover_xhtml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Cover</title>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
  <style>
    @page { margin: 0; }
    body { margin: 0; padding: 0; text-align: center; background-color: #14110f; }
    img { max-width: 100%; height: 100vh; object-fit: contain; }
  </style>
</head>
<body>
  <div style="height: 100vh; display: flex; align-items: center; justify-content: center;">
    <img src="../images/cover.jpg" alt="Legends of the Zambezi Front Cover" />
  </div>
</body>
</html>"""
with open(WORK_EPUB / "OEBPS" / "text" / "cover.xhtml", "w", encoding="utf-8") as f:
    f.write(cover_xhtml)

# Write each chapter
for s in STORIES:
    cid = f"chapter-{s['id']:02d}"
    img_name = f"chapter-{s['id']:02d}.jpg"
    
    # Body paragraphs
    p_htmls = []
    for idx, p in enumerate(s["paragraphs"]):
        cls = ' class="first-p"' if idx == 0 else ''
        p_htmls.append(f"    <p{cls}>{p}</p>")
    body_html = "\n".join(p_htmls)
    
    # Vocab
    vocab_htmls = []
    for v in s["vocabulary"]:
        vocab_htmls.append(f"""      <div class="vocab-item">
        <span class="vocab-word">{v['word']}</span>: {v['definition']}
      </div>""")
    vocab_section = "\n".join(vocab_htmls)
    
    # Questions
    q_htmls = []
    for qidx, q in enumerate(s["questions"], 1):
        opts = "".join([f"<li>{opt}</li>" for opt in q["options"]])
        q_htmls.append(f"""      <div class="question-item">
        <p class="question-title">{qidx}. {q['question']}</p>
        <ol class="option-list">
          {opts}
        </ol>
        <p class="explanation"><strong>Answer ({chr(97 + q['answer'])}):</strong> {q['explanation']}</p>
      </div>""")
    quiz_section = "\n".join(q_htmls)
    
    ch_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>{s['title']}</title>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body>
  <section epub:type="chapter" role="doc-chapter">
    <p class="chapter-badge">{s['chapterBadge']}</p>
    <h2 class="chapter-title">{s['title']}</h2>
    <p class="chapter-subtitle">{s['subtitle']}</p>
    <p class="region-tag">📍 {s['region']}</p>
    
    <div class="illustration-box">
      <img src="../images/{img_name}" alt="{s['title']}" />
      <p class="caption">{s['illustrationCaption']}</p>
    </div>
    
{body_html}
    
    <div class="moral-box">
      <h4>Ancestral Moral Lesson</h4>
      <p>“{s['moral']}”</p>
    </div>
    
    <div class="vocab-box">
      <h4>📖 Cultural Vocabulary</h4>
{vocab_section}
    </div>
    
    <div class="quiz-box">
      <h4>❓ Wonder &amp; Comprehension Questions</h4>
{quiz_section}
    </div>
  </section>
</body>
</html>"""
    with open(WORK_EPUB / "OEBPS" / "text" / f"{cid}.xhtml", "w", encoding="utf-8") as f:
        f.write(ch_content)

# Colophon / Credits
colophon_xhtml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Colophon &amp; Cultural Heritage Acknowledgments</title>
  <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body style="padding-top: 10%;">
  <h2 style="color: #8c4a16; text-align: center;">Heritage &amp; Cultural Acknowledgments</h2>
  <div style="margin: 2em auto; width: 50px; height: 2px; background: #b3591b;"></div>
  
  <p class="first-p">This collection draws reverent inspiration from the oral traditions of the BaTonga, Toka-Leya, Aushi, Chishinga, and Kunda peoples of Zambia. For centuries, these legends were passed through firelight storytelling (<em>Insaka</em>), teaching children that human life is intimately woven with sacred rivers, towering trees, and celestial wonders.</p>
  
  <p>The illustrations in this edition are crafted in an authentic hand-drawn storybook style, combining textured pencil linework with organic watercolor washes that celebrate the warmth and beauty of the Zambian landscape.</p>
  
  <div style="margin-top: 3em; text-align: center; font-size: 0.9em; color: #8c786a;">
    <p>Published in the Republic of Zambia</p>
    <p>First Edition • 2026</p>
    <p>Preserving African Heritage for Future Generations</p>
  </div>
</body>
</html>"""
with open(WORK_EPUB / "OEBPS" / "text" / "colophon.xhtml", "w", encoding="utf-8") as f:
    f.write(colophon_xhtml)

# 5. nav.xhtml (EPUB 3 Table of Contents)
nav_links = []
for s in STORIES:
    cid = f"chapter-{s['id']:02d}"
    nav_links.append(f'        <li><a href="text/{cid}.xhtml">{s["title"]}</a></li>')
nav_links_str = "\n".join(nav_links)

nav_xhtml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="en">
<head>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="styles/style.css"/>
</head>
<body>
  <nav epub:type="toc" id="toc" role="doc-toc">
    <h2>Table of Contents</h2>
    <ol>
      <li><a href="text/cover.xhtml">Cover</a></li>
      <li><a href="text/title.xhtml">Title Page</a></li>
{nav_links_str}
      <li><a href="text/colophon.xhtml">Cultural Acknowledgments</a></li>
    </ol>
  </nav>
</body>
</html>"""
with open(WORK_EPUB / "OEBPS" / "nav.xhtml", "w", encoding="utf-8") as f:
    f.write(nav_xhtml)

# 6. toc.ncx (EPUB 2 compatibility)
navpoints = []
play_order = 1
navpoints.append(f"""    <navPoint id="navPoint-{play_order}" playOrder="{play_order}">
      <navLabel><text>Cover</text></navLabel>
      <content src="text/cover.xhtml"/>
    </navPoint>""")
play_order += 1

navpoints.append(f"""    <navPoint id="navPoint-{play_order}" playOrder="{play_order}">
      <navLabel><text>Title Page</text></navLabel>
      <content src="text/title.xhtml"/>
    </navPoint>""")
play_order += 1

for s in STORIES:
    cid = f"chapter-{s['id']:02d}"
    navpoints.append(f"""    <navPoint id="navPoint-{play_order}" playOrder="{play_order}">
      <navLabel><text>{s['title']}</text></navLabel>
      <content src="text/{cid}.xhtml"/>
    </navPoint>""")
    play_order += 1

navpoints.append(f"""    <navPoint id="navPoint-{play_order}" playOrder="{play_order}">
      <navLabel><text>Cultural Acknowledgments</text></navLabel>
      <content src="text/colophon.xhtml"/>
    </navPoint>""")

toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:zambezi-legends-2026-edition"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>Legends of the Zambezi: Spirits, Giants &amp; Sacred Waters</text>
  </docTitle>
  <navMap>
{chr(10).join(navpoints)}
  </navMap>
</ncx>"""
with open(WORK_EPUB / "OEBPS" / "toc.ncx", "w", encoding="utf-8") as f:
    f.write(toc_ncx)

# 7. package.opf
manifest_items = [
    '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
    '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
    '<item id="style" href="styles/style.css" media-type="text/css"/>',
    '<item id="cover-img" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>',
    '<item id="cover-page" href="text/cover.xhtml" media-type="application/xhtml+xml"/>',
    '<item id="title-page" href="text/title.xhtml" media-type="application/xhtml+xml"/>',
]

spine_items = [
    '<itemref idref="cover-page"/>',
    '<itemref idref="title-page"/>',
]

for s in STORIES:
    cid = f"chapter-{s['id']:02d}"
    img_name = f"chapter-{s['id']:02d}.jpg"
    manifest_items.append(f'<item id="{cid}" href="text/{cid}.xhtml" media-type="application/xhtml+xml"/>')
    manifest_items.append(f'<item id="img-{cid}" href="images/{img_name}" media-type="image/jpeg"/>')
    spine_items.append(f'<itemref idref="{cid}"/>')

manifest_items.append('<item id="colophon" href="text/colophon.xhtml" media-type="application/xhtml+xml"/>')
spine_items.append('<itemref idref="colophon"/>')

manifest_str = "\n    ".join(manifest_items)
spine_str = "\n    ".join(spine_items)
now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

package_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="pub-id" version="3.0" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">urn:uuid:zambezi-legends-2026-edition</dc:identifier>
    <dc:title id="title">Legends of the Zambezi: Spirits, Giants &amp; Sacred Waters</dc:title>
    <dc:language>en</dc:language>
    <dc:creator id="creator">Lawrence Mukombo</dc:creator>
    <dc:publisher>Baobab Heritage Press</dc:publisher>
    <dc:date>{datetime.utcnow().strftime('%Y-%m-%d')}</dc:date>
    <dc:description>An illustrated storybook exploring the sacred folklore and river spirits of Zambia, featuring authentic hand-drawn illustrations and educational comprehension guides.</dc:description>
    <meta property="dcterms:modified">{now_iso}</meta>
    <meta name="cover" content="cover-img"/>
  </metadata>
  <manifest>
    {manifest_str}
  </manifest>
  <spine toc="ncx">
    {spine_str}
  </spine>
  <guide>
    <reference type="cover" title="Cover" href="text/cover.xhtml"/>
    <reference type="toc" title="Table of Contents" href="nav.xhtml"/>
  </guide>
</package>"""

with open(WORK_EPUB / "OEBPS" / "package.opf", "w", encoding="utf-8") as f:
    f.write(package_opf)

print("[SUCCESS] Generated all EPUB 3.0 files in work/epub-zambezi")

# 8. Package EPUB into outputs/Legends-of-the-Zambezi.epub
out_epub_file = OUTPUTS / "Legends-of-the-Zambezi.epub"
with zipfile.ZipFile(out_epub_file, "w") as zf:
    # 1. mimetype (must be uncompressed first entry)
    zf.write(WORK_EPUB / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
    # 2. rest of files
    for p in sorted(WORK_EPUB.rglob("*")):
        if p.is_file() and p.name != "mimetype":
            rel = p.relative_to(WORK_EPUB).as_posix()
            zf.write(p, rel, compress_type=zipfile.ZIP_DEFLATED)

file_mb = out_epub_file.stat().st_size / (1024 * 1024)
print(f"[SUCCESS] Packaged EPUB: {out_epub_file.name} ({file_mb:.2f} MB)")
