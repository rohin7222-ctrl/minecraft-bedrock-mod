# Ben 10 Bedrock Addon - Series Accurate 32x32 HD Item Art & Badges
# Pure Python PNG generation - High Definition, Shaded, Beveled & Emissive
# Strictly under 1000 lines

from addon_graphics import make_png, hex_to_rgba

def _blend(c1, c2, factor):
    """Blends two RGBA colors: factor 0.0 -> c1, factor 1.0 -> c2"""
    return [
        int(c1[0] * (1.0 - factor) + c2[0] * factor),
        int(c1[1] * (1.0 - factor) + c2[1] * factor),
        int(c1[2] * (1.0 - factor) + c2[2] * factor),
        int(c1[3] * (1.0 - factor) + c2[3] * factor)
    ]

def _darken(c, amount=40):
    return [max(0, c[0] - amount), max(0, c[1] - amount), max(0, c[2] - amount), c[3]]

def _lighten(c, amount=50):
    return [min(255, c[0] + amount), min(255, c[1] + amount), min(255, c[2] + amount), c[3]]

def create_hd_omnitrix_watch_icon(watch_id, band_hex, bezel_hex, dial_hex, glow_hex, core_hex, is_recharging=False):
    """
    Generates a 32x32 HD 3D-angled Omnitrix item icon.
    Includes curved wristband, beveled dial housing, rivets, side buttons, and glowing hourglass core.
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_band = hex_to_rgba(band_hex)
    c_bezel = hex_to_rgba(bezel_hex)
    c_dial = hex_to_rgba(dial_hex)
    c_glow = hex_to_rgba(glow_hex) if not is_recharging else hex_to_rgba("#ef4444")
    c_core = hex_to_rgba(core_hex) if not is_recharging else hex_to_rgba("#fca5a5")
    c_black = hex_to_rgba("#090d16")
    c_silver = hex_to_rgba("#cbd5e1")
    c_white = hex_to_rgba("#ffffff")
    c_red_btn = hex_to_rgba("#dc2626")

    cx, cy = 15.5, 12.5 # Dial Center

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans
            dx = x - cx
            dy = y - cy
            dist = (dx * dx + dy * dy) ** 0.5

            # 1. Wristband Strap Arc (Below dial: y from 16 to 30)
            in_band = False
            if y >= 15:
                # Cylindrical band curving downwards
                band_left = 6 + (y - 15) * 0.35
                band_right = 25 - (y - 15) * 0.35
                if band_left <= x <= band_right:
                    in_band = True
                    # Shading from left highlight to right shadow
                    factor = (x - band_left) / max(1.0, (band_right - band_left))
                    if x == int(band_left) or x == int(band_right) or y == 30:
                        pixel = _darken(c_band, 50) # Outer rim shadow
                    elif "classic" in watch_id and (y in (18, 19) or y in (27, 28)):
                        # Classic White edge bands
                        pixel = _lighten(c_white, 10) if factor < 0.6 else c_silver
                    elif "completed" in watch_id and 14 <= x <= 17:
                        # Omniverse Green racing stripe
                        pixel = hex_to_rgba("#22c55e")
                    elif "carnitrix" in watch_id and (x + y) % 5 == 0:
                        # Carnitrix Rust spots
                        pixel = hex_to_rgba("#7f1d1d")
                    else:
                        if factor < 0.3:
                            pixel = _lighten(c_band, 30) # Metallic sheen
                        elif factor < 0.7:
                            pixel = c_band
                        else:
                            pixel = _darken(c_band, 35)

            # 2. Side Buttons (Red activator button on left for Classic, claw brackets for Ultimatrix)
            if "classic" in watch_id or "prototype" in watch_id:
                if 2 <= x <= 6 and 11 <= y <= 14:
                    # Red Pop-Up Activation Release Button
                    pixel = _lighten(c_red_btn, 40) if y == 11 else c_red_btn
                    if x == 2 or y == 14:
                        pixel = _darken(c_red_btn, 40)
            elif "ultimatrix" in watch_id:
                # 4 Stabilizer Claws extending
                if (x in (4, 5, 26, 27) and 7 <= y <= 18) or (x in (6, 7, 24, 25) and y in (6, 19)):
                    pixel = c_silver if (x + y) % 2 == 0 else _darken(c_silver, 40)

            # 3. Outer Octagonal / Beveled Housing (Bezel Rim)
            if dist <= 12.0:
                # Housing bezel plate
                if dist > 8.5:
                    # Octagonal bevel facets
                    if dist >= 11.0:
                        pixel = _darken(c_bezel, 45) # Dark outer rim
                    elif (abs(dx) <= 3 and abs(dy) >= 9) or (abs(dy) <= 3 and abs(dx) >= 9):
                        pixel = _lighten(c_bezel, 35) # Edge highlights
                    else:
                        pixel = c_bezel

                    # 4 Corner Rivets on Classic/Omniverse
                    if ("classic" in watch_id or "ben23" in watch_id) and dist >= 9.5:
                        if (abs(dx - dy) < 1.5 or abs(dx + dy) < 1.5) and dist >= 10.0:
                            pixel = c_white if y < cy else c_silver
                # 4. Dial Face Ring (dist 6.5 to 8.5)
                elif dist > 6.0:
                    pixel = c_black if not is_recharging else hex_to_rgba("#450a0a")
                # 5. Hourglass Core (dist <= 6.0)
                else:
                    # Dual triangles
                    in_hourglass = False
                    if dy < 0 and abs(dx) <= -dy * 0.95:
                        in_hourglass = True
                    elif dy > 0 and abs(dx) <= dy * 0.95:
                        in_hourglass = True

                    if in_hourglass:
                        if dist <= 1.8:
                            pixel = c_core # Blazing white/bright center
                        elif dist <= 4.0:
                            pixel = c_glow # Vivid emerald / crimson glow
                        else:
                            pixel = _blend(c_glow, c_dial, 0.3)
                    else:
                        pixel = c_black

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_omnitrix_activator_icon():
    """
    32x32 Holographic Omnitrix Activator Disc (Image 1 reference).
    A high-tech metallic ring with 4 glowing conduits and an elevated holographic green hourglass.
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
                    # Metallic beveled outer ring
                    angle_shade = (dx - dy) / 30.0
                    pixel = _lighten(c_metal_light, 20) if angle_shade > 0.1 else c_metal_dark
                elif dist >= 10.0:
                    pixel = c_metal_border
                elif dist >= 8.5:
                    # 4 Glowing green energy conduits pointing inward
                    if abs(dx) <= 1.5 or abs(dy) <= 1.5:
                        pixel = c_green
                    else:
                        pixel = c_metal_dark
                elif dist > 7.0:
                    pixel = c_black
                else:
                    # Center Holographic Hourglass Core
                    in_hg = False
                    if dy < 0 and abs(dx) <= -dy * 0.9:
                        in_hg = True
                    elif dy > 0 and abs(dx) <= dy * 0.9:
                        in_hg = True

                    if in_hg:
                        if dist <= 2.0:
                            pixel = c_core
                        elif dist <= 4.5:
                            pixel = c_glow
                        else:
                            pixel = c_green
                    else:
                        pixel = c_black

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_detransform_icon():
    """
    32x32 Emergency Detransform / Revert Badge.
    Crimson warning hexagon with emergency eject glyph and illuminated human runner silhouette.
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

            # Outer Warning Hexagon (r approx 14)
            q_hex = abs(dx) * 0.866 + abs(dy) * 0.5
            hex_dist = max(q_hex, abs(dy))

            if hex_dist <= 15.0:
                if hex_dist >= 13.0:
                    pixel = c_red_border
                elif hex_dist >= 11.5:
                    pixel = c_red_bright if (x + y) % 4 != 0 else c_yellow # Hazard warning stripes
                elif hex_dist >= 10.0:
                    pixel = c_red_border
                else:
                    pixel = c_dark_bg

                    # Human Runner Detransform Silhouette
                    # Head (circle at 15.5, 9.5, r=2)
                    h_dx = x - 15.5
                    h_dy = y - 9.5
                    if (h_dx * h_dx + h_dy * h_dy) <= 4.0:
                        pixel = c_white
                    # Torso (14..17, 12..18)
                    elif 14 <= x <= 17 and 12 <= y <= 18:
                        pixel = c_white
                    # Left Running Arm (10..14, 13..15)
                    elif (11 <= x <= 14 and y == 13) or (9 <= x <= 11 and y == 14):
                        pixel = c_white
                    # Right Running Arm (17..21, 14..16)
                    elif (17 <= x <= 20 and y == 15) or (20 <= x <= 22 and y == 16):
                        pixel = c_white
                    # Left Running Leg (11..15, 19..23)
                    elif (13 <= x <= 15 and y == 19) or (11 <= x <= 13 and y == 21) or (9 <= x <= 11 and y == 22):
                        pixel = c_white
                    # Right Running Leg (16..20, 19..23)
                    elif (16 <= x <= 18 and y == 19) or (18 <= x <= 20 and y == 21) or (20 <= x <= 22 and y == 23):
                        pixel = c_white

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_fusion_icon():
    """
    32x32 Biomnitrix Dual Fusion DNA Matrix Icon.
    Gold and emerald dual-spiral helix representing fused alien DNA samples.
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

                    # Double-Helix DNA Strands
                    # Helix 1 (Green Sine Wave): x = cx + sin(y * 0.4) * 6
                    import math
                    sine_g = math.sin(y * 0.45) * 6.0
                    sine_c = -sine_g

                    diff_g = abs(dx - sine_g)
                    diff_c = abs(dx - sine_c)

                    # Connecting Base Pairs at nodes
                    if abs(y % 4 - 2) == 0 and abs(dx) <= 6.0:
                        pixel = c_gold_dark

                    if diff_g <= 1.2:
                        pixel = c_white if diff_g <= 0.5 else c_green
                    elif diff_c <= 1.2:
                        pixel = c_white if diff_c <= 0.5 else c_cyan

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))

