# Ben 10 Bedrock Addon - Custom Mobile HUD & Display UI
# Series-Accurate Top-Right Omnitrix Status Bar & Bottom Touch Dial
# Strictly under 1000 lines - Pure Python

import os
import json
from addon_graphics import make_png, hex_to_rgba
from addon_hd_item_art import _blend, _darken, _lighten

def create_hud_frame_texture():
    """
    128x32 High-Definition Omnitrix Status Capsule for Top-Right in-game HUD.
    Features titanium shell, glowing green edge glow, round Omnitrix dial gauge,
    and digital power level segment bars.
    """
    w, h = 128, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_shell = hex_to_rgba("#090d16")
    c_border_outer = hex_to_rgba("#16a34a")
    c_border_inner = hex_to_rgba("#334155")
    c_green = hex_to_rgba("#22c55e")
    c_glow = hex_to_rgba("#86efac")
    c_core = hex_to_rgba("#ffffff")
    c_black = hex_to_rgba("#020617")
    c_bar_empty = hex_to_rgba("#1e293b")

    cx, cy = 16.0, 15.5 # Center of round dial badge on left

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Round Omnitrix Dial Widget on Left (x: 2..30, y: 2..30)
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5

            if dist <= 14.5:
                if dist >= 13.0:
                    pixel = c_border_outer # Glowing green rim
                elif dist >= 11.5:
                    pixel = c_border_inner # Titanium bezel
                elif dist >= 9.5:
                    pixel = c_black
                else:
                    # Hourglass Dial
                    in_hg = False
                    if dy < 0 and abs(dx) <= -dy * 0.9:
                        in_hg = True
                    elif dy > 0 and abs(dx) <= dy * 0.9:
                        in_hg = True

                    if in_hg:
                        if dist <= 2.5:
                            pixel = c_core
                        elif dist <= 6.0:
                            pixel = c_glow
                        else:
                            pixel = c_green
                    else:
                        pixel = c_black

            # 2. Digital Readout Capsule on Right (x: 28..126, y: 4..28)
            elif 28 <= x <= 126 and 4 <= y <= 28:
                if x == 28 or x == 126 or y == 4 or y == 28:
                    pixel = c_border_outer # Tech green border
                elif x == 29 or x == 125 or y == 5 or y == 27:
                    pixel = c_border_inner
                else:
                    # Inside Digital LCD Screen
                    # Top Row: Text/Status Banner (y: 6..14)
                    if 6 <= y <= 14:
                        if 34 <= x <= 120 and y == 14:
                            pixel = hex_to_rgba("#14532d") # Separator line
                        else:
                            pixel = c_shell
                    # Bottom Row: 8-Segment Energy Battery Bar (y: 16..24, x: 36..118)
                    elif 16 <= y <= 24 and 36 <= x <= 118:
                        seg = (x - 36) // 10
                        seg_x = (x - 36) % 10
                        if seg_x == 9:
                            pixel = c_shell # Gap between segments
                        else:
                            if seg < 7: # Charged segments
                                pixel = c_green if (y in (16, 24) or seg_x in (0, 8)) else c_glow
                            else: # Depleted segment
                                pixel = c_bar_empty
                    else:
                        pixel = c_shell

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_ability_strip_texture():
    """80x16 5-Slot Ability Icon Sub-Bar for Quick Touch Triggers"""
    w, h = 80, 16
    data = bytearray(w * h * 4)
    c_bg = hex_to_rgba("#0f172a")
    c_border = hex_to_rgba("#475569")
    c_slot_active = hex_to_rgba("#22c55e")
    c_trans = [0, 0, 0, 0]

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            slot = x // 16
            local_x = x % 16

            if local_x in (0, 15) or y in (0, 15):
                pixel = c_border if slot > 0 else c_slot_active
            else:
                pixel = c_bg

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_carousel_slider_texture():
    """128x24 Bottom Carousel Alien Selector Bar"""
    w, h = 128, 24
    data = bytearray(w * h * 4)
    c_metal = hex_to_rgba("#cbd5e1")
    c_dark = hex_to_rgba("#1e293b")
    c_green = hex_to_rgba("#22c55e")
    c_trans = [0, 0, 0, 0]

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # Left Arrow [<] (x: 4..18, y: 4..20)
            if 4 <= x <= 18 and 4 <= y <= 20:
                pixel = c_green if (x == 10 and 8 <= y <= 16) or (x in (9, 11) and 9 <= y <= 15) else c_dark

            # Right Arrow [>] (x: 110..124, y: 4..20)
            elif 110 <= x <= 124 and 4 <= y <= 20:
                pixel = c_green if (x == 118 and 8 <= y <= 16) or (x in (117, 119) and 9 <= y <= 15) else c_dark

            # Center Slider Rails (x: 20..108, y: 8..16)
            elif 20 <= x <= 108 and 8 <= y <= 16:
                if 52 <= x <= 76:
                    pixel = c_green if y in (9, 15) or x in (53, 75) else c_dark
                else:
                    pixel = c_metal if y in (9, 15) else c_dark

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def get_hud_screen_ui():
    """Bedrock Custom UI for the Ben 10 Status HUD - Merged into in-game HUD"""
    return {
        "namespace": "ben10_hud",
        "omnitrix_hud_bar": {
            "type": "panel",
            "size": [128, 32],
            "anchor_from": "top_middle",
            "anchor_to": "top_middle",
            "offset": [0, 4],
            "controls": [
                {
                    "hud_bg@common.image": {
                        "texture": "textures/ui/omnitrix_hud_frame",
                        "size": [128, 32]
                    }
                }
            ]
        },
        "hud_screen": {
            "modifications": [
                {
                    "array_name": "root_panel_controls",
                    "operation": "insert_back",
                    "value": {
                        "ben10_omnitrix_hud@ben10_hud.omnitrix_hud_bar": {}
                    }
                }
            ]
        }
    }

def build_hud_ui(rp_dir):
    """Generates all UI textures and JSON layouts for the HUD screen"""
    ui_tex_dir = os.path.join(rp_dir, "textures", "ui")
    os.makedirs(ui_tex_dir, exist_ok=True)
    with open(os.path.join(ui_tex_dir, "omnitrix_hud_frame.png"), "wb") as f:
        f.write(create_hud_frame_texture())
    with open(os.path.join(ui_tex_dir, "omnitrix_ability_strip.png"), "wb") as f:
        f.write(create_ability_strip_texture())
    with open(os.path.join(ui_tex_dir, "omnitrix_carousel_slider.png"), "wb") as f:
        f.write(create_carousel_slider_texture())

    ui_dir = os.path.join(rp_dir, "ui")
    os.makedirs(ui_dir, exist_ok=True)
    with open(os.path.join(ui_dir, "hud_screen.json"), "w", encoding="utf-8") as f:
        json.dump(get_hud_screen_ui(), f, indent=2)
    with open(os.path.join(ui_dir, "_ui_defs.json"), "w", encoding="utf-8") as f:
        json.dump({"ui_defs": ["ui/hud_screen.json"]}, f, indent=2)

