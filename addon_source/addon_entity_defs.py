# Ben 10 Bedrock Addon - Entity Definitions (BP & RP JSONs)
# Strictly under 1000 lines - Pure Python

def get_bp_kevin_car():
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:kevin_car",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["car", "vehicle", "inanimate"]},
                "minecraft:collision_box": {"width": 1.8, "height": 1.2},
                "minecraft:health": {"value": 120, "max": 120},
                "minecraft:physics": {},
                "minecraft:pushable": {"is_pushable": True, "is_pushable_by_piston": True},
                "minecraft:movement": {"value": 0.55},
                "minecraft:movement.basic": {},
                "minecraft:navigation.walk": {"can_path_over_water": False, "avoid_damage_blocks": True},
                "minecraft:rideable": {
                    "seat_count": 2,
                    "family_types": ["player"],
                    "interact_text": "action.interact.drive",
                    "seats": [
                        {"position": [0.35, 0.4, -0.2], "min_rider_count": 0, "max_rider_count": 1},
                        {"position": [-0.35, 0.4, -0.2], "min_rider_count": 1, "max_rider_count": 2}
                    ]
                },
                "minecraft:input_ground_controlled": {}
            }
        }
    }

def get_bp_vilgax():
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:vilgax",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["vilgax", "monster", "boss"]},
                "minecraft:collision_box": {"width": 1.4, "height": 2.8},
                "minecraft:health": {"value": 300, "max": 300},
                "minecraft:boss": {
                    "name": "§4§lVilgax the Conqueror",
                    "should_darken_sky": True,
                    "hud_range": 40
                },
                "minecraft:movement": {"value": 0.32},
                "minecraft:navigation.walk": {"can_path_over_water": True, "avoid_damage_blocks": True},
                "minecraft:physics": {},
                "minecraft:attack": {"damage": 18},
                "minecraft:behavior.melee_attack": {"priority": 1, "speed_multiplier": 1.25, "track_target": True},
                "minecraft:behavior.nearest_attackable_target": {
                    "priority": 1,
                    "entity_types": [{"filters": {"test": "is_family", "subject": "other", "value": "player"}, "max_dist": 48}]
                },
                "minecraft:behavior.random_stroll": {"priority": 4, "speed_multiplier": 0.8},
                "minecraft:behavior.random_look_around": {"priority": 5}
            }
        }
    }

def get_bp_battle_drone():
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:battle_drone",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["drone", "robot", "monster"]},
                "minecraft:collision_box": {"width": 1.2, "height": 1.9},
                "minecraft:health": {"value": 60, "max": 60},
                "minecraft:attack": {"damage": 10},
                "minecraft:movement": {"value": 0.30},
                "minecraft:navigation.walk": {"can_path_over_water": True, "avoid_damage_blocks": True},
                "minecraft:physics": {},
                "minecraft:behavior.melee_attack": {"priority": 2, "speed_multiplier": 1.15, "track_target": True},
                "minecraft:behavior.nearest_attackable_target": {
                    "priority": 1,
                    "entity_types": [{"filters": {"test": "is_family", "subject": "other", "value": "player"}, "max_dist": 36}]
                },
                "minecraft:behavior.random_stroll": {"priority": 5, "speed_multiplier": 0.75},
                "minecraft:behavior.random_look_around": {"priority": 6}
            }
        }
    }

def get_bp_vilgax_ship():
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:vilgax_ship",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["ship", "vehicle", "inanimate"]},
                "minecraft:collision_box": {"width": 3.0, "height": 1.8},
                "minecraft:health": {"value": 400, "max": 400},
                "minecraft:physics": {"has_gravity": False},
                "minecraft:movement": {"value": 0.45},
                "minecraft:movement.fly": {},
                "minecraft:navigation.fly": {"can_path_over_water": True},
                "minecraft:rideable": {
                    "seat_count": 1,
                    "family_types": ["player"],
                    "interact_text": "action.interact.fly.ship",
                    "seats": [{"position": [0.0, 1.2, 0.0], "min_rider_count": 0, "max_rider_count": 1}]
                },
                "minecraft:input_ground_controlled": {}
            }
        }
    }

