# Ben 10 Bedrock Addon - Entity Builder Module
# Handles registration and writing of Kevin's Car, Vilgax, Battle Drone, Vilgax Ship, Rustbucket, Meteor Pod, and Kevin 11
# Strictly under 1000 lines - Pure Python

import os
import json
from addon_entities import (
    get_kevin_car_geometry,
    get_vilgax_geometry,
    get_battle_drone_geometry,
    get_vilgax_ship_geometry,
    get_rustbucket_geometry,
    get_meteor_pod_geometry,
    get_kevin11_geometry
)
from addon_entity_textures import (
    create_kevin_car_texture,
    create_vilgax_texture,
    create_battle_drone_texture,
    create_vilgax_ship_texture,
    create_rustbucket_texture,
    create_meteor_pod_texture,
    create_kevin11_texture
)
from addon_entity_defs import (
    get_bp_kevin_car,
    get_bp_vilgax,
    get_bp_battle_drone,
    get_bp_vilgax_ship,
    get_bp_rustbucket,
    get_bp_meteor_pod,
    get_bp_kevin11,
    get_rp_client_entity
)
from addon_graphics import make_png, hex_to_rgba

def create_spawner_icon(base_hex, glow_hex):
    """16x16 Spawner Key / Beacon Icon"""
    data = bytearray(16 * 16 * 4)
    c_base = hex_to_rgba(base_hex)
    c_glow = hex_to_rgba(glow_hex)
    c_dark = hex_to_rgba("#090d16")
    c_trans = [0, 0, 0, 0]

    for y in range(16):
        for x in range(16):
            idx = (y * 16 + x) * 4
            pixel = c_trans
            dx = abs(x - 7.5)
            dy = abs(y - 7.5)
            if dx + dy <= 6:
                if dx + dy <= 2:
                    pixel = c_glow
                elif (x + y) % 2 == 0:
                    pixel = c_base
                else:
                    pixel = c_dark
            data[idx:idx+4] = bytes(pixel)
    return make_png(16, 16, bytes(data))

