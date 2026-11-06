# Ben 10 Bedrock Addon - Series Accurate Bosses & Vehicles
# 1. Vilgax the Conqueror (Boss)
# 2. Vilgax Battle Drone (Combat Droid)
# 3. Kevin's Muscle Car (Driveable Vehicle)
# 4. Vilgax's Drone Ship (Flying Battleship)
# 5. Rust Bucket RV Base (Grandpa Max's Camper Van - Idea 81)
# 6. Meteor Pod (Omnitrix Crash Capsule - Idea 82)
# 7. Mutated Kevin 11 (Alien Amalgam Boss - Idea 84)
# Strictly under 1000 lines - Pure Python

def get_kevin_car_geometry():
    """3D Model of Kevin Levin's Green Muscle Car (Dodge Dart with twin black stripes & blower)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.kevin_car",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 4,
                    "visible_bounds_height": 2,
                    "visible_bounds_offset": [0, 1, 0]
                },
                "bones": [
                    {
                        "name": "root",
                        "pivot": [0, 0, 0]
                    },
                    {
                        "name": "body",
                        "parent": "root",
                        "pivot": [0, 5, 0],
                        "cubes": [
                            # Lower Chassis Base
                            {"origin": [-12, 4, -20], "size": [24, 6, 40], "uv": [0, 0]},
                            # Hood & Front Engine Grille
                            {"origin": [-11, 8, -19], "size": [22, 4, 14], "uv": [0, 48]},
                            # Supercharger Blower Scoop (Twin Intake)
                            {"origin": [-4, 12, -14], "size": [8, 3, 6], "uv": [64, 48]},
                            # Cabin & Roof
                            {"origin": [-10, 10, -5], "size": [20, 8, 18], "uv": [0, 70]},
                            # Slanted Windshield & Glass
                            {"origin": [-9.5, 10.5, -6], "size": [19, 7, 1], "uv": [64, 70]},
                            {"origin": [-9.5, 10.5, 12], "size": [19, 7, 1], "uv": [64, 70]},
                            # Rear Trunk
                            {"origin": [-11, 8, 13], "size": [22, 4, 6], "uv": [0, 98]},
                            # Front Bumper & Headlights
                            {"origin": [-12, 3, -22], "size": [24, 4, 2], "uv": [60, 98]},
                            # Rear Bumper & Red Tail Light Strip
                            {"origin": [-12, 4, 20], "size": [24, 3, 2], "uv": [60, 106]}
                        ]
                    },
                    # 4 Authentic Muscle Car Wheels with Silver Rims
                    {
                        "name": "wheel_front_left",
                        "parent": "root",
                        "pivot": [11, 4, -13],
                        "cubes": [{"origin": [10.5, 0, -16], "size": [3, 8, 6], "uv": [96, 0]}]
                    },
                    {
                        "name": "wheel_front_right",
                        "parent": "root",
                        "pivot": [-11, 4, -13],
                        "cubes": [{"origin": [-13.5, 0, -16], "size": [3, 8, 6], "uv": [96, 0]}]
                    },
                    {
                        "name": "wheel_back_left",
                        "parent": "root",
                        "pivot": [11, 4, 11],
                        "cubes": [{"origin": [10.5, 0, 8], "size": [3, 8, 6], "uv": [96, 0]}]
                    },
                    {
                        "name": "wheel_back_right",
                        "parent": "root",
                        "pivot": [-11, 4, 11],
                        "cubes": [{"origin": [-13.5, 0, 8], "size": [3, 8, 6], "uv": [96, 0]}]
                    }
                ]
            }
        ]
    }

def get_vilgax_geometry():
    """3D Model of Vilgax the Conqueror (Chimera An Sui Generis Cybernetic Warlord)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.vilgax",
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": 3,
                    "visible_bounds_height": 4,
                    "visible_bounds_offset": [0, 2, 0]
                },
                "bones": [
                    {
                        "name": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            # Armored Cybernetic Torso
                            {"origin": [-6, 16, -4], "size": [12, 16, 8], "uv": [0, 16]},
                            # Massive Battle Shoulder Plates
                            {"origin": [-9, 28, -5], "size": [4, 5, 10], "uv": [40, 16]},
                            {"origin": [5, 28, -5], "size": [4, 5, 10], "uv": [40, 16]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 32, 0],
                        "cubes": [
                            # Vilgax Squid Face & Cybernetic Respirator Helmet
                            {"origin": [-4, 32, -4], "size": [8, 9, 8], "uv": [0, 0]},
                            # Facial Squid Tentacles / Beard
                            {"origin": [-3.5, 26, -5], "size": [7, 6, 2], "uv": [32, 0]},
                            # Glowing Red Cybernetic Eye
                            {"origin": [1, 35, -4.5], "size": [2, 2, 1], "uv": [52, 0]}
                        ]
                    },
                    {
                        "name": "rightArm",
                        "parent": "body",
                        "pivot": [-7, 30, 0],
                        "cubes": [
                            # Cybernetic Arm & Ruby Laser Gauntlet
                            {"origin": [-11, 14, -3], "size": [5, 17, 6], "uv": [0, 40]},
                            # Massive Arm Energy Blade
                            {"origin": [-12, 6, -1], "size": [2, 14, 2], "uv": [22, 40]}
                        ]
                    },
                    {
                        "name": "leftArm",
                        "parent": "body",
                        "pivot": [7, 30, 0],
                        "cubes": [
                            {"origin": [6, 14, -3], "size": [5, 17, 6], "uv": [32, 40]},
                            # Ruby Energy Shield Emitter
                            {"origin": [10.5, 18, -4], "size": [2, 8, 8], "uv": [48, 48]}
                        ]
                    },
                    {
                        "name": "rightLeg",
                        "parent": "body",
                        "pivot": [-3, 16, 0],
                        "cubes": [
                            {"origin": [-5.5, 0, -3], "size": [5, 16, 6], "uv": [0, 40]}
                        ]
                    },
                    {
                        "name": "leftLeg",
                        "parent": "body",
                        "pivot": [3, 16, 0],
                        "cubes": [
                            {"origin": [0.5, 0, -3], "size": [5, 16, 6], "uv": [0, 40]}
                        ]
                    }
                ]
            }
        ]
    }

