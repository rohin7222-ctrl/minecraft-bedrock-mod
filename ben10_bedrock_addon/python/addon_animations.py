# Ben 10 Bedrock Addon - Series Accurate Player Animations
# 1. animation.ben10.press_omnitrix: Left wrist raises, right hand slams down on the Omnitrix!
# Strictly under 1000 lines - Pure Python

import os
import json

def get_player_press_animation():
    """
    3D Bedrock Animation where the player raises left arm to chest,
    exposing the wrist watch, and the right arm raises up and SLAMS down
    onto the Omnitrix dial before transformation triggers!
    Visible in both 1st-person and 3rd-person!
    """
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.ben10.press_omnitrix": {
                "loop": False,
                "animation_length": 1.1,
                "bones": {
                    "leftarm": {
                        "rotation": {
                            "0.0": [0, 0, 0],
                            "0.3": [45, -55, 20],
                            "0.6": [50, -60, 25],
                            "0.75": [40, -55, 18],  # Recoil from slam impact
                            "1.0": [45, -55, 20],
                            "1.1": [0, 0, 0]
                        },
                        "position": {
                            "0.0": [0, 0, 0],
                            "0.3": [2.5, 1.2, -2.5],
                            "0.6": [2.8, 1.4, -2.8],
                            "0.75": [2.5, 0.9, -2.5], # Impact pushdown
                            "1.0": [2.5, 1.2, -2.5],
                            "1.1": [0, 0, 0]
                        }
                    },
                    "rightarm": {
                        "rotation": {
                            "0.0": [0, 0, 0],
                            "0.35": [-70, 35, -15],  # Hand raised high above left wrist
                            "0.65": [38, 22, 5],     # SLAM! Hand impacts left wrist Omnitrix
                            "0.8": [35, 20, 5],      # Pressing down hard on the dial
                            "1.0": [10, 5, 0],
                            "1.1": [0, 0, 0]
                        },
                        "position": {
                            "0.0": [0, 0, 0],
                            "0.35": [-1.0, 3.5, -1.0],
                            "0.65": [2.6, 1.3, -2.6],  # Matches left wrist coordinates!
                            "0.8": [2.6, 1.1, -2.6],   # Pressed into dial
                            "1.0": [0.5, 0.2, -0.5],
                            "1.1": [0, 0, 0]
                        }
                    }
                }
            },
            # Idea 2: Rotating Dial Turn Animation
            "animation.ben10.dial_spin": {
                "loop": False,
                "animation_length": 0.35,
                "bones": {
                    "leftarm": {
                        "rotation": {
                            "0.0": [0, 0, 0],
                            "0.15": [30, -35, 15],
                            "0.35": [0, 0, 0]
                        },
                        "position": {
                            "0.0": [0, 0, 0],
                            "0.15": [1.2, 0.5, -1.0],
                            "0.35": [0, 0, 0]
                        }
                    }
                }
            }
        }
    }

def build_player_animations(RP_DIR):
    """Writes animation files into RP - without breaking vanilla player camera"""
    anim_dir = os.path.join(RP_DIR, "animations")
    os.makedirs(anim_dir, exist_ok=True)

    with open(os.path.join(anim_dir, "player_omnitrix.animation.json"), "w", encoding="utf-8") as f:
        json.dump(get_player_press_animation(), f, indent=2)

    # Note: Do NOT write player.entity.json as overriding player geometry
    # causes Steve's head/face to block 1st person camera!

