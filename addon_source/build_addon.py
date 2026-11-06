import os
import json
import zipfile
import shutil

from addon_graphics import make_png, hex_to_rgba, create_16x16_icon, create_armor_texture, create_pack_icon
from addon_hd_item_art import (
    create_hd_omnitrix_watch_icon,
    create_hd_omnitrix_activator_icon,
    create_hd_detransform_icon,
    create_hd_fusion_icon,
    create_hd_alien_badge_icon
)
from addon_pixel_art import create_64x64_alien_skin
from addon_omnitrix_models import generate_omnitrix_geometry, create_omnitrix_model_texture
from addon_alien_models import get_alien_geometry
from addon_entity_builder import build_custom_entities
from addon_animations import build_player_animations
from addon_hud_ui import build_hud_ui
from addon_scripts_abilities import get_abilities_code
from addon_scripts import get_main_code
from addon_data import WATCHES, ALL_ALIENS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ADDON_DIR = os.path.join(BASE_DIR, "ben10_bedrock_addon")
BP_DIR = os.path.join(ADDON_DIR, "Ben10_BP")
RP_DIR = os.path.join(ADDON_DIR, "Ben10_RP")

if os.path.exists(ADDON_DIR):
    shutil.rmtree(ADDON_DIR)

os.makedirs(os.path.join(BP_DIR, "items"), exist_ok=True)
os.makedirs(os.path.join(BP_DIR, "recipes"), exist_ok=True)
os.makedirs(os.path.join(BP_DIR, "scripts"), exist_ok=True)
os.makedirs(os.path.join(BP_DIR, "functions"), exist_ok=True)

os.makedirs(os.path.join(RP_DIR, "attachables"), exist_ok=True)
os.makedirs(os.path.join(RP_DIR, "textures", "items"), exist_ok=True)
os.makedirs(os.path.join(RP_DIR, "textures", "models", "armor"), exist_ok=True)
os.makedirs(os.path.join(RP_DIR, "models", "entity"), exist_ok=True)
os.makedirs(os.path.join(RP_DIR, "render_controllers"), exist_ok=True)
os.makedirs(os.path.join(RP_DIR, "texts"), exist_ok=True)

# Generate custom render controllers: hides all head bones in 1st person so camera is never blocked, and isolates watch to leftArm!
rc_json = {
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.ben10_alien": {
            "geometry": "Geometry.default",
            "materials": [{"*": "Material.default"}],
            "textures": ["Texture.default"],
            "part_visibility": [
                {"*": True},
                {"head": "query.is_first_person == 0"},
                {"jaw": "query.is_first_person == 0"},
                {"angler": "query.is_first_person == 0"},
                {"visor": "query.is_first_person == 0"},
                {"helmet": "query.is_first_person == 0"},
                {"horns": "query.is_first_person == 0"},
                {"horn": "query.is_first_person == 0"},
                {"head2": "query.is_first_person == 0"},
                {"snout": "query.is_first_person == 0"}
            ]
        },
        "controller.render.ben10_watch": {
            "geometry": "Geometry.default",
            "materials": [{"*": "Material.default"}],
            "textures": ["Texture.default"],
            "part_visibility": [
                {"*": False},
                {"leftArm": True}
            ]
        }
    }
}
with open(os.path.join(RP_DIR, "render_controllers", "ben10_alien.render_controllers.json"), "w", encoding="utf-8") as f:
    json.dump(rc_json, f, indent=2)

# Generate 100% 3D Alien Morph Geometry (Covers head, face, chest with Omnitrix, arms, and legs)
morph_geo = {
    "format_version": "1.12.0",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.ben10.alien_morph",
                "texture_width": 64,
                "texture_height": 64,
                "visible_bounds_width": 3,
                "visible_bounds_height": 3,
                "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body",
                    "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25}
                    ]
                },
                {
                    "name": "head",
                    "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25},
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [32, 0], "inflate": 0.5}
                    ]
                },
                {
                    "name": "rightArm",
                    "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16], "inflate": 0.25}
                    ]
                },
                {
                    "name": "leftArm",
                    "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48], "inflate": 0.25}
                    ]
                },
                {
                    "name": "rightLeg",
                    "pivot": [-1.9, 12, 0],
                    "cubes": [
                        {"origin": [-3.9, 0, -2], "size": [4, 12, 4], "uv": [0, 16], "inflate": 0.25}
                    ]
                },
                {
                    "name": "leftLeg",
                    "pivot": [1.9, 12, 0],
                    "cubes": [
                        {"origin": [-0.1, 0, -2], "size": [4, 12, 4], "uv": [16, 48], "inflate": 0.25}
                    ]
                }
            ]
        }
    ]
}
with open(os.path.join(RP_DIR, "models", "entity", "alien_morph.geo.json"), "w", encoding="utf-8") as f:
    json.dump(morph_geo, f, indent=2)

