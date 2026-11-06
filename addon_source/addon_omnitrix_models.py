# Ben 10 Bedrock Addon - Series Accurate 3D Omnitrix Models & Textures
# Complete with 3D wristbands, beveled bezels, pop-up buttons, and glowing hourglass cores
# Strictly under 1000 lines - Pure Python

from addon_graphics import make_png, hex_to_rgba
from addon_hd_item_art import create_hd_omnitrix_watch_icon, _blend, _darken, _lighten

# Backward-compatible delegate for 32x32 HD watch icons
def create_3d_watch_item_icon(band_hex, bezel_hex, dial_hex, glow_hex, core_hex, is_recharging=False, watch_id="omnitrix_classic"):
    return create_hd_omnitrix_watch_icon(watch_id, band_hex, bezel_hex, dial_hex, glow_hex, core_hex, is_recharging)

def generate_omnitrix_geometry(model_type="omnitrix_classic"):
    """
    Creates high-definition 3D Minecraft Bedrock geometries for each individual Omnitrix watch.
    Attached strictly to player's leftArm bone, tailored to sit naturally around the wrist.
    """
    cubes = []

    if model_type == "omnitrix_ultimatrix" or "ultimatrix" in model_type:
        # Ultimatrix: Full forearm gauntlet with 4 segmented stabilizer claws
        cubes = [
            # Main Forearm Gauntlet Base (wrist to mid-forearm: y 12.0 to 19.5)
            {
                "origin": [3.8, 12.0, -2.2],
                "size": [4.4, 7.5, 4.4],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 24]}, "*": {"uv": [0, 0], "uv_size": [4, 4]}},
                "inflate": 0.05
            },
            # Raised Circular Bezel Base on wrist
            {
                "origin": [4.0, 13.0, -3.1],
                "size": [4.0, 3.8, 0.9],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # Center Glowing Hourglass Dial Core
            {
                "origin": [4.4, 13.4, -3.3],
                "size": [3.2, 3.0, 0.3],
                "uv": {"north": {"uv": [20, 10], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            },
            # 4 Segmented Stabilizer Claws extending back towards the elbow
            {"origin": [3.7, 18.0, -2.3], "size": [0.8, 3.5, 0.8], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 8]}}},
            {"origin": [7.5, 18.0, -2.3], "size": [0.8, 3.5, 0.8], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 8]}}},
            {"origin": [3.7, 18.0, 1.5], "size": [0.8, 3.5, 0.8], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 8]}}},
            {"origin": [7.5, 18.0, 1.5], "size": [0.8, 3.5, 0.8], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 8]}}},
            # Side Evolution Push Button
            {"origin": [3.1, 14.0, -2.6], "size": [0.8, 1.4, 0.8], "uv": {"*": {"uv": [0, 20], "uv_size": [3, 3]}}}
        ]
    elif model_type == "omnitrix_carnitrix" or "carnitrix" in model_type:
        # Carnitrix: Corrupted bio-mechanical metal with organic jagged flesh-tendrils
        cubes = [
            # Main Rusted Iron Band
            {
                "origin": [3.85, 12.0, -2.15],
                "size": [4.3, 3.6, 4.3],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [8, 8]}}
            },
            # 4 Organic Bone Claws gripping the arm
            {"origin": [3.5, 11.2, -2.3], "size": [0.9, 2.0, 0.9], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 4]}}},
            {"origin": [7.6, 11.2, -2.3], "size": [0.9, 2.0, 0.9], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 4]}}},
            {"origin": [3.5, 14.5, 1.4], "size": [0.9, 2.0, 0.9], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 4]}}},
            {"origin": [7.6, 14.5, 1.4], "size": [0.9, 2.0, 0.9], "uv": {"*": {"uv": [32, 0], "uv_size": [4, 4]}}},
            # Corrupted Octagonal Bezel Base
            {
                "origin": [4.0, 12.3, -3.0],
                "size": [4.0, 3.0, 0.9],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # Bleeding Red Hourglass Dial Core
            {
                "origin": [4.4, 12.6, -3.3],
                "size": [3.2, 2.4, 0.4],
                "uv": {"north": {"uv": [20, 10], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            }
        ]
    elif model_type == "omnitrix_biomnitrix" or "biomnitrix" in model_type:
        # Biomnitrix: Royal Pearl-White and Gold Dual-Core Gauntlet
        cubes = [
            # Main White Band
            {
                "origin": [3.9, 12.0, -2.1],
                "size": [4.2, 3.4, 4.2],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 16]}, "*": {"uv": [48, 0], "uv_size": [8, 8]}}
            },
            # Gold Bezel Housing
            {
                "origin": [4.0, 12.2, -2.9],
                "size": [4.0, 3.0, 0.8],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # Dual Sync Cores (Left and Right)
            {
                "origin": [4.3, 12.5, -3.2],
                "size": [1.5, 2.4, 0.4],
                "uv": {"north": {"uv": [20, 10], "uv_size": [8, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            },
            {
                "origin": [6.2, 12.5, -3.2],
                "size": [1.5, 2.4, 0.4],
                "uv": {"north": {"uv": [28, 10], "uv_size": [8, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            }
        ]
    elif model_type == "omnitrix_completed" or "completed" in model_type:
        # Completed Omnitrix (Omniverse): White polymer chassis with green stripe and angular faceplate
        cubes = [
            # Main White Polymer Band
            {
                "origin": [3.9, 12.0, -2.1],
                "size": [4.2, 3.5, 4.2],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 16]}, "*": {"uv": [48, 0], "uv_size": [8, 8]}}
            },
            # Center Green Racing Stripe
            {
                "origin": [5.4, 11.9, -2.15],
                "size": [1.2, 3.7, 4.3],
                "uv": {"*": {"uv": [20, 10], "uv_size": [4, 4]}}
            },
            # Angular Faceplate
            {
                "origin": [4.1, 12.4, -2.9],
                "size": [3.8, 2.7, 0.8],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # Square Glowing Core
            {
                "origin": [4.4, 12.6, -3.2],
                "size": [3.2, 2.3, 0.4],
                "uv": {"north": {"uv": [20, 10], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            }
        ]
    elif model_type == "omnitrix_recalibrated" or "recalibrated" in model_type:
        # Recalibrated Omnitrix (Alien Force): Sleek black band, silver frame, circular green dial
        cubes = [
            # Sleek Matte Black Band
            {
                "origin": [3.95, 12.0, -2.05],
                "size": [4.1, 3.2, 4.1],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [8, 8]}}
            },
            # Silver Square Beveled Bezel
            {
                "origin": [4.1, 12.2, -2.8],
                "size": [3.8, 2.8, 0.8],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # Circular Dial with 4 Green Conduit Points
            {
                "origin": [4.4, 12.4, -3.1],
                "size": [3.2, 2.4, 0.4],
                "uv": {"north": {"uv": [20, 10], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [2, 2]}}
            }
        ]
    else:
        # Classic Omnitrix (and Ben 23 / Albedo / Reboot variations)
        # Wide Charcoal Casing, White Edge Stripes, Octagonal Bezel with 4 Corner Rivets, Red Pop-Up Button
        cubes = [
            # 1. Main Wrist Cuff Band (wraps arm cleanly, dark charcoal casing)
            {
                "origin": [3.9, 12.0, -2.1],
                "size": [4.2, 3.4, 4.2],
                "uv": {"north": {"uv": [0, 0], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [8, 8]}}
            },
            # 2. White Top & Bottom Wrist Straps
            {
                "origin": [3.85, 11.2, -2.15],
                "size": [4.3, 0.8, 4.3],
                "uv": {"*": {"uv": [48, 0], "uv_size": [8, 8]}}
            },
            {
                "origin": [3.85, 15.4, -2.15],
                "size": [4.3, 0.8, 4.3],
                "uv": {"*": {"uv": [48, 0], "uv_size": [8, 8]}}
            },
            # 3. Octagonal Bezel Base Plate
            {
                "origin": [4.0, 12.2, -2.9],
                "size": [4.0, 3.0, 0.8],
                "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [4, 4]}}
            },
            # 4. 4 Silver Rivet Screws at the 4 corners of the Octagon
            {"origin": [3.8, 14.8, -3.1], "size": [0.5, 0.5, 0.3], "uv": {"*": {"uv": [32, 0], "uv_size": [2, 2]}}},
            {"origin": [7.7, 14.8, -3.1], "size": [0.5, 0.5, 0.3], "uv": {"*": {"uv": [32, 0], "uv_size": [2, 2]}}},
            {"origin": [3.8, 12.1, -3.1], "size": [0.5, 0.5, 0.3], "uv": {"*": {"uv": [32, 0], "uv_size": [2, 2]}}},
            {"origin": [7.7, 12.1, -3.1], "size": [0.5, 0.5, 0.3], "uv": {"*": {"uv": [32, 0], "uv_size": [2, 2]}}},
            # 5. Raised Bezel Cylindrical Dial Rim
            {"origin": [4.3, 12.4, -3.2], "size": [3.4, 2.6, 0.4], "uv": {"north": {"uv": [20, 0], "uv_size": [16, 10]}, "*": {"uv": [20, 0], "uv_size": [2, 2]}}},
            # 6. Center Glowing Hourglass Dial (Emerald Core with 2 Black Triangles)
            {
                "origin": [4.5, 12.6, -3.35],
                "size": [3.0, 2.2, 0.2],
                "uv": {"north": {"uv": [20, 10], "uv_size": [16, 16]}, "*": {"uv": [0, 0], "uv_size": [1, 1]}}
            },
            # 7. Red Pop-Up Activation Release Button on Left Edge (9 o'clock)
            {"origin": [3.3, 13.0, -2.6], "size": [0.7, 1.4, 0.8], "uv": {"*": {"uv": [0, 20], "uv_size": [3, 3]}}}
        ]

    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": f"geometry.ben10.{model_type}",
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": 2,
                    "visible_bounds_height": 2,
                    "visible_bounds_offset": [0, 1, 0]
                },
                "bones": [
                    {
                        "name": "leftArm",
                        "pivot": [5, 22, 0],
                        "cubes": cubes
                    }
                ]
            }
        ]
    }

def create_omnitrix_model_texture(band_hex, bezel_hex, dial_hex, glow_hex, core_hex, is_recharging=False, watch_id="omnitrix_classic"):
    """
    Creates a full 64x64 HD texture matching the 3D model cubes:
    - Cuff band (0..19, 0..19)
    - Bezel plate (20..35, 0..9)
    - Hourglass Dial (20..35, 10..25) with glowing core & black triangles
    - Side Buttons & Rivets (0..7, 20..26)
    - White Straps (48..56, 0..8)
    """
    w, h = 64, 64
    data = bytearray(w * h * 4)
    c_band = hex_to_rgba(band_hex)
    c_bezel = hex_to_rgba(bezel_hex)
    c_dial = hex_to_rgba(dial_hex)
    c_glow = hex_to_rgba(glow_hex) if not is_recharging else hex_to_rgba("#ef4444")
    c_core = hex_to_rgba(core_hex) if not is_recharging else hex_to_rgba("#fca5a5")
    c_black = hex_to_rgba("#0f172a")
    c_silver = hex_to_rgba("#cbd5e1")
    c_trans = [0, 0, 0, 0]

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Wristband area (0,0 to 19,19)
            if 0 <= x < 20 and 0 <= y < 20:
                if x in (0, 19) or y in (0, 19):
                    pixel = _darken(c_band, 40)
                elif 8 <= x <= 11:
                    pixel = _darken(c_band, 25)
                else:
                    pixel = c_band

            # 2. Bezel Ring area (20,0 to 35,9)
            elif 20 <= x < 36 and 0 <= y < 10:
                pixel = c_silver if (x in (20, 35) or y in (0, 9)) else c_bezel

            # 3. Dial Face & Glowing Hourglass (20,10 to 35,25) -> EXACT 16x16 hourglass!
            elif 20 <= x < 36 and 10 <= y < 26:
                dx = (x - 27.5)
                dy = (y - 17.5)
                in_black_triangle = False
                if dx < 0 and abs(dy) < -dx * 0.95:
                    in_black_triangle = True
                elif dx > 0 and abs(dy) < dx * 0.95:
                    in_black_triangle = True

                if in_black_triangle:
                    pixel = c_black
                else:
                    dist = (dx * dx + dy * dy) ** 0.5
                    if dist <= 2.2:
                        pixel = c_core # Bright glowing center core
                    elif dist <= 5.5:
                        pixel = c_glow # Glowing hourglass wings
                    else:
                        pixel = c_dial

            # 4. Side Buttons & Rivets (0,20 to 10,26)
            elif 0 <= x < 10 and 20 <= y < 26:
                pixel = hex_to_rgba("#dc2626") if "classic" in watch_id else c_silver

            # 5. Claws & Corner Rivets (32,0 to 40,16)
            elif 32 <= x < 40 and 0 <= y < 16:
                pixel = c_silver if (x + y) % 2 == 0 else c_bezel

            # 6. White Top & Bottom Wrist Straps (48,0 to 56,8)
            elif 48 <= x < 56 and 0 <= y < 8:
                pixel = hex_to_rgba("#e2e8f0") if (x in (48, 55) or y in (0, 7)) else hex_to_rgba("#ffffff")

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))