def get_battle_drone_geometry():
    """3D Model of Vilgax's Battle Drone (Samurai head, red eye visor, multi-joint spider legs)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.battle_drone",
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": 3,
                    "visible_bounds_height": 3,
                    "visible_bounds_offset": [0, 1.5, 0]
                },
                "bones": [
                    {
                        "name": "body",
                        "pivot": [0, 18, 0],
                        "cubes": [
                            {"origin": [-4, 14, -3], "size": [8, 10, 6], "uv": [0, 16]},
                            {"origin": [-2.5, 8, -2], "size": [5, 6, 4], "uv": [28, 16]},
                            {"origin": [-1.5, 5, -1], "size": [3, 3, 2], "uv": [46, 16]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            {"origin": [-2.5, 24, -2.5], "size": [5, 4, 5], "uv": [0, 0]},
                            {"origin": [-6, 27, -6], "size": [12, 2, 12], "uv": [0, 32]},
                            {"origin": [-2, 24.5, -3], "size": [4, 2, 1], "uv": [24, 0]}
                        ]
                    },
                    {
                        "name": "rightArm",
                        "parent": "body",
                        "pivot": [-4, 22, 0],
                        "cubes": [
                            {"origin": [-7, 12, -1.5], "size": [3, 11, 3], "uv": [36, 32]},
                            {"origin": [-7.5, 8, -2], "size": [4, 4, 4], "uv": [48, 32]}
                        ]
                    },
                    {
                        "name": "leftArm",
                        "parent": "body",
                        "pivot": [4, 22, 0],
                        "cubes": [
                            {"origin": [4, 12, -1.5], "size": [3, 11, 3], "uv": [36, 32]},
                            {"origin": [3.5, 8, -2], "size": [4, 4, 4], "uv": [48, 32]}
                        ]
                    },
                    {
                        "name": "leg_front_left",
                        "parent": "body",
                        "pivot": [3, 10, 2],
                        "cubes": [
                            {"origin": [2.5, 4, 2], "size": [2, 7, 2], "uv": [0, 48]},
                            {"origin": [4, 0, 4], "size": [3, 5, 2], "uv": [8, 48]},
                            {"origin": [3.5, 0, 5], "size": [4, 1, 6], "uv": [20, 48]}
                        ]
                    },
                    {
                        "name": "leg_front_right",
                        "parent": "body",
                        "pivot": [-3, 10, 2],
                        "cubes": [
                            {"origin": [-4.5, 4, 2], "size": [2, 7, 2], "uv": [0, 48]},
                            {"origin": [-7, 0, 4], "size": [3, 5, 2], "uv": [8, 48]},
                            {"origin": [-7.5, 0, 5], "size": [4, 1, 6], "uv": [20, 48]}
                        ]
                    },
                    {
                        "name": "leg_back",
                        "parent": "body",
                        "pivot": [0, 10, -3],
                        "cubes": [
                            {"origin": [-1, 4, -5], "size": [2, 7, 2], "uv": [0, 48]},
                            {"origin": [-1.5, 0, -8], "size": [3, 5, 2], "uv": [8, 48]},
                            {"origin": [-2, 0, -11], "size": [4, 1, 6], "uv": [20, 48]}
                        ]
                    }
                ]
            }
        ]
    }

def get_vilgax_ship_geometry():
    """3D Model of Vilgax's Drone Ship (Central saucer hull + 2 giant engine pods, Image 2)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.vilgax_ship",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 8,
                    "visible_bounds_height": 4,
                    "visible_bounds_offset": [0, 2, 0]
                },
                "bones": [
                    {
                        "name": "root",
                        "pivot": [0, 0, 0],
                        "cubes": [
                            {"origin": [-16, 6, -16], "size": [32, 8, 32], "uv": [0, 0]},
                            {"origin": [-8, 14, -8], "size": [16, 6, 16], "uv": [0, 42]},
                            {"origin": [-14, 8, -17], "size": [28, 4, 1], "uv": [0, 66]},
                            {"origin": [-6, 1, -6], "size": [12, 5, 12], "uv": [64, 42]},
                            {"origin": [16, 8, -4], "size": [12, 4, 8], "uv": [64, 62]},
                            {"origin": [-28, 8, -4], "size": [12, 4, 8], "uv": [64, 62]},
                            {"origin": [28, 2, -10], "size": [14, 18, 20], "uv": [64, 0]},
                            {"origin": [-42, 2, -10], "size": [14, 18, 20], "uv": [64, 0]},
                            {"origin": [30, 0, -8], "size": [10, 2, 16], "uv": [0, 72]},
                            {"origin": [-40, 0, -8], "size": [10, 2, 16], "uv": [0, 72]}
                        ]
                    }
                ]
            }
        ]
    }