# 1. Icons & Base textures
pack_icon_bytes = create_pack_icon()
with open(os.path.join(BP_DIR, "pack_icon.png"), "wb") as f:
    f.write(pack_icon_bytes)
with open(os.path.join(RP_DIR, "pack_icon.png"), "wb") as f:
    f.write(pack_icon_bytes)

texture_data = {
    "detransform": {"textures": "textures/items/detransform"},
    "biomnitrix_fusion_ability": {"textures": "textures/items/biomnitrix_fusion_ability"},
    "biomnitrix_fusion_suit": {"textures": "textures/items/biomnitrix_fusion_ability"}
}

for w in WATCHES:
    # 1. Authentic 32x32 HD 3D-angled inventory item icon
    dial_icon_png = create_hd_omnitrix_watch_icon(w["id"], w["band_hex"], w["bezel_hex"], w["dial_hex"], w["glow_hex"], "#bbf7d0")
    with open(os.path.join(RP_DIR, "textures", "items", f"{w['id']}.png"), "wb") as f:
        f.write(dial_icon_png)
    texture_data[w["id"]] = {"textures": f"textures/items/{w['id']}"}

    recharge_icon_png = create_hd_omnitrix_watch_icon(w["id"], w["band_hex"], w["bezel_hex"], "#7f1d1d", "#ef4444", "#fca5a5", is_recharging=True)
    with open(os.path.join(RP_DIR, "textures", "items", f"{w['id']}_recharging.png"), "wb") as f:
        f.write(recharge_icon_png)
    texture_data[f"{w['id']}_recharging"] = {"textures": f"textures/items/{w['id']}_recharging"}

    # 2. Series-Accurate 3D Model Geometry for each individual watch
    geo_file = os.path.join(RP_DIR, "models", "entity", f"{w['id']}.geo.json")
    with open(geo_file, "w", encoding="utf-8") as f:
        json.dump(generate_omnitrix_geometry(w["id"]), f, indent=2)

    # 3. 64x64 HD Wrist Watch Texture (Normal & Recharging Red)
    wrist_tex_png = create_omnitrix_model_texture(w["band_hex"], w["bezel_hex"], w["dial_hex"], w["glow_hex"], "#bbf7d0", watch_id=w["id"])
    with open(os.path.join(RP_DIR, "textures", "models", "armor", f"{w['id']}_wrist.png"), "wb") as f:
        f.write(wrist_tex_png)
    recharge_tex_png = create_omnitrix_model_texture(w["band_hex"], w["bezel_hex"], "#dc2626", "#ef4444", "#fca5a5", is_recharging=True, watch_id=w["id"])
    with open(os.path.join(RP_DIR, "textures", "models", "armor", f"{w['id']}_recharging.png"), "wb") as f:
        f.write(recharge_tex_png)

    # 4. Attachable that renders the 3D watch on player's left wrist in 1st & 3rd person
    watch_att = {
        "format_version": "1.8.0",
        "minecraft:attachable": {
            "description": {
                "identifier": f"ben10:{w['id']}",
                "materials": {"default": "armor", "enchanted": "armor_enchanted"},
                "textures": {"default": f"textures/models/armor/{w['id']}_wrist", "enchanted": "textures/misc/enchanted_actor_glint"},
                "geometry": {"default": f"geometry.ben10.{w['id']}"},
                "render_controllers": ["controller.render.ben10_watch"]
            }
        }
    }
    with open(os.path.join(RP_DIR, "attachables", f"{w['id']}.json"), "w", encoding="utf-8") as f:
        json.dump(watch_att, f, indent=2)

# Dedicated 32x32 HD Detransform Emergency Revert Icon
with open(os.path.join(RP_DIR, "textures", "items", "detransform.png"), "wb") as f:
    f.write(create_hd_detransform_icon())

