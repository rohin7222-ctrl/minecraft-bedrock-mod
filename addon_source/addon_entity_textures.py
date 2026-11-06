# Ben 10 Bedrock Addon - Series Accurate Entity Textures (Maximum Visual Upgrade)
# Hand-crafted HD textures for Kevin's Car, Rust Bucket RV, Vilgax, Battle Drone, Kevin 11, Ship, and Pod
# Strictly under 1000 lines - Pure Python

from addon_graphics import make_png, hex_to_rgba
from addon_hd_item_art import _blend, _darken, _lighten

def create_kevin_car_texture():
    """128x128 HD Texture for Kevin Levin's Green Muscle Car (Dodge Dart with Blower & Dual Stripes)"""
    w, h = 128, 128
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_green = hex_to_rgba("#16a34a")
    c_green_hi = hex_to_rgba("#4ade80")
    c_green_sh = hex_to_rgba("#14532d")
    c_stripe = hex_to_rgba("#090d16")
    c_chrome = hex_to_rgba("#e2e8f0")
    c_chrome_sh = hex_to_rgba("#94a3b8")
    c_glass = hex_to_rgba("#0f172a")
    c_glass_hi = hex_to_rgba("#38bdf8")
    c_red_tail = hex_to_rgba("#ef4444")
    c_headlight = hex_to_rgba("#fef08a")
    c_tire = hex_to_rgba("#18181b")
    c_rim = hex_to_rgba("#cbd5e1")
    c_black = hex_to_rgba("#020617")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Lower Chassis (0..127, 0..35)
            if 0 <= y <= 35 and 0 <= x < 128:
                if y in (0, 35) or x in (0, 127):
                    pixel = c_green_sh
                elif y < 8:
                    pixel = c_black # Underside frame
                else:
                    pixel = c_green_hi if y in (10, 11) else c_green

            # 2. Flared Wheel Arches / Fenders (0..40, 36..47)
            elif 36 <= y <= 47 and 0 <= x <= 40:
                pixel = c_green_hi if y == 36 else (c_black if y >= 45 else c_green)

            # 3. Supercharger Blower Scoop (74..105, 48..61)
            elif 48 <= y <= 61 and 74 <= x <= 105:
                local_x = x - 74
                if local_x in (6, 7, 18, 19) and y in (53, 54):
                    pixel = hex_to_rgba("#dc2626") # Butterfly valve
                elif local_x in (5, 8, 17, 20) or y in (52, 55):
                    pixel = c_chrome
                else:
                    pixel = c_chrome_sh

            # 4. Front Hood & Rear Trunk (0..85, 62..75) with Dual Black Racing Stripes
            elif 62 <= y <= 75 and 0 <= x <= 85:
                if x <= 55: # Hood
                    if (22 <= x <= 25) or (30 <= x <= 33):
                        pixel = c_stripe
                    elif 26 <= x <= 29:
                        pixel = c_green
                    elif y in (62, 75) or x in (0, 55):
                        pixel = c_green_sh
                    else:
                        pixel = c_green_hi if y in (64, 65) else c_green
                else: # Trunk
                    local_trunk_x = x - 56
                    if (11 <= local_trunk_x <= 13) or (16 <= local_trunk_x <= 18):
                        pixel = c_stripe
                    else:
                        pixel = c_green

            # 5. Dual Chrome Intakes (74..85, 62..65)
            elif 62 <= y <= 65 and 74 <= x <= 85:
                pixel = c_chrome

            # 6. Cabin Greenhouse & Slanted Roof (0..55, 88..105)
            elif 88 <= y <= 105 and 0 <= x <= 55:
                if (22 <= x <= 25) or (30 <= x <= 33):
                    pixel = c_stripe
                elif 26 <= x <= 29:
                    pixel = c_green
                elif y in (88, 105) or x in (0, 55):
                    pixel = c_green_sh
                else:
                    pixel = c_green_hi if y in (90, 91) else c_green

            # 7. Front & Rear Windshields (78..96, 68..85)
            elif 68 <= y <= 85 and 78 <= x <= 96:
                if x in (78, 96) or y in (68, 77, 78, 85):
                    pixel = c_chrome_sh
                elif y in (70, 80) and x in (82, 83, 84):
                    pixel = c_glass_hi
                else:
                    pixel = c_glass

            # 8. Ducktail Spoiler Wing (60..90, 90..98)
            elif 90 <= y <= 98 and 60 <= x <= 90:
                pixel = c_stripe if y >= 96 else c_green_hi

            # 9. Front Bumper, Chrome Grille & Headlights (0..55, 118..127)
            elif 118 <= y <= 127 and 0 <= x <= 55:
                if x in (6, 7, 10, 11, 44, 45, 48, 49) and y in (120, 121, 122):
                    pixel = c_headlight
                elif 16 <= x <= 38 and y in (120, 121):
                    pixel = c_black
                else:
                    pixel = c_chrome

            # 10. Rear Bumper, Taillights & Twin Exhausts (64..127, 118..127)
            elif 118 <= y <= 127 and 64 <= x <= 127:
                if y in (120, 121) and (68 <= x <= 84 or 100 <= x <= 116):
                    pixel = c_red_tail
                elif y in (123, 124) and x in (72, 73, 112, 113):
                    pixel = c_chrome
                else:
                    pixel = c_chrome_sh

            # 11. Muscle Car 5-Spoke Wheels (80..105, 0..15)
            elif 0 <= y <= 15 and 80 <= x <= 105:
                dx = abs(x - 92.5)
                dy = abs(y - 7.5)
                dist_sq = dx * dx + dy * dy
                if dist_sq <= 49:
                    if dist_sq <= 6:
                        pixel = c_chrome
                    elif dist_sq <= 20:
                        pixel = c_rim if (int(dx * 2 + dy * 3) % 2 == 0) else c_black
                    elif dist_sq <= 30:
                        pixel = c_chrome
                    else:
                        pixel = c_tire

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_rustbucket_texture():
    """256x256 High-Fidelity HD Texture for Grandpa Max's Rust Bucket RV (Colossal Motorhome Plumber Base)"""
    w, h = 256, 256
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_cream = hex_to_rgba("#f8fafc")
    c_cream_sh = hex_to_rgba("#e2e8f0")
    c_stripe_red = hex_to_rgba("#dc2626")
    c_stripe_green = hex_to_rgba("#16a34a")
    c_chrome = hex_to_rgba("#cbd5e1")
    c_chrome_sh = hex_to_rgba("#94a3b8")
    c_glass = hex_to_rgba("#1e293b")
    c_glass_hi = hex_to_rgba("#38bdf8")
    c_headlight = hex_to_rgba("#fef08a")
    c_amber = hex_to_rgba("#f59e0b")
    c_tail_red = hex_to_rgba("#ef4444")
    c_tire = hex_to_rgba("#18181b")
    c_rim = hex_to_rgba("#e2e8f0")
    c_black = hex_to_rgba("#090d16")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Main Camper Body (0..180, 0..105)
            if 0 <= y <= 105 and 0 <= x <= 180:
                # Dual Iconic Side Stripes (Red top, Green bottom)
                if 48 <= y <= 54:
                    pixel = c_stripe_red
                elif 55 <= y <= 63:
                    pixel = c_stripe_green
                # Side Windows (Tinted glass with frames)
                elif 22 <= y <= 40 and (24 <= x <= 80 or 105 <= x <= 165) and (x % 30 < 22):
                    if y in (22, 40) or (x % 30 in (0, 21)):
                        pixel = c_chrome # Window frame
                    else:
                        pixel = c_glass_hi if y in (25, 26) and x % 6 == 0 else c_glass
                elif y in (0, 105) or x in (0, 180):
                    pixel = c_cream_sh
                else:
                    pixel = c_cream

            # 2. Front Cab Overhang & Windshield (0..90, 106..135)
            elif 106 <= y <= 135 and 0 <= x <= 90:
                if 112 <= y <= 128 and 12 <= x <= 78:
                    if x in (44, 45) or y in (112, 128):
                        pixel = c_chrome # Windshield wiper & frame
                    else:
                        pixel = c_glass
                else:
                    pixel = c_cream

            # 3. Front Heavy Bullbar Bumper & Quad Headlights (94..170, 106..135)
            elif 106 <= y <= 135 and 94 <= x <= 170:
                # Quad Round Headlights & Amber Indicators
                if (102 <= x <= 112 or 152 <= x <= 162) and 114 <= y <= 122:
                    pixel = c_headlight
                elif (114 <= x <= 118 or 146 <= x <= 150) and 116 <= y <= 120:
                    pixel = c_amber
                elif 124 <= x <= 140 and y in (116, 117):
                    pixel = c_black # Front radiator grille
                else:
                    pixel = c_chrome

            # 4. Roof AC Unit (0..90, 138..165)
            elif 138 <= y <= 165 and 0 <= x <= 90:
                pixel = c_black if (x % 4 == 0 and 144 <= y <= 158) else c_chrome_sh

            # 5. Plumber Satellite Radar Dish (94..130, 138..165)
            elif 138 <= y <= 165 and 94 <= x <= 130:
                pixel = hex_to_rgba("#22c55e") if (x in (110, 111, 112) and y in (148, 149, 150)) else c_chrome

            # 6. Rear Exterior Ladder (136..150, 138..165)
            elif 138 <= y <= 165 and 136 <= x <= 150:
                pixel = c_chrome # Steel tubular ladder

            # 7. Rear Spare Tire Mount (154..180, 138..165)
            elif 138 <= y <= 165 and 154 <= x <= 180:
                dx = abs(x - 167)
                dy = abs(y - 151)
                dist_sq = dx * dx + dy * dy
                if dist_sq <= 81:
                    pixel = c_stripe_green if dist_sq <= 30 else c_tire
                else:
                    pixel = c_chrome

            # 8. Heavy Underside Drive Chassis (0..180, 180..220)
            elif 180 <= y <= 220 and 0 <= x <= 180:
                pixel = c_black if (x + y) % 8 == 0 else hex_to_rgba("#1e293b")

            # 9. Heavy Duty RV Wheels (180..220, 0..30)
            elif 0 <= y <= 30 and 180 <= x <= 220:
                dx = abs(x - 200)
                dy = abs(y - 15)
                dist_sq = dx * dx + dy * dy
                if dist_sq <= 196:
                    if dist_sq <= 36:
                        pixel = c_rim
                    elif dist_sq <= 81:
                        pixel = c_black if int(dx + dy) % 3 == 0 else c_rim
                    else:
                        pixel = c_tire

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_vilgax_texture():
    """128x128 High-Definition Texture for Vilgax the Conqueror"""
    w, h = 128, 128
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_green = hex_to_rgba("#4d7c0f")
    c_green_dark = hex_to_rgba("#365314")
    c_armor = hex_to_rgba("#1e293b")
    c_armor_hi = hex_to_rgba("#334155")
    c_gold = hex_to_rgba("#eab308")
    c_gold_hi = hex_to_rgba("#fef08a")
    c_ruby = hex_to_rgba("#dc2626")
    c_ruby_glow = hex_to_rgba("#ef4444")
    c_bronze = hex_to_rgba("#78350f")
    c_black = hex_to_rgba("#090d16")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Alien Cephalopod Head (0..31, 0..15)
            if 0 <= y <= 15 and 0 <= x <= 31:
                if 8 <= x <= 15 and 8 <= y <= 15: # Front Face
                    if y == 11 and x == 10:
                        pixel = c_ruby_glow # Red eye
                    elif y in (13, 14, 15) and 10 <= x <= 14:
                        pixel = c_armor # Respirator mouth piece
                    else:
                        pixel = c_green_dark if y >= 12 else c_green
                else:
                    pixel = c_green

            # 2. Facial Squid Tentacles (Beard) (36..53, 0..15)
            elif 0 <= y <= 15 and 36 <= x <= 53:
                # 6 distinct segmented tentacles
                tentacle_col = (x - 36) % 3
                if tentacle_col == 2:
                    pixel = c_green_dark # Shadow between tentacles
                else:
                    pixel = c_green_dark if y >= 11 else c_green

            # 3. Glowing Cybernetic Eye Visor (56..65, 0..15)
            elif 0 <= y <= 15 and 56 <= x <= 65:
                pixel = c_ruby_glow if (58 <= x <= 63 and 3 <= y <= 8) else c_gold

            # 4. Armored Torso with Gold Warlord Cuirass (0..43, 18..40)
            elif 18 <= y <= 40 and 0 <= x <= 43:
                # Gold trim borders
                if x in (0, 43) or y in (18, 40) or (x in (21, 22) and 20 <= y <= 38):
                    pixel = c_gold
                elif 28 <= y <= 32 and 18 <= x <= 25:
                    pixel = c_ruby_glow # Ruby energy chest core
                else:
                    pixel = c_armor if (x + y) % 6 != 0 else c_armor_hi

            # 5. Spiked Shoulder Pauldrons (44..75, 18..40 and 76..107, 18..40)
            elif 18 <= y <= 40 and 44 <= x <= 107:
                if y in (18, 19) or x in (44, 75, 76, 107):
                    pixel = c_gold # Gold spiked rim
                else:
                    pixel = c_armor

            # 6. Cybernetic Right Arm & Ruby Blade (0..33, 44..68)
            elif 44 <= y <= 68 and 0 <= x <= 33:
                if 24 <= x <= 33:
                    # Glowing Translucent Ruby Blade
                    pixel = c_ruby_glow if x in (28, 29) else c_ruby
                else:
                    pixel = c_gold if y in (56, 57) else c_bronze

            # 7. Left Arm & Shield Emitter (34..70, 44..68)
            elif 44 <= y <= 68 and 34 <= x <= 70:
                if 58 <= x <= 70:
                    # Ruby Shield Emitter
                    pixel = c_ruby_glow if (62 <= x <= 66 and 50 <= y <= 56) else c_gold
                else:
                    pixel = c_bronze

            # 8. Plated Greaves & Combat Boots (0..47, 70..95)
            elif 70 <= y <= 95 and 0 <= x <= 47:
                if y in (70, 95) or x in (0, 23, 24, 47) or y == 82:
                    pixel = c_gold # Gold kneecap & boot trim
                else:
                    pixel = c_armor

            # 9. Warlord Skull Horns (64..80, 0..15)
            elif 0 <= y <= 15 and 64 <= x <= 80:
                pixel = c_gold if y <= 4 else c_bronze

            # 10. Cybernetic Respirator Harness & Tubes (0..40, 96..115)
            elif 96 <= y <= 115 and 0 <= x <= 40:
                if x in (8, 9, 28, 29) and y in (102, 103):
                    pixel = c_ruby_glow # Filter intake nodes
                elif y in (96, 115) or x in (0, 40):
                    pixel = c_gold # Gold reinforcement frame
                else:
                    pixel = c_bronze # Heavy breathing tubes

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_battle_drone_texture():
    """64x64 HD Texture for Vilgax Battle Drone (Combat Samurai Walker Droid)"""
    w, h = 64, 64
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_orange = hex_to_rgba("#ea580c")
    c_orange_hi = hex_to_rgba("#fb923c")
    c_dark = hex_to_rgba("#18181b")
    c_metal = hex_to_rgba("#71717a")
    c_ruby_eye = hex_to_rgba("#ef4444")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Samurai Sensor Head & Visor (0..31, 0..15)
            if 0 <= y <= 15 and 0 <= x <= 31:
                if 22 <= x <= 30 and 4 <= y <= 8:
                    pixel = c_ruby_eye # Horizontal Crimson Laser Visor
                else:
                    pixel = c_dark

            # 2. Carapace Body (0..40, 16..33)
            elif 16 <= y <= 33 and 0 <= x <= 40:
                if x in (0, 40) or y in (16, 33) or y == 24:
                    pixel = c_orange_hi # Orange hazard border
                else:
                    pixel = c_orange if (x + y) % 4 != 0 else c_dark

            # 3. Conical Helmet Brow (0..35, 34..47)
            elif 34 <= y <= 47 and 0 <= x <= 35:
                pixel = c_orange if y in (34, 47) else c_dark

            # 4. Cannon Arms (42..63, 16..47)
            elif 16 <= y <= 47 and 42 <= x <= 63:
                pixel = c_ruby_eye if y in (44, 45) else (c_orange if y <= 24 else c_metal)

            # 5. Spider Walker Legs (0..31, 48..63)
            elif 48 <= y <= 63 and 0 <= x <= 31:
                pixel = c_orange if y in (48, 63) else c_dark

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_kevin11_texture():
    """128x128 High-Definition Texture for Mutated Kevin 11 (Alien Amalgam Boss)"""
    w, h = 128, 128
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_fourarms = hex_to_rgba("#dc2626")
    c_fourarms_dark = hex_to_rgba("#991b1b")
    c_diamond = hex_to_rgba("#2dd4bf")
    c_diamond_dark = hex_to_rgba("#0f766e")
    c_heatblast = hex_to_rgba("#ea580c")
    c_magma = hex_to_rgba("#fef08a")
    c_ripjaws = hex_to_rgba("#0284c7")
    c_cannonbolt = hex_to_rgba("#eab308")
    c_xlr8_blue = hex_to_rgba("#38bdf8")
    c_black = hex_to_rgba("#090d16")
    c_white = hex_to_rgba("#ffffff")
    c_gold = hex_to_rgba("#facc15")
    c_eye_red = hex_to_rgba("#ef4444")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # 1. Split Face: Left Human/Fourarms, Right Magma (0..31, 0..15)
            if 0 <= y <= 15 and 0 <= x <= 31:
                if 8 <= x <= 15 and 8 <= y <= 15: # Front Face
                    if x < 12: # Left Half: Kevin's human pale/Fourarms red
                        if y == 11 and x == 10:
                            pixel = c_eye_red # Fourarms red eye
                        elif y <= 9:
                            pixel = c_black # Kevin's black hair
                        else:
                            pixel = c_fourarms
                    else: # Right Half: Heatblast Magma Stone
                        if y == 11 and x == 13:
                            pixel = c_magma # Yellow fire eye
                        elif y in (13, 14) and x in (13, 14):
                            pixel = c_heatblast # Lava seam
                        else:
                            pixel = hex_to_rgba("#78350f") # Obsidian rock
                elif y <= 7: # Forehead Fourarms Upper Eyes
                    if y == 6 and x in (10, 13):
                        pixel = c_gold # Golden upper eyes
                    else:
                        pixel = c_fourarms if x < 16 else hex_to_rgba("#78350f")
                else:
                    pixel = c_fourarms if x < 16 else hex_to_rgba("#78350f")

            # 2. Flame Crown (34..49, 0..15)
            elif 0 <= y <= 15 and 34 <= x <= 49:
                pixel = c_magma if (x in (38, 39, 44, 45) and y <= 8) else c_heatblast

            # 3. Torso: Left Fourarms Red Muscle with White Shirt, Right Heatblast Rock (0..33, 18..40)
            elif 18 <= y <= 40 and 0 <= x <= 33:
                if x < 16:
                    pixel = c_black if x in (7, 8) else (c_white if y <= 28 else c_fourarms)
                else:
                    pixel = c_magma if (x + y) % 5 == 0 else hex_to_rgba("#78350f")

            # 4. Diamondhead Back Spikes (34..47, 18..40)
            elif 18 <= y <= 40 and 34 <= x <= 47:
                pixel = c_diamond if (x + y) % 2 == 0 else c_diamond_dark

            # 5. Cannonbolt Shell on Back (48..63, 18..40)
            elif 18 <= y <= 40 and 48 <= x <= 63:
                pixel = c_cannonbolt if (x in (48, 63) or y in (18, 40)) else hex_to_rgba("#ca8a04")

            # 6. Upper Left Arm: Four Arms (0..21, 42..60)
            elif 42 <= y <= 60 and 0 <= x <= 21:
                pixel = c_gold if y in (52, 53) else c_fourarms

            # 7. Lower Left Arm: Ripjaws (22..39, 42..60)
            elif 42 <= y <= 60 and 22 <= x <= 39:
                pixel = c_white if y >= 56 and x % 2 == 0 else c_ripjaws

            # 8. Upper Right Arm: Heatblast (40..61, 42..60)
            elif 42 <= y <= 60 and 40 <= x <= 61:
                pixel = c_magma if (x + y) % 4 == 0 else hex_to_rgba("#78350f")

            # 9. Lower Right Arm: Diamondhead Crystal Blade (62..83, 42..60)
            elif 42 <= y <= 60 and 62 <= x <= 83:
                pixel = c_diamond if x in (68, 69, 78, 79) else c_diamond_dark

            # 10. XLR8 Speed Legs & Tail (0..60, 62..85)
            elif 62 <= y <= 85 and 0 <= x <= 60:
                if x >= 36: # Tail with black/blue stripes
                    pixel = c_xlr8_blue if (x // 3) % 2 == 0 else c_black
                else: # Speed legs with roller heels
                    pixel = c_xlr8_blue if (y in (66, 74, 80)) else c_black

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_vilgax_ship_texture():
    """128x128 HD Texture for Vilgax Drone Battleship"""
    w, h = 128, 128
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_hull = hex_to_rgba("#1e293b")
    c_panel = hex_to_rgba("#334155")
    c_red_glow = hex_to_rgba("#ef4444")
    c_engine = hex_to_rgba("#dc2626")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans
            if 0 <= y < 48 and 0 <= x < 64:
                pixel = c_red_glow if (x in (28, 29, 34, 35) and 20 <= y <= 28) else (c_hull if (x + y) % 6 != 0 else c_panel)
            elif 48 <= y < 70 and 0 <= x < 64:
                pixel = c_red_glow if y in (54, 55) else c_hull
            elif 0 <= y < 64 and 64 <= x < 128:
                # Engine Nacelles
                pixel = c_engine if (x >= 115 or y in (10, 50)) else c_hull
            elif 64 <= y < 128:
                pixel = c_red_glow if y >= 118 else c_panel
            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_meteor_pod_texture():
    """64x64 HD Texture for Crashed Omnitrix Meteor Pod"""
    w, h = 64, 64
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_rock = hex_to_rgba("#27272a")
    c_rock_dark = hex_to_rgba("#18181b")
    c_core = hex_to_rgba("#22c55e")
    c_glow = hex_to_rgba("#86efac")

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans
            if 0 <= y < 34 and 0 <= x < 34:
                # Meteor outer shell with heat scorch fissures
                pixel = c_glow if (x in (14, 15) and 8 <= y <= 24) else (c_rock if (x + y) % 5 != 0 else c_rock_dark)
            elif 34 <= y < 64 and 0 <= x < 34:
                # Open hydraulic hatch
                pixel = c_rock if y in (34, 63) or x in (0, 33) else c_rock_dark
            elif 34 <= y < 64 and 34 <= x < 64:
                # Internal Galvanic pedestal with glowing green core
                dx = abs(x - 49)
                dy = abs(y - 49)
                pixel = c_glow if dx + dy <= 4 else (c_core if dx + dy <= 8 else c_rock_dark)
            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))
