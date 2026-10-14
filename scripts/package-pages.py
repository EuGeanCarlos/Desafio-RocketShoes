"""Empacota apenas os recursos públicos versionados do projeto original."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / '.'
FILES = ['img/favicon.ico', 'img/icon-arrow.svg', 'img/icon-bag.svg', 'img/icon-search.svg', 'img/img-video.png', 'img/logo.svg', 'img/tenis-1-ampliado.png', 'img/tenis-1-galeria.png', 'img/tenis-2-galeria.png', 'img/tenis-3-galeria.png', 'index.html', 'style.css']
DEST = ROOT / "_site"
DEST.mkdir(exist_ok=True)
for name in FILES:
    target = DEST / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / name, target)
assert (DEST / "index.html").is_file(), "Entrada index.html ausente"
(DEST / ".nojekyll").touch()
