from addon_data_classic import CLASSIC_ALIENS
from addon_data_af_ult import AF_ALIENS, ULTIMATE_ALIENS
from addon_data_ov_au import OMNIVERSE_ALIENS, BEN23_ALIENS, REBOOT_ALIENS, CARNITRIX_ALIENS, ALBEDO_ALIENS

# 9 Omnitrix Watches
WATCHES = [
    {
        "id": "omnitrix_classic",
        "name": "Classic Omnitrix",
        "desc": "The original Prototype Omnitrix (2005) with 19 Classic Aliens",
        "band_hex": "#1f2421", "bezel_hex": "#9ca3af", "dial_hex": "#22c55e", "glow_hex": "#86efac",
        "recipe_keys": {"I": "minecraft:iron_ingot", "S": "minecraft:emerald", "E": "minecraft:ender_pearl"},
        "recipe_pattern": [" I ", "SES", " I "]
    },
    {
        "id": "omnitrix_recalibrated",
        "name": "Recalibrated Omnitrix",
        "desc": "The sleek Alien Force Omnitrix with Humungousaur Growth",
        "band_hex": "#0f172a", "bezel_hex": "#334155", "dial_hex": "#10b981", "glow_hex": "#a7f3d0",
        "recipe_keys": {"O": "ben10:omnitrix_classic", "D": "minecraft:diamond", "R": "minecraft:redstone"},
        "recipe_pattern": [" D ", "ROR", " D "]
    },
    {
        "id": "omnitrix_ultimatrix",
        "name": "The Ultimatrix",
        "desc": "Albedo's gauntlet featuring 13 Ultimate forms including fan-favorites",
        "band_hex": "#1e293b", "bezel_hex": "#0f766e", "dial_hex": "#14b8a6", "glow_hex": "#99f6e4",
        "recipe_keys": {"O": "ben10:omnitrix_recalibrated", "N": "minecraft:netherite_ingot", "A": "minecraft:amethyst_shard"},
        "recipe_pattern": [" A ", "NON", " A "]
    },
    {
        "id": "omnitrix_completed",
        "name": "Completed Omnitrix (Omniverse)",
        "desc": "Azmuth's definitive finished masterpiece with Master Control",
        "band_hex": "#f8fafc", "bezel_hex": "#16a34a", "dial_hex": "#4ade80", "glow_hex": "#bbf7d0",
        "recipe_keys": {"U": "ben10:omnitrix_ultimatrix", "N": "minecraft:nether_star", "E": "minecraft:emerald_block"},
        "recipe_pattern": [" E ", "NUN", " E "]
    },
    {
        "id": "biomnitrix_left",
        "name": "The Biomnitrix (Left Watch)",
        "desc": "Ben 10,000's Left Gauntlet: Select Alien 1 for Dynamic Fusion",
        "band_hex": "#ca8a04", "bezel_hex": "#713f12", "dial_hex": "#22c55e", "glow_hex": "#86efac",
        "recipe_keys": {"C": "ben10:omnitrix_completed", "G": "minecraft:gold_block", "E": "minecraft:echo_shard"},
        "recipe_pattern": [" G ", "ECE", " G "]
    },
    {
        "id": "biomnitrix_right",
        "name": "The Biomnitrix (Right Watch)",
        "desc": "Ben 10,000's Right Gauntlet: Select Alien 2 for Dynamic Fusion",
        "band_hex": "#ca8a04", "bezel_hex": "#713f12", "dial_hex": "#22c55e", "glow_hex": "#86efac",
        "recipe_keys": {"B": "ben10:biomnitrix_left", "G": "minecraft:gold_ingot"},
        "recipe_pattern": ["   ", "GBG", "   "]
    },
    {
        "id": "omnitrix_ben23",
        "name": "Ben 23's Hero Watch",
        "desc": "Dimension 23's billionaire electric-blue and gold watch",
        "band_hex": "#0284c7", "bezel_hex": "#eab308", "dial_hex": "#38bdf8", "glow_hex": "#bae6fd",
        "recipe_keys": {"O": "ben10:omnitrix_classic", "L": "minecraft:lapis_block", "G": "minecraft:gold_ingot"},
        "recipe_pattern": [" G ", "LOL", " G "]
    },
    {
        "id": "omnitrix_reboot",
        "name": "Reboot Omnitrix",
        "desc": "Omni-Enhanced & Omni-Kix high-tech modern watch",
        "band_hex": "#f8fafc", "bezel_hex": "#18181b", "dial_hex": "#84cc16", "glow_hex": "#bef264",
        "recipe_keys": {"O": "ben10:omnitrix_classic", "Q": "minecraft:quartz_block", "C": "minecraft:copper_ingot"},
        "recipe_pattern": [" C ", "QOQ", " C "]
    },
    {
        "id": "omnitrix_carnitrix",
        "name": "The Carnitrix (Horror AU)",
        "desc": "The gruesome biomechanical death-device created for devastation",
        "band_hex": "#18181b", "bezel_hex": "#450a0a", "dial_hex": "#991b1b", "glow_hex": "#ef4444",
        "recipe_keys": {"O": "ben10:omnitrix_classic", "S": "minecraft:skeleton_skull", "F": "minecraft:fermented_spider_eye"},
        "recipe_pattern": [" S ", "FOF", " S "]
    },
    {
        "id": "omnitrix_albedo",
        "name": "Albedo's Crimson Omnitrix",
        "desc": "Corrupted crimson Omnitrix wielded by Albedo",
        "band_hex": "#18181b", "bezel_hex": "#7f1d1d", "dial_hex": "#ef4444", "glow_hex": "#fca5a5",
        "recipe_keys": {"O": "ben10:omnitrix_classic", "R": "minecraft:redstone_block", "W": "minecraft:nether_wart"},
        "recipe_pattern": [" W ", "ROR", " W "]
    }
]

ALL_ALIENS = CLASSIC_ALIENS + AF_ALIENS + ULTIMATE_ALIENS + OMNIVERSE_ALIENS + BEN23_ALIENS + REBOOT_ALIENS + CARNITRIX_ALIENS + ALBEDO_ALIENS
print(f"Loaded {len(WATCHES)} Watches and {len(ALL_ALIENS)} Aliens successfully across clean modules!")
