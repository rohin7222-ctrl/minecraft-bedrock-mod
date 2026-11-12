"""
build_civilization_addon.py - Modular coordinator for packaging Civilization.mcaddon.
All sub-tasks are divided into builder_modules and addon_src/scripts.
Zero files exceed 1000 lines across the entire codebase.
"""

from pathlib import Path
from builder_modules.bundler import prepare_directories, copy_icons_and_scripts, package_mcaddon
from builder_modules.manifests import write_manifests
from builder_modules.spawn_rules import generate_spawn_rules
from builder_modules.ui_defs import generate_ui_and_texts

def main():
    root_dir = Path(__file__).resolve().parent
    base_dir = root_dir / "civilization_addon_build"
    output_mcaddon = root_dir / "Civilization.mcaddon"

    print("=== BUILDING CIVILIZATION PART 5 ADDON ===")
    bp_dir, rp_dir = prepare_directories(base_dir)

    write_manifests(bp_dir, rp_dir)
    generate_spawn_rules(bp_dir)
    generate_ui_and_texts(rp_dir)
    copy_icons_and_scripts(root_dir, bp_dir, rp_dir)
    package_mcaddon(base_dir, output_mcaddon)
    print("=== BUILD COMPLETE ===")

if __name__ == "__main__":
    main()
