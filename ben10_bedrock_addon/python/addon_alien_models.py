# Ben 10 Bedrock Addon - Series Accurate 3D Alien Geometries
# Replicating exact Minecraft 3D models (Four Arms with 4 arms, XLR8 with tail, Diamondhead with back spikes, etc.)
import json

from addon_alien_models_modern import get_modern_alien_geometry

def get_alien_geometry(alien_id):
    """Returns dedicated 3D Bedrock geometry with species-specific custom bones"""
    modern = get_modern_alien_geometry(alien_id)
    if modern:
        return modern

    # 1. FOUR ARMS (4 Distinct 3D Arms, broad muscular chest)
    if "four_arms" in alien_id or "fourarms" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.fourarms",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-5, 12, -2.5], "size": [10, 12, 5], "uv": [16, 16], "inflate": 0.25}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25}
                    ]
                },
                # Upper Right Arm
                {
                    "name": "rightArm", "pivot": [-5, 23, 0],
                    "cubes": [
                        {"origin": [-10, 14, -2.5], "size": [5, 11, 5], "uv": [40, 16], "inflate": 0.2}
                    ]
                },
                # Lower Right Arm (Secondary arm!)
                {
                    "name": "rightArm2", "parent": "body", "pivot": [-5, 16, 0],
                    "cubes": [
                        {"origin": [-9.5, 8, -2], "size": [4, 9, 4], "uv": [40, 32], "inflate": 0.15}
                    ]
                },
                # Upper Left Arm
                {
                    "name": "leftArm", "pivot": [5, 23, 0],
                    "cubes": [
                        {"origin": [5, 14, -2.5], "size": [5, 11, 5], "uv": [32, 48], "inflate": 0.2}
                    ]
                },
                # Lower Left Arm (Secondary arm!)
                {
                    "name": "leftArm2", "parent": "body", "pivot": [5, 16, 0],
                    "cubes": [
                        {"origin": [5.5, 8, -2], "size": [4, 9, 4], "uv": [48, 48], "inflate": 0.15}
                    ]
                },
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4.5, 0, -2.5], "size": [4.5, 12, 5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2.5], "size": [4.5, 12, 5], "uv": [16, 48]}]}
            ]
        }

    # 2. XLR8 (Aerodynamic cone helmet, 3D tail, scissor claws)
    elif "xlr8" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.xlr8",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.1}
                    ]
                },
                # Segmented Raptor Tail attached to body
                {
                    "name": "tail", "parent": "body", "pivot": [0, 14, 2],
                    "cubes": [
                        {"origin": [-1.5, 13, 2], "size": [3, 3, 6], "uv": [0, 32]},
                        {"origin": [-1, 12.5, 7.5], "size": [2, 2, 7], "uv": [0, 42]}
                    ]
                },
                # Aerodynamic Cone Helmet
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 24, -3.5], "size": [7, 7, 7], "uv": [0, 0], "inflate": 0.2},
                        {"origin": [-2.5, 25, 3.5], "size": [5, 5, 5], "uv": [32, 0]} # Pointed cone back
                    ]
                },
                # Arms with scissor claws
                {
                    "name": "rightArm", "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-8, 12, -2], "size": [3.5, 12, 3.5], "uv": [40, 16]},
                        {"origin": [-7.5, 9, -1.5], "size": [2, 3, 2], "uv": [40, 0]} # Claws
                    ]
                },
                {
                    "name": "leftArm", "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4.5, 12, -2], "size": [3.5, 12, 3.5], "uv": [32, 48]},
                        {"origin": [5.5, 9, -1.5], "size": [2, 3, 2], "uv": [40, 0]} # Claws
                    ]
                },
                # Digitigrade legs with roller balls at feet
                {
                    "name": "rightLeg", "pivot": [-2, 12, 0],
                    "cubes": [
                        {"origin": [-3.5, 2, -2], "size": [3.5, 10, 3.5], "uv": [0, 16]},
                        {"origin": [-3.5, 0, -2], "size": [3.5, 2.5, 3.5], "uv": [52, 0]} # Wheels
                    ]
                },
                {
                    "name": "leftLeg", "pivot": [2, 12, 0],
                    "cubes": [
                        {"origin": [0, 2, -2], "size": [3.5, 10, 3.5], "uv": [16, 48]},
                        {"origin": [0, 0, -2], "size": [3.5, 2.5, 3.5], "uv": [52, 0]} # Wheels
                    ]
                }
            ]
        }

    # 3. DIAMONDHEAD (2 Massive Crystal Shoulder Spikes, 2 Head Horns)
    elif "diamondhead" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.diamondhead",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4.5, 12, -2.5], "size": [9, 12, 5], "uv": [16, 16], "inflate": 0.25},
                        # 2 Massive Diagonal Crystal Spikes on the back
                        {"origin": [-6.5, 19, 2.5], "size": [3, 8, 3], "uv": [0, 32]},
                        {"origin": [3.5, 19, 2.5], "size": [3, 8, 3], "uv": [0, 32]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25},
                        # 2 Back Horn Spikes on Head
                        {"origin": [-2.5, 28, 3], "size": [5, 4, 4], "uv": [32, 0]}
                    ]
                },
                {
                    "name": "rightArm", "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-8.5, 12, -2.5], "size": [4.5, 12, 5], "uv": [40, 16], "inflate": 0.2}
                    ]
                },
                {
                    "name": "leftArm", "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4, 12, -2.5], "size": [4.5, 12, 5], "uv": [32, 48], "inflate": 0.2}
                    ]
                },
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 4. HEATBLAST (Flaming Crown on Head, Shoulder Magma Shards, Volcanic Fists)
    elif "heatblast" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.heatblast",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25},
                        # Magma collar
                        {"origin": [-5, 21, -3], "size": [10, 3, 6], "uv": [16, 32], "inflate": 0.1}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25},
                        # Flaming Hair / Spikes on Crown
                        {"origin": [-3, 31.5, -3], "size": [6, 4, 6], "uv": [32, 0]}
                    ]
                },
                {
                    "name": "rightArm", "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-8.5, 11, -2.5], "size": [4.5, 13, 5], "uv": [40, 16], "inflate": 0.2},
                        {"origin": [-9, 21, -3], "size": [4, 3, 4], "uv": [40, 48]} # Shoulder rock
                    ]
                },
                {
                    "name": "leftArm", "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4, 11, -2.5], "size": [4.5, 13, 5], "uv": [32, 48], "inflate": 0.2},
                        {"origin": [5, 21, -3], "size": [4, 3, 4], "uv": [40, 48]} # Shoulder rock
                    ]
                },
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 5. WILDMUTT (Idea 31: Quadruped 4-Legged Beast, Gill Slits, Quill Spikes, NO EYES!)
    elif "wildmutt" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.wildmutt",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 16, 0],
                    "cubes": [
                        # Muscular hunchback beast torso
                        {"origin": [-5, 10, -5], "size": [10, 10, 13], "uv": [16, 16], "inflate": 0.2},
                        # Quill spines along spine
                        {"origin": [-1, 20, -3], "size": [2, 3, 10], "uv": [0, 32]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 15, -5],
                    "cubes": [
                        # Eyeless beast muzzle & jaw
                        {"origin": [-4, 11, -12], "size": [8, 8, 8], "uv": [0, 0]},
                        # Sharp predatory lower jaw
                        {"origin": [-3.5, 9, -11], "size": [7, 3, 7], "uv": [32, 0]},
                        # Neck gill gills
                        {"origin": [-5, 12, -7], "size": [10, 5, 3], "uv": [32, 16]}
                    ]
                },
                # Front Arms (Beast Forelegs with razor claws)
                {
                    "name": "rightArm", "pivot": [-5, 15, -3],
                    "cubes": [{"origin": [-8.5, 0, -5], "size": [4.5, 16, 4.5], "uv": [40, 16]}]
                },
                {
                    "name": "leftArm", "pivot": [5, 15, -3],
                    "cubes": [{"origin": [4, 0, -5], "size": [4.5, 16, 4.5], "uv": [32, 48]}]
                },
                # Hindlegs
                {
                    "name": "rightLeg", "pivot": [-4, 12, 5],
                    "cubes": [{"origin": [-7, 0, 4], "size": [4, 13, 5], "uv": [0, 16]}]
                },
                {
                    "name": "leftLeg", "pivot": [4, 12, 5],
                    "cubes": [{"origin": [3, 0, 4], "size": [4, 13, 5], "uv": [16, 48]}]
                }
            ]
        }

    # 6. STINKFLY (Idea 32: 4 Eye Stalks, 4 Articulated Bug Wings, Stinger Tail)
    elif "stinkfly" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.stinkfly",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 12, -2], "size": [7, 12, 4], "uv": [16, 16]},
                        # 4 Bug Wings on upper back
                        {"origin": [-12, 17, 2.5], "size": [11, 8, 0.5], "uv": [0, 32]},
                        {"origin": [1, 17, 2.5], "size": [11, 8, 0.5], "uv": [0, 32]},
                        {"origin": [-10, 11, 2.8], "size": [9, 6, 0.5], "uv": [0, 42]},
                        {"origin": [1, 11, 2.8], "size": [9, 6, 0.5], "uv": [0, 42]}
                    ]
                },
                # Tail with Stinger Barb
                {
                    "name": "tail", "parent": "body", "pivot": [0, 13, 2],
                    "cubes": [
                        {"origin": [-1, 12, 2], "size": [2, 2, 7], "uv": [32, 32]},
                        {"origin": [-0.5, 13, 8.5], "size": [1, 3, 2], "uv": [32, 42]} # Poison barb
                    ]
                },
                # Head with 4 Distinct Eye Stalks
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3, 24, -3], "size": [6, 7, 6], "uv": [0, 0]},
                        # 4 Eye Stalks extending diagonally
                        {"origin": [-7, 27, -5], "size": [4, 2, 2], "uv": [32, 0]},
                        {"origin": [3, 27, -5], "size": [4, 2, 2], "uv": [32, 0]},
                        {"origin": [-7, 29, -1], "size": [4, 2, 2], "uv": [32, 6]},
                        {"origin": [3, 29, -1], "size": [4, 2, 2], "uv": [32, 6]}
                    ]
                },
                {"name": "rightArm", "pivot": [-4, 22, 0], "cubes": [{"origin": [-7.5, 12, -2], "size": [3.5, 12, 3.5], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [4, 22, 0], "cubes": [{"origin": [4, 12, -2], "size": [3.5, 12, 3.5], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-3.5, 0, -2], "size": [3.5, 12, 3.5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [3.5, 12, 3.5], "uv": [16, 48]}]}
            ]
        }

    # 7. RIPJAWS (Idea 33: Hinged Angler Jaw, Lure on Head, Dorsal Fin)
    elif "ripjaws" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.ripjaws",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16]},
                        # Dorsal fin along the back
                        {"origin": [-0.5, 14, 2], "size": [1, 10, 4], "uv": [0, 32]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        # Upper skull & eyes
                        {"origin": [-4, 25, -4], "size": [8, 7, 8], "uv": [0, 0]},
                        # Massive hinged unhinging predator jaw
                        {"origin": [-4.5, 22, -6], "size": [9, 5, 8], "uv": [32, 0]},
                        # Luminescent anglerfish lure extending above head
                        {"origin": [-0.5, 32, -2], "size": [1, 5, 3], "uv": [32, 16]},
                        {"origin": [-1, 35, 1], "size": [2, 2, 2], "uv": [32, 26]} # Glowing tip bulb
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8.5, 11, -2], "size": [4, 13, 4], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4.5, 11, -2], "size": [4, 13, 4], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 8. CANNONBOLT (Idea 34: Massive Hunchback Armored Carapace Shell)
    elif "cannonbolt" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.cannonbolt",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-6, 10, -4], "size": [12, 14, 8], "uv": [16, 16]},
                        # Massive Rounded Armored Carapace Shell on back
                        {"origin": [-7, 9, 3], "size": [14, 16, 7], "uv": [0, 32]},
                        # Chest armor plates
                        {"origin": [-5, 12, -4.8], "size": [10, 11, 2], "uv": [16, 42]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        # Head tucked low into hunchback shell
                        {"origin": [-3.5, 21, -6], "size": [7, 7, 7], "uv": [0, 0]},
                        {"origin": [-4, 25, -4], "size": [8, 4, 6], "uv": [32, 0]} # Shell hood
                    ]
                },
                # Bulky Armored Arms
                {
                    "name": "rightArm", "pivot": [-7, 21, 0],
                    "cubes": [{"origin": [-12, 9, -3.5], "size": [5.5, 14, 6], "uv": [40, 16]}]
                },
                {
                    "name": "leftArm", "pivot": [7, 21, 0],
                    "cubes": [{"origin": [6.5, 9, -3.5], "size": [5.5, 14, 6], "uv": [32, 48]}]
                },
                {"name": "rightLeg", "pivot": [-3, 10, 0], "cubes": [{"origin": [-6, 0, -3], "size": [5, 10, 6], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [3, 10, 0], "cubes": [{"origin": [1, 0, -3], "size": [5, 10, 6], "uv": [16, 48]}]}
            ]
        }

    # 9. GREY MATTER (Idea 35: Miniature Galvan Scale, Big Frog Eyes)
    elif "greymatter" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.greymatter",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 2, "visible_bounds_height": 2, "visible_bounds_offset": [0, 0.8, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 14, 0],
                    "cubes": [
                        {"origin": [-2.5, 8, -1.5], "size": [5, 7, 3], "uv": [16, 16]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 15, 0],
                    "cubes": [
                        # Big bulbous Galvan head
                        {"origin": [-3.5, 15, -3.5], "size": [7, 6, 7], "uv": [0, 0]},
                        # Prominent Frog Eye Bulges on sides
                        {"origin": [-4.5, 18, -3], "size": [2, 3, 3], "uv": [32, 0]},
                        {"origin": [2.5, 18, -3], "size": [2, 3, 3], "uv": [32, 0]}
                    ]
                },
                {"name": "rightArm", "pivot": [-3, 14, 0], "cubes": [{"origin": [-4.5, 7, -1], "size": [2, 8, 2], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [3, 14, 0], "cubes": [{"origin": [2.5, 7, -1], "size": [2, 8, 2], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-1.5, 8, 0], "cubes": [{"origin": [-2.5, 0, -1], "size": [2, 8, 2], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [1.5, 8, 0], "cubes": [{"origin": [0.5, 0, -1], "size": [2, 8, 2], "uv": [16, 48]}]}
            ]
        }

    # 10. WAY BIG (Idea 36: Cosmic Titan Crescent Fin & Shoulder Blades)
    elif "waybig" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.waybig",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 5, "visible_bounds_height": 6, "visible_bounds_offset": [0, 2.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-5.5, 12, -3], "size": [11, 13, 6], "uv": [16, 16], "inflate": 0.3},
                        # Giant Cosmic Shoulder Blades
                        {"origin": [-11, 22, -3], "size": [5, 9, 6], "uv": [0, 32]},
                        {"origin": [6, 22, -3], "size": [5, 9, 6], "uv": [0, 32]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 25, 0],
                    "cubes": [
                        {"origin": [-4, 25, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25},
                        # Iconic Crescent Fin on top of head
                        {"origin": [-1, 33, -3], "size": [2, 10, 7], "uv": [32, 0]}
                    ]
                },
                {"name": "rightArm", "pivot": [-6, 22, 0], "cubes": [{"origin": [-11, 10, -3], "size": [5, 15, 6], "uv": [40, 16], "inflate": 0.25}]},
                {"name": "leftArm", "pivot": [6, 22, 0], "cubes": [{"origin": [6, 10, -3], "size": [5, 15, 6], "uv": [32, 48], "inflate": 0.25}]},
                {"name": "rightLeg", "pivot": [-2.5, 12, 0], "cubes": [{"origin": [-5, 0, -2.5], "size": [5, 13, 5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2.5, 12, 0], "cubes": [{"origin": [0, 0, -2.5], "size": [5, 13, 5], "uv": [16, 48]}]}
            ]
        }

    # 11. GHOSTFREAK (Idea 37: Exposed Chest Tendrils & Hooded Shadow Form)
    elif "ghostfreak" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.ghostfreak",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 11, -2], "size": [8, 13, 4], "uv": [16, 16]},
                        # Exposed Chest Tendril Track
                        {"origin": [-2.5, 13, -2.8], "size": [5, 8, 1], "uv": [0, 32]},
                        # Wispy Ghost Tail (hanging below torso)
                        {"origin": [-2, 4, -1.5], "size": [4, 7, 3], "uv": [32, 32]}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 24, -3.5], "size": [7, 8, 7], "uv": [0, 0]},
                        # Pointed ghostly shroud top
                        {"origin": [-2, 31, -2], "size": [4, 4, 4], "uv": [32, 0]}
                    ]
                },
                {"name": "rightArm", "pivot": [-4.5, 22, 0], "cubes": [{"origin": [-8, 11, -2], "size": [3.5, 14, 3.5], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [4.5, 22, 0], "cubes": [{"origin": [4.5, 11, -2], "size": [3.5, 14, 3.5], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 11, 0], "cubes": [{"origin": [-3.5, 0, -1.8], "size": [3.5, 11, 3.5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 11, 0], "cubes": [{"origin": [0, 0, -1.8], "size": [3.5, 11, 3.5], "uv": [16, 48]}]}
            ]
        }

    # 12. UPGRADE (Idea 38: Galvanic Optic Ring & Nanite Shoulders)
    elif "upgrade" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.upgrade",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.2},
                        {"origin": [-4.5, 14, -2.5], "size": [9, 9, 5], "uv": [0, 32], "inflate": 0.1} # Nanite chest plate
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.2},
                        # Circular Optic Ring on Face
                        {"origin": [-2.5, 26, -4.8], "size": [5, 5, 1], "uv": [32, 0]}
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8.5, 11, -2.5], "size": [4.5, 13, 5], "uv": [40, 16], "inflate": 0.15}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 11, -2.5], "size": [4.5, 13, 5], "uv": [32, 48], "inflate": 0.15}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # DEFAULT ALIEN MORPH (Full Humanoid covering Steve 100%)
    else:
        return {
            "description": {
                "identifier": "geometry.ben10.alien_morph",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {"name": "body", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25}]},
                {"name": "head", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.25}, {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [32, 0], "inflate": 0.5}]},
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16], "inflate": 0.25}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48], "inflate": 0.25}]},
                {"name": "rightLeg", "pivot": [-1.9, 12, 0], "cubes": [{"origin": [-3.9, 0, -2], "size": [4, 12, 4], "uv": [0, 16], "inflate": 0.25}]},
                {"name": "leftLeg", "pivot": [1.9, 12, 0], "cubes": [{"origin": [-0.1, 0, -2], "size": [4, 12, 4], "uv": [16, 48], "inflate": 0.25}]}
            ]
        }