def create_hd_alien_badge_icon(alien_id, base_hex, detail_hex, accent_hex):
    """
    32x32 HD Series-Accurate Alien Badge Icons.
    Includes metallic circular bezel, luminous green Omnitrix rim, and distinct alien face/silhouette.
    """
    w, h = 32, 32
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]
    c_base = hex_to_rgba(base_hex)
    c_det = hex_to_rgba(detail_hex)
    c_acc = hex_to_rgba(accent_hex)
    c_metal = hex_to_rgba("#334155")
    c_metal_rim = hex_to_rgba("#0f172a")
    c_omni_green = hex_to_rgba("#22c55e")
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

            # 1. Bezel & Tech Rim (Outer: dist <= 15.0)
            if dist <= 15.0:
                if dist >= 13.5:
                    pixel = c_metal_rim
                elif dist >= 12.0:
                    # Omnitrix Green Glow Ring
                    pixel = c_omni_green if (x + y) % 3 != 0 else hex_to_rgba("#86efac")
                elif dist >= 10.5:
                    pixel = c_metal_rim
                else:
                    # 2. Inside Species Emblem Face Area
                    pixel = _darken(c_base, 60) # Dark recessed background

                    # Species Face Artwork
                    if "heatblast" in alien_id:
                        # Magma Rock Face with Flaming Crown & Fiery Eyes
                        if 9 <= x <= 22 and 8 <= y <= 23:
                            if y <= 11:
                                # Blazing Flame Crown
                                pixel = hex_to_rgba("#fbbf24") if (x + y) % 2 == 0 else hex_to_rgba("#f97316")
                            elif y in (15, 16) and x in (12, 13, 18, 19):
                                pixel = c_white # Glowing Fire Eyes
                            elif (x + y) % 4 == 0:
                                pixel = hex_to_rgba("#ea580c") # Magma fissures
                            else:
                                pixel = hex_to_rgba("#78350f") # Obsidian rock
                    elif "four_arms" in alien_id or "fourarms" in alien_id:
                        # Crimson Tetramand Face with 4 Golden Eyes & Black Forehead Ridge
                        if 10 <= x <= 21 and 8 <= y <= 24:
                            if 15 <= x <= 16 and y <= 18:
                                pixel = c_black # Central crest
                            elif (y in (13, 14) and x in (12, 13, 18, 19)) or (y in (17, 18) and x in (11, 12, 19, 20)):
                                pixel = c_gold # 4 Golden Eyes
                            elif y >= 22 and 13 <= x <= 18:
                                pixel = c_black # Mouth chin
                            else:
                                pixel = hex_to_rgba("#b91c1c")
                    elif "xlr8" in alien_id:
                        # Glossy Aerodynamic Black Helmet with Neon Cyan Visor
                        if 9 <= x <= 22 and 7 <= y <= 25:
                            if 12 <= x <= 19 and 12 <= y <= 18:
                                if y in (14, 15) and x in (14, 17):
                                    pixel = hex_to_rgba("#4ade80") # Green slit eye
                                else:
                                    pixel = hex_to_rgba("#38bdf8") # Cyan visor
                            else:
                                pixel = hex_to_rgba("#0f172a") # Black helmet
                    elif "diamondhead" in alien_id:
                        # Faceted Cyan Crystal Head with Sharp Back Spikes & Yellow Eye
                        if 9 <= x <= 23 and 7 <= y <= 24:
                            if y <= 10 and x >= 18:
                                pixel = hex_to_rgba("#5eead4") # Crystal crown spike
                            elif y in (14, 15) and x in (13, 14):
                                pixel = c_gold # Yellow eye
                            elif (dx + dy) % 3 == 0:
                                pixel = hex_to_rgba("#99f6e4") # Crystalline facet sheen
                            else:
                                pixel = hex_to_rgba("#0d9488")
                    elif "ripjaws" in alien_id:
                        # Deep Blue Anglerfish with Glowing Lure & Needle Fangs
                        if y <= 9 and 15 <= x <= 16:
                            pixel = hex_to_rgba("#4ade80") # Angler lure bulb
                        elif 9 <= x <= 22 and 10 <= y <= 24:
                            if y in (19, 20) and 11 <= x <= 20:
                                pixel = c_white if x % 2 == 0 else hex_to_rgba("#7f1d1d") # Razor fangs & mouth
                            elif y in (14, 15) and x in (12, 19):
                                pixel = hex_to_rgba("#38bdf8") # Fish eyes
                            else:
                                pixel = hex_to_rgba("#0284c7")
                    elif "upgrade" in alien_id:
                        # Black Nanite Face with Concentric Emerald Optic & Circuit Traces
                        if dist <= 8.5:
                            if dist <= 2.2:
                                pixel = hex_to_rgba("#86efac") # Center optic core
                            elif 3.5 <= dist <= 5.0:
                                pixel = c_omni_green # Concentric optic ring
                            elif (abs(dx) <= 0.8 and dist <= 7.5) or (abs(dy) <= 0.8 and dist <= 7.5):
                                pixel = c_omni_green # Branching circuit lines
                            else:
                                pixel = c_black
                    elif "ghostfreak" in alien_id:
                        # Swirling Ectoplasmic Shroud with Wandering Purple Eye
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if 14 <= x <= 17 and 13 <= y <= 16:
                                pixel = hex_to_rgba("#a855f7") if dist <= 2.0 else hex_to_rgba("#581c87")
                            elif (x + y) % 5 == 0:
                                pixel = hex_to_rgba("#94a3b8") # Phantom crease
                            else:
                                pixel = hex_to_rgba("#f1f5f9")
                    elif "cannonbolt" in alien_id:
                        # Yellow Carapace Shell with Clean White Faceplate & Green Eyes
                        if 8 <= x <= 23 and 8 <= y <= 24:
                            if 11 <= x <= 20 and 11 <= y <= 21:
                                if y in (15, 16) and x in (13, 18):
                                    pixel = c_omni_green
                                else:
                                    pixel = c_white
                            else:
                                pixel = hex_to_rgba("#eab308") # Yellow armor plate
                    elif "wildmutt" in alien_id:
                        # Vulpimancer Beast Pelt with Snout Nostrils & Spine Quills
                        if 9 <= x <= 22 and 9 <= y <= 23:
                            if y in (17, 18) and 14 <= x <= 17:
                                pixel = hex_to_rgba("#451a03") # Dark nostrils
                            elif y in (15, 16) and (x == 12 or x == 19):
                                pixel = c_white # Quill whisker tips
                            else:
                                pixel = hex_to_rgba("#ea580c")
                    elif "greymatter" in alien_id:
                        # Galvan Cranium with Giant Green Frog Eyes & Slit Pupil
                        if 9 <= x <= 22 and 9 <= y <= 23:
                            if (10 <= x <= 14 and 12 <= y <= 17) or (17 <= x <= 21 and 12 <= y <= 17):
                                pixel = c_black if y in (14, 15) and x in (12, 19) else c_omni_green
                            else:
                                pixel = hex_to_rgba("#94a3b8")
                    elif "way_big" in alien_id or "waybig" in alien_id:
                        # Tokustar Colossal Armor with Red Crest Blade
                        if 10 <= x <= 21 and 6 <= y <= 25:
                            if 14 <= x <= 17 and y <= 14:
                                pixel = hex_to_rgba("#dc2626") # Red blade crest
                            elif y in (16, 17) and x in (12, 19):
                                pixel = c_gold
                            else:
                                pixel = c_white
                    elif "alien_x" in alien_id or "alienx" in alien_id:
                        # Celestial Black Void with Glowing Stars & 3 Silver Horns
                        if 9 <= x <= 22 and 7 <= y <= 24:
                            if y <= 11 and x in (11, 15, 16, 20):
                                pixel = c_silver # Triple horn crown
                            elif y in (15, 16) and x in (13, 18):
                                pixel = hex_to_rgba("#4ade80") # Star-green eyes
                            elif (x * 7 + y * 13) % 11 == 0:
                                pixel = c_white # Twinkling star nebula
                            else:
                                pixel = c_black
                    elif "feedback" in alien_id:
                        # Conductoid Black Chassis with Golden Plug Antennae & Green Eye
                        if 9 <= x <= 22 and 7 <= y <= 24:
                            if y <= 10 and x in (10, 11, 20, 21):
                                pixel = c_gold # Golden plug prongs
                            elif dist <= 2.2:
                                pixel = c_omni_green # Center cyclops optic
                            else:
                                pixel = c_black
                    elif "rath" in alien_id:
                        # Fierce Orange Tiger with Black Stripes & Green Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = c_omni_green
                            elif y in (18, 19) and 13 <= x <= 18:
                                pixel = c_white # White muzzle
                            elif (x + y) % 4 == 0:
                                pixel = c_black # Tiger stripe
                            else:
                                pixel = hex_to_rgba("#ea580c")
                    elif "humungousaur" in alien_id:
                        # Tough Reptilian Dinosaur Brow & Golden Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = c_gold
                            elif y >= 19 and 13 <= x <= 18:
                                pixel = hex_to_rgba("#451a03")
                            else:
                                pixel = hex_to_rgba("#78350f")
                    elif "bigchill" in alien_id:
                        # Chilling Blue Moth Cowl with Glowing Frost Eyes
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if y in (14, 15) and x in (12, 19):
                                pixel = hex_to_rgba("#38bdf8") # Frost cyan eyes
                            elif y <= 10 and x in (11, 20):
                                pixel = hex_to_rgba("#0284c7") # Folded antennae
                            else:
                                pixel = hex_to_rgba("#0f172a")
                    elif "swampfire" in alien_id:
                        # Mossy Bark Head with Orange Flame Mask
                        if 9 <= x <= 22 and 8 <= y <= 24:
                            if 12 <= x <= 19 and 12 <= y <= 19:
                                pixel = hex_to_rgba("#f97316") if y not in (15, 16) or x not in (14, 17) else c_gold
                            else:
                                pixel = hex_to_rgba("#365314")
                    else:
                        # Clean Series Omnitrix Silhouette with Glowing Accent Eyes
                        if 10 <= x <= 21 and 9 <= y <= 23:
                            if y in (15, 16) and x in (13, 18):
                                pixel = c_acc
                            elif (x + y) % 3 == 0:
                                pixel = _lighten(c_base, 25)
                            else:
                                pixel = c_base

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))
