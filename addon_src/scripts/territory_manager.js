/**
 * ============================================================================
 * TERRITORY_MANAGER.JS - TERRITORY REGISTRY, BELL ANCHOR & CITIZEN CACHE
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import {
  TERRITORY_PREFIXES,
  TERRITORY_ROOTS,
  JOB_ROLES,
  BASE_VOCABULARY,
  AUTONOMOUS_DISCOVERY_POOL,
  VILLAGER_NAMES,
  PERSONALITIES,
  MOODS
} from "./config.js";

export const territoryRegistry = new Map();
export const agentCache = new Map();

export function generateRandomTerritoryName() {
  const prefix = TERRITORY_PREFIXES[Math.floor(Math.random() * TERRITORY_PREFIXES.length)];
  const root = TERRITORY_ROOTS[Math.floor(Math.random() * TERRITORY_ROOTS.length)];
  return `${prefix} ${root}`;
}

export function calculateVillageLevel(conceptCount) {
  if (conceptCount >= 60) {
    return { level: 4, name: "Imperial Metropolis", radius: 130, badge: "👑 Level 4: Imperial Metropolis", nextTarget: 100 };
  } else if (conceptCount >= 36) {
    return { level: 3, name: "Grand Citadel", radius: 100, badge: "🏰 Level 3: Grand Citadel", nextTarget: 60 };
  } else if (conceptCount >= 16) {
    return { level: 2, name: "Flourishing Township", radius: 75, badge: "🌾 Level 2: Flourishing Township", nextTarget: 36 };
  } else {
    return { level: 1, name: "Frontier Settlement", radius: 50, badge: "🏕️ Level 1: Frontier Settlement", nextTarget: 16 };
  }
}

export function createDefaultStorehouse() {
  return {
    logs: 32,
    planks: 48,
    cobblestone: 40,
    iron_ore: 12,
    coal: 16,
    diamonds: 2,
    redstone: 8,
    axes: 4,
    pickaxes: 4,
    building_kits: 3,
    housesBuilt: 1,
    bedsPlaced: 2,
    lastActivity: "Supply chain initialized"
  };
}

export function persistTerritory(terr) {
  try {
    const rawData = JSON.stringify({
      id: terr.id,
      name: terr.name,
      centerX: terr.centerX,
      centerY: terr.centerY,
      centerZ: terr.centerZ,
      radius: terr.radius,
      level: terr.level,
      levelName: terr.levelName,
      hasBellAnchor: terr.hasBellAnchor,
      conceptsMastered: Array.from(terr.conceptsMastered || []),
      storehouse: terr.storehouse || createDefaultStorehouse()
    });
    world.setDynamicProperty(`civ_terr_${terr.id}`, rawData);
  } catch (_) {}
}

export function findNearbyBell(dimension, loc, maxRadius = 24) {
  try {
    const baseX = Math.floor(loc.x);
    const baseZ = Math.floor(loc.z);
    const baseY = Math.floor(loc.y);

    for (let r = 0; r <= maxRadius; r += 2) {
      for (let dx = -r; dx <= r; dx += 2) {
        for (let dz = -r; dz <= r; dz += 2) {
          if (Math.abs(dx) !== r && Math.abs(dz) !== r) continue;
          for (let dy = -3; dy <= 4; dy++) {
            const block = dimension.getBlock({ x: baseX + dx, y: baseY + dy, z: baseZ + dz });
            if (block && block.typeId === "minecraft:bell") {
              return { x: baseX + dx, y: baseY + dy, z: baseZ + dz };
            }
          }
        }
      }
    }
  } catch (_) {}
  return null;
}

export function resolveVillagerTerritory(villager) {
  const loc = villager.location;
  let terrId = villager.getDynamicProperty("civ_terr_id");

  if (terrId && territoryRegistry.has(terrId)) {
    return territoryRegistry.get(terrId);
  }

  if (terrId) {
    try {
      const savedRaw = world.getDynamicProperty(`civ_terr_${terrId}`);
      if (savedRaw) {
        const parsed = JSON.parse(savedRaw);
        const terr = {
          id: parsed.id,
          name: parsed.name,
          centerX: parsed.centerX,
          centerY: parsed.centerY,
          centerZ: parsed.centerZ,
          radius: parsed.radius,
          level: parsed.level,
          levelName: parsed.levelName,
          hasBellAnchor: parsed.hasBellAnchor,
          conceptsMastered: new Set(parsed.conceptsMastered || []),
          storehouse: parsed.storehouse || createDefaultStorehouse()
        };
        territoryRegistry.set(terrId, terr);
        return terr;
      }
    } catch (_) {}
  }

  for (const [id, terr] of territoryRegistry.entries()) {
    const dx = loc.x - terr.centerX;
    const dz = loc.z - terr.centerZ;
    const dist = Math.sqrt(dx * dx + dz * dz);
    if (dist <= terr.radius + 20) {
      villager.setDynamicProperty("civ_terr_id", terr.id);
      return terr;
    }
  }

  const newId = `terr_${Math.floor(loc.x)}_${Math.floor(loc.z)}`;
  let newName = generateRandomTerritoryName();

  let cx = Math.floor(loc.x);
  let cy = Math.floor(loc.y);
  let cz = Math.floor(loc.z);
  let hasBell = false;

  const initialBell = findNearbyBell(villager.dimension, loc, 24);
  if (initialBell) {
    cx = initialBell.x;
    cy = initialBell.y;
    cz = initialBell.z;
    hasBell = true;
  }

  const levelInfo = calculateVillageLevel(15);
  const newTerr = {
    id: newId,
    name: newName,
    centerX: cx,
    centerY: cy,
    centerZ: cz,
    radius: levelInfo.radius,
    level: levelInfo.level,
    levelName: levelInfo.name,
    hasBellAnchor: hasBell,
    conceptsMastered: new Set(["civilization", "peaceful", "emerald", "architecture", "metallurgy", "forestry", "mining"]),
    storehouse: createDefaultStorehouse()
  };

  villager.setDynamicProperty("civ_terr_id", newTerr.id);
  territoryRegistry.set(newId, newTerr);
  persistTerritory(newTerr);
  return newTerr;
}

export function getAgent(villager) {
  const vId = villager.id;
  if (agentCache.has(vId)) {
    return agentCache.get(vId);
  }

  let name = villager.getDynamicProperty("civ_name");
  let personalityIdx = villager.getDynamicProperty("civ_pers_idx");
  let roleId = villager.getDynamicProperty("civ_job_role");

  const territory = resolveVillagerTerritory(villager);

  if (!name) {
    name = VILLAGER_NAMES[Math.floor(Math.random() * VILLAGER_NAMES.length)];
    personalityIdx = Math.floor(Math.random() * PERSONALITIES.length);
    villager.setDynamicProperty("civ_name", name);
    villager.setDynamicProperty("civ_pers_idx", personalityIdx);
  }

  let jobRole = JOB_ROLES.find(j => j.id === roleId);
  if (!jobRole) {
    jobRole = JOB_ROLES[Math.floor(Math.random() * JOB_ROLES.length)];
    villager.setDynamicProperty("civ_job_role", jobRole.id);
    villager.setDynamicProperty("civ_tool_durability", 35);
  }

  let vocabStr = villager.getDynamicProperty("civ_vocab");
  let vocabulary = { ...BASE_VOCABULARY };
  if (vocabStr) {
    try {
      vocabulary = { ...BASE_VOCABULARY, ...JSON.parse(vocabStr) };
    } catch (_) {}
  }

  if (!territory.conceptsMastered) territory.conceptsMastered = new Set();
  for (const word of Object.keys(vocabulary)) {
    territory.conceptsMastered.add(word);
  }

  const totalConcepts = Math.max(15, territory.conceptsMastered.size);
  const levelInfo = calculateVillageLevel(totalConcepts);
  if (levelInfo.level > territory.level) {
    territory.level = levelInfo.level;
    territory.levelName = levelInfo.name;
    territory.radius = levelInfo.radius;
    persistTerritory(territory);
  }

  try {
    const anchorIcon = territory.hasBellAnchor ? "🔔" : "🏛️";
    villager.nameTag = `§6${name} §e[${jobRole.emoji} ${jobRole.title}]\n§b${anchorIcon} ${territory.name} §8(Lvl ${territory.level})`;
  } catch (_) {}

  const personality = PERSONALITIES[(personalityIdx || 0) % PERSONALITIES.length];
  let friendship = villager.getDynamicProperty("civ_friendship") || 15;
  let moodIdx = villager.getDynamicProperty("civ_mood_idx") || 0;
  let mood = MOODS[moodIdx % MOODS.length];

  const agent = { name, jobRole, personality, territory, friendship, mood, vocabulary, dirty: false };
  agentCache.set(vId, agent);
  return agent;
}

export function saveAgent(villager, agent) {
  try {
    villager.setDynamicProperty("civ_friendship", agent.friendship);
    if (agent.dirty) {
      villager.setDynamicProperty("civ_vocab", JSON.stringify(agent.vocabulary));
      agent.dirty = false;
    }
  } catch (_) {}
}

export function initTerritoryManager() {
  // Clear agent cache if it exceeds 250 entities
  system.runInterval(() => {
    if (agentCache.size > 250) {
      agentCache.clear();
    }
  }, 6000);

  // Environmental Autonomous Learning (Epiphanies)
  system.runInterval(() => {
    try {
      const players = world.getAllPlayers();
      if (players.length === 0) return;

      const randomPlayer = players[Math.floor(Math.random() * players.length)];
      const nearbyVillagers = randomPlayer.dimension.getEntities({
        type: "minecraft:villager",
        location: randomPlayer.location,
        maxDistance: 32
      });

      if (nearbyVillagers.length === 0) return;

      const scholar = nearbyVillagers[Math.floor(Math.random() * nearbyVillagers.length)];
      if (!scholar || !scholar.isValid()) return;

      const agent = getAgent(scholar);
      const known = new Set(Object.keys(agent.vocabulary));
      const undiscovered = AUTONOMOUS_DISCOVERY_POOL.filter(item => !known.has(item.word));
      if (undiscovered.length === 0) return;

      const epiphany = undiscovered[Math.floor(Math.random() * undiscovered.length)];
      agent.vocabulary[epiphany.word] = epiphany.meaning;
      agent.dirty = true;
      saveAgent(scholar, agent);

      if (!agent.territory.conceptsMastered) agent.territory.conceptsMastered = new Set();
      agent.territory.conceptsMastered.add(epiphany.word);

      const totalCount = agent.territory.conceptsMastered.size;
      const oldLevel = agent.territory.level;
      const newLevelInfo = calculateVillageLevel(totalCount);

      if (newLevelInfo.level > oldLevel) {
        agent.territory.level = newLevelInfo.level;
        agent.territory.levelName = newLevelInfo.name;
        agent.territory.radius = newLevelInfo.radius;
        persistTerritory(agent.territory);

        for (const p of world.getAllPlayers()) {
          const d = Math.sqrt((p.location.x - agent.territory.centerX)**2 + (p.location.z - agent.territory.centerZ)**2);
          if (d <= agent.territory.radius + 25) {
            p.sendMessage(`§6🎉 [CIVILIZATION ADVANCEMENT] §b${agent.territory.name}§f has advanced to §e${newLevelInfo.badge}§f! Territory perimeter expanded to §a${newLevelInfo.radius} Blocks§f!`);
          }
        }
      }
    } catch (_) {}
  }, 300);

  // Peer-to-Peer Knowledge Diffusion
  system.runInterval(() => {
    try {
      const players = world.getAllPlayers();
      if (players.length === 0) return;

      const randomPlayer = players[Math.floor(Math.random() * players.length)];
      const nearbyVillagers = randomPlayer.dimension.getEntities({
        type: "minecraft:villager",
        location: randomPlayer.location,
        maxDistance: 24
      });

      if (nearbyVillagers.length < 2) return;

      const speaker = nearbyVillagers[Math.floor(Math.random() * nearbyVillagers.length)];
      if (!speaker || !speaker.isValid()) return;

      const peers = randomPlayer.dimension.getEntities({
        type: "minecraft:villager",
        location: speaker.location,
        maxDistance: 6
      }).filter(v => v.id !== speaker.id);

      if (peers.length > 0) {
        const listener = peers[0];
        const sAgent = getAgent(speaker);
        const lAgent = getAgent(listener);

        const sWords = Object.keys(sAgent.vocabulary);
        const newForListener = sWords.filter(w => !lAgent.vocabulary[w]);

        if (newForListener.length > 0) {
          const word = newForListener[0];
          lAgent.vocabulary[word] = sAgent.vocabulary[word];
          lAgent.dirty = true;
          saveAgent(listener, lAgent);

          if (lAgent.territory.conceptsMastered) {
            lAgent.territory.conceptsMastered.add(word);
          }
        }
      }
    } catch (_) {}
  }, 400);

  // Dynamic Bell Placement, Break & Chime Events
  world.afterEvents.playerPlaceBlock.subscribe((event) => {
    const { block } = event;
    if (!block || block.typeId !== "minecraft:bell") return;

    const bellPos = block.location;
    let bestTerr = null;
    let minDistance = 999999;

    for (const [id, terr] of territoryRegistry.entries()) {
      const dx = bellPos.x - terr.centerX;
      const dz = bellPos.z - terr.centerZ;
      const dist = Math.sqrt(dx * dx + dz * dz);

      if (dist <= terr.radius + 60 && dist < minDistance) {
        minDistance = dist;
        bestTerr = terr;
      }
    }

    if (bestTerr) {
      bestTerr.centerX = bellPos.x;
      bestTerr.centerY = bellPos.y;
      bestTerr.centerZ = bellPos.z;
      bestTerr.hasBellAnchor = true;
      persistTerritory(bestTerr);

      for (const p of world.getAllPlayers()) {
        const pDist = Math.sqrt((p.location.x - bellPos.x)**2 + (p.location.z - bellPos.z)**2);
        if (pDist <= bestTerr.radius + 30) {
          p.sendMessage(`§6🔔 [${bestTerr.name}]§f Civic Bell Re-Anchored! Boundary center dynamically updated to [${bellPos.x}, ${bellPos.y}, ${bellPos.z}].`);
        }
      }
    }
  });

  world.afterEvents.playerBreakBlock.subscribe((event) => {
    const { brokenBlockPermutation, block } = event;
    const isBell = brokenBlockPermutation && (
      brokenBlockPermutation.matches("minecraft:bell") || 
      (brokenBlockPermutation.type && brokenBlockPermutation.type.id === "minecraft:bell")
    );

    if (isBell) {
      const bellPos = block.location;
      for (const [id, terr] of territoryRegistry.entries()) {
        if (Math.abs(terr.centerX - bellPos.x) < 1.5 && Math.abs(terr.centerZ - bellPos.z) < 1.5) {
          terr.hasBellAnchor = false;
          persistTerritory(terr);
        }
      }
    }
  });

  world.afterEvents.playerInteractWithBlock.subscribe((event) => {
    const { block, player } = event;
    if (!block || block.typeId !== "minecraft:bell" || !player || !player.isValid()) return;

    const bellPos = block.location;
    for (const [id, terr] of territoryRegistry.entries()) {
      const dx = bellPos.x - terr.centerX;
      const dz = bellPos.z - terr.centerZ;
      const dist = Math.sqrt(dx * dx + dz * dz);
      if (dist <= terr.radius + 20) {
        player.sendMessage(`§6🔔 [The Civic Bell of ${terr.name} Chimes]§f The 5 Guilds stand united across our ${terr.levelName}!`);
        break;
      }
    }
  });
}