# Dedicated 32x32 HD Omnitrix Activator Item Icon
with open(os.path.join(RP_DIR, "textures", "items", "omnitrix_activator.png"), "wb") as f:
    f.write(create_hd_omnitrix_activator_icon())
texture_data["omnitrix_activator"] = {"textures": "textures/items/omnitrix_activator"}

# Dedicated 32x32 HD Alien Ability Item Icon
with open(os.path.join(RP_DIR, "textures", "items", "alien_ability.png"), "wb") as f:
    f.write(create_hd_omnitrix_activator_icon())
texture_data["alien_ability"] = {"textures": "textures/items/alien_ability"}

# Dedicated 32x32 HD Biomnitrix Dual Fusion Ability Icon
with open(os.path.join(RP_DIR, "textures", "items", "biomnitrix_fusion_ability.png"), "wb") as f:
    f.write(create_hd_fusion_icon())

with open(os.path.join(RP_DIR, "textures", "models", "armor", "biomnitrix_fusion_layer_1.png"), "wb") as f:
    f.write(create_64x64_alien_skin("#ca8a04", "#0284c7", "#22c55e", "four_arms"))

attachable_fusion = {
    "format_version": "1.8.0",
    "minecraft:attachable": {
        "description": {
            "identifier": "ben10:biomnitrix_fusion_suit",
            "materials": {"default": "armor", "enchanted": "armor_enchanted"},
            "textures": {"default": "textures/models/armor/biomnitrix_fusion_layer_1", "enchanted": "textures/misc/enchanted_actor_glint"},
            "geometry": {"default": "geometry.ben10.fourarms"},
            "render_controllers": ["controller.render.ben10_alien"]
        }
    }
}
with open(os.path.join(RP_DIR, "attachables", "biomnitrix_fusion_suit.json"), "w", encoding="utf-8") as f:
    json.dump(attachable_fusion, f, indent=2)

for a in ALL_ALIENS:
    # 1. Authentic 32x32 HD Species-Specific Pixel Art Icon
    with open(os.path.join(RP_DIR, "textures", "items", f"{a['id']}_ability.png"), "wb") as f:
        f.write(create_hd_alien_badge_icon(a["id"], a["base_hex"], a["detail_hex"], a["accent_hex"]))
    texture_data[f"{a['id']}_ability"] = {"textures": f"textures/items/{a['id']}_ability"}
    texture_data[f"{a['id']}_suit"] = {"textures": f"textures/items/{a['id']}_ability"}

    # 2. Full 64x64 3D Humanoid Alien Skin (Face on head, Omnitrix on chest, colored arms & legs!)
    with open(os.path.join(RP_DIR, "textures", "models", "armor", f"{a['id']}_layer_1.png"), "wb") as f:
        f.write(create_64x64_alien_skin(a["base_hex"], a["detail_hex"], a["accent_hex"], a["id"]))

    # 3. Complete 3D Alien Morph Attachable (Dedicated species geometry!)
    alien_geo = get_alien_geometry(a["id"])
    geo_id = alien_geo["description"]["identifier"]
    geo_file = os.path.join(RP_DIR, "models", "entity", f"{a['id']}.geo.json")
    with open(geo_file, "w", encoding="utf-8") as f:
        json.dump({"format_version": "1.12.0", "minecraft:geometry": [alien_geo]}, f, indent=2)

    att_json = {
        "format_version": "1.8.0",
        "minecraft:attachable": {
            "description": {
                "identifier": f"ben10:{a['id']}_suit",
                "materials": {"default": "armor", "enchanted": "armor_enchanted"},
                "textures": {"default": f"textures/models/armor/{a['id']}_layer_1", "enchanted": "textures/misc/enchanted_actor_glint"},
                "geometry": {"default": geo_id},
                "scripts": {
                    "initialize": ["variable.is_first_person = c.is_first_person;"],
                    "pre_animation": ["variable.is_first_person = c.is_first_person;"]
                },
                "render_controllers": ["controller.render.ben10_alien"]
            }
        }
    }
    with open(os.path.join(RP_DIR, "attachables", f"{a['id']}_suit.json"), "w", encoding="utf-8") as f:
        json.dump(att_json, f, indent=2)

# Build Custom Series Bosses & Vehicles (Kevin's Car, Vilgax, Battle Drone, Vilgax Ship)
build_custom_entities(BP_DIR, RP_DIR, texture_data)

