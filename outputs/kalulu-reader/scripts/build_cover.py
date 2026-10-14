from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'assets' / 'cover-art-original.png'
output = ROOT / 'dist' / 'stories-from-the-baobab-tree-kindle-cover.jpg'

image = Image.open(source).convert('RGB')
target_ratio = 1600 / 2560
crop_width = round(image.height * target_ratio)
left = max(0, (image.width - crop_width) // 2)
image = image.crop((left, 0, left + crop_width, image.height)).resize((1600, 2560), Image.Resampling.LANCZOS)

draw = ImageDraw.Draw(image, 'RGBA')
font_dir = ROOT / 'assets' / 'fonts'
title_font = ImageFont.truetype(str(font_dir / 'Ubuntu-B.ttf'), 132)
subtitle_font = ImageFont.truetype(str(font_dir / 'Ubuntu-M.ttf'), 57)
author_font = ImageFont.truetype(str(font_dir / 'Ubuntu-B.ttf'), 60)

def centered(text, y, font, fill, stroke=0):
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=4, align='center', stroke_width=stroke)
    x = (1600 - (box[2] - box[0])) / 2
    draw.multiline_text((x, y), text, font=font, fill=fill, spacing=4, align='center', stroke_width=stroke, stroke_fill=(0, 0, 0, 180))

draw.rounded_rectangle((90, 95, 1510, 850), radius=45, fill=(9, 45, 35, 190), outline=(238, 193, 93, 220), width=5)
centered('STORIES FROM THE\nBAOBAB TREE', 165, title_font, (255, 248, 224, 255), 2)
centered('Ten Original Zambian Stories\nfor Young Readers', 535, subtitle_font, (250, 214, 120, 255), 1)
draw.rounded_rectangle((370, 2365, 1230, 2485), radius=30, fill=(9, 45, 35, 205))
centered('LAWRENCE MUKOMBO', 2390, author_font, (255, 248, 224, 255), 1)

output.parent.mkdir(parents=True, exist_ok=True)
image.save(output, 'JPEG', quality=94, optimize=True, dpi=(300, 300))
print(output)
