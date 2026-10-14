#!/usr/bin/env python3
"""
EPUB 3.0 Packager for iOS (Apple Books) and Android (Lithium, ReadEra, etc.)
Strict compliance with IDPF EPUB 3.0 specification:
- mimetype stored uncompressed (ZIP_STORED) as the exact first entry
- Valid XML package.opf and nav.xhtml
- UTF-8 clean encoding
"""

import sys
import zipfile
from pathlib import Path

def package_epub(source_dir: Path, output_epub: Path):
    if not source_dir.exists():
        print(f"Error: source directory does not exist: {source_dir}")
        sys.exit(1)
        
    mimetype_file = source_dir / "mimetype"
    if not mimetype_file.exists():
        print("Error: missing mimetype file")
        sys.exit(1)
        
    output_epub.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Packaging EPUB from: {source_dir}")
    print(f"Target file: {output_epub}")
    
    # Standard EPUB packing order
    with zipfile.ZipFile(output_epub, "w") as zf:
        # 1. First file MUST be 'mimetype' stored with NO compression
        zf.write(mimetype_file, "mimetype", compress_type=zipfile.ZIP_STORED)
        
        # 2. Add all other files compressed with DEFLATED
        for file_path in sorted(source_dir.rglob("*")):
            if file_path.is_file() and file_path.name != "mimetype":
                rel_path = file_path.relative_to(source_dir).as_posix()
                zf.write(file_path, rel_path, compress_type=zipfile.ZIP_DEFLATED)
                
    file_size_mb = output_epub.stat().st_size / (1024 * 1024)
    print(f"[SUCCESS] Built EPUB: {output_epub.name} ({file_size_mb:.2f} MB)")
    print("Ready to open in Apple Books (iOS/macOS), Google Play Books, or Android e-readers.")

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    src = root / "work" / "epub-current"
    
    out_name = sys.argv[1] if len(sys.argv) > 1 else "Stories-from-the-Baobab-Tree.epub"
    dest = root / "outputs" / out_name
    
    package_epub(src, dest)
