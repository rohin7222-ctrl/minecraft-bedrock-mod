# Ben 10 Bedrock Addon - Series Accurate 3D Alien Geometries (Modern & AU Aliens)
# Alien Force, Ultimate Alien, Omniverse, and AU 3D Models (Strictly under 1000 lines)

def get_modern_alien_geometry(alien_id):
    """Returns dedicated 3D Bedrock geometry for Alien Force, Ultimate, Omniverse, and AU aliens"""

    # 1. HUMUNGOUSAUR (Broad Muscular Torso, Thick Spiked Tail & Dinosaur Snout)
    if "humungousaur" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.humungousaur",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 4, "visible_bounds_height": 4, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-5.5, 11, -3], "size": [11, 13, 6], "uv": [16, 16], "inflate": 0.2},
                        {"origin": [-2, 11, 3], "size": [4, 4, 10], "uv": [0, 32]}, # Spiked dinosaur tail
                        {"origin": [-1.5, 12, 12], "size": [3, 2, 3], "uv": [0, 46]} # Tail club
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        {"origin": [-3.5, 24, -7], "size": [7, 5, 3], "uv": [32, 0]} # Reptilian dinosaur snout
                    ]
                },
                {"name": "rightArm", "pivot": [-6, 23, 0], "cubes": [{"origin": [-11, 11, -3], "size": [5, 13, 6], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [6, 23, 0], "cubes": [{"origin": [6, 11, -3], "size": [5, 13, 6], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2.5, 12, 0], "cubes": [{"origin": [-5.5, 0, -3], "size": [5, 12, 6], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2.5, 12, 0], "cubes": [{"origin": [0.5, 0, -3], "size": [5, 12, 6], "uv": [16, 48]}]}
            ]
        }

    # 2. SWAMPFIRE (Plant Bark Torso, Flaming Branch Shoulders, Methane Fire Crown)
    elif "swampfire" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.swampfire",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25},
                        {"origin": [-6, 20, -3], "size": [3, 4, 6], "uv": [0, 32]}, # Vine flame shoulder right
                        {"origin": [3, 20, -3], "size": [3, 4, 6], "uv": [0, 32]} # Vine flame shoulder left
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.2},
                        {"origin": [-3, 31, -3], "size": [6, 4, 6], "uv": [32, 0]} # Fire crown petals
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16], "inflate": 0.2}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48], "inflate": 0.2}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 3. BIG CHILL (Moth Wings, Cloak Torso & Insect Antennae)
    elif "bigchill" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.bigchill",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 4, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.15},
                        {"origin": [-7, 10, 2], "size": [6, 16, 1], "uv": [0, 32]}, # Left folded moth wing
                        {"origin": [1, 10, 2], "size": [6, 16, 1], "uv": [0, 32]} # Right folded moth wing
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        {"origin": [-4.5, 30, -5], "size": [1.5, 5, 2], "uv": [32, 0]}, # Left moth antenna
                        {"origin": [3, 30, -5], "size": [1.5, 5, 2], "uv": [32, 0]} # Right moth antenna
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-7.5, 11, -1.5], "size": [3.5, 13, 3.5], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 11, -1.5], "size": [3.5, 13, 3.5], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-3.5, 0, -1.5], "size": [3.5, 12, 3.5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -1.5], "size": [3.5, 12, 3.5], "uv": [16, 48]}]}
            ]
        }

    # 4. CHROMASTONE (Crystal Back Spires, Large Cyclops Head Horn)
    elif "chromastone" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.chromastone",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25},
                        {"origin": [-3, 16, 2], "size": [2, 9, 2], "uv": [0, 32]}, # Back crystal spire 1
                        {"origin": [1, 16, 2], "size": [2, 9, 2], "uv": [0, 32]} # Back crystal spire 2
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.2},
                        {"origin": [-1, 31, -3], "size": [2, 7, 3], "uv": [32, 0]} # Large cyan head horn spike
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16], "inflate": 0.2}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48], "inflate": 0.2}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 5. ECHO ECHO (Sonic Amplifier Resonator Canisters & Headphones)
    elif "echoecho" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.echoecho",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 2.5, "visible_bounds_height": 2.5, "visible_bounds_offset": [0, 1, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 12, -2], "size": [7, 10, 4], "uv": [16, 16]},
                        {"origin": [-3, 14, 2], "size": [2, 7, 2], "uv": [0, 32]}, # Back speaker canister 1
                        {"origin": [1, 14, 2], "size": [2, 7, 2], "uv": [0, 32]} # Back speaker canister 2
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 22, -3.5], "size": [7, 7, 7], "uv": [0, 0]},
                        {"origin": [-4.5, 23, -2], "size": [1, 4, 4], "uv": [32, 0]}, # Left headphone bell
                        {"origin": [3.5, 23, -2], "size": [1, 4, 4], "uv": [32, 0]} # Right headphone bell
                    ]
                },
                {"name": "rightArm", "pivot": [-4.5, 21, 0], "cubes": [{"origin": [-6.5, 12, -1.5], "size": [2.5, 9, 3], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [4.5, 21, 0], "cubes": [{"origin": [4, 12, -1.5], "size": [2.5, 9, 3], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-1.8, 12, 0], "cubes": [{"origin": [-3, 3, -1.5], "size": [2.5, 9, 3], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [1.8, 12, 0], "cubes": [{"origin": [0.5, 3, -1.5], "size": [2.5, 9, 3], "uv": [16, 48]}]}
            ]
        }

    # 6. FEEDBACK (Conductoid Golden Antenna Plugs & Tail)
    elif "feedback" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.feedback",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.2},
                        {"origin": [-1, 12, 2], "size": [2, 2, 8], "uv": [0, 32]}, # Conductoid plug tail
                        {"origin": [-1.5, 11.5, 10], "size": [3, 3, 2], "uv": [0, 44]} # Golden tail plug prongs
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        {"origin": [-5.5, 29, -2], "size": [1.5, 6, 2], "uv": [32, 0]}, # Left antenna plug
                        {"origin": [4, 29, -2], "size": [1.5, 6, 2], "uv": [32, 0]} # Right antenna plug
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16], "inflate": 0.15}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48], "inflate": 0.15}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    # 7. RATH (Appoplexian Tiger Snout & Wrist Claws)
    elif "rath" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.rath",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-5, 11, -2.5], "size": [10, 13, 5], "uv": [16, 16], "inflate": 0.25}
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        {"origin": [-3, 24, -6], "size": [6, 4, 2], "uv": [32, 0]}, # Tiger muzzle snout
                        {"origin": [-4.5, 31, -1], "size": [2, 3, 2], "uv": [32, 8]}, # Left feline ear
                        {"origin": [2.5, 31, -1], "size": [2, 3, 2], "uv": [32, 8]} # Right feline ear
                    ]
                },
                {
                    "name": "rightArm", "pivot": [-6, 23, 0],
                    "cubes": [
                        {"origin": [-10, 11, -2.5], "size": [4.5, 13, 5], "uv": [40, 16]},
                        {"origin": [-10.5, 11, -5.5], "size": [1, 1.5, 4], "uv": [40, 34]} # Razor wrist claw
                    ]
                },
                {
                    "name": "leftArm", "pivot": [6, 23, 0],
                    "cubes": [
                        {"origin": [5.5, 11, -2.5], "size": [4.5, 13, 5], "uv": [32, 48]},
                        {"origin": [9.5, 11, -5.5], "size": [1, 1.5, 4], "uv": [40, 34]} # Razor wrist claw
                    ]
                },
                {"name": "rightLeg", "pivot": [-2.5, 12, 0], "cubes": [{"origin": [-5, 0, -2.5], "size": [4.5, 12, 5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2.5, 12, 0], "cubes": [{"origin": [0.5, 0, -2.5], "size": [4.5, 12, 5], "uv": [16, 48]}]}
            ]
        }

    # 8. ALIEN X (Celestialsapien 3 Cosmic Head Horns)
    elif "alien_x" in alien_id or "alienx" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.alienx",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {"name": "body", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.2}]},
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        # 3 Iconic Cosmic Horns
                        {"origin": [-1, 32, -2], "size": [2, 5, 2], "uv": [32, 0]}, # Center Horn
                        {"origin": [-3.5, 31, -2], "size": [1.5, 4, 2], "uv": [32, 0]}, # Left Horn
                        {"origin": [2, 31, -2], "size": [1.5, 4, 2], "uv": [32, 0]} # Right Horn
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-7.5, 12, -1.8], "size": [3.5, 12, 3.5], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 12, -1.8], "size": [3.5, 12, 3.5], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-3.8, 0, -1.8], "size": [3.8, 12, 3.8], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -1.8], "size": [3.8, 12, 3.8], "uv": [16, 48]}]}
            ]
        }

    # 9. ARMODRILLO (Heavy Drilling Jackhammers & Armored Carapace)
    elif "armodrillo" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.armodrillo",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3.5, "visible_bounds_height": 3.5, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-5, 11, -2.5], "size": [10, 13, 5], "uv": [16, 16], "inflate": 0.25},
                        {"origin": [-6, 18, -3], "size": [12, 6, 6], "uv": [0, 32]} # Heavy drill shoulder plate
                    ]
                },
                {"name": "head", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]}]},
                {
                    "name": "rightArm", "pivot": [-6, 22, 0],
                    "cubes": [
                        {"origin": [-11, 10, -3], "size": [5, 14, 6], "uv": [40, 16]},
                        {"origin": [-10, 8, -2], "size": [3, 4, 4], "uv": [40, 36]} # Jackhammer drill bit
                    ]
                },
                {
                    "name": "leftArm", "pivot": [6, 22, 0],
                    "cubes": [
                        {"origin": [6, 10, -3], "size": [5, 14, 6], "uv": [32, 48]},
                        {"origin": [7, 8, -2], "size": [3, 4, 4], "uv": [40, 36]} # Jackhammer drill bit
                    ]
                },
                {"name": "rightLeg", "pivot": [-2.5, 12, 0], "cubes": [{"origin": [-5, 0, -2.5], "size": [5, 12, 5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2.5, 12, 0], "cubes": [{"origin": [0, 0, -2.5], "size": [5, 12, 5], "uv": [16, 48]}]}
            ]
        }

    # 10. WATER HAZARD (Mollusk Barnacle Shell & Palm Water Blasters)
    elif "water_hazard" in alien_id or "waterhazard" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.waterhazard",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4.5, 11, -2.5], "size": [9, 13, 5], "uv": [16, 16], "inflate": 0.2},
                        {"origin": [-4, 13, 2.2], "size": [8, 10, 2], "uv": [0, 32]} # Crab shell back
                    ]
                },
                {"name": "head", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.2}]},
                {
                    "name": "rightArm", "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-9, 11, -2.5], "size": [4.5, 13, 5], "uv": [40, 16]},
                        {"origin": [-8.5, 9, -2], "size": [3, 2, 4], "uv": [40, 36]} # Palm water blaster nozzle
                    ]
                },
                {
                    "name": "leftArm", "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4.5, 11, -2.5], "size": [4.5, 13, 5], "uv": [32, 48]},
                        {"origin": [5.5, 9, -2], "size": [3, 2, 4], "uv": [40, 36]} # Palm water blaster nozzle
                    ]
                },
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4.5, 0, -2.5], "size": [4.5, 12, 5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2.5], "size": [4.5, 12, 5], "uv": [16, 48]}]}
            ]
        }

    # 11. GOOP (Polymorph Slime with Floating Anti-Gravity UFO Projector)
    elif "goop" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.goop",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3.5, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {"name": "body", "pivot": [0, 24, 0], "cubes": [{"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.15}]},
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 23, -3.5], "size": [7, 7, 7], "uv": [0, 0]},
                        # Floating Anti-Gravity UFO Projector Disc hovering above head!
                        {"origin": [-4.5, 33, -4.5], "size": [9, 1.5, 9], "uv": [0, 32]},
                        {"origin": [-2, 34.5, -2], "size": [4, 1.5, 4], "uv": [0, 44]}
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-7.5, 11, -1.8], "size": [3.5, 13, 3.5], "uv": [40, 16]}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 11, -1.8], "size": [3.5, 13, 3.5], "uv": [32, 48]}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-3.5, 0, -1.8], "size": [3.5, 12, 3.5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -1.8], "size": [3.5, 12, 3.5], "uv": [16, 48]}]}
            ]
        }

    # 12. JETRAY (Manta Ray Flight Wings & Horns)
    elif "jetray" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.jetray",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 4, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.1},
                        {"origin": [-1, 11, 2], "size": [2, 2, 9], "uv": [0, 32]} # Neuroshock tail
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                        {"origin": [-4.5, 30, -3], "size": [1.5, 5, 2], "uv": [32, 0]}, # Left crest horn
                        {"origin": [3, 30, -3], "size": [1.5, 5, 2], "uv": [32, 0]} # Right crest horn
                    ]
                },
                {
                    "name": "rightArm", "pivot": [-5, 22, 0],
                    "cubes": [
                        {"origin": [-8, 12, -2], "size": [4, 12, 4], "uv": [40, 16]},
                        {"origin": [-14, 12, 0], "size": [6, 10, 0.5], "uv": [32, 32]} # Manta flight wing
                    ]
                },
                {
                    "name": "leftArm", "pivot": [5, 22, 0],
                    "cubes": [
                        {"origin": [4, 12, -2], "size": [4, 12, 4], "uv": [32, 48]},
                        {"origin": [8, 12, 0], "size": [6, 10, 0.5], "uv": [32, 32]} # Manta flight wing
                    ]
                },
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-3.5, 0, -1.8], "size": [3.5, 12, 3.5], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -1.8], "size": [3.5, 12, 3.5], "uv": [16, 48]}]}
            ]
        }

    # 13. SPIDERMONKEY (4 Simian Arms & Long Monkey Tail)
    elif "spidermonkey" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.spidermonkey",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-3.5, 12, -2], "size": [7, 10, 4], "uv": [16, 16]},
                        {"origin": [-1, 12, 2], "size": [2, 2, 8], "uv": [0, 32]} # Simian furry tail
                    ]
                },
                {"name": "head", "pivot": [0, 24, 0], "cubes": [{"origin": [-3.5, 22, -3.5], "size": [7, 7, 7], "uv": [0, 0]}]},
                {"name": "rightArm", "pivot": [-4.5, 21, 0], "cubes": [{"origin": [-7.5, 12, -1.5], "size": [3, 9, 3], "uv": [40, 16]}]},
                {"name": "rightArm2", "parent": "body", "pivot": [-4.5, 15, 0], "cubes": [{"origin": [-7.5, 6, -1.5], "size": [3, 9, 3], "uv": [40, 32]}]},
                {"name": "leftArm", "pivot": [4.5, 21, 0], "cubes": [{"origin": [4.5, 12, -1.5], "size": [3, 9, 3], "uv": [32, 48]}]},
                {"name": "leftArm2", "parent": "body", "pivot": [4.5, 15, 0], "cubes": [{"origin": [4.5, 6, -1.5], "size": [3, 9, 3], "uv": [48, 48]}]},
                {"name": "rightLeg", "pivot": [-1.8, 12, 0], "cubes": [{"origin": [-3, 3, -1.5], "size": [2.5, 9, 3], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [1.8, 12, 0], "cubes": [{"origin": [0.5, 3, -1.5], "size": [2.5, 9, 3], "uv": [16, 48]}]}
            ]
        }

    # 14. CARNITRIX HORROR VARIANTS
    elif "carnitrix" in alien_id:
        return {
            "description": {
                "identifier": "geometry.ben10.carnitrix_horror",
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 3, "visible_bounds_offset": [0, 1.5, 0]
            },
            "bones": [
                {
                    "name": "body", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 12, -2], "size": [8, 12, 4], "uv": [16, 16], "inflate": 0.25},
                        {"origin": [-4.5, 14, -2.8], "size": [9, 8, 1.5], "uv": [16, 32]} # Exposed bloody ribcage spikes
                    ]
                },
                {
                    "name": "head", "pivot": [0, 24, 0],
                    "cubes": [
                        {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0], "inflate": 0.3},
                        {"origin": [-5, 26, -4.5], "size": [10, 4, 1], "uv": [32, 0]}
                    ]
                },
                {"name": "rightArm", "pivot": [-5, 22, 0], "cubes": [{"origin": [-9, 10, -2.5], "size": [5, 14, 5], "uv": [40, 16], "inflate": 0.25}]},
                {"name": "leftArm", "pivot": [5, 22, 0], "cubes": [{"origin": [4, 11, -2], "size": [4, 13, 4], "uv": [32, 48], "inflate": 0.2}]},
                {"name": "rightLeg", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                {"name": "leftLeg", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
            ]
        }

    return None
