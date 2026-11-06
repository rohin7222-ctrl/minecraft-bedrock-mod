# Ben 10 Bedrock Addon - Series Accurate Bosses & Vehicles (Maximum Visual Upgrade)
# 1. Kevin's Muscle Car (Dodge Dart with Blower & Dual Stripes)
# 2. Rust Bucket RV Base (Grandpa Max's Iconic Camper Van)
# 3. Vilgax the Conqueror (Chimera An Sui Generis Cybernetic Warlord)
# 4. Vilgax Battle Drone (Combat Spider Walker Droid)
# 5. Mutated Kevin 11 (Alien Amalgam Boss)
# 6. Vilgax Drone Ship (Flying Battleship)
# 7. Meteor Pod (Galvanic Crash Capsule)
# Strictly under 1000 lines - Pure Python

def get_kevin_car_geometry():
    """3D Model of Kevin Levin's Green Muscle Car with supercharger scoop, spoiler, and 5-spoke wheels"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.kevin_car",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 4.5,
                    "visible_bounds_height": 2.2,
                    "visible_bounds_offset": [0, 1, 0]
                },
                "bones": [
                    {"name": "root", "pivot": [0, 0, 0]},
                    {
                        "name": "body",
                        "parent": "root",
                        "pivot": [0, 5, 0],
                        "cubes": [
                            # Lower Chassis Base (Green with black underside)
                            {"origin": [-12, 4, -20], "size": [24, 6, 40], "uv": [0, 0]},
                            # Front Engine Hood
                            {"origin": [-11, 8, -19], "size": [22, 4, 14], "uv": [0, 48]},
                            # Supercharger Blower Scoop with Twin Chrome Intakes
                            {"origin": [-4, 12, -14], "size": [8, 3, 7], "uv": [74, 48]},
                            # Cabin & Slanted Roof
                            {"origin": [-10, 10, -5], "size": [20, 8, 18], "uv": [0, 68]},
                            # Front Slanted Windshield (Tinted glass)
                            {"origin": [-9.5, 10.5, -5.8], "size": [19, 7.2, 1], "uv": [78, 68]},
                            # Rear Slanted Window
                            {"origin": [-9.5, 10.5, 12.8], "size": [19, 7.2, 1], "uv": [78, 78]},
                            # Rear Trunk
                            {"origin": [-11, 8, 13], "size": [22, 4, 7], "uv": [0, 96]},
                            # Rear Ducktail Spoiler Wing
                            {"origin": [-12, 12, 18], "size": [24, 2, 3], "uv": [60, 96]},
                            # Front Bumper, Chrome Grille & Headlights
                            {"origin": [-12, 3, -22], "size": [24, 5, 2], "uv": [0, 110]},
                            # Rear Bumper, Tail Light Bar & Twin Exhausts
                            {"origin": [-12, 3, 20], "size": [24, 5, 2], "uv": [54, 110]}
                        ]
                    },
                    # 4 Individual Rotating Wheels with Silver 5-Spoke Rims
                    {"name": "wheel_front_left", "parent": "root", "pivot": [11, 4, -13], "cubes": [{"origin": [10.5, 0, -16], "size": [3, 8, 6], "uv": [80, 0]}]},
                    {"name": "wheel_front_right", "parent": "root", "pivot": [-11, 4, -13], "cubes": [{"origin": [-13.5, 0, -16], "size": [3, 8, 6], "uv": [80, 0]}]},
                    {"name": "wheel_back_left", "parent": "root", "pivot": [11, 4, 11], "cubes": [{"origin": [10.5, 0, 8], "size": [3, 8, 6], "uv": [80, 0]}]},
                    {"name": "wheel_back_right", "parent": "root", "pivot": [-11, 4, 11], "cubes": [{"origin": [-13.5, 0, 8], "size": [3, 8, 6], "uv": [80, 0]}]}
                ]
            }
        ]
    }

def get_rustbucket_geometry():
    """3D Model of Grandpa Max's Rust Bucket RV (256x256 High-Fidelity Camper Van)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.rustbucket",
                    "texture_width": 256,
                    "texture_height": 256,
                    "visible_bounds_width": 6.5,
                    "visible_bounds_height": 3.8,
                    "visible_bounds_offset": [0, 1.8, 0]
                },
                "bones": [
                    {"name": "root", "pivot": [0, 0, 0]},
                    {
                        "name": "body",
                        "parent": "root",
                        "pivot": [0, 5, 0],
                        "cubes": [
                            # Main Camper RV Body (White with classic Red/Green side stripe)
                            {"origin": [-14, 6, -26], "size": [28, 16, 52], "uv": [0, 0]},
                            # Front Cab Overhang & Windshield
                            {"origin": [-13, 9, -29], "size": [26, 12, 4], "uv": [0, 72]},
                            # Roof Air Conditioner Unit
                            {"origin": [-6, 22, -2], "size": [12, 4, 16], "uv": [64, 72]},
                            # Grandpa Max's Plumber Satellite Radar Dish
                            {"origin": [-3, 26, 4], "size": [6, 4, 6], "uv": [124, 72]},
                            # Front Chrome Bumper & Headlight Pods
                            {"origin": [-14, 4, -31], "size": [28, 5, 3], "uv": [0, 92]},
                            # Rear Ladder & Spare Tire Cover
                            {"origin": [-4, 7, 26], "size": [8, 9, 3], "uv": [66, 92]}
                        ]
                    },
                    # 6 Heavy Duty RV Wheels (Dual rear axle)
                    {"name": "wheel_fl", "parent": "root", "pivot": [13, 5, -18], "cubes": [{"origin": [12.5, 0, -21], "size": [3.5, 9, 7], "uv": [160, 0]}]},
                    {"name": "wheel_fr", "parent": "root", "pivot": [-13, 5, -18], "cubes": [{"origin": [-16.0, 0, -21], "size": [3.5, 9, 7], "uv": [160, 0]}]},
                    {"name": "wheel_ml", "parent": "root", "pivot": [13, 5, 8], "cubes": [{"origin": [12.5, 0, 5], "size": [3.5, 9, 7], "uv": [160, 0]}]},
                    {"name": "wheel_mr", "parent": "root", "pivot": [-13, 5, 8], "cubes": [{"origin": [-16.0, 0, 5], "size": [3.5, 9, 7], "uv": [160, 0]}]},
                    {"name": "wheel_rl", "parent": "root", "pivot": [13, 5, 17], "cubes": [{"origin": [12.5, 0, 14], "size": [3.5, 9, 7], "uv": [160, 0]}]},
                    {"name": "wheel_rr", "parent": "root", "pivot": [-13, 5, 17], "cubes": [{"origin": [-16.0, 0, 14], "size": [3.5, 9, 7], "uv": [160, 0]}]}
                ]
            }
        ]
    }

