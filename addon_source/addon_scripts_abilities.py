# Ben 10 Bedrock Addon - Modular Abilities Code
# Series Accurate Species Powers & Crouch Variations (Strictly under 1000 lines)

def get_abilities_code():
    return r"""export function executeAbilityByType(player, abilityType, alienName, colorCode, isCrouching = false) {
  const aLower = alienName.toLowerCase();

  // 1. Heatblast: Fire Boarding & Flame Flight (Idea 51)
  if (abilityType === "fire_breath" || aLower.includes("heatblast")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.ghast.fireball @a ~ ~ ~ 1 0.8");
      player.runCommandAsync("particle minecraft:basic_flame_particle ^ ^0.2 ^1");
      player.runCommandAsync("particle minecraft:lava_particle ^ ^0.2 ^2");
      player.runCommandAsync("particle minecraft:smoke_particle ^ ^0.2 ^3");
      player.runCommandAsync("effect @s levitation 2 2 true");
      player.runCommandAsync("effect @s slow_falling 5 1 true");
      player.runCommandAsync("effect @s speed 4 4 true");
      player.runCommandAsync("damage @e[r=7,rm=1,type=!player] 18 fire by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] FIRE SURFBOARD FLIGHT!`);
    } else {
      player.runCommandAsync("playsound mob.ghast.fireball @a ~ ~ ~ 1 1");
      player.runCommandAsync("particle minecraft:basic_flame_particle ^ ^1.2 ^2");
      player.runCommandAsync("particle minecraft:basic_flame_particle ^0.5 ^1.2 ^3");
      player.runCommandAsync("damage @e[r=8,rm=1,type=!player] 14 fire by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Flame Burst!`);
    }
    return;
  }

  // 2. Four Arms: Earth Fissure Slam & Sonic Thunderclap (Idea 60)
  if (abilityType === "thunder_clap" || aLower.includes("four arms") || aLower.includes("fourarms")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.warden.sonic_boom @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("playsound random.explode @a ~ ~ ~ 1 0.8");
      player.runCommandAsync("camerashake add @s 3.0 1.2 positional");
      player.runCommandAsync("particle minecraft:huge_explosion_emitter ~ ~1 ~");
      player.runCommandAsync("particle minecraft:sonic_boom ~ ~1.5 ~");
      player.runCommandAsync("damage @e[r=11,rm=1,type=!player] 25 entity_attack by @s");
      player.runCommandAsync("effect @e[r=11,rm=1,type=!player] levitation 1 5 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] 4-ARM GROUND FISSURE SLAM!`);
    } else {
      player.runCommandAsync("playsound mob.warden.sonic_boom @a ~ ~ ~ 1 1");
      player.runCommandAsync("playsound random.explode @a ~ ~ ~ 0.8 1.2");
      player.runCommandAsync("particle minecraft:sonic_boom ^ ^1.2 ^2");
      player.runCommandAsync("damage @e[r=9,rm=1,type=!player] 18 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Thunder Clap Slam!`);
    }
    return;
  }

  // 3. XLR8: Supersonic Water Running, Mirage & Tornado Vortex (Idea 53)
  if (abilityType === "speed_dash" || aLower.includes("xlr8")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.enderdragon.growl @a ~ ~ ~ 1 1.8");
      player.runCommandAsync("playsound mob.warden.sonic_boom @a ~ ~ ~ 0.8 1.5");
      player.runCommandAsync("particle minecraft:sonic_boom ~ ~1 ~");
      player.runCommandAsync("particle minecraft:huge_explosion_emitter ~ ~1 ~");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] levitation 2 3 true");
      player.runCommandAsync("damage @e[r=9,rm=1,type=!player] 18 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] SUPERSONIC TORNADO VORTEX!`);
    } else {
      player.runCommandAsync("playsound random.bow @a ~ ~ ~ 1 0.4");
      player.runCommandAsync("playsound mob.enderdragon.growl @a ~ ~ ~ 0.5 2.0");
      player.runCommandAsync("effect @s speed 4 12 true");
      player.runCommandAsync("effect @s dolphins_grace 4 3 true");
      player.runCommandAsync("particle minecraft:crit ^ ^1 ^2");
      player.runCommandAsync("particle minecraft:sonic_boom ^ ^1 ^-1");
      player.runCommandAsync("damage @e[r=7,rm=1,type=!player] 14 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Supersonic Mirage Dash!`);
    }
    return;
  }

  // 4. Diamondhead: Crystal Ramp Launch & Spike Rain (Idea 52)
  if (abilityType === "diamond_shards" || aLower.includes("diamondhead")) {
    if (isCrouching) {
      player.runCommandAsync("playsound random.glass @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("playsound random.anvil_land @a ~ ~ ~ 0.8 1.5");
      player.runCommandAsync("camerashake add @s 1.5 0.6 positional");
      player.runCommandAsync("particle minecraft:blue_flame_particle ~ ~1 ~");
      player.runCommandAsync("particle minecraft:blue_flame_particle ~ ~2 ~");
      player.runCommandAsync("effect @s levitation 1 4 true");
      player.runCommandAsync("effect @s slow_falling 4 1 true");
      player.runCommandAsync("effect @s resistance 5 3 true");
      player.runCommandAsync("damage @e[r=10,rm=1,type=!player] 20 projectile by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] CRYSTAL SPIRE LAUNCH & SHARDS!`);
    } else {
      player.runCommandAsync("playsound random.glass @a ~ ~ ~ 1 1");
      player.runCommandAsync("particle minecraft:blue_flame_particle ^ ^1.2 ^4");
      player.runCommandAsync("damage @e[r=14,rm=1,type=!player] 15 projectile by @s");
      player.runCommandAsync("effect @s absorption 5 1 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Diamond Shard Barrage!`);
    }
    return;
  }

  // 5. Cannonbolt: Pinball Ricochet & Heavy Shell Roll (Idea 54)
  if (abilityType === "ball_roll" || aLower.includes("cannonbolt")) {
    if (isCrouching) {
      player.runCommandAsync("playsound random.anvil_land @a ~ ~ ~ 1 1.8");
      player.runCommandAsync("playsound mob.iron_golem.death @a ~ ~ ~ 1 1.5");
      player.runCommandAsync("camerashake add @s 2.5 0.8 positional");
      player.runCommandAsync("particle minecraft:huge_explosion_emitter ~ ~1 ~");
      player.runCommandAsync("effect @s resistance 5 5 true");
      player.runCommandAsync("effect @s speed 3 8 true");
      player.runCommandAsync("damage @e[r=8,rm=1,type=!player] 24 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] PINBALL SPHERE RICOCHET SLAM!`);
    } else {
      player.runCommandAsync("playsound random.anvil_land @a ~ ~ ~ 0.8 1.8");
      player.runCommandAsync("effect @s resistance 3 4 true");
      player.runCommandAsync("effect @s speed 3 5 true");
      player.runCommandAsync("damage @e[r=7,rm=1,type=!player] 16 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Armored Ball Charge!`);
    }
    return;
  }

  // 6. Ghostfreak: Block Phasing & Spectral Terror (Idea 55)
  if (abilityType === "ghost_phase" || aLower.includes("ghostfreak")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.vex.charge @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("playsound mob.wither.ambient @a ~ ~ ~ 0.8 1.2");
      player.runCommandAsync("particle minecraft:witch_spell ~ ~1 ~");
      player.runCommandAsync("effect @s invisibility 8 0 true");
      player.runCommandAsync("effect @s absorption 10 2 true");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] blindness 6 1 true");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] weakness 8 2 true");
      player.runCommandAsync("damage @e[r=9,rm=1,type=!player] 18 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] SPECTRAL POSSESSION & TERROR!`);
    } else {
      player.runCommandAsync("playsound mob.vex.charge @a ~ ~ ~ 1 1");
      player.runCommandAsync("tp @s ^ ^ ^5");
      player.runCommandAsync("effect @s invisibility 6 0 true");
      player.runCommandAsync("effect @e[r=6,rm=1,type=!player] blindness 4 0 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Wall Phasing Teleport!`);
    }
    return;
  }

  // 7. Wildmutt: Sensory Echolocation & Beast Pounce (Idea 58)
  if (abilityType === "wildmutt_pounce" || aLower.includes("wildmutt")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.warden.listening @a ~ ~ ~ 1 1.2");
      player.runCommandAsync("playsound mob.wolf.pant @a ~ ~ ~ 1 0.8");
      player.runCommandAsync("particle minecraft:sonic_boom ~ ~1 ~");
      player.runCommandAsync("effect @s night_vision 20 0 true");
      player.runCommandAsync("effect @e[r=22,rm=1,type=!player] glowing 10 0 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] VULPIMANCER ECHOLOCATION SCENT!`);
    } else {
      player.runCommandAsync("playsound mob.wolf.growl @a ~ ~ ~ 1 0.8");
      player.runCommandAsync("effect @s jump_boost 3 3 true");
      player.runCommandAsync("effect @s speed 3 4 true");
      player.runCommandAsync("damage @e[r=7,rm=1,type=!player] 16 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Savage Beast Pounce!`);
    }
    return;
  }

  // 8. Ripjaws: Aquatic Superiority & Steel Jaw Snap (Idea 57)
  if (abilityType === "ripjaws_bite" || aLower.includes("ripjaws")) {
    if (isCrouching) {
      player.runCommandAsync("playsound random.splash @a ~ ~ ~ 1 1.2");
      player.runCommandAsync("playsound mob.iron_golem.death @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("effect @s conduit_power 30 0 true");
      player.runCommandAsync("effect @s water_breathing 30 0 true");
      player.runCommandAsync("effect @s dolphins_grace 15 4 true");
      player.runCommandAsync("effect @s speed 10 4 true");
      player.runCommandAsync("damage @e[r=8,rm=1,type=!player] 22 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] APEX OCEAN PREDATOR STRIKE!`);
    } else {
      player.runCommandAsync("playsound random.anvil_land @a ~ ~ ~ 1 1.6");
      player.runCommandAsync("particle minecraft:crit ^ ^1.2 ^2");
      player.runCommandAsync("damage @e[r=6,rm=1,type=!player] 20 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Steel Jaw Crunch!`);
    }
    return;
  }

  // 9. Grey Matter: Anatomical Weakness Scan & Brain Overclock (Idea 56)
  if (abilityType === "greymatter_scan" || aLower.includes("grey matter") || aLower.includes("greymatter")) {
    if (isCrouching) {
      player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.8");
      player.runCommandAsync("effect @s night_vision 30 0 true");
      player.runCommandAsync("effect @s haste 25 3 true");
      player.runCommandAsync("effect @s jump_boost 20 2 true");
      player.runCommandAsync("effect @s speed 20 2 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] GALVAN BRAIN OVERCLOCK!`);
    } else {
      player.runCommandAsync("playsound mob.warden.listening @a ~ ~ ~ 1 1.5");
      player.runCommandAsync("particle minecraft:electric_spark_particle ~ ~1 ~");
      player.runCommandAsync("effect @e[r=16,rm=1,type=!player] slowness 10 3 true");
      player.runCommandAsync("effect @e[r=16,rm=1,type=!player] weakness 10 3 true");
      player.runCommandAsync("effect @e[r=16,rm=1,type=!player] glowing 10 0 true");
      player.runCommandAsync("damage @e[r=16,rm=1,type=!player] 8 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] ANATOMICAL WEAKNESS EXPOSED!`);
    }
    return;
  }

  // 10. Upgrade: Nanite Machine Merge & Optic Laser (Idea 59)
  if (abilityType === "machine_upgrade" || aLower.includes("upgrade")) {
    if (isCrouching) {
      player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.2");
      player.runCommandAsync("playsound mob.guardian.attack @a ~ ~ ~ 1 1");
      player.runCommandAsync("particle minecraft:electric_spark_particle ~ ~1 ~");
      player.runCommandAsync("effect @e[r=10,type=iron_golem] strength 45 4 true");
      player.runCommandAsync("effect @e[r=10,type=iron_golem] speed 45 3 true");
      player.runCommandAsync("effect @e[r=10,type=iron_golem] resistance 45 3 true");
      player.runCommandAsync("effect @s strength 20 4 true");
      player.runCommandAsync("effect @s resistance 20 3 true");
      player.runCommandAsync("damage @e[r=10,rm=1,type=!player,type=!iron_golem] 20 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] GALVANIC NANITE OVERDRIVE!`);
    } else {
      player.runCommandAsync("playsound mob.guardian.attack @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("particle minecraft:villager_happy ^ ^1.5 ^4");
      player.runCommandAsync("particle minecraft:electric_spark_particle ^ ^1.5 ^4");
      player.runCommandAsync("damage @e[r=14,rm=1,type=!player] 18 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Galvanic Optic Laser!`);
    }
    return;
  }

  // 11. Stinkfly: Toxic Slime Flight & Acid Spit
  if (abilityType === "slime_spit" || aLower.includes("stinkfly")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.slime.attack @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("particle minecraft:slime ~ ~1 ~");
      player.runCommandAsync("effect @s levitation 2 2 true");
      player.runCommandAsync("effect @s slow_falling 6 1 true");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] slowness 10 4 true");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] poison 6 1 true");
      player.runCommandAsync("damage @e[r=9,rm=1,type=!player] 16 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] TOXIC SLIME GEYSER & FLIGHT!`);
    } else {
      player.runCommandAsync("playsound mob.slime.attack @a ~ ~ ~ 1 1.2");
      player.runCommandAsync("particle minecraft:villager_happy ^ ^1.2 ^2");
      player.runCommandAsync("damage @e[r=8,rm=1,type=!player] 12 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Acid Slime Spit!`);
    }
    return;
  }

  // 12. Humungousaur Titan Stomp
  if (abilityType === "humungousaur_growth" || aLower.includes("humungousaur")) {
    player.runCommandAsync("playsound mob.enderdragon.growl @a ~ ~ ~ 1 0.7");
    player.runCommandAsync("camerashake add @s 2 1.5 positional");
    player.runCommandAsync("particle minecraft:huge_explosion_emitter ~ ~1 ~");
    player.runCommandAsync("particle minecraft:sonic_boom ~ ~1.5 ~");
    player.runCommandAsync("effect @s strength 20 6 true");
    player.runCommandAsync("effect @s resistance 20 4 true");
    player.runCommandAsync("damage @e[r=10,rm=1,type=!player] 22 entity_attack by @s");
    player.runCommandAsync("title @s actionbar §6§l[HUMUNGOUSAUR] TITAN GROWTH (60 FT) STOMP!");
    return;
  }

  // 13. Upchuck: Matter Devour & Plasma Spit
  if (abilityType === "matter_eat" || aLower.includes("upchuck")) {
    if (isCrouching) {
      player.runCommandAsync("playsound mob.slime.attack @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("particle minecraft:slime ~ ~1 ~");
      player.runCommandAsync("damage @e[r=6,rm=1,type=!player] 12 entity_attack by @s");
      player.runCommandAsync("effect @s absorption 15 2 true");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Devoured Matter Tendrils!`);
    } else {
      player.runCommandAsync("playsound mob.ghast.fireball @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("particle minecraft:huge_explosion_emitter ^ ^1.5 ^4");
      player.runCommandAsync("damage @e[r=12,rm=1,type=!player] 20 fire by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Explosive Plasma Spit!`);
    }
    return;
  }

  switch (abilityType) {
    case "optic_laser":
      player.runCommandAsync("playsound mob.guardian.attack @a ~ ~ ~ 1 1.2");
      player.runCommandAsync("particle minecraft:villager_happy ^ ^1.5 ^4");
      player.runCommandAsync("damage @e[r=14,rm=1,type=!player] 20 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Optic Laser Beam!`);
      break;

    case "cosmic_beam":
      player.runCommandAsync("playsound mob.warden.sonic_boom @a ~ ~ ~ 1 0.7");
      player.runCommandAsync("particle minecraft:sonic_boom ^ ^2 ^4");
      player.runCommandAsync("damage @e[r=16,rm=1,type=!player] 26 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Cosmic Beam Ray!`);
      break;

    case "frost_breath":
      player.runCommandAsync("playsound random.fizz @a ~ ~ ~ 1 1.5");
      player.runCommandAsync("particle minecraft:water_splash_particle_manual ^ ^1.2 ^2");
      player.runCommandAsync("effect @e[r=9,rm=1,type=!player] slowness 8 4 true");
      player.runCommandAsync("damage @e[r=9,rm=1,type=!player] 14 freeze by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Cryo Frost Breath!`);
      break;

    case "sonic_screech":
      player.runCommandAsync("playsound mob.warden.sonic_boom @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("particle minecraft:sonic_boom ^ ^1.2 ^2");
      player.runCommandAsync("damage @e[r=10,rm=1,type=!player] 18 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Sonic Screech!`);
      break;

    case "reality_warp":
      player.runCommandAsync("playsound beacon.power @a ~ ~ ~ 1 0.5");
      player.runCommandAsync("particle minecraft:totem_particle ~ ~1 ~");
      player.runCommandAsync("damage @e[r=15,rm=1,type=!player] 32 magic by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Reality Warp Obliteration!`);
      break;

    default:
      player.runCommandAsync("particle minecraft:crit ^ ^1 ^2");
      player.runCommandAsync("damage @e[r=8,rm=1,type=!player] 12 entity_attack by @s");
      player.runCommandAsync(`title @s actionbar ${colorCode}[${alienName}] Alien Strike!`);
      break;
  }
}
"""

