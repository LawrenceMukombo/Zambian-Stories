import html
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image as PILImage
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch as INCH
from reportlab.platypus import (Image, PageBreak, Paragraph, SimpleDocTemplate,
                               Spacer)
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
DIST = ROOT / 'dist'
EPUB_STAGE = BUILD / 'epub'
BOOK = json.loads((BUILD / 'book.json').read_text(encoding='utf-8'))
FULL_EDITION = '--full' in sys.argv
STORIES = BOOK['stories'] if FULL_EDITION else [s for s in BOOK['stories'] if 16 <= s['id'] <= 25]
SLUG = 'complete' if FULL_EDITION else 'original'


def image_extension(story_id):
    return 'jpg' if story_id <= 25 else 'png' if story_id <= 40 else 'svg'


def clean_text(value):
    return re.sub(r'<[^>]+>', '', html.unescape(value or '')).strip()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


def build_epub():
    if EPUB_STAGE.exists():
        shutil.rmtree(EPUB_STAGE)
    oebps = EPUB_STAGE / 'OEBPS'
    meta = EPUB_STAGE / 'META-INF'
    (oebps / 'text').mkdir(parents=True)
    (oebps / 'images').mkdir(parents=True)
    meta.mkdir(parents=True)
    write(EPUB_STAGE / 'mimetype', 'application/epub+zip')
    write(meta / 'container.xml', '<?xml version="1.0"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
    css = '''body{font-family:serif;line-height:1.55;margin:5%}h1,h2{text-align:center;color:#183934}img{display:block;max-width:90%;max-height:55vh;margin:1em auto}.chapter{page-break-before:always}.lesson{background:#f4ead0;padding:1em;border-radius:.4em}.source{font-size:.85em;color:#555}nav ol{line-height:1.8}'''
    write(oebps / 'style.css', css)
    nav_items = []
    front_ids = ['copyright', 'dedication', 'toc', 'acknowledgements']
    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>', '<item id="css" href="style.css" media-type="text/css"/>', '<item id="title" href="text/title.xhtml" media-type="application/xhtml+xml"/>'] + [f'<item id="{x}" href="text/{x}.xhtml" media-type="application/xhtml+xml"/>' for x in front_ids] + ['<item id="author" href="text/author.xhtml" media-type="application/xhtml+xml"/>']
    spine = ['<itemref idref="title"/>'] + [f'<itemref idref="{x}"/>' for x in front_ids]
    title = f'''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>{escape(BOOK['title'])}</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>{escape(BOOK['title'])}</h1><h2>{escape(BOOK['subtitle'])}</h2><p style="text-align:center">Lawrence Mukombo</p><p style="text-align:center">Original-story edition</p></body></html>'''
    write(oebps / 'text' / 'title.xhtml', title)
    copyright_doc = f'''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Copyright</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>Copyright</h1><p>Copyright &#169; 2026 Lawrence Mukombo.</p><p>All rights reserved. No part of this original-story edition may be reproduced, stored, or transmitted by any means without prior written permission, except for brief quotations used in reviews or as permitted by law.</p><p>First edition. Published in Zambia.</p><p>Cover artwork created with generative artificial intelligence under the direction of Lawrence Mukombo.</p></body></html>'''
    dedication_doc = '''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Dedication</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>Dedication</h1><p>Dedicated with love to <strong>Chawana Mukombo</strong>, my daughter.</p><p>May these stories encourage you to grow in wisdom, courage, kindness, honesty, and respect for others.</p></body></html>'''
    acknowledgements_doc = '''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Acknowledgements</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>Acknowledgements</h1><p>Grateful acknowledgement is given to the families, teachers, readers, storytellers, educators, cultural custodians, and communities who keep oral and written storytelling alive.</p><p>This original collection was created to celebrate Zambian settings and experiences, encourage reading, and help young readers reflect on honesty, courage, kindness, teamwork, responsibility, and respect for others.</p><p>Special thanks go to every young reader whose curiosity gives stories their purpose.</p></body></html>'''
    about_doc = '''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>About the Author</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>About the Author</h1><p><strong>Lawrence Mukombo</strong> is a Zambian writer and compiler with a passion for storytelling, literacy, and learning. Through stories rooted in familiar communities, schools, friendships, and landscapes, he aims to help young readers build confidence, curiosity, character, and a lasting love of books.</p><p>Lawrence lives in Zambia. Reader correspondence may be sent to <a href="mailto:lawrencemukombo2@gmail.com">lawrencemukombo2@gmail.com</a>.</p></body></html>'''
    write(oebps / 'text' / 'copyright.xhtml', copyright_doc)
    write(oebps / 'text' / 'dedication.xhtml', dedication_doc)
    write(oebps / 'text' / 'acknowledgements.xhtml', acknowledgements_doc)
    write(oebps / 'text' / 'author.xhtml', about_doc)
    for story in STORIES:
        sid = story['id']
        img_name = f'story-{sid:02d}.{image_extension(sid)}'
        shutil.copy2(ROOT / 'assets' / 'covers' / img_name, oebps / 'images' / img_name)
        paragraphs = ''.join(f'<h3>{escape(b["text"])}</h3>' if b.get('type') == 'subheading' else f'<p>{escape(b["text"])}</p>' for b in story['body'])
        words = ''.join(f'<li>{escape(w)}</li>' for w in story['newWords'])
        questions = ''.join(f'<li>{escape(q)}</li>' for q in story['questions'])
        doc = f'''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>{escape(story['title'])}</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body class="chapter"><img src="../images/{img_name}" alt="Illustration for {escape(story['title'])}"/><h1>{escape(story['title'])}</h1>{paragraphs}<section class="lesson"><h2>Lesson from the Story</h2><p>{escape(story['lesson'])}</p><h2>New Words</h2><ul>{words}</ul><h2>Think About It</h2><ol>{questions}</ol></section></body></html>'''
        write(oebps / 'text' / f's{sid}.xhtml', doc)
        media = {'jpg': 'image/jpeg', 'png': 'image/png', 'svg': 'image/svg+xml'}[image_extension(sid)]
        manifest.extend([f'<item id="s{sid}" href="text/s{sid}.xhtml" media-type="application/xhtml+xml"/>', f'<item id="img{sid}" href="images/{img_name}" media-type="{media}"/>'])
        spine.append(f'<itemref idref="s{sid}"/>')
        nav_items.append(f'<li><a href="text/s{sid}.xhtml">{escape(story["title"])}</a></li>')
    toc_items = ''.join(nav_items)
    visible_toc_items = ''.join(f'<li><a href="s{s["id"]}.xhtml">{escape(s["title"])}</a></li>' for s in STORIES)
    toc_doc = f'''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Contents</title><link rel="stylesheet" href="../style.css" type="text/css"/></head><body><h1>Contents</h1><ol>{visible_toc_items}</ol><p><a href="author.xhtml">About the Author</a></p></body></html>'''
    write(oebps / 'text' / 'toc.xhtml', toc_doc)
    spine.append('<itemref idref="author"/>')
    nav = f'''<?xml version="1.0" encoding="utf-8"?><html xmlns="http://www.w3.org/1999/xhtml"><head><title>Contents</title><link rel="stylesheet" href="style.css" type="text/css"/></head><body><nav epub:type="toc" xmlns:epub="http://www.idpf.org/2007/ops"><h1>Contents</h1><ol><li><a href="text/dedication.xhtml">Dedication</a></li><li><a href="text/acknowledgements.xhtml">Acknowledgements</a></li>{toc_items}<li><a href="text/author.xhtml">About the Author</a></li></ol></nav><nav epub:type="landmarks" xmlns:epub="http://www.idpf.org/2007/ops"><ol><li><a epub:type="toc" href="text/toc.xhtml">Table of Contents</a></li><li><a epub:type="bodymatter" href="text/s{STORIES[0]['id']}.xhtml">Start Reading</a></li></ol></nav></body></html>'''
    write(oebps / 'nav.xhtml', nav)
    opf = f'''<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">urn:uuid:stories-baobab-original-2026</dc:identifier><dc:title id="main-title">{escape(BOOK['title'])}</dc:title><dc:title id="subtitle">{escape(BOOK['subtitle'])}</dc:title><meta refines="#main-title" property="title-type">main</meta><meta refines="#subtitle" property="title-type">subtitle</meta><dc:creator>{escape(BOOK['creator'])}</dc:creator><dc:language>en</dc:language><dc:rights>Copyright 2026 Lawrence Mukombo. All rights reserved.</dc:rights><meta property="dcterms:modified">2026-09-03T00:00:00Z</meta></metadata><manifest>{''.join(manifest)}</manifest><spine>{''.join(spine)}</spine></package>'''
    write(oebps / 'package.opf', opf)
    out = DIST / f'stories-from-the-baobab-tree-{SLUG}.epub'
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w') as zf:
        zf.write(EPUB_STAGE / 'mimetype', 'mimetype', compress_type=zipfile.ZIP_STORED)
        for path in sorted(EPUB_STAGE.rglob('*')):
            if path.is_file() and path.name != 'mimetype':
                zf.write(path, path.relative_to(EPUB_STAGE).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
    return out


def page_number(canvas, doc):
    if doc.page <= 8:
        return
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(HexColor('#555555'))
    canvas.drawCentredString(3 * INCH, 0.38 * INCH, str(doc.page - 8))
    canvas.setFont('Helvetica', 7)
    if doc.page % 2:
        canvas.drawRightString(5.35 * INCH, 8.62 * INCH, BOOK['title'])
    else:
        canvas.drawString(.75 * INCH, 8.62 * INCH, BOOK['creator'])
    canvas.restoreState()


def build_pdf():
    out = DIST / f'stories-from-the-baobab-tree-{SLUG}-6x9.pdf'
    out.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    title = ParagraphStyle('BookTitle', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=25, leading=30, alignment=TA_CENTER, textColor='#183934', spaceAfter=18)
    chapter = ParagraphStyle('Chapter', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, alignment=TA_CENTER, textColor='#183934', spaceAfter=14)
    body = ParagraphStyle('Body', parent=styles['BodyText'], fontName='Helvetica', fontSize=10.5, leading=14, spaceAfter=7)
    small = ParagraphStyle('Small', parent=body, fontSize=9, leading=12)
    doc = SimpleDocTemplate(str(out), pagesize=(6 * inch, 9 * inch), rightMargin=.65 * inch, leftMargin=.75 * inch, topMargin=.65 * inch, bottomMargin=.65 * inch, title=BOOK['title'], author=BOOK['creator'])
    edition_label = 'Complete 60-story review edition' if FULL_EDITION else BOOK['subtitle']
    rights_copy = ('This complete edition contains all 60 stories from the private reader. Rights or a confirmed public-domain basis must be documented for every sourced story before commercial publication.' if FULL_EDITION else 'This edition contains the original Jelita and Mulenga stories and the original Children of Northwestern Province stories (chapters 16-25 of the private reader).')
    center = ParagraphStyle('Center', parent=body, alignment=TA_CENTER)
    front_heading = ParagraphStyle('FrontHeading', parent=chapter, spaceBefore=24)
    flow = [Spacer(1, 2.3 * INCH), Paragraph(escape(BOOK['title']), title), PageBreak(), Spacer(1, 1), PageBreak(), Spacer(1, 1.6 * INCH), Paragraph(escape(BOOK['title']), title), Paragraph(escape(edition_label), chapter), Spacer(1, .35 * INCH), Paragraph('Lawrence Mukombo', center), PageBreak(), Paragraph('Copyright', front_heading), Paragraph('Copyright 2026 Lawrence Mukombo.', center), Paragraph('All rights reserved. No part of this original-story edition may be reproduced, stored, or transmitted by any means without prior written permission, except for brief quotations used in reviews or as permitted by law.', center), Paragraph('First edition. Published in Zambia.', center), Paragraph('Cover artwork created with generative artificial intelligence under the direction of Lawrence Mukombo.', center), PageBreak(), Spacer(1, 1.45 * INCH), Paragraph('Dedication', front_heading), Paragraph('Dedicated with love to <b>Chawana Mukombo</b>, my daughter.', center), Paragraph('May these stories encourage you to grow in wisdom, courage, kindness, honesty, and respect for others.', center), PageBreak(), Spacer(1, 1), PageBreak(), Paragraph('Contents', front_heading)]
    for i, story in enumerate(STORIES, 1):
        flow.append(Paragraph(f'{i}. {escape(story["title"])}', body))
    flow.extend([Paragraph('About the Author', body), PageBreak(), Paragraph('Acknowledgements', front_heading), Paragraph('Grateful acknowledgement is given to the families, teachers, readers, storytellers, educators, cultural custodians, and communities who keep oral and written storytelling alive.', body), Paragraph('This original collection was created to celebrate Zambian settings and experiences, encourage reading, and help young readers reflect on honesty, courage, kindness, teamwork, responsibility, and respect for others.', body), Paragraph('Special thanks go to every young reader whose curiosity gives stories their purpose.', body)])
    for story in STORIES:
        flow.append(PageBreak())
        ext = image_extension(story['id'])
        img = ROOT / 'assets' / 'covers' / f'story-{story["id"]:02d}.{ext}'
        if ext in ('jpg', 'png'):
            print_dir = BUILD / 'print-images'
            print_dir.mkdir(parents=True, exist_ok=True)
            print_img = print_dir / f'story-{story["id"]:02d}.jpg'
            with PILImage.open(img) as source:
                source = source.convert('RGB')
                source.thumbnail((1200, 1200), PILImage.Resampling.LANCZOS)
                source.save(print_img, 'JPEG', quality=88, optimize=True)
            flow.extend([Image(str(print_img), width=3.65 * INCH, height=2.74 * INCH, kind='proportional'), Spacer(1, .12 * INCH)])
        flow.append(Paragraph(escape(story['title']), chapter))
        for block in story['body']:
            style = styles['Heading2'] if block.get('type') == 'subheading' else body
            flow.append(Paragraph(escape(block['text']), style))
        flow.extend([Spacer(1, .08 * INCH), Paragraph('Lesson from the Story', styles['Heading2']), Paragraph(escape(story['lesson']), body), Paragraph('New Words', styles['Heading2'])])
        for word in story['newWords']:
            flow.append(Paragraph('- ' + escape(word), small))
        flow.append(Paragraph('Think About It', styles['Heading2']))
        for index, question in enumerate(story['questions'], 1):
            flow.append(Paragraph(f'{index}. {escape(question)}', small))
    flow.extend([PageBreak(), Paragraph('About the Author', front_heading), Paragraph('<b>Lawrence Mukombo</b> is a Zambian writer and compiler with a passion for storytelling, literacy, and learning. Through stories rooted in familiar communities, schools, friendships, and landscapes, he aims to help young readers build confidence, curiosity, character, and a lasting love of books.', body), Paragraph('Lawrence lives in Zambia. Reader correspondence may be sent to lawrencemukombo2@gmail.com.', body), PageBreak(), Spacer(1, 1)])
    doc.build(flow, onFirstPage=page_number, onLaterPages=page_number)
    reader = PdfReader(str(out))
    if len(reader.pages) % 2:
        writer = PdfWriter()
        writer.clone_document_from_reader(reader)
        writer.add_blank_page(width=6 * inch, height=9 * inch)
        even_out = out.with_suffix('.even.pdf')
        with even_out.open('wb') as stream:
            writer.write(stream)
        even_out.replace(out)
    return out


def verify(epub, pdf):
    with zipfile.ZipFile(epub) as zf:
        assert zf.namelist()[0] == 'mimetype'
        assert zf.read('mimetype') == b'application/epub+zip'
        assert len([n for n in zf.namelist() if re.match(r'OEBPS/text/s\d+\.xhtml$', n)]) == len(STORIES)
    reader = PdfReader(str(pdf))
    assert len(reader.pages) >= 24
    report = {
        'build_mode': 'complete 60-story review edition' if FULL_EDITION else 'commercial-safe original stories only',
        'included_story_ids': [s['id'] for s in STORIES],
        'excluded_story_ids': [] if FULL_EDITION else list(range(1, 16)) + list(range(26, 61)),
        'epub': {'file': epub.name, 'bytes': epub.stat().st_size, 'stories': len(STORIES)},
        'print_pdf': {'file': pdf.name, 'bytes': pdf.stat().st_size, 'trim': '6 x 9 in', 'bleed': False, 'pages': len(reader.pages)},
        'rights_note': 'Stories 1-15 require provenance review. Stories 26-60 require written permission or a confirmed public-domain basis before commercial distribution.',
        'remaining_checks': ['Inspect EPUB in Kindle Previewer', 'Inspect PDF in KDP Print Previewer', 'Create a separate full-wrap print cover after selecting paper/ink and final page count', 'Confirm metadata and disclose AI-generated content in KDP if applicable']
    }
    (DIST / f'publication-preflight-{SLUG}.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    epub_path = build_epub()
    pdf_path = build_pdf()
    verify(epub_path, pdf_path)