def build_custom_entities(BP_DIR, RP_DIR, texture_data):
    """Assembles all 7 entities, models, textures, BP and RP definitions"""
    os.makedirs(os.path.join(BP_DIR, "entities"), exist_ok=True)
    os.makedirs(os.path.join(BP_DIR, "items"), exist_ok=True)
    os.makedirs(os.path.join(RP_DIR, "items"), exist_ok=True)
    os.makedirs(os.path.join(RP_DIR, "entity"), exist_ok=True)
    os.makedirs(os.path.join(RP_DIR, "textures", "entity"), exist_ok=True)

    entities = [
        {
            "id": "kevin_car",
            "name": "Kevin's Muscle Car",
            "geo": get_kevin_car_geometry(),
            "tex": create_kevin_car_texture(),
            "bp": get_bp_kevin_car(),
            "geo_id": "geometry.ben10.kevin_car",
            "color_base": "#16a34a",
            "color_glow": "#86efac",
            "item_name": "Kevin's Car Key"
        },
        {
            "id": "vilgax",
            "name": "Vilgax the Conqueror",
            "geo": get_vilgax_geometry(),
            "tex": create_vilgax_texture(),
            "bp": get_bp_vilgax(),
            "geo_id": "geometry.ben10.vilgax",
            "color_base": "#849688",
            "color_glow": "#ef4444",
            "item_name": "Summon Vilgax"
        },
        {
            "id": "battle_drone",
            "name": "Vilgax Battle Drone",
            "geo": get_battle_drone_geometry(),
            "tex": create_battle_drone_texture(),
            "bp": get_bp_battle_drone(),
            "geo_id": "geometry.ben10.battle_drone",
            "color_base": "#ea580c",
            "color_glow": "#f97316",
            "item_name": "Deploy Battle Drone"
        },
        {
            "id": "vilgax_ship",
            "name": "Vilgax Drone Battleship",
            "geo": get_vilgax_ship_geometry(),
            "tex": create_vilgax_ship_texture(),
            "bp": get_bp_vilgax_ship(),
            "geo_id": "geometry.ben10.vilgax_ship",
            "color_base": "#9a3412",
            "color_glow": "#ef4444",
            "item_name": "Vilgax Ship Beacon"
        },
        {
            "id": "rustbucket",
            "name": "Rust Bucket RV",
            "geo": get_rustbucket_geometry(),
            "tex": create_rustbucket_texture(),
            "bp": get_bp_rustbucket(),
            "geo_id": "geometry.ben10.rustbucket",
            "color_base": "#f8fafc",
            "color_glow": "#16a34a",
            "item_name": "Rust Bucket Keys"
        },
        {
            "id": "meteor_pod",
            "name": "Omnitrix Meteor Pod",
            "geo": get_meteor_pod_geometry(),
            "tex": create_meteor_pod_texture(),
            "bp": get_bp_meteor_pod(),
            "geo_id": "geometry.ben10.meteor_pod",
            "color_base": "#27272a",
            "color_glow": "#22c55e",
            "item_name": "Omnitrix Crash Capsule"
        },
        {
            "id": "kevin11",
            "name": "Mutated Kevin 11",
            "geo": get_kevin11_geometry(),
            "tex": create_kevin11_texture(),
            "bp": get_bp_kevin11(),
            "geo_id": "geometry.ben10.kevin11",
            "color_base": "#dc2626",
            "color_glow": "#2dd4bf",
            "item_name": "Summon Kevin 11 Boss"
        }
    ]

    for ent in entities:
        # 1. Write 3D Geometry
        geo_path = os.path.join(RP_DIR, "models", "entity", f"{ent['id']}.geo.json")
        with open(geo_path, "w", encoding="utf-8") as f:
            json.dump(ent["geo"], f, indent=2)

        # 2. Write HD Entity Texture
        tex_path = os.path.join(RP_DIR, "textures", "entity", f"{ent['id']}.png")
        with open(tex_path, "wb") as f:
            f.write(ent["tex"])

        # 3. Write BP Entity
        bp_path = os.path.join(BP_DIR, "entities", f"{ent['id']}.json")
        with open(bp_path, "w", encoding="utf-8") as f:
            json.dump(ent["bp"], f, indent=2)

        # 4. Write RP Client Entity
        rp_path = os.path.join(RP_DIR, "entity", f"{ent['id']}.entity.json")
        rp_client = get_rp_client_entity(f"ben10:{ent['id']}", ent["geo_id"], f"textures/entity/{ent['id']}")
        with open(rp_path, "w", encoding="utf-8") as f:
            json.dump(rp_client, f, indent=2)

        # 5. Spawner Item Icon & Texture
        spawner_item_id = f"{ent['id']}_spawner"
        icon_bytes = create_spawner_icon(ent["color_base"], ent["color_glow"])
        with open(os.path.join(RP_DIR, "textures", "items", f"{spawner_item_id}.png"), "wb") as f:
            f.write(icon_bytes)
        texture_data[spawner_item_id] = {"textures": f"textures/items/{spawner_item_id}"}

        # 6. Write BP & RP Spawner Item
        item_bp = {
            "format_version": "1.20.80",
            "minecraft:item": {
                "description": {
                    "identifier": f"ben10:{spawner_item_id}",
                    "menu_category": {"category": "items", "group": "itemGroup.name.mobEgg"}
                },
                "components": {
                    "minecraft:icon": spawner_item_id,
                    "minecraft:display_name": {"value": f"§e[Ben 10] §a{ent['item_name']}"},
                    "minecraft:max_stack_size": 64,
                    "minecraft:cooldown": {"category": "spawner", "duration": 1.0}
                }
            }
        }
        with open(os.path.join(BP_DIR, "items", f"{spawner_item_id}.json"), "w", encoding="utf-8") as f:
            json.dump(item_bp, f, indent=2)

        item_rp = {
            "format_version": "1.20.80",
            "minecraft:item": {
                "description": {"identifier": f"ben10:{spawner_item_id}"},
                "components": {"minecraft:icon": spawner_item_id}
            }
        }
        with open(os.path.join(RP_DIR, "items", f"{spawner_item_id}.json"), "w", encoding="utf-8") as f:
            json.dump(item_rp, f, indent=2)
