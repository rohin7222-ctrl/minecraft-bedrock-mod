# Ben 10 Bedrock Addon - Series Accurate 32x32 HD Item Art & Badges
# Pure Python PNG generation - Hand-Crafted Solid Pixel Art (Zero Noise / Zero Dither)
# Strictly under 1000 lines

from addon_graphics import make_png, hex_to_rgba

def _darken(c, amount=40):
    return [max(0, c[0] - amount), max(0, c[1] - amount), max(0, c[2] - amount), c[3]]

def _lighten(c, amount=50):
    return [min(255, c[0] + amount), min(255, c[1] + amount), min(255, c[2] + amount), c[3]]

def _blend(c1, c2, factor=0.5):
    return [
        int(c1[0] * (1.0 - factor) + c2[0] * factor),
        int(c1[1] * (1.0 - factor) + c2[1] * factor),
        int(c1[2] * (1.0 - factor) + c2[2] * factor),
        int(c1[3] * (1.0 - factor) + c2[3] * factor)
    ]

def create_hd_omnitrix_watch_icon(watch_id, band_hex, bezel_hex, dial_hex, glow_hex, core_hex, is_recharging=False):
    """
    Generates a solid, cartoon-accurate 32x32 Omnitrix item icon.
    Features:
    - Shaded curved wristband with white straps (Classic) / green stripe (Omniverse)
    - Octagonal metallic bezel with 4 silver corner rivets
    - Red pop-up activation button on 9 o'clock side
    - Authentic glowing green dial with 2 bold black triangular side wedges pointing inward
    - White-hot luminous core in the hourglass center
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_band = hex_to_rgba(band_hex)
    c_bezel = hex_to_rgba(bezel_hex)
    c_glow = hex_to_rgba(glow_hex) if not is_recharging else hex_to_rgba("#ef4444")
    c_core = hex_to_rgba(core_hex) if not is_recharging else hex_to_rgba("#fca5a5")
    c_black = hex_to_rgba("#090d16")
    c_silver = hex_to_rgba("#cbd5e1")
    c_white = hex_to_rgba("#ffffff")
    c_red_btn = hex_to_rgba("#dc2626")

    is_classic = "classic" in watch_id or "prototype" in watch_id
    is_ult = "ultimatrix" in watch_id
    is_ov = "completed" in watch_id or "omniverse" in watch_id
    is_carn = "carnitrix" in watch_id
    is_b23 = "ben23" in watch_id
    is_bio = "biomnitrix" in watch_id

    cx, cy = 15.5, 13.5 # Bezel Center

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5

            # 1. Wristband Strap (y: 15..30)
            if 15 <= y <= 30:
                band_left = int(7.0 + (y - 15) * 0.3)
                band_right = int(24.0 - (y - 15) * 0.3)
                if band_left <= x <= band_right:
                    if x == band_left or x == band_right or y == 30:
                        pixel = _darken(c_band, 55) # Deep shadow outline
                    elif is_classic and (y in (17, 18) or y in (26, 27)):
                        pixel = c_white if x < 16 else c_silver # Classic white straps
                    elif is_ov and 14 <= x <= 17:
                        pixel = hex_to_rgba("#22c55e") # Omniverse green racing stripe
                    elif is_b23 and (x in (band_left + 1, band_right - 1)):
                        pixel = hex_to_rgba("#eab308") # Ben 23 gold edge trim
                    elif is_carn and (x in (9, 14, 21) or y in (20, 24)):
                        pixel = hex_to_rgba("#7f1d1d") # Carnitrix rusted bio-metal
                    else:
                        # Smooth horizontal gradient: highlight on left, shadow on right
                        if x <= band_left + 2:
                            pixel = _lighten(c_band, 35)
                        elif x <= 16:
                            pixel = c_band
                        else:
                            pixel = _darken(c_band, 30)

            # 2. Side Buttons & Features
            if is_classic:
                # Classic Red Pop-Up Activation Release Button on Left (x: 2..5, y: 11..15)
                if 2 <= x <= 5 and 12 <= y <= 15:
                    if x == 2 or y == 15:
                        pixel = _darken(c_red_btn, 40)
                    elif y == 12 or x == 3:
                        pixel = _lighten(c_red_btn, 45) # Button top highlight
                    else:
                        pixel = c_red_btn
            elif is_ult:
                # Ultimatrix Stabilizer Claws extending up forearm
                if (x in (3, 4, 27, 28) and 8 <= y <= 20) or (x in (5, 6, 25, 26) and y in (7, 8)):
                    pixel = c_silver if x in (3, 27) else _darken(c_silver, 30)

            # 3. Outer Octagonal / Beveled Bezel (dist <= 12.0)
            if dist <= 12.0:
                if dist >= 10.0:
                    # Octagonal outer bezel plate
                    if dist >= 11.2:
                        pixel = _darken(c_bezel, 50) # Outer rim border
                    elif dy < -2:
                        pixel = _lighten(c_bezel, 40) # Top rim highlight
                    elif dy > 2:
                        pixel = _darken(c_bezel, 30) # Bottom rim shadow
                    else:
                        pixel = c_bezel

                    # 4 Silver Corner Rivets on Classic/Omniverse
                    if (is_classic or is_b23) and dist >= 10.2:
                        if (x in (6, 7, 24, 25) and y in (5, 6, 21, 22)):
                            pixel = c_white if y <= 6 else c_silver
                elif dist >= 8.0:
                    # Inner Metallic Dial Rim
                    pixel = c_black if not is_recharging else hex_to_rgba("#450a0a")
                else:
                    # 4. Dial Face: BOLD GLOWING GREEN with TWO BLACK SIDE WEDGES
                    # Left black wedge: cuts in from west toward center
                    # Right black wedge: cuts in from east toward center
                    is_black_wedge = False
                    if dx < -0.8: # Left side
                        if abs(dy) < (-dx * 0.88):
                            is_black_wedge = True
                    elif dx > 0.8: # Right side
                        if abs(dy) < (dx * 0.88):
                            is_black_wedge = True

                    if is_black_wedge:
                        pixel = c_black
                    else:
                        # Glowing Hourglass: Top, Center, Bottom
                        if dist <= 2.2:
                            pixel = c_core # Blazing white/bright lime center core
                        elif dist <= 5.0:
                            pixel = c_glow # Vivid emerald / electric cyan / crimson
                        else:
                            pixel = _darken(c_glow, 25)

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_omnitrix_activator_icon():
    """
    32x32 Holographic Omnitrix Activator Disc (Image 1 reference).
    A high-tech metallic ring with 4 glowing green conduits and a bold glowing hourglass core.
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_metal_light = hex_to_rgba("#94a3b8")
    c_metal_dark = hex_to_rgba("#1e293b")
    c_metal_border = hex_to_rgba("#0f172a")
    c_green = hex_to_rgba("#22c55e")
    c_glow = hex_to_rgba("#86efac")
    c_core = hex_to_rgba("#ffffff")
    c_black = hex_to_rgba("#020617")

    cx, cy = 15.5, 15.5

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            pixel = c_trans

            if dist <= 15.0:
                if dist >= 13.5:
                    pixel = c_metal_border
                elif dist >= 11.5:
                    pixel = c_metal_light if (dx - dy) > 0 else c_metal_dark
                elif dist >= 10.0:
                    pixel = c_metal_border
                elif dist >= 8.5:
                    # 4 Glowing green energy conduits pointing inward at 12, 3, 6, 9 o'clock
                    if abs(dx) <= 1.5 or abs(dy) <= 1.5:
                        pixel = c_green
                    else:
                        pixel = c_metal_dark
                elif dist > 7.0:
                    pixel = c_black
                else:
                    # Center Glowing Hourglass Dial
                    is_black_wedge = False
                    if dx < -0.8:
                        if abs(dy) < (-dx * 0.88):
                            is_black_wedge = True
                    elif dx > 0.8:
                        if abs(dy) < (dx * 0.88):
                            is_black_wedge = True

                    if is_black_wedge:
                        pixel = c_black
                    else:
                        if dist <= 2.2:
                            pixel = c_core
                        elif dist <= 5.0:
                            pixel = c_glow
                        else:
                            pixel = c_green

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_detransform_icon():
    """
    32x32 Emergency Detransform / Revert Badge.
    Crimson warning hexagon with hazard borders and illuminated white human runner silhouette.
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_red_border = hex_to_rgba("#991b1b")
    c_red_bright = hex_to_rgba("#ef4444")
    c_dark_bg = hex_to_rgba("#18181b")
    c_white = hex_to_rgba("#ffffff")
    c_yellow = hex_to_rgba("#facc15")

    cx, cy = 15.5, 15.5

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            pixel = c_trans

            q_hex = abs(dx) * 0.866 + abs(dy) * 0.5
            hex_dist = max(q_hex, abs(dy))

            if hex_dist <= 15.0:
                if hex_dist >= 13.0:
                    pixel = c_red_border
                elif hex_dist >= 11.5:
                    # Solid yellow and red warning stripes on corners
                    pixel = c_yellow if (x < 10 or x > 21) else c_red_bright
                elif hex_dist >= 10.0:
                    pixel = c_red_border
                else:
                    pixel = c_dark_bg

                    # Human Runner Detransform Silhouette (Solid White Pixels)
                    # Head (circle at 15.5, 9.5)
                    h_dx = x - 15.5
                    h_dy = y - 9.5
                    if (h_dx * h_dx + h_dy * h_dy) <= 4.5:
                        pixel = c_white
                    # Torso (14..17, 12..18)
                    elif 14 <= x <= 17 and 12 <= y <= 18:
                        pixel = c_white
                    # Running Left Arm (forward)
                    elif (10 <= x <= 13 and y == 13) or (9 <= x <= 11 and y == 14):
                        pixel = c_white
                    # Running Right Arm (back)
                    elif (18 <= x <= 21 and y == 15) or (20 <= x <= 22 and y == 16):
                        pixel = c_white
                    # Running Forward Leg
                    elif (12 <= x <= 15 and y == 19) or (10 <= x <= 13 and y == 21) or (8 <= x <= 11 and y == 22):
                        pixel = c_white
                    # Running Back Leg
                    elif (16 <= x <= 18 and y == 19) or (18 <= x <= 20 and y == 21) or (20 <= x <= 22 and y == 23):
                        pixel = c_white

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_fusion_icon():
    """
    32x32 Biomnitrix Dual Fusion DNA Matrix Icon.
    Gold gauntlet bezel with clean intertwining green and cyan DNA helix ribbons.
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_gold = hex_to_rgba("#eab308")
    c_gold_dark = hex_to_rgba("#854d0e")
    c_green = hex_to_rgba("#22c55e")
    c_cyan = hex_to_rgba("#06b6d4")
    c_white = hex_to_rgba("#ffffff")
    c_dark = hex_to_rgba("#090d16")

    cx, cy = 15.5, 15.5

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            pixel = c_trans

            if dist <= 15.0:
                if dist >= 13.5:
                    pixel = c_gold_dark
                elif dist >= 11.5:
                    pixel = c_gold
                elif dist >= 10.0:
                    pixel = c_gold_dark
                else:
                    pixel = c_dark
                    import math
                    sine_g = math.sin(y * 0.45) * 6.0
                    sine_c = -sine_g

                    diff_g = abs(dx - sine_g)
                    diff_c = abs(dx - sine_c)

                    # Base pair rungs
                    if y in (8, 12, 16, 20, 24) and abs(dx) <= 6.0:
                        pixel = c_gold_dark

                    if diff_g <= 1.3:
                        pixel = c_white if diff_g <= 0.6 else c_green
                    elif diff_c <= 1.3:
                        pixel = c_white if diff_c <= 0.6 else c_cyan

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_alien_badge_icon(alien_id, base_hex, detail_hex, accent_hex):
    """
    32x32 HD Series-Accurate Alien Badge Icons.
    Features:
    - Titanium dark bezel with glowing green Omnitrix tech rim
    - Crisp, solid-color cartoon silhouettes & facial features (NO noise, NO checkerboards)
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_base = hex_to_rgba(base_hex)
    c_det = hex_to_rgba(detail_hex)
    c_acc = hex_to_rgba(accent_hex)
    c_metal_rim = hex_to_rgba("#0f172a")
    c_omni_green = hex_to_rgba("#22c55e")
    c_omni_glow = hex_to_rgba("#86efac")
    c_white = hex_to_rgba("#ffffff")
    c_black = hex_to_rgba("#020617")
    c_gold = hex_to_rgba("#facc15")
    c_silver = hex_to_rgba("#cbd5e1")

    cx, cy = 15.5, 15.5

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5
            pixel = c_trans

            # 1. Bezel & Outer Tech Rim (dist <= 15.0)
            if dist <= 15.0:
                if dist >= 13.5:
                    pixel = c_metal_rim
                elif dist >= 12.0:
                    pixel = c_omni_glow if dy < -4 else c_omni_green # Glowing green tech rim
                elif dist >= 10.5:
                    pixel = c_metal_rim
                else:
                    # 2. Inside Species Emblem Face Area
                    pixel = _darken(c_base, 65) # Deep contrast background

                    # Species Face Artwork (Solid shapes with clean pixel anatomy)
                    if "heatblast" in alien_id:
                        # Solid Charcoal Obsidian Rock Face + Solid Orange/Yellow Fire Hair + Glowing Eyes
                        if 10 <= x <= 21 and 8 <= y <= 23:
                            if y <= 11:
                                # Fire Crown Hair (Solid bright flame)
                                pixel = hex_to_rgba("#facc15") if y in (9, 10) and 13 <= x <= 18 else hex_to_rgba("#ea580c")
                            elif y in (15, 16) and x in (12, 13, 18, 19):
                                pixel = c_white # Glowing Fire Eyes
                            elif y == 19 and 14 <= x <= 17:
                                pixel = hex_to_rgba("#ea580c") # Molten mouth
                            else:
                                pixel = hex_to_rgba("#78350f") # Obsidian rock face
                    elif "four_arms" in alien_id or "fourarms" in alien_id:
                        # Crimson Tetramand Face + Black Mohawk + 4 Sharp Golden Eyes
                        if 10 <= x <= 21 and 8 <= y <= 24:
                            if 15 <= x <= 16 and y <= 17:
                                pixel = c_black # Central crest
                            elif (y in (13, 14) and x in (12, 13, 18, 19)) or (y in (17, 18) and x in (11, 12, 19, 20)):
                                pixel = c_gold # 4 Golden Eyes
                            elif y == 21 and 13 <= x <= 18:
                                pixel = c_black # Mouth chin
                            else:
                                pixel = hex_to_rgba("#b91c1c") # Crimson Tetramand skin
                    elif "xlr8" in alien_id:
                        # Sleek Black Helmet + Solid Bright Cyan Visor + Green Slit Eyes
                        if 9 <= x <= 22 and 7 <= y <= 25:
                            if 12 <= x <= 19 and 12 <= y <= 18:
                                if y in (14, 15) and x in (14, 17):
                                    pixel = hex_to_rgba("#4ade80") # Green slit eye
                                else:
                                    pixel = hex_to_rgba("#38bdf8") # Cyan visor
                            else:
                                pixel = hex_to_rgba("#0f172a") # Glossy black helmet
                    elif "diamondhead" in alien_id:
                        # Sharp Cyan Crystal Face + Back Horn Spikes + Yellow Eyes
                        if 9 <= x <= 23 and 7 <= y <= 24:
                            if y <= 10 and x >= 17:
                                pixel = hex_to_rgba("#5eead4") # Crystal crown spike
                            elif y in (14, 15) and x in (12, 13):
                                pixel = c_gold # Yellow eyes
                            elif x in (10, 11) or y >= 21:
                                pixel = hex_to_rgba("#0f766e") # Facet shadow
                            else:
                                pixel = hex_to_rgba("#2dd4bf") # Pure cyan crystal
                    elif "ripjaws" in alien_id:
                        # Deep Blue Sea Predator + Glowing Angler Lure + White Fangs
                        if y <= 9 and 15 <= x <= 16:
                            pixel = hex_to_rgba("#4ade80") # Bioluminescent green lure
                        elif 9 <= x <= 22 and 10 <= y <= 24:
                            if y in (18, 19) and 11 <= x <= 20:
                                pixel = c_white if x in (12, 14, 17, 19) else hex_to_rgba("#7f1d1d")
                            elif y in (13, 14) and x in (11, 20):
                                pixel = hex_to_rgba("#38bdf8") # Fish eyes
                            else:
                                pixel = hex_to_rgba("#0284c7")
                    elif "upgrade" in alien_id:
                        # Jet Black Nanite Chassis + Concentric Neon Green Optic & Circuit Traces
                        if dist <= 8.5:
                            if dist <= 2.2:
                                pixel = hex_to_rgba("#86efac") # Center optic core
                            elif 3.5 <= dist <= 5.0:
                                pixel = c_omni_green # Concentric optic ring
                            elif (abs(dx) <= 0.8 and y >= 19) or (abs(dy) <= 0.8 and dist <= 7.5):
                                pixel = c_omni_green # Circuit traces
                            else:
                                pixel = c_black
                    elif "ghostfreak" in alien_id:
                        # Ectoplasmic White Shroud + Wandering Purple Eye
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if 14 <= x <= 17 and 13 <= y <= 16:
                                pixel = hex_to_rgba("#a855f7") if dist <= 2.0 else hex_to_rgba("#581c87")
                            else:
                                pixel = hex_to_rgba("#f1f5f9")
                    elif "cannonbolt" in alien_id:
                        # Golden Carapace Brow + Clean White Faceplate + Green Eyes
                        if 8 <= x <= 23 and 8 <= y <= 24:
                            if 11 <= x <= 20 and 11 <= y <= 21:
                                if y in (15, 16) and x in (13, 18):
                                    pixel = c_omni_green
                                else:
                                    pixel = c_white
                            else:
                                pixel = hex_to_rgba("#eab308")
                    elif "wildmutt" in alien_id:
                        # Vulpimancer Orange Snout + Dark Nostrils + White Quills
                        if 9 <= x <= 22 and 9 <= y <= 23:
                            if y in (17, 18) and 14 <= x <= 17:
                                pixel = hex_to_rgba("#451a03") # Snout nostrils
                            elif y in (14, 15) and (x == 11 or x == 20):
                                pixel = c_white # Quill whisker tips
                            else:
                                pixel = hex_to_rgba("#ea580c")
                    elif "greymatter" in alien_id:
                        # Galvan Grey Head + Giant Green Bulb Frog Eyes + Slit Pupil
                        if 9 <= x <= 22 and 9 <= y <= 23:
                            if (10 <= x <= 14 and 12 <= y <= 17) or (17 <= x <= 21 and 12 <= y <= 17):
                                pixel = c_black if y in (14, 15) and x in (12, 19) else c_omni_green
                            else:
                                pixel = hex_to_rgba("#94a3b8")
                    elif "way_big" in alien_id or "waybig" in alien_id:
                        # Tokustar Colossal White Armor + Red Crest Blade
                        if 10 <= x <= 21 and 6 <= y <= 25:
                            if 14 <= x <= 17 and y <= 13:
                                pixel = hex_to_rgba("#dc2626") # Tall red blade crest
                            elif y in (16, 17) and x in (12, 19):
                                pixel = c_gold
                            else:
                                pixel = c_white
                    elif "alien_x" in alien_id or "alienx" in alien_id:
                        # Celestial Black Void + 3 Silver Horns + Green Star Eyes
                        if 9 <= x <= 22 and 7 <= y <= 24:
                            if y <= 11 and x in (11, 15, 16, 20):
                                pixel = c_silver # Triple horn crest
                            elif y in (15, 16) and x in (13, 18):
                                pixel = hex_to_rgba("#4ade80") # Star-green eyes
                            else:
                                pixel = c_black
                    elif "feedback" in alien_id:
                        # Conductoid Black Face + Green Eye + Gold Plug Antennae
                        if 9 <= x <= 22 and 7 <= y <= 24:
                            if y <= 10 and x in (10, 11, 20, 21):
                                pixel = c_gold # Golden plug antennae
                            elif dist <= 2.2:
                                pixel = c_omni_green # Center cyclops optic
                            else:
                                pixel = c_black
                    elif "rath" in alien_id:
                        # Fierce Orange Tiger + Black Stripes + White Muzzle + Green Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = c_omni_green # Green eyes
                            elif y in (18, 19) and 13 <= x <= 18:
                                pixel = c_white # White tiger muzzle
                            elif (x in (10, 21) and y in (10, 11)) or (y == 10 and x in (14, 17)):
                                pixel = c_black # Tiger stripes
                            else:
                                pixel = hex_to_rgba("#ea580c")
                    elif "humungousaur" in alien_id:
                        # Tough Brown Dinosaur Brow + Golden Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = c_gold
                            elif y >= 19 and 13 <= x <= 18:
                                pixel = hex_to_rgba("#451a03")
                            else:
                                pixel = hex_to_rgba("#78350f")
                    elif "bigchill" in alien_id:
                        # Midnight Blue Moth Hood + Glowing Cyan Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = hex_to_rgba("#38bdf8") # Cyan frost eyes
                            elif y <= 10 and x in (11, 20):
                                pixel = hex_to_rgba("#0284c7") # Folded antennae
                            else:
                                pixel = hex_to_rgba("#0f172a")
                    elif "swampfire" in alien_id:
                        # Olive Bark Face + Orange Flame Mask
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if 12 <= x <= 19 and 12 <= y <= 19:
                                pixel = hex_to_rgba("#f97316") if y not in (15, 16) or x not in (14, 17) else c_gold
                            else:
                                pixel = hex_to_rgba("#365314")
                    else:
                        # Clean Bold Omnitrix Emblem for other aliens
                        is_black_wedge = False
                        if dx < -0.8:
                            if abs(dy) < (-dx * 0.88):
                                is_black_wedge = True
                        elif dx > 0.8:
                            if abs(dy) < (dx * 0.88):
                                is_black_wedge = True

                        if is_black_wedge:
                            pixel = c_black
                        else:
                            pixel = c_acc if dist <= 2.2 else c_base

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_spawner_icon(entity_id):
    """
    32x32 Hand-Crafted HD Pixel Art for Spawner Keys & Summon Beacons
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_black = hex_to_rgba("#090d16")
    c_white = hex_to_rgba("#ffffff")
    c_silver = hex_to_rgba("#cbd5e1")
    c_chrome = hex_to_rgba("#94a3b8")
    c_gold = hex_to_rgba("#facc15")
    c_brass = hex_to_rgba("#d97706")
    c_green = hex_to_rgba("#16a34a")
    c_omni_green = hex_to_rgba("#22c55e")
    c_omni_glow = hex_to_rgba("#86efac")
    c_red = hex_to_rgba("#dc2626")
    c_red_glow = hex_to_rgba("#ef4444")
    c_orange = hex_to_rgba("#ea580c")
    c_cyan = hex_to_rgba("#2dd4bf")

    cx, cy = 15.5, 15.5

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5

            if "kevin_car" in entity_id:
                # Green Muscle Car Key with Remote Fob & Silver Key Blade
                # Keyring at top (12..19, 2..8)
                if 2 <= y <= 8 and 12 <= x <= 19:
                    d_ring = ((x - 15.5)**2 + (y - 5.5)**2)**0.5
                    if 2.0 <= d_ring <= 3.5:
                        pixel = c_silver
                # Remote Fob Body (10..21, 8..20)
                elif 8 <= y <= 20 and 10 <= x <= 21:
                    if x in (10, 21) or y in (8, 20):
                        pixel = c_black # Black rubber casing
                    elif 11 <= y <= 17 and 13 <= x <= 18:
                        # Green Omnitrix remote button
                        pixel = c_omni_glow if (x in (15, 16) and y in (13, 14)) else c_green
                    else:
                        pixel = hex_to_rgba("#1e293b")
                # Silver Ignition Key Blade (14..17, 21..30)
                elif 21 <= y <= 30 and 14 <= x <= 17:
                    if x == 17 and y in (23, 26, 28):
                        pixel = c_trans # Key blade teeth cutouts
                    elif x in (14, 17) or y == 30:
                        pixel = c_chrome
                    else:
                        pixel = c_silver

            elif "rustbucket" in entity_id:
                # Vintage Brass RV Key + Red/Green Camper Van Tag
                # Brass Key (Top left to bottom right)
                if 2 <= y <= 12 and 6 <= x <= 16:
                    d_head = ((x - 11)**2 + (y - 7)**2)**0.5
                    if d_head <= 4.5:
                        pixel = c_trans if d_head <= 1.8 else (c_gold if d_head >= 3.5 else c_brass)
                elif 11 <= y <= 22 and 10 <= x <= 13:
                    pixel = c_trans if (x == 13 and y in (14, 18)) else c_brass
                # Rust Bucket RV Camper Keychain Tag (14..29, 14..28)
                elif 14 <= y <= 28 and 14 <= x <= 29:
                    if x in (14, 29) or y in (14, 28):
                        pixel = c_black
                    elif 19 <= y <= 21:
                        pixel = c_red # Red camper stripe
                    elif 22 <= y <= 24:
                        pixel = c_green # Green camper stripe
                    else:
                        pixel = c_white

            elif "vilgax_spawner" in entity_id or "vilgax" in entity_id:
                # Warlord Vilgax Seal: Alien Green Squid Skull with Crimson Eye
                if dist <= 12.0:
                    if dist >= 10.5:
                        pixel = c_gold # Golden warlord border
                    elif y <= 16 and 9 <= x <= 22:
                        # Skull Dome & Eye
                        if y in (12, 13) and x in (11, 12):
                            pixel = c_red_glow # Glowing red cybernetic eye
                        elif y in (14, 15) and 13 <= x <= 18:
                            pixel = hex_to_rgba("#334155") # Respirator
                        else:
                            pixel = hex_to_rgba("#4d7c0f") # Alien green skin
                    elif y > 16 and 10 <= x <= 21:
                        # Tentacles
                        t_mod = (x - 10) % 3
                        pixel = hex_to_rgba("#14532d") if t_mod == 2 else hex_to_rgba("#4d7c0f")
                    else:
                        pixel = c_black

            elif "battle_drone" in entity_id:
                # Samurai Battle Droid Helmet with Crimson Laser Visor
                if 6 <= y <= 26 and 6 <= x <= 25:
                    if 14 <= y <= 17 and 10 <= x <= 21:
                        pixel = c_red_glow # Horizontal Red Laser Eye Visor
                    elif y in (6, 7, 25, 26) or x in (6, 7, 24, 25):
                        pixel = c_orange # Orange hazard armor trim
                    else:
                        pixel = hex_to_rgba("#18181b")

            elif "kevin11" in entity_id:
                # Mutated Kevin 11 Amalgam Crest (Half Fourarms, Half Diamondhead)
                if dist <= 12.0:
                    if dist >= 10.5:
                        pixel = c_black # Dark spiked border
                    elif dx < 0:
                        # Left Half: Four Arms Crimson Muscle & Black Stripe
                        pixel = c_black if (abs(dx) <= 2) else c_red
                    else:
                        # Right Half: Diamondhead Cyan Crystal
                        pixel = c_cyan if ((x + y) % 3 != 0) else hex_to_rgba("#0f766e")

            elif "meteor_pod" in entity_id:
                # Cracked Meteor Crash Pod with Glowing Green Galvanic Fissures
                if dist <= 11.0:
                    if dist <= 4.0:
                        pixel = c_omni_glow # Glowing emerald core
                    elif (x in (14, 15, 17) and 8 <= y <= 22) or (y in (15, 16) and 8 <= x <= 22):
                        pixel = c_omni_green # Glowing fissure lines
                    else:
                        pixel = hex_to_rgba("#27272a") # Scorch meteor rock

            elif "vilgax_ship" in entity_id:
                # Alien Drone Battleship Beacon
                if dist <= 12.0:
                    if dist <= 3.5:
                        pixel = c_red_glow # Red plasma bridge
                    elif 7.0 <= dist <= 9.0:
                        pixel = c_red # Plasma engine thruster ring
                    else:
                        pixel = hex_to_rgba("#1e293b")

            else:
                # Generic Spawner Key
                if dist <= 10.0:
                    pixel = c_omni_green if dist <= 3.0 else c_black

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))
