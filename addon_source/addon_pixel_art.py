# Ben 10 Bedrock Addon - Series Accurate 64x64 HD Alien Textures & Skins
# Pure Python PNG generation - Smooth Shading, Anatomical Details, Zero Dither Noise
# Strictly under 1000 lines

from addon_graphics import make_png, hex_to_rgba
from addon_hd_item_art import (
    create_hd_omnitrix_watch_icon,
    create_hd_omnitrix_activator_icon,
    create_hd_detransform_icon,
    create_hd_fusion_icon,
    create_hd_alien_badge_icon,
    _blend, _darken, _lighten
)

# Backward-compatibility delegates
def create_omnitrix_dial_icon(accent_hex, dial_hex, ring_hex, core_hex, edge_hex):
    return create_hd_omnitrix_activator_icon()

def create_alien_face_icon(alien_id, base_hex, detail_hex, accent_hex):
    return create_hd_alien_badge_icon(alien_id, base_hex, detail_hex, accent_hex)

def create_64x64_alien_skin(base_color_hex, detail_color_hex="#ffffff", accent_color_hex="#22c55e", alien_id=""):
    """
    Generates high-definition, series-accurate 64x64 Minecraft skins for all aliens.
    Uses smooth anatomical shading, clean solid uniform pieces, and bold chest Omnitrix badges.
    Zero checkerboard noise / zero modulo stippling.
    """
    if isinstance(base_color_hex, str) and not base_color_hex.startswith("#"):
        alien_id, base_color_hex, accent_color_hex = base_color_hex, detail_color_hex, accent_color_hex
        detail_color_hex = "#ffffff"

    w, h = 64, 64
    data = bytearray(w * h * 4)
    c_trans = [0, 0, 0, 0]

    c_base = hex_to_rgba(base_color_hex)
    c_det = hex_to_rgba(detail_color_hex)
    c_acc = hex_to_rgba(accent_color_hex)
    c_shadow = _darken(c_base, 35)
    c_highlight = _lighten(c_base, 25)

    c_white = hex_to_rgba("#ffffff")
    c_black = hex_to_rgba("#090d16")
    c_omni_green = hex_to_rgba("#22c55e")
    c_omni_glow = hex_to_rgba("#86efac")
    c_gold = hex_to_rgba("#facc15")

    # Species identification
    is_fourarms = "four_arms" in alien_id or "fourarms" in alien_id
    is_diamondhead = "diamondhead" in alien_id
    is_xlr8 = "xlr8" in alien_id
    is_heatblast = "heatblast" in alien_id
    is_wildmutt = "wildmutt" in alien_id
    is_stinkfly = "stinkfly" in alien_id
    is_ripjaws = "ripjaws" in alien_id
    is_cannonbolt = "cannonbolt" in alien_id
    is_greymatter = "greymatter" in alien_id
    is_waybig = "waybig" in alien_id or "way_big" in alien_id
    is_ghostfreak = "ghostfreak" in alien_id
    is_upgrade = "upgrade" in alien_id
    is_carnitrix = "carnitrix" in alien_id
    is_ben23 = "ben23" in alien_id
    is_humungousaur = "humungousaur" in alien_id
    is_echoecho = "echoecho" in alien_id
    is_bigchill = "bigchill" in alien_id
    is_chromastone = "chromastone" in alien_id
    is_swampfire = "swampfire" in alien_id
    is_rath = "rath" in alien_id
    is_feedback = "feedback" in alien_id
    is_alienx = "alien_x" in alien_id or "alienx" in alien_id

    # Omnitrix Badge Colors
    badge_core = hex_to_rgba("#ef4444") if is_carnitrix else (hex_to_rgba("#38bdf8") if is_ben23 else c_omni_green)
    badge_glow = hex_to_rgba("#fca5a5") if is_carnitrix else (hex_to_rgba("#bae6fd") if is_ben23 else c_omni_glow)

    for y in range(h):
        for x in range(w):
            idx = (y * w + x) * 4
            pixel = c_trans

            # =========================================================================
            # 1. HEAD (x: 0..31, y: 0..15) -> Standard Minecraft 8x8x8 Head layout
            # Front face is (8..15, 8..15)
            # =========================================================================
            if 0 <= x < 32 and 0 <= y < 16:
                if 8 <= x <= 15 and 8 <= y <= 15: # Front Face
                    if is_fourarms:
                        # Crimson Tetramand skin with 4 Golden Eyes & Black Mohawk
                        if x in (11, 12) and y <= 11:
                            pixel = c_black # Central crest
                        elif (y == 10 and x in (10, 13)) or (y == 12 and x in (9, 14)):
                            pixel = c_gold # 4 Golden Eyes
                        elif y == 14 and 10 <= x <= 13:
                            pixel = _darken(c_base, 50) # Mouth line
                        else:
                            pixel = c_base
                    elif is_heatblast:
                        # Obsidian rock with white-hot eyes & flame crown hair
                        if y <= 9 and 10 <= x <= 13:
                            pixel = hex_to_rgba("#f97316") # Flame crown hair
                        elif y in (11, 12) and x in (10, 13):
                            pixel = hex_to_rgba("#fef08a") # White-hot eyes
                        elif y == 14 and 11 <= x <= 12:
                            pixel = hex_to_rgba("#f97316") # Lava mouth
                        else:
                            pixel = hex_to_rgba("#78350f") # Solid obsidian rock
                    elif is_diamondhead:
                        # Faceted Cyan Crystal Head with Yellow Eyes
                        if y in (11, 12) and x in (10, 13):
                            pixel = c_gold # Yellow eyes
                        elif x in (8, 15) or y == 15:
                            pixel = hex_to_rgba("#0f766e") # Crystal facet shadow
                        else:
                            pixel = hex_to_rgba("#2dd4bf") # Pure cyan crystal
                    elif is_xlr8:
                        # Black aerodynamic helmet with cyan visor and green slit eyes
                        if 9 <= x <= 14 and 10 <= y <= 13:
                            if y == 11 and x in (11, 12):
                                pixel = hex_to_rgba("#4ade80") # Green slit eye
                            else:
                                pixel = hex_to_rgba("#38bdf8") # Cyan visor
                        else:
                            pixel = hex_to_rgba("#0f172a") # Glossy black helmet
                    elif is_upgrade:
                        # Obsidian nanite chassis with green circular optic & circuits
                        if (y in (11, 12) and x in (11, 12)):
                            pixel = hex_to_rgba("#86efac") # Center optic
                        elif (y in (10, 13) and x in (11, 12)) or (y in (11, 12) and x in (10, 13)):
                            pixel = c_omni_green # Optic ring
                        elif (x == 11 and y == 14) or (x in (9, 14) and y == 12):
                            pixel = c_omni_green # Circuit lines
                        else:
                            pixel = c_black
                    elif is_ghostfreak:
                        # Ectoplasmic shroud with wandering purple eye
                        if y == 11 and x == 11:
                            pixel = hex_to_rgba("#a855f7") # Wandering purple pupil
                        elif y in (10, 11, 12) and x in (10, 11, 12):
                            pixel = hex_to_rgba("#581c87") # Eye socket track
                        else:
                            pixel = hex_to_rgba("#f1f5f9")
                    elif is_ripjaws:
                        # Blue aquatic scales, razor white fangs, green angler lure
                        if y == 8 and 11 <= x <= 12:
                            pixel = hex_to_rgba("#4ade80") # Angler lure
                        elif y in (13, 14) and 9 <= x <= 14:
                            pixel = c_white if x in (9, 11, 13) else hex_to_rgba("#991b1b")
                        elif y == 10 and x in (9, 14):
                            pixel = hex_to_rgba("#38bdf8") # Fish eyes
                        else:
                            pixel = hex_to_rgba("#0284c7")
                    elif is_cannonbolt:
                        # Yellow carapace rim with white faceplate and green eyes
                        if y in (11, 12) and x in (10, 13):
                            pixel = c_omni_green # Green eyes
                        elif y <= 9 or x in (8, 15):
                            pixel = hex_to_rgba("#eab308") # Yellow carapace brow
                        else:
                            pixel = hex_to_rgba("#ffffff") # White faceplate
                    elif is_greymatter:
                        # Galvan grey skin with massive green bulb frog eyes
                        if 9 <= x <= 14 and 10 <= y <= 13:
                            if y == 11 and x in (11, 12):
                                pixel = c_black # Horizontal slit pupil
                            else:
                                pixel = c_omni_green # Big green eye
                        else:
                            pixel = hex_to_rgba("#94a3b8")
                    elif is_alienx:
                        # Deep cosmic black void with glowing green star eyes
                        if y in (11, 12) and x in (10, 13):
                            pixel = hex_to_rgba("#4ade80") # Green star eyes
                        else:
                            pixel = c_black
                    elif is_rath:
                        # Fierce orange tiger with black stripes and white muzzle
                        if y in (11, 12) and x in (10, 13):
                            pixel = c_omni_green # Green glare
                        elif y in (13, 14) and 10 <= x <= 13:
                            pixel = c_white # White tiger muzzle
                        elif (x in (9, 14) and y in (9, 10)) or (y == 9 and x in (11, 12)):
                            pixel = c_black # Tiger stripe
                        else:
                            pixel = hex_to_rgba("#ea580c")
                    elif is_feedback:
                        # Obsidian black conductoid with green cyclops eye & gold plugs
                        if y in (11, 12) and x in (11, 12):
                            pixel = c_omni_green # Center cyclops optic
                        elif y <= 9 and x in (9, 14):
                            pixel = c_gold # Golden antenna plugs
                        else:
                            pixel = c_black
                    else:
                        # Default Alien Head: Clean species face with expressive eyes
                        if y in (11, 12) and x in (10, 13):
                            pixel = c_acc # Alien eyes
                        elif y == 14 and 10 <= x <= 13:
                            pixel = c_shadow # Mouth line
                        else:
                            pixel = c_base
                else:
                    # Top, bottom, sides and back of head
                    if is_heatblast:
                        pixel = hex_to_rgba("#f97316") if y <= 7 else hex_to_rgba("#78350f")
                    elif is_diamondhead:
                        pixel = hex_to_rgba("#14b8a6")
                    elif is_xlr8:
                        pixel = hex_to_rgba("#0f172a")
                    elif is_upgrade:
                        pixel = c_omni_green if (x in (4, 12, 20, 28) and y == 4) else c_black
                    elif is_alienx:
                        pixel = c_black
                    else:
                        pixel = c_base

            # =========================================================================
            # 2. TORSO / BODY (x: 16..39, y: 16..31)
            # Front chest is (20..27, 20..31)
            # =========================================================================
            elif 16 <= x < 40 and 16 <= y < 32:
                # Front Chest Area (20..27, 20..31)
                if 20 <= x <= 27 and 20 <= y <= 31:
                    # Center Chest Omnitrix Badge (22..25, 22..25)
                    is_badge = (22 <= x <= 25 and 22 <= y <= 25)
                    if is_badge:
                        # 4x4 Omnitrix Chest Badge
                        if (x in (23, 24) and y in (23, 24)):
                            pixel = badge_glow # Hourglass center glow
                        elif (x == 22 and y in (22, 25)) or (x == 25 and y in (22, 25)):
                            pixel = badge_core # Hourglass wings
                        else:
                            pixel = c_black # Hourglass dark cuts
                    elif is_fourarms:
                        # Classic White Shirt with Black Vertical Center Stripe & Black Pants
                        if x in (23, 24):
                            pixel = c_black # Vertical black stripe
                        elif y >= 28:
                            pixel = hex_to_rgba("#18181b") # Black pants
                        else:
                            pixel = c_white # White shirt
                    elif is_diamondhead:
                        # Iconic Half-Black / Half-White Split Uniform!
                        if x < 24:
                            pixel = c_black # Right half black
                        else:
                            pixel = c_white # Left half white
                    elif is_xlr8:
                        # Black aerodynamic bodysuit with white center stripe
                        if x in (23, 24):
                            pixel = hex_to_rgba("#e0f2fe") # White streak
                        else:
                            pixel = hex_to_rgba("#0f172a") # Black bodysuit
                    elif is_heatblast:
                        # Volcanic charcoal plates connected by molten magma seams
                        if (x in (21, 26) and y in (21, 27)) or (y == 26 and 22 <= x <= 25):
                            pixel = hex_to_rgba("#f97316") # Molten magma seams
                        else:
                            pixel = hex_to_rgba("#78350f") # Obsidian plates
                    elif is_cannonbolt:
                        # Yellow armor rim around clean white chestplate
                        if x in (20, 27) or y in (20, 31):
                            pixel = hex_to_rgba("#ca8a04") # Yellow armor rim
                        else:
                            pixel = c_white # White chestplate
                    elif is_upgrade:
                        # Obsidian nanite chassis with green circuit traces
                        if (x in (21, 26) and 20 <= y <= 28) or (y in (21, 28) and 20 <= x <= 27):
                            pixel = c_omni_green # Circuit trace
                        else:
                            pixel = c_black
                    elif is_ghostfreak:
                        pixel = hex_to_rgba("#f1f5f9")
                    elif is_waybig:
                        # Colossal White armor with Red shoulder accents
                        if x in (20, 21, 26, 27) and y <= 25:
                            pixel = hex_to_rgba("#dc2626")
                        else:
                            pixel = c_white
                    elif is_swampfire:
                        if x in (21, 26) and y >= 26:
                            pixel = hex_to_rgba("#f97316")
                        else:
                            pixel = hex_to_rgba("#365314")
                    elif is_rath:
                        if 22 <= x <= 25 and y >= 24:
                            pixel = c_white # White chest patch
                        else:
                            pixel = hex_to_rgba("#ea580c")
                    elif is_feedback:
                        if x in (21, 26) and y >= 26:
                            pixel = c_omni_green
                        else:
                            pixel = c_black
                    elif is_alienx:
                        pixel = c_black
                    else:
                        pixel = c_base
                else:
                    # Sides and Back of Torso
                    if is_fourarms:
                        pixel = hex_to_rgba("#18181b") if y >= 28 else c_white
                    elif is_diamondhead:
                        pixel = c_black if x < 24 else c_white
                    elif is_cannonbolt:
                        pixel = hex_to_rgba("#eab308") if x >= 28 else hex_to_rgba("#ca8a04")
                    elif is_upgrade:
                        pixel = c_omni_green if (x in (29, 37) and 22 <= y <= 28) else c_black
                    elif is_alienx:
                        pixel = c_black
                    else:
                        pixel = c_base

            # =========================================================================
            # 3. RIGHT ARM (x: 40..55, y: 16..31)
            # =========================================================================
            elif 40 <= x < 56 and 16 <= y < 32:
                if is_fourarms:
                    pixel = c_gold if y in (26, 27) else hex_to_rgba("#b91c1c")
                elif is_diamondhead:
                    pixel = hex_to_rgba("#2dd4bf") if y >= 24 else c_black
                elif is_xlr8:
                    pixel = hex_to_rgba("#38bdf8") if y >= 24 else hex_to_rgba("#0f172a")
                elif is_heatblast:
                    pixel = hex_to_rgba("#ea580c") if y >= 26 else hex_to_rgba("#78350f")
                elif is_cannonbolt:
                    pixel = hex_to_rgba("#eab308") if y < 22 else c_white
                elif is_upgrade:
                    pixel = c_omni_green if (y in (20, 26) and x in (44, 52)) else c_black
                elif is_feedback:
                    pixel = c_gold if y >= 28 else c_black
                elif is_alienx:
                    pixel = c_black
                else:
                    pixel = c_acc if y >= 28 else c_base

            # =========================================================================
            # 4. SECONDARY RIGHT ARM / EXTRA LIMBS (x: 40..55, y: 32..47)
            # =========================================================================
            elif 40 <= x < 56 and 32 <= y < 48:
                if is_fourarms:
                    pixel = c_gold if y in (42, 43) else hex_to_rgba("#b91c1c")
                elif is_cannonbolt:
                    pixel = hex_to_rgba("#eab308")
                else:
                    pixel = c_base

            # =========================================================================
            # 5. LEFT ARM (x: 32..47, y: 48..63)
            # =========================================================================
            elif 32 <= x < 48 and 48 <= y < 64:
                if is_fourarms:
                    pixel = c_gold if y in (58, 59) else hex_to_rgba("#b91c1c")
                elif is_diamondhead:
                    pixel = hex_to_rgba("#2dd4bf") if y >= 56 else c_white
                elif is_xlr8:
                    pixel = hex_to_rgba("#38bdf8") if y >= 56 else hex_to_rgba("#0f172a")
                elif is_heatblast:
                    pixel = hex_to_rgba("#ea580c") if y >= 58 else hex_to_rgba("#78350f")
                elif is_cannonbolt:
                    pixel = hex_to_rgba("#eab308") if y < 54 else c_white
                elif is_upgrade:
                    pixel = c_omni_green if (y in (52, 58) and x in (36, 44)) else c_black
                elif is_feedback:
                    pixel = c_gold if y >= 60 else c_black
                elif is_alienx:
                    pixel = c_black
                else:
                    pixel = c_acc if y >= 60 else c_base

            # =========================================================================
            # 6. SECONDARY LEFT ARM (x: 48..63, y: 48..63)
            # =========================================================================
            elif 48 <= x < 64 and 48 <= y < 64:
                if is_fourarms:
                    pixel = c_gold if y in (58, 59) else hex_to_rgba("#b91c1c")
                else:
                    pixel = c_base

            # =========================================================================
            # 7. RIGHT LEG (x: 0..15, y: 16..31)
            # =========================================================================
            elif 0 <= x < 16 and 16 <= y < 32:
                if is_fourarms:
                    pixel = hex_to_rgba("#b91c1c") if y >= 28 else hex_to_rgba("#18181b")
                elif is_diamondhead:
                    pixel = hex_to_rgba("#090d16") # Right black pant leg
                elif is_xlr8:
                    pixel = hex_to_rgba("#0f172a") if y < 28 else hex_to_rgba("#38bdf8")
                elif is_heatblast:
                    pixel = hex_to_rgba("#f97316") if y in (21, 27) else hex_to_rgba("#78350f")
                elif is_cannonbolt:
                    pixel = hex_to_rgba("#0f172a") if y >= 28 else c_white
                elif is_upgrade:
                    pixel = c_omni_green if (x in (4, 12) and y == 24) else c_black
                elif is_alienx:
                    pixel = c_black
                else:
                    pixel = c_shadow if y >= 28 else c_base

            # =========================================================================
            # 8. LEFT LEG (x: 16..31, y: 48..63)
            # =========================================================================
            elif 16 <= x < 32 and 48 <= y < 64:
                if is_fourarms:
                    pixel = hex_to_rgba("#b91c1c") if y >= 60 else hex_to_rgba("#18181b")
                elif is_diamondhead:
                    pixel = c_white # Left white pant leg
                elif is_xlr8:
                    pixel = hex_to_rgba("#0f172a") if y < 60 else hex_to_rgba("#38bdf8")
                elif is_heatblast:
                    pixel = hex_to_rgba("#f97316") if y in (53, 59) else hex_to_rgba("#78350f")
                elif is_cannonbolt:
                    pixel = hex_to_rgba("#0f172a") if y >= 60 else c_white
                elif is_upgrade:
                    pixel = c_omni_green if (x in (20, 28) and y == 56) else c_black
                elif is_alienx:
                    pixel = c_black
                else:
                    pixel = c_shadow if y >= 60 else c_base

            # =========================================================================
            # 9. EXTRA PARTS / TAIL / BACK SHELL (x: 0..31, y: 32..47)
            # =========================================================================
            elif 0 <= x < 32 and 32 <= y < 48:
                if is_xlr8:
                    # Segmented Raptor Tail (solid blue and black rings)
                    pixel = hex_to_rgba("#38bdf8") if y in (33, 34, 38, 39, 43, 44) else hex_to_rgba("#0f172a")
                elif is_diamondhead:
                    # Sharp Back Crystal Spikes
                    pixel = hex_to_rgba("#2dd4bf") if x in (4, 5, 12, 13, 20, 21, 28, 29) else hex_to_rgba("#5eead4")
                elif is_cannonbolt:
                    # Giant Yellow Carapace Shell
                    pixel = hex_to_rgba("#eab308") if 4 <= x <= 27 and 34 <= y <= 45 else hex_to_rgba("#ca8a04")
                elif is_swampfire:
                    pixel = hex_to_rgba("#365314")
                elif is_bigchill:
                    pixel = hex_to_rgba("#0284c7") if x in (6, 14, 22) else hex_to_rgba("#0f172a")
                else:
                    pixel = c_base

            data[idx:idx+4] = bytes(pixel)

    return make_png(w, h, bytes(data))
