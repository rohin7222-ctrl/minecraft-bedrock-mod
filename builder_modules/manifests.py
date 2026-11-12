"""
builder_modules/manifests.py - Manifest generator for Behavior Pack & Resource Pack.
Part of the modular build system for Civilization Addon.
"""

import json
from pathlib import Path

def write_manifests(bp_dir: Path, rp_dir: Path):
    """Generates Bedrock 1.20/1.21 compatible manifest.json files."""
    bp_manifest = {
        "format_version": 2,
        "header": {
            "name": "Civilization AI Addon - Behavior Pack (Beta APIs)",
            "description": "Part 5 Masterpiece: 6 Job AIs, Simulated Catch-Up & Dynamic Territories (Beta APIs)",
            "uuid": "c4a3b8d2-5e1f-4a7b-8c2d-9e0f1a2b3c4d",
            "version": [5, 0, 0],
            "min_engine_version": [1, 20, 80]
        },
        "modules": [
            {
                "description": "Civilization Logic Data",
                "type": "data",
                "uuid": "d5b4c9e3-6f2a-4b8c-9d3e-0f1a2b3c4d5e",
                "version": [5, 0, 0]
            },
            {
                "description": "Civilization Scripting Engine",
                "type": "script",
                "language": "javascript",
                "entry": "scripts/main.js",
                "uuid": "e6c5d0f4-7a3b-4c9d-0e4f-1a2b3c4d5e6f",
                "version": [5, 0, 0]
            }
        ],
        "dependencies": [
            {"module_name": "@minecraft/server", "version": "1.12.0-beta"},
            {"module_name": "@minecraft/server-ui", "version": "1.3.0-beta"},
            {"uuid": "f7d6e1a5-8b4c-4d0e-1f5a-2b3c4d5e6f7a", "version": [5, 0, 0]}
        ]
    }

    rp_manifest = {
        "format_version": 2,
        "header": {
            "name": "Civilization AI Addon - Resource Pack",
            "description": "Part 5 Masterpiece: UI Definitions and Top-Left World Clock Overlay",
            "uuid": "f7d6e1a5-8b4c-4d0e-1f5a-2b3c4d5e6f7a",
            "version": [5, 0, 0],
            "min_engine_version": [1, 20, 80]
        },
        "modules": [
            {
                "description": "Civilization UI & Resource Definitions",
                "type": "resources",
                "uuid": "a8e7f2b6-9c5d-4e1f-2a6b-3c4d5e6f7a8b",
                "version": [5, 0, 0]
            }
        ]
    }

    (bp_dir / "manifest.json").write_text(json.dumps(bp_manifest, indent=2), encoding="utf-8")
    (rp_dir / "manifest.json").write_text(json.dumps(rp_manifest, indent=2), encoding="utf-8")

