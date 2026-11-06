# Ben 10 Bedrock Addon - Series Accurate Entity Textures
# Textures for Kevin's Car, Vilgax, Battle Drone, Vilgax Ship, Rust Bucket, Meteor Pod, and Kevin 11
# Strictly under 1000 lines - Pure Python

from addon_graphics import make_png, hex_to_rgba

def create_kevin_car_texture():
    """128x128 HD Texture for Kevin Levin's Green Muscle Car"""
    data = bytearray(128 * 128 * 4)
    c_green = hex_to_rgba("#16a34a")
    c_stripe = hex_to_rgba("#090d16")
    c_chrome = hex_to_rgba("#94a3b8")
    c_window = hex_to_rgba("#1e293b")
    c_red_tail = hex_to_rgba("#ef4444")
    c_headlight = hex_to_rgba("#fef08a")
    c_tire = hex_to_rgba("#18181b")
    c_rim = hex_to_rgba("#cbd5e1")
    c_trans = [0, 0, 0, 0]

    for y in range(128):
        for x in range(128):
            idx = (y * 128 + x) * 4
            pixel = c_trans

            if 0 <= y < 96 and 0 <= x < 64:
                if 28 <= x <= 31 or 34 <= x <= 37:
                    pixel = c_stripe
                elif 58 <= y <= 72 and 10 <= x <= 54:
                    pixel = c_window
                elif 44 <= y <= 48 and 20 <= x <= 44:
                    pixel = c_chrome
                else:
                    pixel = c_green if (x + y) % 3 != 0 else hex_to_rgba("#15803d")
            elif 96 <= y < 128 and 0 <= x < 64:
                pixel = c_headlight if x in (4, 5, 58, 59) else (c_red_tail if y > 120 else c_chrome)
            elif 0 <= y < 32 and 96 <= x < 128:
                dx = abs(x - 112)
                dy = abs(y - 16)
                if dx * dx + dy * dy <= 49:
                    pixel = c_rim if dx * dx + dy * dy <= 16 else c_tire
                else:
                    pixel = c_trans
            data[idx:idx+4] = bytes(pixel)

    return make_png(128, 128, bytes(data))

def create_vilgax_texture():
    """64x64 HD Texture for Vilgax the Conqueror"""
    data = bytearray(64 * 64 * 4)
    c_skin = hex_to_rgba("#4d7c0f")
    c_armor = hex_to_rgba("#1e293b")
    c_gold = hex_to_rgba("#eab308")
    c_ruby = hex_to_rgba("#dc2626")
    c_eye = hex_to_rgba("#ef4444")
    c_respirator = hex_to_rgba("#64748b")
    c_trans = [0, 0, 0, 0]

    for y in range(64):
        for x in range(64):
            idx = (y * 64 + x) * 4
            pixel = c_trans
            if 0 <= y < 16 and 0 <= x < 32:
                if y in (6, 7) and x in (11, 14):
                    pixel = c_eye
                elif y >= 8 and 10 <= x <= 15:
                    pixel = c_respirator
                else:
                    pixel = c_skin
            elif 16 <= y < 40 and 0 <= x < 40:
                if y in (16, 17) or x in (0, 39):
                    pixel = c_gold
                elif (x + y) % 4 == 0:
                    pixel = c_ruby
                else:
                    pixel = c_armor
            elif 40 <= y < 64:
                pixel = c_ruby if (x + y) % 3 == 0 else c_armor
            data[idx:idx+4] = bytes(pixel)

    return make_png(64, 64, bytes(data))

def create_battle_drone_texture():
    """64x64 HD Texture for Vilgax Battle Drone (Orange & dark grey)"""
    data = bytearray(64 * 64 * 4)
    c_orange = hex_to_rgba("#ea580c")
    c_dark = hex_to_rgba("#18181b")
    c_red_eye = hex_to_rgba("#ef4444")
    c_metal = hex_to_rgba("#71717a")
    c_trans = [0, 0, 0, 0]

    for y in range(64):
        for x in range(64):
            idx = (y * 64 + x) * 4
            pixel = c_trans
            if 0 <= y < 16 and 0 <= x < 32:
                pixel = c_red_eye if y in (6, 7) and 8 <= x <= 16 else c_dark
            elif 16 <= y < 32 and 0 <= x < 32:
                pixel = c_orange if (x + y) % 2 == 0 else hex_to_rgba("#c2410c")
            elif 32 <= y < 48:
                pixel = c_dark if y >= 40 else c_metal
            elif 48 <= y < 64:
                pixel = c_orange if x >= 20 else c_metal
            data[idx:idx+4] = bytes(pixel)

    return make_png(64, 64, bytes(data))

