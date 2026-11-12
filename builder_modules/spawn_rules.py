"""
builder_modules/spawn_rules.py - Bedrock monster spawn rule generator.
Disables natural monster spawning by setting conditions to empty list [].
"""

import json
from pathlib import Path

BEDROCK_MONSTER_IDS = [
    "minecraft:blaze", "minecraft:bogged", "minecraft:breeze", "minecraft:cave_spider",
    "minecraft:creeper", "minecraft:drowned", "minecraft:elder_guardian", "minecraft:endermite",
    "minecraft:evocation_illager", "minecraft:evoker", "minecraft:ghast", "minecraft:guardian",
    "minecraft:hoglin", "minecraft:husk", "minecraft:illusion_illager", "minecraft:illusioner",
    "minecraft:magma_cube", "minecraft:phantom", "minecraft:piglin_brute", "minecraft:pillager",
    "minecraft:ravager", "minecraft:shulker", "minecraft:silverfish", "minecraft:skeleton",
    "minecraft:slime", "minecraft:stray", "minecraft:vex", "minecraft:vindicator",
    "minecraft:warden", "minecraft:witch", "minecraft:wither_skeleton", "minecraft:zoglin",
    "minecraft:zombie", "minecraft:zombie_villager", "minecraft:zombie_villager_v2",
    "minecraft:enderman", "minecraft:spider", "minecraft:zombie_pigman", "minecraft:zombified_piglin",
    "minecraft:wither", "minecraft:ender_dragon", "minecraft:zombie_horse", "minecraft:creaking",
    "minecraft:creaking_transient"
]

def generate_spawn_rules(bp_dir: Path):
    """Generates zero-condition spawn rules for all Bedrock hostile mobs."""
    spawn_dir = bp_dir / "spawn_rules"
    spawn_dir.mkdir(parents=True, exist_ok=True)

    for mob in BEDROCK_MONSTER_IDS:
        short_name = mob.replace("minecraft:", "")
        rule = {
            "format_version": "1.8.0",
            "minecraft:spawn_rules": {
                "description": {
                    "identifier": mob,
                    "population_control": "monster"
                },
                "conditions": []
            }
        }
        (spawn_dir / f"{short_name}.json").write_text(json.dumps(rule, indent=2), encoding="utf-8")