with open(os.path.join(RP_DIR, "textures", "item_texture.json"), "w", encoding="utf-8") as f:
    json.dump({"resource_pack_name": "ben10_rp", "texture_name": "atlas.items", "texture_data": texture_data}, f, indent=2)

# 2. BP Items & Recipes
def write_bp_item(filename, identifier, icon, name, category="equipment", is_armor=False, is_ability=False):
    item_json = {
        "format_version": "1.20.80",
        "minecraft:item": {
            "description": {"identifier": identifier, "menu_category": {"category": category}},
            "components": {
                "minecraft:icon": icon,
                "minecraft:display_name": {"value": name},
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True
            }
        }
    }
    if is_armor:
        item_json["minecraft:item"]["components"]["minecraft:wearable"] = {"slot": "slot.armor.chest"}
        item_json["minecraft:item"]["components"]["minecraft:armor"] = {"protection": 10}
    if is_ability:
        item_json["minecraft:item"]["components"]["minecraft:cooldown"] = {"category": "ben10_power", "duration": 0.5}
    with open(os.path.join(BP_DIR, "items", filename), "w", encoding="utf-8") as f:
        json.dump(item_json, f, indent=2)

for w in WATCHES:
    write_bp_item(f"{w['id']}.json", f"ben10:{w['id']}", w["id"], f"item.ben10:{w['id']}.name", is_armor=True)
    write_bp_item(f"{w['id']}_recharging.json", f"ben10:{w['id']}_recharging", f"{w['id']}_recharging", f"item.ben10:{w['id']}_recharging.name")

    rec_json = {
        "format_version": "1.12.0",
        "minecraft:recipe_shaped": {
            "description": {"identifier": f"ben10:{w['id']}_crafting"},
            "tags": ["crafting_table"],
            "pattern": w["recipe_pattern"],
            "key": {k: {"item": v} for k, v in w["recipe_keys"].items()},
            "result": {"item": f"ben10:{w['id']}", "count": 1}
        }
    }
    with open(os.path.join(BP_DIR, "recipes", f"{w['id']}.json"), "w", encoding="utf-8") as f:
        json.dump(rec_json, f, indent=2)

write_bp_item("omnitrix_activator.json", "ben10:omnitrix_activator", "omnitrix_activator", "item.ben10:omnitrix_activator.name")
write_bp_item("alien_ability.json", "ben10:alien_ability", "alien_ability", "item.ben10:alien_ability.name", is_ability=True)
write_bp_item("detransform.json", "ben10:detransform", "detransform", "item.ben10:detransform.name")
write_bp_item("biomnitrix_fusion_ability.json", "ben10:biomnitrix_fusion_ability", "biomnitrix_fusion_ability", "item.ben10:biomnitrix_fusion_ability.name", is_ability=True)
write_bp_item("biomnitrix_fusion_suit.json", "ben10:biomnitrix_fusion_suit", "biomnitrix_fusion_ability", "item.ben10:biomnitrix_fusion_suit.name", is_armor=True)

for a in ALL_ALIENS:
    write_bp_item(f"{a['id']}_suit.json", f"ben10:{a['id']}_suit", f"{a['id']}_ability", f"item.ben10:{a['id']}_suit.name", is_armor=True)
    write_bp_item(f"{a['id']}_ability.json", f"ben10:{a['id']}_ability", f"{a['id']}_ability", f"item.ben10:{a['id']}_ability.name", is_ability=True)

# 3. Localization
lang_lines = [
    "## Ben 10 Bedrock Addon Localization",
    "item.ben10:omnitrix_activator.name=§aOmnitrix Activator",
    "item.ben10:alien_ability.name=§aAlien Ability",
    "item.ben10:detransform.name=§cDetransform Dial",
    "item.ben10:biomnitrix_fusion_ability.name=§eBiomnitrix Dynamic Fusion Strike",
    "item.ben10:biomnitrix_fusion_suit.name=§eBiomnitrix Custom Fusion Suit"
]
for w in WATCHES:
    lang_lines.append(f"item.ben10:{w['id']}.name=§a{w['name']}")
    lang_lines.append(f"item.ben10:{w['id']}_recharging.name=§c{w['name']} (Recharging...)")