def create_vilgax_ship_texture():
    """128x128 HD Texture for Vilgax's Drone Battleship"""
    data = bytearray(128 * 128 * 4)
    c_hull = hex_to_rgba("#9a3412")
    c_panel = hex_to_rgba("#7c2d12")
    c_red_glow = hex_to_rgba("#ef4444")
    c_engine = hex_to_rgba("#1c1917")
    c_trans = [0, 0, 0, 0]

    for y in range(128):
        for x in range(128):
            idx = (y * 128 + x) * 4
            pixel = c_trans
            if 0 <= y < 48 and 0 <= x < 64:
                pixel = c_hull if (x + y) % 4 != 0 else c_panel
            elif 48 <= y < 70 and 0 <= x < 64:
                pixel = c_red_glow if (x % 4 == 0) else c_engine
            elif 0 <= y < 64 and 64 <= x < 128:
                pixel = c_hull if (x + y) % 3 == 0 else c_panel
            elif 64 <= y < 128:
                pixel = c_red_glow if y >= 110 else c_engine
            data[idx:idx+4] = bytes(pixel)

    return make_png(128, 128, bytes(data))

def create_rustbucket_texture():
    """128x128 HD Texture for Grandpa Max's Rust Bucket RV Camper (Idea 81)"""
    data = bytearray(128 * 128 * 4)
    c_white = hex_to_rgba("#f8fafc")
    c_stripe_green = hex_to_rgba("#16a34a")
    c_stripe_red = hex_to_rgba("#dc2626")
    c_chrome = hex_to_rgba("#94a3b8")
    c_window = hex_to_rgba("#1e293b")
    c_tire = hex_to_rgba("#18181b")
    c_rim = hex_to_rgba("#cbd5e1")
    c_trans = [0, 0, 0, 0]

    for y in range(128):
        for x in range(128):
            idx = (y * 128 + x) * 4
            pixel = c_trans
            if 0 <= y < 70 and 0 <= x < 90:
                if 32 <= y <= 35:
                    pixel = c_stripe_red
                elif 36 <= y <= 40:
                    pixel = c_stripe_green
                elif 14 <= y <= 24 and 10 <= x <= 80 and x % 16 < 12:
                    pixel = c_window
                else:
                    pixel = c_white if (x + y) % 5 != 0 else hex_to_rgba("#e2e8f0")
            elif 70 <= y < 100:
                pixel = c_window if y <= 85 and 0 <= x < 40 else c_chrome
            elif 0 <= y < 32 and 96 <= x < 128:
                dx = abs(x - 112)
                dy = abs(y - 16)
                if dx * dx + dy * dy <= 49:
                    pixel = c_rim if dx * dx + dy * dy <= 16 else c_tire
            data[idx:idx+4] = bytes(pixel)

    return make_png(128, 128, bytes(data))

def create_meteor_pod_texture():
    """64x64 HD Texture for Crashed Omnitrix Meteor Pod (Idea 82)"""
    data = bytearray(64 * 64 * 4)
    c_rock = hex_to_rgba("#27272a")
    c_crater = hex_to_rgba("#18181b")
    c_galvan_core = hex_to_rgba("#22c55e")
    c_omni_glow = hex_to_rgba("#86efac")
    c_trans = [0, 0, 0, 0]

    for y in range(64):
        for x in range(64):
            idx = (y * 64 + x) * 4
            pixel = c_trans
            if 0 <= y < 30 and 0 <= x < 32:
                pixel = c_rock if (x + y) % 3 != 0 else c_crater
            elif 30 <= y < 64 and 0 <= x < 32:
                pixel = c_omni_glow if (x + y) % 4 == 0 else c_galvan_core
            elif 0 <= y < 32 and 32 <= x < 64:
                pixel = c_omni_glow if (x in (46, 47, 48) and y in (14, 15, 16)) else c_rock
            data[idx:idx+4] = bytes(pixel)

    return make_png(64, 64, bytes(data))

def create_kevin11_texture():
    """64x64 HD Texture for Mutated Kevin 11 Amalgam Boss (Idea 84)"""
    data = bytearray(64 * 64 * 4)
    c_fourarms = hex_to_rgba("#dc2626")
    c_diamond = hex_to_rgba("#2dd4bf")
    c_heatblast = hex_to_rgba("#ea580c")
    c_black = hex_to_rgba("#0f172a")
    c_white = hex_to_rgba("#ffffff")
    c_eye_red = hex_to_rgba("#ef4444")
    c_eye_yellow = hex_to_rgba("#facc15")
    c_trans = [0, 0, 0, 0]

    for y in range(64):
        for x in range(64):
            idx = (y * 64 + x) * 4
            pixel = c_trans
            if 0 <= y < 16 and 0 <= x < 32:
                if y == 10 and x in (10, 13):
                    pixel = c_eye_red if x < 12 else c_eye_yellow
                else:
                    pixel = c_fourarms if x < 16 else c_diamond
            elif 16 <= y < 32 and 0 <= x < 40:
                if x < 20:
                    pixel = c_white if y < 28 else c_black
                else:
                    pixel = c_heatblast if (x + y) % 2 == 0 else hex_to_rgba("#78350f")
            elif 32 <= y < 64:
                pixel = c_diamond if x >= 32 else (c_fourarms if (x + y) % 2 == 0 else c_black)
            data[idx:idx+4] = bytes(pixel)

    return make_png(64, 64, bytes(data))
