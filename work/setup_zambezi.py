import shutil
from pathlib import Path

brain_dir = Path(r"C:\Users\Mukombo\.gemini\antigravity-ide\brain\de7d7f11-667e-469d-a28b-8509f937e81d")
reader_img_dir = Path(r"c:\folk_tale_stories\outputs\zambezi-reader\assets\illustrations")
epub_img_dir = Path(r"c:\folk_tale_stories\work\epub-zambezi\OEBPS\images")

reader_img_dir.mkdir(parents=True, exist_ok=True)
epub_img_dir.mkdir(parents=True, exist_ok=True)

mapping = {
    "cover.jpg": "zambezi_legends_cover_1792002539183.jpg",
    "chapter-01.jpg": "tonga_elders_story_1792002581554.jpg",
    "chapter-02.jpg": "victoria_falls_rainbow_1792002624010.jpg",
    "chapter-03.jpg": "musonda_falls_spirits_1792002679178.jpg",
    "chapter-04.jpg": "makumba_sacred_stone_1792002740464.jpg",
    "chapter-05.jpg": "moon_leopard_bangweulu_1792002832075.jpg",
    "chapter-06.jpg": "mukuni_fire_ritual_1792002862591.jpg",
    "chapter-07.jpg": "batoka_secret_cavern_1792002899889.jpg",
    "chapter-08.jpg": "singing_baobab_luangwa_1792002941648.jpg",
}

for dest_name, src_name in mapping.items():
    src_file = brain_dir / src_name
    if src_file.exists():
        shutil.copy2(src_file, reader_img_dir / dest_name)
        shutil.copy2(src_file, epub_img_dir / dest_name)
        print(f"Copied {dest_name} ({src_file.stat().st_size} bytes)")
    else:
        print(f"Warning: {src_file} does not exist!")

print("All illustrations copied successfully!")