for a in ALL_ALIENS:
    lang_lines.append(f"item.ben10:{a['id']}_suit.name={a['color_code']}{a['name']} Suit")
    lang_lines.append(f"item.ben10:{a['id']}_ability.name={a['color_code']}{a['name']}: {a['ability_name']}")

# Series Bosses & Vehicles Lang
lang_lines.append("item.ben10:kevin_car_spawner.name=§aKevin's Car Key")
lang_lines.append("item.ben10:vilgax_spawner.name=§4Summon Vilgax")
lang_lines.append("item.ben10:battle_drone_spawner.name=§cDeploy Battle Drone")
lang_lines.append("item.ben10:vilgax_ship_spawner.name=§6Vilgax Ship Beacon")
lang_lines.append("entity.ben10:kevin_car.name=Kevin's Muscle Car")
lang_lines.append("entity.ben10:vilgax.name=Vilgax the Conqueror")
lang_lines.append("entity.ben10:battle_drone.name=Vilgax Battle Drone")
lang_lines.append("entity.ben10:vilgax_ship.name=Vilgax Drone Battleship")
lang_lines.append("action.interact.ride.car=Drive Kevin's Car")
lang_lines.append("action.interact.fly.ship=Pilot Warship")

with open(os.path.join(RP_DIR, "texts", "en_US.lang"), "w", encoding="utf-8") as f:
    f.write("\n".join(lang_lines) + "\n")
with open(os.path.join(RP_DIR, "texts", "languages.json"), "w", encoding="utf-8") as f:
    json.dump(["en_US"], f)

# 4. Manifests
UUID_BP_HEADER = "e4c3f248-5fd4-4fce-a16a-7f8278de7d59"
UUID_BP_DATA = "dfa444ca-78a6-4ff2-adf9-ea98c642e6e7"
UUID_BP_SCRIPT = "9902c22a-4507-459b-a465-bd0ccddcbae5"
UUID_RP_HEADER = "9eb93634-3b0c-42e5-8007-4ccf37f306ba"
UUID_RP_MODULE = "786a8dc5-ab73-45d8-9778-f55ee3bc92b1"