def get_vilgax_geometry():
    """3D Model of Vilgax the Conqueror (128x128 High-Definition Cephalopod Cybernetic Warlord)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.vilgax",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 3.5,
                    "visible_bounds_height": 4.5,
                    "visible_bounds_offset": [0, 2.2, 0]
                },
                "bones": [
                    {
                        "name": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            # Armored Cybernetic Torso with Gold Warlord Cuirass
                            {"origin": [-6, 16, -4], "size": [12, 16, 8], "uv": [0, 18]},
                            # Left Spiked Shoulder Pauldron
                            {"origin": [5.5, 27, -5], "size": [5, 6, 10], "uv": [44, 18]},
                            # Right Spiked Shoulder Pauldron
                            {"origin": [-10.5, 27, -5], "size": [5, 6, 10], "uv": [76, 18]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 32, 0],
                        "cubes": [
                            # Vilgax Alien Squid Head
                            {"origin": [-4, 32, -4], "size": [8, 9, 8], "uv": [0, 0]},
                            # 6 Segmented Facial Squid Tentacles (Beard)
                            {"origin": [-3.5, 26, -5.2], "size": [7, 7, 2], "uv": [36, 0]},
                            # Glowing Red Cybernetic Eye Visor Implant
                            {"origin": [1, 35, -4.8], "size": [2.5, 2.5, 1], "uv": [56, 0]}
                        ]
                    },
                    {
                        "name": "rightArm",
                        "parent": "body",
                        "pivot": [-7, 30, 0],
                        "cubes": [
                            # Heavy Armored Cybernetic Right Arm
                            {"origin": [-11, 14, -3], "size": [5, 17, 6], "uv": [0, 44]},
                            # Translucent Ruby Laser Energy Blade
                            {"origin": [-12, 4, -1], "size": [2, 16, 2], "uv": [24, 44]}
                        ]
                    },
                    {
                        "name": "leftArm",
                        "parent": "body",
                        "pivot": [7, 30, 0],
                        "cubes": [
                            # Left Arm with Ruby Shield Emitter
                            {"origin": [6, 14, -3], "size": [5, 17, 6], "uv": [34, 44]},
                            # Shield Projector Emitter Node
                            {"origin": [10.5, 18, -4], "size": [2, 8, 8], "uv": [58, 44]}
                        ]
                    },
                    {
                        "name": "rightLeg",
                        "parent": "body",
                        "pivot": [-3, 16, 0],
                        "cubes": [
                            # Heavy Plated Greaves (Dedicated Right Leg UV)
                            {"origin": [-5.5, 0, -3], "size": [5, 16, 6], "uv": [0, 70]}
                        ]
                    },
                    {
                        "name": "leftLeg",
                        "parent": "body",
                        "pivot": [3, 16, 0],
                        "cubes": [
                            # Heavy Plated Greaves (Dedicated Left Leg UV)
                            {"origin": [0.5, 0, -3], "size": [5, 16, 6], "uv": [24, 70]}
                        ]
                    }
                ]
            }
        ]
    }

def get_battle_drone_geometry():
    """3D Model of Vilgax Battle Drone (Combat Samurai Walker Droid)"""
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
                            {"origin": [-2.5, 8, -2], "size": [5, 6, 4], "uv": [28, 16]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            {"origin": [-2.5, 24, -2.5], "size": [5, 4, 5], "uv": [0, 0]},
                            # Conical Samurai Sensor Helmet Brow
                            {"origin": [-5, 27, -5], "size": [10, 2, 10], "uv": [0, 34]},
                            # Glowing Crimson Laser Visor
                            {"origin": [-2, 24.5, -3], "size": [4, 2, 1], "uv": [22, 0]}
                        ]
                    },
                    {
                        "name": "rightArm",
                        "parent": "body",
                        "pivot": [-4, 22, 0],
                        "cubes": [
                            {"origin": [-7, 12, -1.5], "size": [3, 11, 3], "uv": [42, 34]},
                            {"origin": [-7.5, 8, -2], "size": [4, 4, 4], "uv": [48, 16]}
                        ]
                    },
                    {
                        "name": "leftArm",
                        "parent": "body",
                        "pivot": [4, 22, 0],
                        "cubes": [
                            {"origin": [4, 12, -1.5], "size": [3, 11, 3], "uv": [42, 34]},
                            {"origin": [3.5, 8, -2], "size": [4, 4, 4], "uv": [48, 16]}
                        ]
                    },
                    # 3 Hydraulic Spider Walker Legs
                    {"name": "leg_front_left", "parent": "body", "pivot": [3, 10, 2], "cubes": [{"origin": [2.5, 0, 2], "size": [3, 10, 4], "uv": [0, 48]}]},
                    {"name": "leg_front_right", "parent": "body", "pivot": [-3, 10, 2], "cubes": [{"origin": [-5.5, 0, 2], "size": [3, 10, 4], "uv": [0, 48]}]},
                    {"name": "leg_back", "parent": "body", "pivot": [0, 10, -3], "cubes": [{"origin": [-1.5, 0, -6], "size": [3, 10, 4], "uv": [16, 48]}]}
                ]
            }
        ]
    }

def get_kevin11_geometry():
    """3D Model of Mutated Kevin 11 (Alien Amalgam Boss)"""
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": "geometry.ben10.kevin11",
                    "texture_width": 128,
                    "texture_height": 128,
                    "visible_bounds_width": 4,
                    "visible_bounds_height": 4,
                    "visible_bounds_offset": [0, 2, 0]
                },
                "bones": [
                    {
                        "name": "body",
                        "pivot": [0, 24, 0],
                        "cubes": [
                            # Half-Fourarms, Half-Heatblast Torso
                            {"origin": [-5, 12, -3], "size": [10, 14, 6], "uv": [0, 18]},
                            # Diamondhead Crystalline Back Spikes
                            {"origin": [-2, 18, 3], "size": [4, 10, 2], "uv": [34, 18]},
                            # Cannonbolt Yellow Armored Carapace Shell on Back
                            {"origin": [-4, 13, 3], "size": [8, 10, 3], "uv": [48, 18]}
                        ]
                    },
                    {
                        "name": "head",
                        "parent": "body",
                        "pivot": [0, 26, 0],
                        "cubes": [
                            # Split Amalgam Face: Left Human/Fourarms, Right Magma Rock
                            {"origin": [-4, 26, -4], "size": [8, 8, 8], "uv": [0, 0]},
                            # Heatblast Flame Crown on right side
                            {"origin": [0, 34, -3], "size": [4, 4, 6], "uv": [34, 0]}
                        ]
                    },
                    # Upper Left Arm: Four Arms' Massive Red Arm
                    {"name": "arm_upper_left", "parent": "body", "pivot": [5, 24, 0], "cubes": [{"origin": [5, 14, -2.5], "size": [5, 12, 5], "uv": [0, 42]}]},
                    # Lower Left Arm: Ripjaws' Webbed Aquatic Claw
                    {"name": "arm_lower_left", "parent": "body", "pivot": [5, 16, 0], "cubes": [{"origin": [5, 7, -2], "size": [4, 8, 4], "uv": [22, 42]}]},
                    # Upper Right Arm: Heatblast's Volcanic Magma Arm
                    {"name": "arm_upper_right", "parent": "body", "pivot": [-5, 24, 0], "cubes": [{"origin": [-10, 14, -2.5], "size": [5, 12, 5], "uv": [40, 42]}]},
                    # Lower Right Arm: Diamondhead's Crystal Blade Forearm
                    {"name": "arm_lower_right", "parent": "body", "pivot": [-5, 16, 0], "cubes": [{"origin": [-9.5, 5, -2], "size": [4, 10, 4], "uv": [62, 42]}]},
                    # XLR8 Raptor Speed Legs with Roller Heels
                    {"name": "rightLeg", "parent": "body", "pivot": [-2, 12, 0], "cubes": [{"origin": [-4, 0, -2], "size": [4, 12, 4], "uv": [0, 62]}]},
                    {"name": "leftLeg", "parent": "body", "pivot": [2, 12, 0], "cubes": [{"origin": [0, 0, -2], "size": [4, 12, 4], "uv": [18, 62]}]},
                    # XLR8 Segmented Tail
                    {"name": "tail", "parent": "body", "pivot": [0, 14, 3], "cubes": [{"origin": [-1.5, 13, 3], "size": [3, 3, 9], "uv": [36, 62]}]}
                ]
            }
        ]
    }

def get_vilgax_ship_geometry():
    """3D Model of Vilgax's Drone Ship (Central saucer hull + 2 giant engine pods)"""
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
                            {"origin": [28, 2, -10], "size": [14, 18, 20], "uv": [64, 0]},
                            {"origin": [-42, 2, -10], "size": [14, 18, 20], "uv": [64, 0]}
                        ]
                    }
                ]
            }
        ]
    }

def get_meteor_pod_geometry():
    """3D Model of Omnitrix Meteor Pod (Galvanic Crash Capsule)"""
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
                    "visible_bounds_offset": [0, 1.5, 0]
                },
                "bones": [
                    {
                        "name": "root",
                        "pivot": [0, 0, 0],
                        "cubes": [
                            {"origin": [-8, 0, -8], "size": [16, 16, 16], "uv": [0, 0]},
                            # Open Hydraulic Top Hatch revealing glowing core
                            {"origin": [-6, 16, -6], "size": [12, 3, 12], "uv": [0, 34]},
                            # Internal Galvanic Hourglass Pedestal
                            {"origin": [-2.5, 12, -2.5], "size": [5, 6, 5], "uv": [38, 34]}
                        ]
                    }
                ]
            }
        ]
    }