def get_rustbucket_geometry():
    """3D Model of Grandpa Max's Rust Bucket RV Camper Van (Idea 81)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.rustbucket",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 6,
                    "visible_bounds_height": 3,
                    "visible_bounds_offset": [0, 1.5, 0]
                },
                "bones": [
                    {
                        "name": "root",
                        "pivot": [0, 0, 0],
                        "cubes": [
                            # Main Camper RV Body (White with Red/Green side stripe)
                            {"origin": [-14, 6, -26], "size": [28, 16, 52], "uv": [0, 0]},
                            # Front Cab Windshield
                            {"origin": [-13, 10, -28], "size": [26, 10, 3], "uv": [0, 70]},
                            # Roof Air Conditioner & Plumber Satellite Dish
                            {"origin": [-6, 22, 2], "size": [12, 4, 14], "uv": [60, 70]},
                            {"origin": [-2, 26, 6], "size": [4, 3, 4], "uv": [100, 70]},
                            # Front Bumper & Headlights
                            {"origin": [-14, 5, -29], "size": [28, 4, 3], "uv": [0, 85]},
                            # Rear Ladder & Spare Tire
                            {"origin": [-4, 7, 26], "size": [8, 8, 3], "uv": [64, 85]}
                        ]
                    },
                    # 6 Sturdy RV Road Wheels
                    {"name": "wheel_f_l", "parent": "root", "pivot": [13, 5, -18], "cubes": [{"origin": [12, 0, -21], "size": [3, 8, 6], "uv": [96, 0]}]},
                    {"name": "wheel_f_r", "parent": "root", "pivot": [-13, 5, -18], "cubes": [{"origin": [-15, 0, -21], "size": [3, 8, 6], "uv": [96, 0]}]},
                    {"name": "wheel_m_l", "parent": "root", "pivot": [13, 5, 8], "cubes": [{"origin": [12, 0, 5], "size": [3, 8, 6], "uv": [96, 0]}]},
                    {"name": "wheel_m_r", "parent": "root", "pivot": [-13, 5, 8], "cubes": [{"origin": [-15, 0, 5], "size": [3, 8, 6], "uv": [96, 0]}]},
                    {"name": "wheel_b_l", "parent": "root", "pivot": [13, 5, 18], "cubes": [{"origin": [12, 0, 15], "size": [3, 8, 6], "uv": [96, 0]}]},
                    {"name": "wheel_b_r", "parent": "root", "pivot": [-13, 5, 18], "cubes": [{"origin": [-15, 0, 15], "size": [3, 8, 6], "uv": [96, 0]}]}
                ]
            }
        ]
    }

def get_meteor_pod_geometry():
    """3D Model of the Crashed Omnitrix Meteor Pod / Capsule (Idea 82)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.meteor_pod",
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": 3,
                    "visible_bounds_height": 3,
                    "visible_bounds_offset": [0, 1, 0]
                },
                "bones": [
                    {
                        "name": "pod",
                        "pivot": [0, 0, 0],
                        "cubes": [
                            # Outer Meteorite Crater Rock Shell
                            {"origin": [-8, 0, -8], "size": [16, 12, 16], "uv": [0, 0]},
                            # Opened Pod Hatch (Tapered Galvan Capsule)
                            {"origin": [-6, 10, -6], "size": [12, 6, 12], "uv": [0, 30]},
                            # Glowing Emerald Center Pedestal (Holds the Omnitrix!)
                            {"origin": [-3, 8, -3], "size": [6, 8, 6], "uv": [36, 0]}
                        ]
                    }
                ]
            }
        ]
    }

