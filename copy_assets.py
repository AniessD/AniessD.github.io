import filecmp
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent
dest = root / "en"


def sync_file(src: Path, dst: Path):
    """Copie src vers dst seulement si dst n'existe pas ou diffère."""
    if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print("Copié :", dst.relative_to(root))


# Fichiers partagés
for f in ["styles.css", "fonts.html", "fix-accessibility.html"]:
    sync_file(root / f, dest / f)

# Dossier images : copie des fichiers nouveaux ou modifiés
src_img = root / "images"
dst_img = dest / "images"

if src_img.exists():
    source_files = set()
    for p in src_img.rglob("*"):
        if p.is_file():
            rel = p.relative_to(src_img)
            source_files.add(rel)
            sync_file(p, dst_img / rel)

    # Suppression des fichiers qui n'existent plus à la source
    if dst_img.exists():
        for p in list(dst_img.rglob("*")):
            if p.is_file() and p.relative_to(dst_img) not in source_files:
                print("Suppression :", p.relative_to(root))
                p.unlink()

# Dossier documents : copie des fichiers nouveaux ou modifiés
src_doc = root / "documents"
dst_doc = dest / "documents"

if src_doc.exists():
    source_files = set()
    for p in src_doc.rglob("*"):
        if p.is_file():
            rel = p.relative_to(src_doc)
            source_files.add(rel)
            sync_file(p, dst_doc / rel)

    # Suppression des fichiers qui n'existent plus à la source
    if dst_doc.exists():
        for p in list(dst_doc.rglob("*")):
            if p.is_file() and p.relative_to(dst_doc) not in source_files:
                print("Suppression :", p.relative_to(root))
                p.unlink()
