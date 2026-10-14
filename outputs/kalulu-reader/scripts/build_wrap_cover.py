from pathlib import Path
from textwrap import wrap
import json

from PIL import Image
from pypdf import PdfReader
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
interior = DIST / 'stories-from-the-baobab-tree-original-6x9.pdf'
cover_art = DIST / 'stories-from-the-baobab-tree-kindle-cover.jpg'
output = DIST / 'stories-from-the-baobab-tree-paperback-cover-standard-color.pdf'

pages = len(PdfReader(str(interior)).pages)
spine = pages * 0.002252
width = 0.125 + 6 + spine + 6 + 0.125
height = 9.25

pdfmetrics.registerFont(TTFont('Ubuntu', str(ROOT / 'assets' / 'fonts' / 'Ubuntu-R.ttf')))
pdfmetrics.registerFont(TTFont('UbuntuBold', str(ROOT / 'assets' / 'fonts' / 'Ubuntu-B.ttf')))

c = canvas.Canvas(str(output), pagesize=(width * inch, height * inch), pageCompression=1)
c.setFillColor(HexColor('#123b32'))
c.rect(0, 0, width * inch, height * inch, stroke=0, fill=1)

front_x = (0.125 + 6 + spine) * inch
c.drawImage(ImageReader(str(cover_art)), front_x, 0, width=6.125 * inch, height=9.25 * inch, preserveAspectRatio=False, mask='auto')

c.setFillColor(HexColor('#f5d27c'))
c.setFont('UbuntuBold', 20)
c.drawString(0.55 * inch, 8.35 * inch, 'STORIES FROM THE BAOBAB TREE')
c.setFillColor(white)
c.setFont('Ubuntu', 11)
description = ('Ten original Zambian stories about curiosity, courage, honesty and teamwork. '
               'Follow young characters through school mysteries, community challenges and meaningful discoveries. '
               'Each story includes a life lesson, new vocabulary and questions for thoughtful discussion.')
y = 7.75 * inch
for paragraph in wrap(description, width=54):
    c.drawString(0.55 * inch, y, paragraph)
    y -= 0.22 * inch

c.setFillColor(HexColor('#f5d27c'))
c.setFont('UbuntuBold', 14)
c.drawString(0.55 * inch, 5.95 * inch, 'For readers aged 8-12')
c.setFillColor(white)
c.setFont('Ubuntu', 10)
features = ['Original stories rooted in Zambian places and experiences', 'Vocabulary and reading-comprehension activities', 'Themes of friendship, responsibility and problem-solving']
y = 5.55 * inch
for item in features:
    for index, line in enumerate(wrap(item, width=52)):
        prefix = '- ' if index == 0 else '  '
        c.drawString(0.58 * inch, y, prefix + line)
        y -= 0.2 * inch
    y -= 0.07 * inch

c.setFillColor(HexColor('#f5d27c'))
c.setFont('UbuntuBold', 13)
c.drawString(0.55 * inch, 3.85 * inch, 'ABOUT THE AUTHOR')
c.setFillColor(white)
c.setFont('Ubuntu', 9.5)
bio = ('Lawrence Mukombo is a Zambian writer and compiler with a passion for storytelling, literacy and learning. '
       'His stories help young readers build curiosity, character and a lasting love of books.')
y = 3.5 * inch
for line in wrap(bio, width=62):
    c.drawString(0.55 * inch, y, line)
    y -= 0.19 * inch

# Leave a clean barcode area on the lower-right portion of the back cover.
c.setFillColor(HexColor('#fffdf7'))
c.roundRect(3.65 * inch, 0.48 * inch, 2.0 * inch, 1.2 * inch, 5, stroke=0, fill=1)
c.setFillColor(HexColor('#123b32'))
c.setFont('Ubuntu', 7)
c.drawCentredString(4.65 * inch, 0.58 * inch, 'BARCODE AREA')

c.setTitle('Stories from the Baobab Tree - Paperback Cover')
c.setAuthor('Lawrence Mukombo')
c.save()
report_path = DIST / 'publication-preflight-original.json'
if report_path.exists():
    report = json.loads(report_path.read_text(encoding='utf-8'))
    report['paperback_cover'] = {
        'file': output.name,
        'interior': 'standard color on white paper',
        'trim': '6 x 9 in',
        'bleed': '0.125 in',
        'spine_inches': round(spine, 4),
        'full_size_inches': [round(width, 4), height],
        'spine_text': False
    }
    report['remaining_checks'] = [
        'Inspect EPUB in Kindle Previewer',
        'Inspect interior and wrap cover in KDP Print Previewer',
        'Order and inspect a physical proof copy',
        'Confirm metadata and disclose AI-generated cover artwork in KDP'
    ]
    report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
print(f'{output} | pages={pages} spine={spine:.4f}in size={width:.4f}x{height:.4f}in')
