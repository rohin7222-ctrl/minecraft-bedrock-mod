# Ben 10 Bedrock Addon - Modular Bedrock 1.20.80+ / 1.21.x JavaScript Logic
# Interactive Omnitrix Dial UI (@minecraft/server-ui), Series Sound FX, Battery Timers
# Strictly under 1000 lines - Pure Python

def get_main_code():
    return r"""import { world, system, EquipmentSlot, ItemStack } from "@minecraft/server";
import { ActionFormData, ModalFormData, MessageFormData } from "@minecraft/server-ui";
import { ALL_ALIENS, WATCH_ALIENS, FUSION_POOL, PLAYLIST_CLASSIC, PLAYLIST_AF, PLAYLIST_ULTIMATE, PLAYLIST_OMNIVERSE } from "./aliens_data.js";
import { executeAbilityByType, executeFusionAbility } from "./abilities.js";

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

// Mobile Safe Form Show with UserBusy Retry
function showActionFormSafe(player, form, onSelect, retries = 4) {
  form.show(player).then((response) => {
    if (response.canceled) {
      if (response.cancelationReason === "UserBusy" && retries > 0) {
        system.runTimeout(() => {
          showActionFormSafe(player, form, onSelect, retries - 1);
        }, 5);
      }
      return;
    }
    if (typeof onSelect === "function") {
      onSelect(response.selection);
    }
  });
}

function showModalFormSafe(player, form, onSubmit, retries = 4) {
  form.show(player).then((response) => {
    if (response.canceled) {
      if (response.cancelationReason === "UserBusy" && retries > 0) {
        system.runTimeout(() => {
          showModalFormSafe(player, form, onSubmit, retries - 1);
        }, 5);
      }
      return;
    }
    if (typeof onSubmit === "function") {
      onSubmit(response.formValues);
    }
  });
}

// Dedicated Sub-Menu for an Alien Playlist (Instant fast selection without scrolling)
function openAlienPlaylistUI(player, playlistTitle, aliens, state) {
  const form = new ActionFormData();
  form.title(playlistTitle);
  form.body(`§aSelect alien DNA sample to initiate transformation (${aliens.length} Available):`);
  form.button("§8« [ RETURN TO GALVAN OS DIAL ]", "textures/items/detransform.png");

  for (const alien of aliens) {
    const iconPath = `textures/items/${alien.id}_ability.png`;
    form.button(`§a§l[ ⚡ ${alien.name.toUpperCase()} ⚡ ]\n§7${alien.species} • ⚔ ${alien.ability_type.replace('_', ' ').toUpperCase()}`, iconPath);
  }

  showActionFormSafe(player, form, (sel) => {
    if (sel === undefined || sel === null) return;
    if (sel === 0) {
      openOmnitrixDialUI(player, state);
      return;
    }
    const selectedAlien = aliens[sel - 1];
    if (selectedAlien) {
      transformPlayer(player, selectedAlien, state);
    }
  });
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
  const usePlaylists = alienList.length > 12 || state.masterControl;

  const form = new ActionFormData();
  form.title(`§2§l[ ⚡ GALVAN OS: ${watchName} ⚡ ]`);

  let statusText = `§2╔═══════════════════════════════════════╗\n`;
  statusText += `§a  ● GALVAN CORE: §fONLINE §8| §bGALVAN PRIME: §aLINKED\n`;
  statusText += `§6  ● DEVICE: §e${watchName} §8| §3BATTERY: §a100%\n`;
  if (state.isTransformed) {
    statusText += `§e  ● CURRENT MORPH: §a${state.currentAlien.name.toUpperCase()} §8[⏳ ${state.transformSeconds}s]\n`;
  } else {
    statusText += `§b  ● STATUS: §fSTANDBY §8(DNA MATRIX READY)\n`;
  }
  if (state.masterControl) {
    statusText += `§3  ● PROTOCOL: §bMASTER CONTROL ACTIVE (UNLIMITED)\n`;
  }
  statusText += `§2╚═══════════════════════════════════════╝\n`;
  statusText += usePlaylists
    ? `§7Select an Alien Playlist below to quickly morph:`
    : `§7Touch any alien DNA matrix profile below to morph:`;
  form.body(statusText);

  let hasDetransformBtn = false;
  // If transformed into modern watch, or master control, show Revert button at top!
  if (state.isTransformed && (!isClassic || state.transformSeconds <= 0 || state.masterControl)) {
    form.button("§c§l[ ⚡ EMERGENCY MANUAL REVERT ⚡ ]\n§8Tap to return to normal Steve", "textures/items/detransform.png");
    hasDetransformBtn = true;
  }

  // Master Control Mode Switch
  let hasMasterBtn = false;
  if (!state.isTransformed) {
    form.button(`§b§l[ ⚡ MASTER CONTROL: ${state.masterControl ? "ON" : "OFF"} ⚡ ]\n§8Toggle Infinite Energy & Instant Morph`, "textures/items/omnitrix_activator.png");
    hasMasterBtn = true;
  }

  // Biomnitrix Dual Fusion Mode
  let hasFusionBtn = false;
  if (watchKey === "omnitrix_biomnitrix") {
    form.button("§e§l[ 🧬 BIOMNITRIX DUAL FUSION MATRIX 🧬 ]\n§8Combine 2 Alien DNA Samples", "textures/items/biomnitrix_fusion_ability.png");
    hasFusionBtn = true;
  }

  if (usePlaylists) {
    form.button("§e§l[ 🌟 PLAYLIST 1: ORIGINAL 10 🌟 ]\n§8Heatblast, Four Arms, XLR8, Diamondhead...", "textures/items/heatblast_ability.png");
    form.button("§b§l[ ⚡ PLAYLIST 2: ALIEN FORCE ⚡ ]\n§8Swampfire, Humungousaur, Big Chill, Echo Echo...", "textures/items/swampfire_ability.png");
    form.button("§6§l[ 💥 PLAYLIST 3: ULTIMATE EVOLUTION 💥 ]\n§8Ult. Swampfire, Ult. Humungousaur, UA Aliens...", "textures/items/ultimate_humungousaur_ability.png");
    form.button("§d§l[ 🔮 PLAYLIST 4: OMNIVERSE & EXPANDED 🔮 ]\n§8Feedback, Bloxx, Gravattack, Crashhopper...", "textures/items/feedback_ability.png");
    form.button("§a§l[ 🧬 PLAYLIST 5: BIOMNITRIX FUSIONS 🧬 ]\n§8Mecha-Fourarms, Mecha-XLR8, Custom Combos...", "textures/items/biomnitrix_fusion_ability.png");
    form.button(`§f§l[ 👑 PLAYLIST 6: COMPLETE ARCHIVE (${alienList.length}) 👑 ]\n§8Full Alien Database`, "textures/items/omnitrix_activator.png");
  } else {
    for (const alien of alienList) {
      const iconPath = `textures/items/${alien.id}_ability.png`;
      form.button(`§a§l[ ⚡ ${alien.name.toUpperCase()} ⚡ ]\n§7${alien.species} • ⚔ ${alien.ability_type.replace('_', ' ').toUpperCase()}`, iconPath);
    }
  }

  showActionFormSafe(player, form, (sel) => {
    if (sel === undefined || sel === null) return;

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

    if (usePlaylists) {
      if (sel === 0) openAlienPlaylistUI(player, "§e§l[ 🌟 PLAYLIST 1: ORIGINAL 10 🌟 ]", PLAYLIST_CLASSIC.length ? PLAYLIST_CLASSIC : alienList.slice(0, 10), state);
      else if (sel === 1) openAlienPlaylistUI(player, "§b§l[ ⚡ PLAYLIST 2: ALIEN FORCE ⚡ ]", PLAYLIST_AF.length ? PLAYLIST_AF : alienList.slice(10, 20), state);
      else if (sel === 2) openAlienPlaylistUI(player, "§6§l[ 💥 PLAYLIST 3: ULTIMATE ALIENS 💥 ]", PLAYLIST_ULTIMATE.length ? PLAYLIST_ULTIMATE : alienList.slice(20, 32), state);
      else if (sel === 3) openAlienPlaylistUI(player, "§d§l[ 🔮 PLAYLIST 4: OMNIVERSE & EXPANDED 🔮 ]", PLAYLIST_OMNIVERSE.length ? PLAYLIST_OMNIVERSE : alienList.slice(32), state);
      else if (sel === 4) openBiomnitrixFusionUI(player, state);
      else if (sel === 5) openAlienPlaylistUI(player, `§f§l[ 👑 COMPLETE ARCHIVE (${alienList.length}) 👑 ]`, alienList, state);
      return;
    }

    const selectedAlien = alienList[sel];
    if (selectedAlien) {
      transformPlayer(player, selectedAlien, state);
    }
  });
}

// Biomnitrix Dynamic Fusion Menu with 1-Click Upgrade Fusions & Custom Combiner
function openBiomnitrixFusionUI(player, state) {
  const form = new ActionFormData();
  form.title("§e§l[ 🧬 BIOMNITRIX DUAL FUSION 🧬 ]");
  form.body("§7Choose an iconic Upgrade Mechamorph Hybrid or create a custom DNA combo:");

  form.button("§a§l[ ⚡ MECHA-FOURARMS ⚡ ]\n§8Upgrade + Four Arms (EMP Quake Slam)", "textures/items/upgrade_ability.png");
  form.button("§b§l[ ⚡ MECHA-XLR8 ⚡ ]\n§8Upgrade + XLR8 (Lightning Vortex Dash)", "textures/items/upgrade_ability.png");
  form.button("§6§l[ ⚡ MECHA-HEATBLAST ⚡ ]\n§8Upgrade + Heatblast (Galvanic Plasma Flame)", "textures/items/upgrade_ability.png");
  form.button("§3§l[ ⚡ MECHA-DIAMONDHEAD ⚡ ]\n§8Upgrade + Diamondhead (Charged Crystal Railgun)", "textures/items/upgrade_ability.png");
  form.button("§2§l[ ⚡ MECHA-RIPJAWS ⚡ ]\n§8Upgrade + Ripjaws (Hydro-Electric Cyber Bite)", "textures/items/upgrade_ability.png");
  form.button("§e§l[ ⚡ MECHA-CANNONBOLT ⚡ ]\n§8Upgrade + Cannonbolt (Galvanic EMP Pinball)", "textures/items/upgrade_ability.png");
  form.button("§f§l[ 🧬 CUSTOM DUAL FUSION MATRIX 🧬 ]\n§8Combine Any 2 Aliens from Database", "textures/items/biomnitrix_fusion_ability.png");

  showActionFormSafe(player, form, (sel) => {
    if (sel === undefined || sel === null) return;
    const upgradeAlien = ALL_ALIENS.find(a => a.id === "upgrade") || FUSION_POOL[0];
    const fourarmsAlien = ALL_ALIENS.find(a => a.id === "four_arms" || a.id === "fourarms") || FUSION_POOL[1];
    const xlr8Alien = ALL_ALIENS.find(a => a.id === "xlr8") || FUSION_POOL[2];
    const heatblastAlien = ALL_ALIENS.find(a => a.id === "heatblast") || FUSION_POOL[3];
    const diamondheadAlien = ALL_ALIENS.find(a => a.id === "diamondhead") || FUSION_POOL[4];
    const ripjawsAlien = ALL_ALIENS.find(a => a.id === "ripjaws") || FUSION_POOL[5];
    const cannonboltAlien = ALL_ALIENS.find(a => a.id === "cannonbolt") || FUSION_POOL[6];

    if (sel === 0) transformFusion(player, upgradeAlien, fourarmsAlien, state);
    else if (sel === 1) transformFusion(player, upgradeAlien, xlr8Alien, state);
    else if (sel === 2) transformFusion(player, upgradeAlien, heatblastAlien, state);
    else if (sel === 3) transformFusion(player, upgradeAlien, diamondheadAlien, state);
    else if (sel === 4) transformFusion(player, upgradeAlien, ripjawsAlien, state);
    else if (sel === 5) transformFusion(player, upgradeAlien, cannonboltAlien, state);
    else if (sel === 6) openCustomBiomnitrixModal(player, state);
  });
}

function openCustomBiomnitrixModal(player, state) {
  const form = new ModalFormData();
  form.title("§e§l[ 🧬 CUSTOM DUAL DNA FUSION 🧬 ]");
  const alienNames = FUSION_POOL.map(a => a.name);
  form.dropdown("§6Select Primary Alien (Alien 1):", alienNames, 0);
  form.dropdown("§bSelect Secondary Alien (Alien 2):", alienNames, 1);

  showModalFormSafe(player, form, (formValues) => {
    if (!formValues) return;
    const a1 = FUSION_POOL[formValues[0]];
    const a2 = FUSION_POOL[formValues[1]];
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

  system.runTimeout(() => {
    player.runCommandAsync("title @s times 4 40 8");
    player.runCommandAsync(`title @s title ${alien.color_code}§l[ ${alien.name.toUpperCase()}! ]`);
    player.runCommandAsync(`title @s subtitle §aSpecies: §f${alien.species} §8| §e⚔ ${alien.ability_type.replace('_', ' ').toUpperCase()}`);
  }, 6);

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
  // Hide human Steve model so ONLY the authentic 3D alien morph renders!
  player.runCommandAsync(`effect @s invisibility ${state.masterControl ? 9999 : 65} 1 true`);
}

function transformFusion(player, a1, a2, state) {
  state.isTransformed = true;
  state.isFusion = true;
  state.currentAlien = a1;
  state.fusionAlien1 = a1;
  state.fusionAlien2 = a2;
  state.transformSeconds = state.masterControl ? 9999 : 75;
  state.rechargeSeconds = 0;

  const isMecha = a1.id === "upgrade" || a2.id === "upgrade";
  const partner = a1.id === "upgrade" ? a2 : a1;
  const fusionName = isMecha ? `Mecha-${partner.name}` : `${a1.name.slice(0, Math.ceil(a1.name.length / 2))}-${a2.name.slice(Math.floor(a2.name.length / 2))}`;

  player.runCommandAsync("playsound beacon.power @a ~ ~ ~ 1 1.2");
  player.runCommandAsync("playsound random.explode @a ~ ~ ~ 1 1.5");
  player.runCommandAsync("particle minecraft:totem_particle ~ ~1 ~");
  player.runCommandAsync("particle minecraft:electric_spark_particle ~ ~1 ~");
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
  // Hide human model
  player.runCommandAsync(`effect @s invisibility ${state.masterControl ? 9999 : 75} 1 true`);
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

  system.runTimeout(() => {
    player.runCommandAsync("title @s times 4 30 6");
    player.runCommandAsync("title @s title §7[NORMAL FORM]");
    player.runCommandAsync(`title @s subtitle ${state.masterControl ? "§bInstant Recharge (Master Control)" : "§cOmnitrix Battery Recharging (25s)..."}`);
  }, 6);

  safeEquip(player, "chest", "air");
  safeEquip(player, "mainhand", "ben10:omnitrix_activator");
  player.runCommandAsync("clear @s ben10:detransform");
  player.runCommandAsync("clear @s ben10:alien_ability");
  player.runCommandAsync("clear @s ben10:biomnitrix_fusion_ability");
  player.runCommandAsync("effect @s clear");
}

// 1-Second Battery & Holographic HUD Tick Loop
system.runInterval(() => {
  for (const player of world.getAllPlayers()) {
    const state = getPlayerState(player);
    const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

    if (state.rechargeSeconds > 0) {
      state.rechargeSeconds--;
      if (state.rechargeSeconds === 0) {
        player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 2.0");
        player.runCommandAsync("playsound beacon.activate @a ~ ~ ~ 1 1.5");
        player.runCommandAsync("title @s actionbar §a§l[OMNITRIX RECHARGED & READY!]");
      }
    }

    if (state.isTransformed) {
      if (!state.masterControl) {
        state.transformSeconds--;

        // Classic Prototype Timeout Beep (Audible tick down in last 10s)
        if (state.transformSeconds <= 10 && state.transformSeconds > 0) {
          player.runCommandAsync("playsound note.harp @a ~ ~ ~ 1 1.8");
          player.runCommandAsync("particle minecraft:redstone_wire_dust_particle ~ ~1 ~");
        }

        if (state.transformSeconds <= 0) {
          detransform(player, state);
          continue;
        }
      }

      // Live High-Tech Actionbar HUD Display with Dynamic Battery Gauge
      const name = state.isFusion && state.fusionAlien1 && state.fusionAlien2
        ? (state.fusionAlien1.id === "upgrade" || state.fusionAlien2.id === "upgrade"
            ? `Mecha-${(state.fusionAlien1.id === "upgrade" ? state.fusionAlien2 : state.fusionAlien1).name}`
            : `${state.fusionAlien1.name.slice(0, 4)}-${state.fusionAlien2.name.slice(0, 4)}`)
        : (state.currentAlien ? state.currentAlien.name : "ALIEN");
      const color = state.currentAlien ? state.currentAlien.color_code : "§a";
      const barsFilled = Math.max(0, Math.min(6, Math.ceil(state.transformSeconds / 10)));
      const energyBar = "█".repeat(barsFilled) + "-".repeat(6 - barsFilled);
      const timerStr = state.masterControl ? "§3[∞ MASTER CONTROL]" : `§e[⚡ ${energyBar} §f${state.transformSeconds}s§e]`;
      const revertHint = isClassic ? "§7(Prototype Lock)" : "§c(Sneak+Punch to Revert)";
      player.runCommandAsync(`title @s actionbar ${color}§l[ ${name.toUpperCase()} ] ${timerStr} §8| ${revertHint}`);
    } else if (state.rechargeSeconds > 0) {
      player.runCommandAsync(`title @s actionbar §c§l[ ⚠ RECHARGING ⚠ ] §e⏳ ${state.rechargeSeconds}s Remaining §8| §7Please Wait...`);
    } else if (state.activeWatch) {
      const activeName = state.activeWatch.replace("omnitrix_", "").replace("_", " ").toUpperCase();
      player.runCommandAsync(`title @s actionbar §2[ ⚡ §a§lOMNITRIX: ${activeName} §r§2⚡ ] §8| §aTAP SCREEN TO OPEN DIAL`);
    }
  }
}, 20);

// Unified Robust Item Interaction Handler (Works on Mobile Touch, Blocks, Air & Inventory)
function handleItemActivation(item, player) {
  if (!item || !player) return;
  const state = getPlayerState(player);
  const now = Date.now();
  if (now - state.lastTapTime < 250) return;
  state.lastTapTime = now;
  const isClassic = !state.activeWatch || state.activeWatch === "omnitrix_classic";

  // 1. Omnitrix Watch Held: Tap screen to Synchronize AND open Dial UI immediately!
  if (item.typeId.startsWith("ben10:omnitrix_") || item.typeId.startsWith("ben10:biomnitrix_")) {
    const rawWatchId = item.typeId.replace("ben10:", "").replace("_recharging", "");
    state.activeWatch = rawWatchId;
    player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.2");
    player.runCommandAsync("playsound beacon.power @a ~ ~ ~ 1 1.5");
    player.runCommandAsync("particle minecraft:villager_happy ~ ~1 ~");
    player.runCommandAsync(`title @s actionbar §a§l[OMNITRIX ACTIVE] §f${rawWatchId.replace('omnitrix_', '').replace('_', ' ').toUpperCase()}`);
    openOmnitrixDialUI(player, state);
    return;
  }

  // 2. Omnitrix Activator: Opens Interactive Dial UI!
  if (item.typeId === "ben10:omnitrix_activator") {
    openOmnitrixDialUI(player, state);
    return;
  }

  // 3. Dedicated Alien Ability Item
  if (item.typeId === "ben10:alien_ability" || item.typeId === "ben10:biomnitrix_fusion_ability") {
    if (!state.isTransformed || !state.currentAlien) {
      player.runCommandAsync("title @s actionbar §c[NO ACTIVE TRANSFORMATION]");
      return;
    }
    if (state.isFusion && state.fusionAlien1 && state.fusionAlien2) {
      executeFusionAbility(player, state.fusionAlien1, state.fusionAlien2, player.isSneaking);
    } else {
      executeAbilityByType(player, state.currentAlien.ability_type, state.currentAlien.name, state.currentAlien.color_code, player.isSneaking);
    }
    return;
  }

  // 4. Dedicated Detransform Item
  if (item.typeId === "ben10:detransform") {
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
    return;
  }

  // 5. Direct Alien Badges / Abilities
  if (item.typeId.endsWith("_badge") || (item.typeId.endsWith("_ability") && item.typeId !== "ben10:alien_ability" && item.typeId !== "ben10:biomnitrix_fusion_ability")) {
    const rawAlienId = item.typeId.replace("ben10:", "").replace("_badge", "").replace("_ability", "");
    const directAlien = ALL_ALIENS.find(a => a.id === rawAlienId);
    if (directAlien) {
      transformPlayer(player, directAlien, state);
      return;
    }
  }

  // 6. Entity Spawner Items
  if (item.typeId.startsWith("ben10:") && item.typeId.endsWith("_spawner")) {
    const rawEntity = item.typeId.replace("ben10:", "").replace("_spawner", "");
    player.runCommandAsync(`summon ben10:${rawEntity} ~ ~ ~`);
    player.runCommandAsync("playsound random.anvil_use @a ~ ~ ~ 1 1.4");
    player.runCommandAsync("particle minecraft:villager_happy ~ ~1 ~");
    player.runCommandAsync(`title @s actionbar §e[SUMMONED] §a§l${rawEntity.replace('_', ' ').toUpperCase()}!`);
    return;
  }
}

// Subscribed to both afterEvents.itemUse (air) and afterEvents.itemUseOn (blocks) for 100% mobile reliability!
world.afterEvents.itemUse.subscribe((event) => {
  handleItemActivation(event.itemStack, event.source);
});

world.afterEvents.itemUseOn.subscribe((event) => {
  handleItemActivation(event.itemStack, event.source);
});

// Chat Voice Commands System (!transform, !revert, !omnitrix, !mastercontrol, !dial, !fusion, !summon)
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

  if (msg.startsWith("!fusion")) {
    event.cancel = true;
    const query = msg.replace("!fusion", "").trim();
    const upgradeAlien = ALL_ALIENS.find(a => a.id === "upgrade") || FUSION_POOL[0];
    system.run(() => {
      if (query.includes("fourarms") || query.includes("four")) {
        const fourarms = ALL_ALIENS.find(a => a.id === "four_arms" || a.id === "fourarms") || FUSION_POOL[1];
        transformFusion(player, upgradeAlien, fourarms, state);
      } else if (query.includes("xlr8")) {
        const xlr8 = ALL_ALIENS.find(a => a.id === "xlr8") || FUSION_POOL[2];
        transformFusion(player, upgradeAlien, xlr8, state);
      } else if (query.includes("heatblast") || query.includes("heat")) {
        const heat = ALL_ALIENS.find(a => a.id === "heatblast") || FUSION_POOL[3];
        transformFusion(player, upgradeAlien, heat, state);
      } else if (query.includes("diamondhead") || query.includes("diamond")) {
        const dia = ALL_ALIENS.find(a => a.id === "diamondhead") || FUSION_POOL[4];
        transformFusion(player, upgradeAlien, dia, state);
      } else if (query.includes("ripjaws") || query.includes("rip")) {
        const rip = ALL_ALIENS.find(a => a.id === "ripjaws") || FUSION_POOL[5];
        transformFusion(player, upgradeAlien, rip, state);
      } else if (query.includes("cannonbolt") || query.includes("cannon")) {
        const can = ALL_ALIENS.find(a => a.id === "cannonbolt") || FUSION_POOL[6];
        transformFusion(player, upgradeAlien, can, state);
      } else {
        openBiomnitrixFusionUI(player, state);
      }
    });
    return;
  }

  if (msg === "!car" || msg === "!kevin") {
    event.cancel = true;
    system.run(() => {
      player.runCommandAsync("summon ben10:kevin_car ~ ~ ~");
      player.runCommandAsync("title @s actionbar §a§l[SUMMONED] Kevin's Muscle Car!");
    });
    return;
  }

  if (msg === "!rustbucket" || msg === "!rv") {
    event.cancel = true;
    system.run(() => {
      player.runCommandAsync("summon ben10:rustbucket ~ ~ ~");
      player.runCommandAsync("title @s actionbar §a§l[SUMMONED] Grandpa Max's Rust Bucket RV!");
    });
    return;
  }

  if (msg === "!drone") {
    event.cancel = true;
    system.run(() => {
      player.runCommandAsync("summon ben10:battle_drone ~ ~ ~");
      player.runCommandAsync("title @s actionbar §c§l[DEPLOYED] Vilgax Battle Drone!");
    });
    return;
  }

  if (msg === "!ship") {
    event.cancel = true;
    system.run(() => {
      player.runCommandAsync("summon ben10:vilgax_ship ~ ~ ~");
      player.runCommandAsync("title @s actionbar §4§l[SUMMONED] Vilgax Drone Warship!");
    });
    return;
  }

  if (msg === "!vilgax") {
    event.cancel = true;
    system.run(() => {
      player.runCommandAsync("summon ben10:vilgax ~ ~ ~");
      player.runCommandAsync("title @s actionbar §4§l[BOSS SUMMONED] Vilgax the Conqueror!");
    });
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

// Auto-equip & Welcome Starter Kit upon entering the world (Safe 20-tick delay)
world.afterEvents.playerSpawn.subscribe((event) => {
  const player = event.player;
  if (!player) return;
  system.runTimeout(() => {
    player.runCommandAsync("title @s title §a§lBEN 10 ADDON");
    player.runCommandAsync("title @s subtitle §eTap with Omnitrix to transform!");
    player.runCommandAsync("give @s ben10:omnitrix_classic 1");
    player.runCommandAsync("give @s ben10:omnitrix_activator 1");
    player.runCommandAsync("give @s ben10:kevin_car_spawner 1");
    player.runCommandAsync("give @s ben10:rustbucket_spawner 1");
    player.runCommandAsync("playsound random.levelup @a ~ ~ ~ 1 1.5");
  }, 20);
});
"""
