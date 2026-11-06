# Ben 10 Bedrock Addon - Modular Bedrock 1.21.20+ JavaScript Logic
# Interactive Omnitrix Dial UI (@minecraft/server-ui), Series Sound FX, Battery Timers
# Strictly under 1000 lines - Pure Python

def get_main_code():
    return r"""import { world, system, EquipmentSlot, ItemStack } from "@minecraft/server";
import { ActionFormData, ModalFormData, MessageFormData } from "@minecraft/server-ui";
import { ALL_ALIENS, WATCH_ALIENS, FUSION_POOL } from "./aliens_data.js";
import { executeAbilityByType } from "./abilities.js";

const playerStates = new Map();

function getPlayerState(player) {
  if (!playerStates.has(player.id)) {
    playerStates.set(player.id, {
      activeWatch: "omnitrix_classic",
      selectedAlienIndex: 0,
      isTransformed: false,
      currentAlien: null,
      transformSeconds: 0,
      rechargeSeconds: 0,
      isFusion: false,
      fusionAlien1: null,
      fusionAlien2: null,
      lastTapTime: 0,
      abilityCooldown: 0,
      masterControl: false,
      lifeFormLock: false,
      selfDestructSeconds: 0
    });
  }
  return playerStates.get(player.id);
}

function safeEquip(player, slot, itemId) {
  try {
    const equippable = player.getComponent("minecraft:equippable");
    if (!equippable) return false;

    let targetSlot = null;
    if (slot === "mainhand") targetSlot = EquipmentSlot.Mainhand;
    else if (slot === "offhand") targetSlot = EquipmentSlot.Offhand;
    else if (slot === "head") targetSlot = EquipmentSlot.Head;
    else if (slot === "chest") targetSlot = EquipmentSlot.Chest;
    else if (slot === "legs") targetSlot = EquipmentSlot.Legs;
    else if (slot === "feet") targetSlot = EquipmentSlot.Feet;

    if (targetSlot !== null) {
      if (itemId === null || itemId === "air") {
        equippable.setEquipment(targetSlot, undefined);
      } else {
        equippable.setEquipment(targetSlot, new ItemStack(itemId, 1));
      }
      return true;
    }
  } catch (e) {
    try {
      if (slot === "chest") {
        player.runCommandAsync(`replaceitem entity @s slot.armor.chest 0 ${itemId || "air"} 1 0`);
      } else if (slot === "mainhand") {
        player.runCommandAsync(`replaceitem entity @s slot.weapon.mainhand 0 ${itemId || "air"} 1 0`);
      }
    } catch (err) {}
  }
  return false;
}

// Interactive Omnitrix Dial UI via @minecraft/server-ui
function openOmnitrixDialUI(player, state) {
  if (state.rechargeSeconds > 0) {
    player.runCommandAsync("playsound random.break @a ~ ~ ~ 1 0.8");
    player.runCommandAsync(`title @s actionbar §c§l[OMNITRIX RECHARGING] §e⏳ ${state.rechargeSeconds}s Remaining`);
    return;
  }

  // Hologram Dial Activation Sound & FX
  player.runCommandAsync("playsound random.click @a ~ ~ ~ 1 1.8");
  player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 1.6");
  player.runCommandAsync("particle minecraft:villager_happy ~ ~1 ~");

  const watchKey = state.activeWatch ? state.activeWatch : "omnitrix_classic";
  const watchName = watchKey.replace("omnitrix_", "").replace("_", " ").toUpperCase();
  const alienList = WATCH_ALIENS[watchKey] || ALL_ALIENS;
  const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

  const form = new ActionFormData();
  form.title(`§2§l┏━━━━━━━━━━━━━━━━━━━━┓\n§a⚡ OMNITRIX: ${watchName} ⚡\n§2┗━━━━━━━━━━━━━━━━━━━━┛`);

  let statusText = `§a● CORE SYSTEM: §fONLINE §8| §bUSER: §fBEN TENNYSON\n`;
  statusText += `§e● STATUS: ${state.isTransformed ? "§eTRANSFORMED (" + state.currentAlien.name + ")" : "§bSTANDBY (HUMAN)"}\n`;
  if (state.isTransformed) {
    statusText += `§e● ENERGY TIMER: §f${state.transformSeconds}s ${isClassic ? "§7[Prototype Countdown]" : "§a[Manual Revert Ready]"}\n`;
  }
  if (state.masterControl) {
    statusText += `§b● MODE: §3MASTER CONTROL (UNLIMITED ENERGY)\n`;
  }
  statusText += `\n§7Touch any alien DNA matrix below to transform:`;
  form.body(statusText);

  let hasDetransformBtn = false;
  // If transformed into modern watch, or master control, show Revert button at top!
  if (state.isTransformed && (!isClassic || state.transformSeconds <= 0 || state.masterControl)) {
    form.button("§c§l[ ⚡ EMERGENCY MANUAL REVERT ⚡ ]\n§8Tap to return to normal Steve", "textures/items/detransform");
    hasDetransformBtn = true;
  }

  // Master Control Mode Switch
  let hasMasterBtn = false;
  if (!state.isTransformed) {
    form.button(`§b§l[ ⚡ MASTER CONTROL: ${state.masterControl ? "ON" : "OFF"} ⚡ ]\n§8Toggle Infinite Energy & Instant Morph`, "textures/items/omnitrix_activator");
    hasMasterBtn = true;
  }

  // Biomnitrix Dual Fusion Mode
  let hasFusionBtn = false;
  if (watchKey === "omnitrix_biomnitrix") {
    form.button("§e§l[ 🧬 BIOMNITRIX DUAL FUSION MATRIX 🧬 ]\n§8Combine 2 Alien DNA Samples", "textures/items/biomnitrix_fusion_ability");
    hasFusionBtn = true;
  }

  // List all series-accurate aliens for this Omnitrix with full stats
  for (const alien of alienList) {
    const iconPath = `textures/items/${alien.id}_ability`;
    form.button(`§2§l${alien.name.toUpperCase()}\n§7[${alien.species} • ⚔ ${alien.ability_type.replace('_', ' ').toUpperCase()}]`, iconPath);
  }

  form.show(player).then((response) => {
    if (response.canceled) return;

    let sel = response.selection;

    if (hasDetransformBtn) {
      if (sel === 0) {
        detransform(player, state);
        return;
      }
      sel--;
    }

    if (hasMasterBtn) {
      if (sel === 0) {
        state.masterControl = !state.masterControl;
        player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.8");
        player.runCommandAsync(`title @s actionbar §b§l[MASTER CONTROL ${state.masterControl ? "ENABLED" : "DISABLED"}]`);
        return;
      }
      sel--;
    }

    if (hasFusionBtn) {
      if (sel === 0) {
        openBiomnitrixFusionUI(player, state);
        return;
      }
      sel--;
    }

    const selectedAlien = alienList[sel];
    if (selectedAlien) {
      transformPlayer(player, selectedAlien, state);
    }
  });
}

// Biomnitrix Dynamic Fusion Menu
function openBiomnitrixFusionUI(player, state) {
  const form = new ModalFormData();
  form.title("§e§l🧬 BIOMNITRIX DUAL FUSION 🧬");

  const alienNames = FUSION_POOL.map(a => a.name);
  form.dropdown("§6Select Primary Alien (Alien 1):", alienNames, 0);
  form.dropdown("§bSelect Secondary Alien (Alien 2):", alienNames, 1);

  form.show(player).then((response) => {
    if (response.canceled) return;
    const idx1 = response.formValues[0];
    const idx2 = response.formValues[1];
    const a1 = FUSION_POOL[idx1];
    const a2 = FUSION_POOL[idx2];
    if (a1 && a2) {
      transformFusion(player, a1, a2, state);
    }
  });
}

function transformPlayer(player, alien, state) {
  const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

  // Mistransformation chance on Classic Prototype (6% chance)
  if (isClassic && !state.masterControl && Math.random() < 0.06 && !state.isFusion) {
    const watchAliens = WATCH_ALIENS[state.activeWatch || "omnitrix_classic"];
    if (watchAliens && watchAliens.length > 1) {
      const randomAlien = watchAliens[Math.floor(Math.random() * watchAliens.length)];
      if (randomAlien.id !== alien.id) {
        player.runCommandAsync("playsound random.break @a ~ ~ ~ 1 0.7");
        player.runCommandAsync("title @s subtitle §c§l[MISTRANSFORMATION!] §eRecalibrating...");
        alien = randomAlien;
      }
    }
  }

  state.isTransformed = true;
  state.isFusion = false;
  state.currentAlien = alien;
  state.fusionAlien1 = null;
  state.fusionAlien2 = null;
  state.transformSeconds = state.masterControl ? 9999 : 60;
  state.rechargeSeconds = 0;

  // Blinding Emerald Screen Flash & Sound Effects
  player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.4");
  player.runCommandAsync("playsound random.explode @a ~ ~ ~ 0.8 1.8");
  player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.8");
  player.runCommandAsync("camerashake add @s 1.5 0.5 positional");

  const flashColor = (state.activeWatch === "omnitrix_carnitrix" || state.activeWatch === "omnitrix_albedo") ? "§c§l█§4█████████§c§l█" : "§a§l█§2█████████§a§l█";
  player.runCommandAsync("title @s times 0 8 4");
  player.runCommandAsync(`title @s title ${flashColor}`);

  player.runCommandAsync("particle minecraft:villager_happy ~ ~1 ~");
  player.runCommandAsync("particle minecraft:sonic_boom ~ ~1 ~");

  // Alien Vocal Shout
  system.runTimeout(() => {
    player.runCommandAsync("title @s times 4 35 8");
    player.runCommandAsync(`title @s title ${alien.color_code}§l[ ${alien.name.toUpperCase()}! ]`);
    player.runCommandAsync(`title @s subtitle §7Species: §f${alien.species} §8| §bHome: §f${alien.species} Prime`);
  }, 8);

  // Equip 3D Alien Suit Armor
  safeEquip(player, "chest", `ben10:${alien.id}_suit`);

  // Equip Alien Ability item in mainhand
  safeEquip(player, "mainhand", "ben10:alien_ability");

  // Modern Omnitrixes provide Detransform item in hotbar!
  if (!isClassic) {
    player.runCommandAsync("give @s ben10:detransform 1");
  } else {
    player.runCommandAsync("clear @s ben10:detransform");
  }

  // Alien Status Effects
  for (const eff of alien.effects) {
    player.runCommandAsync(`effect @s ${eff.effect} ${state.masterControl ? 9999 : 65} ${eff.amplifier} true`);
  }
}

function transformFusion(player, a1, a2, state) {
  state.isTransformed = true;
  state.isFusion = true;
  state.currentAlien = a1;
  state.fusionAlien1 = a1;
  state.fusionAlien2 = a2;
  state.transformSeconds = state.masterControl ? 9999 : 75;
  state.rechargeSeconds = 0;

  const fusionName = `${a1.name.slice(0, Math.ceil(a1.name.length / 2))}-${a2.name.slice(Math.floor(a2.name.length / 2))}`;

  player.runCommandAsync("playsound beacon.power @a ~ ~ ~ 1 1.2");
  player.runCommandAsync("playsound random.explode @a ~ ~ ~ 1 1.5");
  player.runCommandAsync("particle minecraft:totem_particle ~ ~1 ~");
  player.runCommandAsync("title @s times 0 10 5");
  player.runCommandAsync("title @s title §e§l█§6█████████§e§l█");

  system.runTimeout(() => {
    player.runCommandAsync("title @s times 4 40 8");
    player.runCommandAsync(`title @s title §e§l[ ${fusionName.toUpperCase()}! ]`);
    player.runCommandAsync(`title @s subtitle §6[BIOMNITRIX FUSION] §f${a1.name} + ${a2.name}`);
  }, 8);

  safeEquip(player, "chest", "ben10:biomnitrix_fusion_suit");
  safeEquip(player, "mainhand", "ben10:biomnitrix_fusion_ability");
  player.runCommandAsync("give @s ben10:detransform 1");

  for (const eff of a1.effects) {
    player.runCommandAsync(`effect @s ${eff.effect} 75 ${eff.amplifier} true`);
  }
  for (const eff of a2.effects) {
    player.runCommandAsync(`effect @s ${eff.effect} 75 ${eff.amplifier} true`);
  }
}

function detransform(player, state) {
  state.isTransformed = false;
  state.isFusion = false;
  state.currentAlien = null;
  state.fusionAlien1 = null;
  state.fusionAlien2 = null;
  state.transformSeconds = 0;
  state.rechargeSeconds = state.masterControl ? 0 : 25;

  player.runCommandAsync("playsound random.explode @a ~ ~ ~ 0.6 1.8");
  player.runCommandAsync("playsound mob.slime.attack @a ~ ~ ~ 1 1.4");
  player.runCommandAsync("title @s times 0 8 4");
  player.runCommandAsync("title @s title §c§l█§4█████████§c§l█");
  player.runCommandAsync("title @s subtitle §c§l[REVERTED - RECHARGING]");

  player.runCommandAsync("particle minecraft:redstone_wire_dust_particle ~ ~1 ~");
  player.runCommandAsync("particle minecraft:smoke_particle ~ ~1 ~");

  player.runCommandAsync("effect @s clear");

  // Re-equip Wristwatch and Activator
  safeEquip(player, "chest", `ben10:${state.activeWatch || "omnitrix_classic"}`);
  player.runCommandAsync("clear @s ben10:alien_ability");
  player.runCommandAsync("clear @s ben10:biomnitrix_fusion_ability");
  player.runCommandAsync("clear @s ben10:detransform");

  // Ensure Omnitrix Activator is safely in inventory
  player.runCommandAsync("give @s ben10:omnitrix_activator 1");
}

// 1-Second Periodic Heartbeat Tick Loop
system.runInterval(() => {
  for (const player of world.getAllPlayers()) {
    const state = getPlayerState(player);
    const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

    if (state.isTransformed) {
      if (!state.masterControl && !state.lifeFormLock) {
        state.transformSeconds--;
      }

      const ratio = Math.max(0, Math.min(1.0, state.transformSeconds / 60.0));
      const bars = Math.round(ratio * 10);
      const batteryBar = `§a[${"█".repeat(bars)}${"░".repeat(10 - bars)}]`;

      if (state.transformSeconds <= 10 && state.transformSeconds > 0) {
        player.runCommandAsync("particle minecraft:redstone_wire_dust_particle ~ ~1 ~");
        if (state.transformSeconds === 10) {
          player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 0.8");
          player.runCommandAsync(`title @s actionbar §c§l[TIMEOUT IMMINENT] §4§l♥ ♥ ♥ §e10s §4§l♥ ♥ ♥ ${batteryBar}`);
        } else if (state.transformSeconds === 5) {
          player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 1.3");
          player.runCommandAsync(`title @s actionbar §c§l[TIMEOUT WARNING] §4§l♥ ♥ §e5s §4§l♥ ♥ ${batteryBar}`);
        } else if (state.transformSeconds <= 3) {
          player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 1.8");
          player.runCommandAsync("playsound random.click @a ~ ~ ~ 1 2.0");
          player.runCommandAsync(`title @s actionbar §4§l[SHUTTING DOWN!] §c§l♥ §4${state.transformSeconds}s §c§l♥ ${batteryBar}`);
        }
      } else {
        if (isClassic) {
          player.runCommandAsync(`title @s actionbar §8[ §a§l◎ CLASSIC OMNITRIX §8] ${state.currentAlien.color_code}§l${state.currentAlien.name.toUpperCase()} §8| §e⏳ ${state.transformSeconds}s §7[Auto-Revert at 0s]`);
        } else {
          player.runCommandAsync(`title @s actionbar §8[ ${state.currentAlien.color_code}§l◎ ${state.currentAlien.name.toUpperCase()} §8] ${batteryBar} §e${state.transformSeconds}s §8| §a[Sneak+Tap: REVERT]`);
        }
      }

      // Classic Omnitrix auto-reverts when timer reaches 0!
      if (state.transformSeconds <= 0) {
        detransform(player, state);
      }
    } else if (state.rechargeSeconds > 0) {
      state.rechargeSeconds--;

      const rechRatio = Math.max(0, Math.min(1.0, (25 - state.rechargeSeconds) / 25.0));
      const rechBars = Math.round(rechRatio * 10);
      const rechBar = `§c[${"█".repeat(rechBars)}${"░".repeat(10 - rechBars)}]`;
      player.runCommandAsync(`title @s actionbar §8[ §c§l◎ RECHARGING §8] ${rechBar} §e${state.rechargeSeconds}s`);

      if (state.rechargeSeconds <= 0) {
        player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.4");
        player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 2.0");
        player.runCommandAsync("title @s title §a§lOMNITRIX RECHARGED!");
        player.runCommandAsync(`title @s subtitle §8[§aAZMUTH AI§8] §f"Recharge complete. All systems nominal."`);
      }
    }
  }
}, 20);

// Interaction & Item Event Listeners
world.beforeEvents.itemUse.subscribe((event) => {
  const player = event.source;
  const item = event.itemStack;
  if (!item || !player) return;

  const state = getPlayerState(player);
  const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

  // 1. Direct Equipping of Omnitrix Watch from Hand -> Wrist!
  if (item.typeId.startsWith("ben10:omnitrix_")) {
    event.cancel = true;
    system.run(() => {
      state.activeWatch = item.typeId.replace("ben10:", "");
      state.selectedAlienIndex = 0;
      safeEquip(player, "chest", item.typeId);
      player.runCommandAsync("give @s ben10:omnitrix_activator 1");
      player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("playsound random.orb @a ~ ~ ~ 1 1.8");
      player.runCommandAsync("title @s title §a§lOMNITRIX ATTACHED!");
      player.runCommandAsync("title @s subtitle §eBiometric lock engaged to left wrist");
      openOmnitrixDialUI(player, state);
    });
    return;
  }

  // 2. Omnitrix Activator: Opens Interactive Dial UI!
  if (item.typeId === "ben10:omnitrix_activator") {
    event.cancel = true;
    system.run(() => {
      openOmnitrixDialUI(player, state);
    });
    return;
  }

  // 3. Dedicated Alien Ability Item
  if (item.typeId === "ben10:alien_ability" || item.typeId === "ben10:biomnitrix_fusion_ability") {
    event.cancel = true;
    system.run(() => {
      if (!state.isTransformed || !state.currentAlien) {
        player.runCommandAsync("title @s actionbar §c[NO ACTIVE TRANSFORMATION]");
        return;
      }

      // Modern Omnitrix Manual Revert via Sneak + Tap
      if (player.isSneaking && !isClassic) {
        player.runCommandAsync("title @s title §a§l[MANUAL REVERT]");
        player.runCommandAsync("title @s subtitle §eChest Dial Pressed");
        detransform(player, state);
        return;
      }

      if (state.isFusion && state.fusionAlien1 && state.fusionAlien2) {
        executeAbilityByType(player, state.fusionAlien1.ability_type, state.fusionAlien1.name, state.fusionAlien1.color_code, player.isSneaking);
      } else {
        executeAbilityByType(player, state.currentAlien.ability_type, state.currentAlien.name, state.currentAlien.color_code, player.isSneaking);
      }
    });
    return;
  }

  // 4. Dedicated Detransform Item
  if (item.typeId === "ben10:detransform") {
    event.cancel = true;
    system.run(() => {
      if (state.isTransformed) {
        if (isClassic && state.transformSeconds > 0 && !state.masterControl) {
          player.runCommandAsync("playsound random.break @a ~ ~ ~ 1 0.8");
          player.runCommandAsync(`title @s actionbar §c§l[PROTOTYPE ERROR] §eClassic Manual Revert Locked! ⏳ ${state.transformSeconds}s Remaining`);
          return;
        }
        player.runCommandAsync("title @s title §a§l[MANUAL REVERT]");
        player.runCommandAsync("title @s subtitle §eReverted to normal form");
        detransform(player, state);
      }
    });
    return;
  }

  // 5. Direct Alien Badges
  if (item.typeId.endsWith("_badge")) {
    const rawAlienId = item.typeId.replace("ben10:", "").replace("_badge", "");
    const directAlien = ALL_ALIENS.find(a => a.id === rawAlienId);
    if (directAlien) {
      event.cancel = true;
      system.run(() => {
        if (!state.activeWatch) state.activeWatch = directAlien.watch;
        transformPlayer(player, directAlien, state);
      });
      return;
    }
  }

  // 6. Entity Spawner Items
  if (item.typeId.startsWith("ben10:") && item.typeId.endsWith("_spawner")) {
    event.cancel = true;
    system.run(() => {
      const rawEntity = item.typeId.replace("ben10:", "").replace("_spawner", "");
      player.runCommandAsync(`summon ben10:${rawEntity} ~ ~ ~`);
      player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.4");
      player.runCommandAsync("particle minecraft:villager_happy ~ ~1 ~");
      player.runCommandAsync(`title @s actionbar §e[SUMMONED] §a§l${rawEntity.replace('_', ' ').toUpperCase()}!`);
    });
    return;
  }
});

// Chat Voice Commands System (!transform, !revert, !omnitrix, !mastercontrol, !dial)
world.beforeEvents.chatSend.subscribe((event) => {
  const msg = event.message.trim().toLowerCase();
  const player = event.sender;
  const state = getPlayerState(player);

  if (msg.startsWith("!transform ") || msg.startsWith("!alien ")) {
    event.cancel = true;
    const query = msg.replace("!transform ", "").replace("!alien ", "").trim();
    const found = ALL_ALIENS.find(a => a.name.toLowerCase().includes(query) || a.id.toLowerCase().includes(query));
    if (found) {
      system.run(() => {
        transformPlayer(player, found, state);
      });
    } else {
      system.run(() => {
        player.runCommandAsync(`title @s actionbar §c[DNA ERROR] Alien "${query}" not found in database!`);
      });
    }
    return;
  }

  if (msg === "!revert" || msg === "!detransform" || msg === "!human") {
    event.cancel = true;
    system.run(() => {
      const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";
      if (isClassic && state.transformSeconds > 0 && !state.masterControl) {
        player.runCommandAsync("playsound random.break @a ~ ~ ~ 1 0.8");
        player.runCommandAsync(`title @s actionbar §c§l[PROTOTYPE ERROR] §eClassic Manual Revert Locked! ⏳ ${state.transformSeconds}s Remaining`);
        return;
      }
      detransform(player, state);
    });
    return;
  }

  if (msg === "!mastercontrol" || msg === "!mc") {
    event.cancel = true;
    system.run(() => {
      state.masterControl = !state.masterControl;
      player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.8");
      player.runCommandAsync(`title @s actionbar §b§l[MASTER CONTROL ${state.masterControl ? "ENABLED" : "DISABLED"}]`);
    });
    return;
  }

  if (msg === "!dial" || msg === "!menu") {
    event.cancel = true;
    system.run(() => {
      openOmnitrixDialUI(player, state);
    });
    return;
  }
});

// Auto-equip & Welcome Starter Kit upon entering the world
world.afterEvents.playerSpawn.subscribe((event) => {
  const player = event.player;
  if (!player) return;
  if (event.initialSpawn) {
    player.runCommandAsync("title @s title §a§lBEN 10 ADDON ULTIMATE");
    player.runCommandAsync("title @s subtitle §eEquip an Omnitrix or tap Activator to transform!");
    player.runCommandAsync("give @s ben10:omnitrix_classic 1");
    player.runCommandAsync("give @s ben10:omnitrix_activator 1");
    player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.5");
  }
});
"""