bp_manifest = {
    "format_version": 2,
    "header": {
        "name": "Ben 10: Omnitrix Origins (BP)",
        "description": "9 Legendary Omnitrixes, 76 Aliens, Humungousaur Titan Growth, Ultimates & Dynamic Biomnitrix Fusions! Smooth 60 FPS Mobile Optimized.",
        "uuid": UUID_BP_HEADER,
        "version": [2, 1, 0],
        "min_engine_version": [1, 21, 0]
    },
    "modules": [
        {"type": "data", "description": "Ben 10 Behavior Data", "uuid": UUID_BP_DATA, "version": [2, 1, 0]},
        {"type": "script", "description": "Ben 10 Logic Script", "uuid": UUID_BP_SCRIPT, "version": [2, 1, 0], "entry": "scripts/main.js"}
    ],
    "dependencies": [
        {"module_name": "@minecraft/server", "version": "1.13.0"},
        {"module_name": "@minecraft/server-ui", "version": "1.3.0"},
        {"uuid": UUID_RP_HEADER, "version": [2, 1, 0]}
    ]
}
with open(os.path.join(BP_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(bp_manifest, f, indent=2)

rp_manifest = {
    "format_version": 2,
    "header": {
        "name": "Ben 10: Omnitrix Origins (RP)",
        "description": "High performance textures, sound effects, Carnitrix horror effects, and alien models.",
        "uuid": UUID_RP_HEADER,
        "version": [2, 1, 0],
        "min_engine_version": [1, 21, 0]
    },
    "modules": [{"type": "resources", "description": "Ben 10 Assets", "uuid": UUID_RP_MODULE, "version": [2, 1, 0]}]
}
with open(os.path.join(RP_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(rp_manifest, f, indent=2)

# 5. Build 3D Player Animations (Wrist raise + Omnitrix Hand Slam) & Mobile HUD UI
build_player_animations(RP_DIR)
build_hud_ui(RP_DIR)

# 6. Modular JavaScript Files in BP/scripts/

watches_clean = [{"id": w["id"], "name": w["name"]} for w in WATCHES]
aliens_data_code = f"""export const WATCHES = {json.dumps(watches_clean, separators=(',', ':'))};
export const ALL_ALIENS = {json.dumps(ALL_ALIENS, separators=(',', ':'))};

export const WATCH_ALIENS = {{}};
for (const w of WATCHES) {{
  WATCH_ALIENS[w.id] = ALL_ALIENS.filter(a => a.watch === w.id);
}}

// Completed Omnitrix contains Master Access to all aliens
WATCH_ALIENS["omnitrix_completed"] = ALL_ALIENS.filter(a => a.watch === "omnitrix_classic" || a.watch === "omnitrix_recalibrated" || a.watch === "omnitrix_completed" || a.watch === "omnitrix_ultimatrix");

// Biomnitrix Dynamic Fusion Roster Pool
export const FUSION_POOL = ALL_ALIENS.filter(a => a.watch === "omnitrix_classic" || a.watch === "omnitrix_recalibrated" || a.watch === "omnitrix_completed");
"""
with open(os.path.join(BP_DIR, "scripts", "aliens_data.js"), "w", encoding="utf-8") as f:
    f.write(aliens_data_code)

# scripts/abilities.js (All skills and special attacks!)
with open(os.path.join(BP_DIR, "scripts", "abilities.js"), "w", encoding="utf-8") as f:
    f.write(get_abilities_code())

# scripts/main.js
with open(os.path.join(BP_DIR, "scripts", "main.js"), "w", encoding="utf-8") as f:
    f.write(get_main_code())

# 6. Helper functions
with open(os.path.join(BP_DIR, "functions", "ben10_give_all.mcfunction"), "w", encoding="utf-8") as f:
    lines = [f"give @s ben10:{w['id']} 1" for w in WATCHES]
    lines.append("give @s ben10:omnitrix_activator 1")
    lines.append("give @s ben10:detransform 1")
    lines.append("give @s ben10:kevin_car_spawner 1")
    lines.append("give @s ben10:vilgax_spawner 1")
    lines.append("give @s ben10:battle_drone_spawner 1")
    lines.append("give @s ben10:vilgax_ship_spawner 1")
    lines.append("title @s actionbar §aAll Omnitrixes, Omnitrix Activator, Bosses & Vehicles Received!\n")
    f.write("\n".join(lines))

for a in ALL_ALIENS:
    func_text = f"effect @s clear\nreplaceitem entity @s slot.armor.chest 0 ben10:{a['id']}_suit 1 0\ngive @s ben10:{a['id']}_ability 1\ngive @s ben10:detransform 1\ntitle @s title {a['color_code']}§l{a['name']}\ntitle @s subtitle §aTransformed!\n"
    with open(os.path.join(BP_DIR, "functions", f"transform_{a['id']}.mcfunction"), "w", encoding="utf-8") as f:
        f.write(func_text)

with open(os.path.join(BP_DIR, "functions", "detransform.mcfunction"), "w", encoding="utf-8") as f:
    f.write("effect @s clear\nreplaceitem entity @s slot.armor.chest 0 air 1 0\ntitle @s actionbar §aDetransformed!\n")

# 7. Zip packages
def zip_folder(source_dir, target_zip):
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, source_dir)
                zipf.write(abs_path, rel_path)

bp_mcpack = os.path.join(ADDON_DIR, "Ben10_BP.mcpack")
rp_mcpack = os.path.join(ADDON_DIR, "Ben10_RP.mcpack")
mcaddon_file = os.path.join(ADDON_DIR, "Ben10_Bedrock_Mobile_Edition.mcaddon")
workspace_mcaddon = os.path.join(BASE_DIR, "Ben10_Bedrock_Mobile_Edition.mcaddon")

zip_folder(BP_DIR, bp_mcpack)
zip_folder(RP_DIR, rp_mcpack)

with zipfile.ZipFile(mcaddon_file, 'w', zipfile.ZIP_DEFLATED) as addon_zip:
    for root, _, files in os.walk(BP_DIR):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.join("Ben10_BP", os.path.relpath(abs_path, BP_DIR))
            addon_zip.write(abs_path, rel_path)
    for root, _, files in os.walk(RP_DIR):
        for file in files:
            abs_path = os.path.join(root, file)
            rel_path = os.path.join("Ben10_RP", os.path.relpath(abs_path, RP_DIR))
            addon_zip.write(abs_path, rel_path)

shutil.copyfile(mcaddon_file, workspace_mcaddon)
print(f"Build complete! 9 Watches & {len(ALL_ALIENS)} Aliens. Output at {workspace_mcaddon}")