def get_bp_rustbucket():
    """Grandpa Max's 4-Seat Rust Bucket RV Camper (Idea 81)"""
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:rustbucket",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["rv", "vehicle", "inanimate"]},
                "minecraft:collision_box": {"width": 2.2, "height": 1.8},
                "minecraft:health": {"value": 250, "max": 250},
                "minecraft:physics": {},
                "minecraft:pushable": {"is_pushable": True},
                "minecraft:movement": {"value": 0.48},
                "minecraft:movement.basic": {},
                "minecraft:navigation.walk": {"can_path_over_water": False, "avoid_damage_blocks": True},
                "minecraft:rideable": {
                    "seat_count": 4,
                    "family_types": ["player"],
                    "interact_text": "action.interact.drive.rustbucket",
                    "seats": [
                        {"position": [0.45, 0.6, -1.0], "min_rider_count": 0, "max_rider_count": 1},
                        {"position": [-0.45, 0.6, -1.0], "min_rider_count": 1, "max_rider_count": 2},
                        {"position": [0.45, 0.6, 0.6], "min_rider_count": 2, "max_rider_count": 3},
                        {"position": [-0.45, 0.6, 0.6], "min_rider_count": 3, "max_rider_count": 4}
                    ]
                },
                "minecraft:input_ground_controlled": {}
            }
        }
    }

def get_bp_meteor_pod():
    """Crashed Omnitrix Meteor Pod Capsule (Idea 82)"""
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:meteor_pod",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["pod", "capsule", "inanimate"]},
                "minecraft:collision_box": {"width": 1.5, "height": 1.2},
                "minecraft:health": {"value": 50, "max": 50},
                "minecraft:physics": {},
                "minecraft:interact": {
                    "interactions": [
                        {
                            "on_interact": {
                                "filters": {"test": "is_family", "subject": "other", "value": "player"}
                            },
                            "spawn_items": [{"name": "ben10:omnitrix_classic", "count": 1}],
                            "particle_on_start": {"particle_type": "minecraft:huge_explosion_emitter", "offset": [0, 1, 0]},
                            "play_sound": "random.levelup",
                            "hurt_item": 50
                        }
                    ]
                }
            }
        }
    }

def get_bp_kevin11():
    """Mutated Kevin 11 Amalgam Boss (Idea 84)"""
    return {
        "format_version": "1.20.80",
        "minecraft:entity": {
            "description": {
                "identifier": "ben10:kevin11",
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False
            },
            "components": {
                "minecraft:type_family": {"family": ["kevin11", "monster", "boss"]},
                "minecraft:collision_box": {"width": 1.6, "height": 2.4},
                "minecraft:health": {"value": 250, "max": 250},
                "minecraft:boss": {
                    "name": "§c§lMutated Kevin 11",
                    "should_darken_sky": True,
                    "hud_range": 35
                },
                "minecraft:attack": {"damage": 16},
                "minecraft:movement": {"value": 0.35},
                "minecraft:navigation.walk": {"can_path_over_water": True, "avoid_damage_blocks": True},
                "minecraft:physics": {},
                "minecraft:behavior.melee_attack": {"priority": 1, "speed_multiplier": 1.2, "track_target": True},
                "minecraft:behavior.nearest_attackable_target": {
                    "priority": 1,
                    "entity_types": [{"filters": {"test": "is_family", "subject": "other", "value": "player"}, "max_dist": 40}]
                },
                "minecraft:behavior.random_stroll": {"priority": 4, "speed_multiplier": 0.8},
                "minecraft:behavior.random_look_around": {"priority": 5}
            }
        }
    }

def get_rp_client_entity(identifier, geo_id, texture_path):
    return {
        "format_version": "1.10.0",
        "minecraft:client_entity": {
            "description": {
                "identifier": identifier,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": texture_path},
                "geometry": {"default": geo_id},
                "render_controllers": ["controller.render.default"],
                "spawn_egg": {"base_color": "#16a34a", "overlay_color": "#090d16"}
            }
        }
    }
