"""
builder_modules/bundler.py - Copies assets and packages Civilization.mcaddon.
Part of the modular build architecture for Civilization Addon.
"""

import shutil
import zipfile
from pathlib import Path

def prepare_directories(base_dir: Path):
    """Sets up fresh BP and RP directories."""
    bp_dir = base_dir / "Civilization BP"
    rp_dir = base_dir / "Civilization RP"

    if base_dir.exists():
        shutil.rmtree(base_dir)

    (bp_dir / "scripts").mkdir(parents=True, exist_ok=True)
    (bp_dir / "spawn_rules").mkdir(parents=True, exist_ok=True)
    (rp_dir / "texts").mkdir(parents=True, exist_ok=True)
    (rp_dir / "ui").mkdir(parents=True, exist_ok=True)

    return bp_dir, rp_dir

def copy_icons_and_scripts(root_dir: Path, bp_dir: Path, rp_dir: Path):
    """Copies pack icons and modular JavaScript scripts into behavior pack."""
    icon_src = root_dir / "pack_icon_civilization.png"
    if icon_src.exists():
        shutil.copyfile(icon_src, bp_dir / "pack_icon.png")
        shutil.copyfile(icon_src, rp_dir / "pack_icon.png")

    scripts_src = root_dir / "addon_src" / "scripts"
    scripts_dest = bp_dir / "scripts"
    for js_file in scripts_src.glob("*.js"):
        shutil.copyfile(js_file, scripts_dest / js_file.name)

def package_mcaddon(base_dir: Path, output_file: Path):
    """Creates Civilization.mcaddon zip archive from build directory."""
    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in base_dir.rglob("*"):
            if p.is_file():
                arcname = p.relative_to(base_dir)
                zf.write(p, arcname)
    print(f"[Bundler] Packaged {output_file.name} ({output_file.stat().st_size} bytes)")