def get_kevin11_geometry():
    """3D Model of Mutated Kevin 11 Amalgam Boss (Idea 84)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.kevin11",
                    "texture_width": 64,
                    "texture_height": 64,
                    "visible_bounds_width": 3,
                    "visible_bounds_height": 3,
                    "visible_bounds_offset": [0, 1.5, 0]
                },
                "bones": [
                    {
                        "name": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            {"origin": [-5, 12, -3], "size": [10, 12, 6], "uv": [16, 16]},
                            # Heatblast Magma Shoulder Collar
                            {"origin": [-6, 22, -4], "size": [5, 4, 8], "uv": [0, 34]},
                            # Diamondhead Crystal Back Spikes
                            {"origin": [2, 20, 2], "size": [3, 10, 3], "uv": [32, 0]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            {"origin": [-4, 24, -4], "size": [8, 8, 8], "uv": [0, 0]},
                            # Horn on right side
                            {"origin": [-5, 30, -2], "size": [2, 5, 2], "uv": [32, 10]}
                        ]
                    },
                    # 4 Amalgam Arms
                    {"name": "rightArm1", "parent": "body", "pivot": [-6, 22, 0], "cubes": [{"origin": [-9, 12, -2], "size": [4, 12, 4], "uv": [40, 16]}]},
                    {"name": "leftArm1", "parent": "body", "pivot": [6, 22, 0], "cubes": [{"origin": [5, 12, -2], "size": [4, 12, 4], "uv": [32, 48]}]},
                    {"name": "rightArm2", "parent": "body", "pivot": [-6, 16, 0], "cubes": [{"origin": [-9, 6, -2], "size": [4, 10, 4], "uv": [40, 32]}]},
                    {"name": "leftArm2", "parent": "body", "pivot": [6, 16, 0], "cubes": [{"origin": [5, 6, -2], "size": [4, 10, 4], "uv": [48, 48]}]},
                    {"name": "rightLeg", "parent": "body", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 16]}]},
                    {"name": "leftLeg", "parent": "body", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [16, 48]}]}
                ]
            }
        ]
    }
