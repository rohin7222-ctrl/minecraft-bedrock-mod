"""
builder_modules/ui_defs.py - UI definitions and HUD screen layout generator.
Configures Top-Left World Clock overlay and pack localization text.
"""

import json
from pathlib import Path

def generate_ui_and_texts(rp_dir: Path):
    """Generates _ui_defs.json, hud_screen.json, and texts/en_US.lang."""
    ui_dir = rp_dir / "ui"
    texts_dir = rp_dir / "texts"
    ui_dir.mkdir(parents=True, exist_ok=True)
    texts_dir.mkdir(parents=True, exist_ok=True)

    ui_defs = {
        "ui_defs": [
            "ui/hud_screen.json"
        ]
    }
    (ui_dir / "_ui_defs.json").write_text(json.dumps(ui_defs, indent=2), encoding="utf-8")

    hud_screen = {
        "namespace": "hud",
        "hud_actionbar_text": {
            "type": "panel",
            "anchor_from": "top_left",
            "anchor_to": "top_left",
            "offset": [12, 46],
            "size": ["100%c", 16],
            "controls": [
                {
                    "actionbar_message": {
                        "type": "label",
                        "text": "$actionbar_text",
                        "text_alignment": "left",
                        "color": [1.0, 0.84, 0.0],
                        "shadow": True,
                        "font_size": "normal"
                    }
                }
            ]
        }
    }
    (ui_dir / "hud_screen.json").write_text(json.dumps(hud_screen, indent=2), encoding="utf-8")

    lang_content = (
        "pack.name=Civilization RP (Part 5: 6 Job AIs & Economy)\n"
        "pack.description=Living World Civilization with 6 Autonomous Job AIs (Hunter, Woodcutter, Miner, Crafter, "
        "Storage Manager, Builder), Simulated Catch-up Engine, House & Bed Construction, Dynamic Bell Center, "
        "Village Levels (50m-130m expansion), Mountain Safe-Return AI, World Real-Time sync, and zero particles!\n"
    )
    (texts_dir / "en_US.lang").write_text(lang_content, encoding="utf-8")

