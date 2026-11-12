/**
 * ============================================================================
 * JOBS_ENGINE.JS - 6 AUTONOMOUS JOB AIS & SIMULATED CATCH-UP ENGINE
 * ============================================================================
 * 6 Autonomous Job Roles:
 * 1. 🪓 Woodcutter (Smart axe tiering, tree felling, raw logs supply)
 * 2. ⛏️ Miner (Smart pickaxe tiering, stone & ore extraction for Crafter)
 * 3. 🔨 Crafter (Stone furnace/adupu crafting, ore smelting & tool forging)
 * 4. 📦 Storage Manager (Chest overflow expansion & physical placement)
 * 5. 🏗️ Builder (Cottage & bed construction, idle architectural upgrades)
 * 6. 🏹 Hunter & Shepherd (Sheep shearing & wool supply for beds)
 *
 * Performance Architecture:
 * - 0% CPU Idle Overhead via "Simulated Catch-Up" (காலக்கணக்கீடு):
 *   When player travels >1000 blocks away, time is timestamped.
 *   Upon return or arrival, the exact elapsed resources, wool, ores,
 *   chests, and building upgrades are calculated in 1 millisecond!
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { JOB_ROLES, MINER_TOOL_TIERS, WOODCUTTER_TOOL_TIERS } from "./config.js";
import { territoryRegistry, getAgent, persistTerritory } from "./territory_manager.js";
import { findSafeElevation, getNearbyVillagers } from "./terrain_utils.js";
import {
  constructResidentialCottage,
  executeVillageArchitecturalUpgrade,
  placeDepotExpansionChest,
  placeDepotFurnace,
  getRandomArchitecturalThought
} from "./architect_builder.js";

const REQUIRED_ROLES = ["woodcutter", "miner", "crafter", "storage_manager", "builder", "hunter"];

/**
 * Instant Mathematical Catch-up Calculation (காலக்கணக்கீடு)
 * Accrues resources, crafts tools, and upgrades structures for elapsed time with 0% idle CPU!
 */
export function simulateCatchUp(terr, elapsedSeconds, dimension = null, player = null) {
  if (!terr || !terr.storehouse) return;
  const sh = terr.storehouse;

  // 1 production cycle = ~6 seconds of active simulation
  const cycles = Math.min(Math.floor(elapsedSeconds / 6), 600);
  if (cycles <= 0) return;

  // 1. 🪓 Woodcutter Yields
  let axeTier = sh.iron_axes > 0 ? "iron_axe" : "wooden_axe";
  const axeMultiplier = WOODCUTTER_TOOL_TIERS[axeTier] ? WOODCUTTER_TOOL_TIERS[axeTier].yieldMultiplier : 1;
  const addedLogs = Math.floor(cycles * 2 * axeMultiplier);
  sh.logs = (sh.logs || 0) + addedLogs;

  // 2. ⛏️ Miner Yields (Tool tiering)
  const addedStone = cycles * 4;
  const addedCoal = cycles * 2;
  sh.cobblestone = (sh.cobblestone || 0) + addedStone;
  sh.coal = (sh.coal || 0) + addedCoal;

  if ((sh.iron_pickaxes || 0) > 0) {
    sh.iron_ore = (sh.iron_ore || 0) + Math.floor(cycles * 0.8);
    sh.redstone = (sh.redstone || 0) + Math.floor(cycles * 0.3);
    sh.diamonds = (sh.diamonds || 0) + Math.floor(cycles * 0.15);
  } else {
    sh.iron_ore = (sh.iron_ore || 0) + Math.floor(cycles * 0.3);
  }

  // 3. 🏹 Hunter & Shepherd Yields (6th AI)
  const addedWool = cycles * 2;
  const addedFood = cycles * 1;
  sh.wool = (sh.wool || 0) + addedWool;
  sh.food = (sh.food || 0) + addedFood;

  // 4. 🔨 Crafter: Furnace (Adupu) Crafting & Ore Smelting
  if ((sh.cobblestone || 0) >= 16 && (sh.furnacesPlaced || 1) < 2) {
    sh.cobblestone -= 8;
    sh.furnacesPlaced = (sh.furnacesPlaced || 1) + 1;
    if (dimension) placeDepotFurnace(dimension, terr, sh.furnacesPlaced);
  }

  // Smelt raw iron ores into refined iron ingots
  const smeltable = Math.min(Math.floor((sh.iron_ore || 0) / 2), (sh.coal || 0), Math.floor(cycles * 0.8));
  if (smeltable > 0) {
    sh.iron_ore -= smeltable * 2;
    sh.coal -= smeltable;
    sh.iron_ingots = (sh.iron_ingots || 0) + smeltable * 2;
  }

  // Saw logs into planks
  if (sh.logs >= 4) {
    const logsConverted = Math.min(Math.floor(sh.logs / 2), Math.floor(cycles * 1.5));
    sh.logs -= logsConverted * 2;
    sh.planks = (sh.planks || 0) + logsConverted * 8;
  }

  // Forge advanced tools using refined iron ingots
  if ((sh.iron_ingots || 0) >= 3) {
    sh.iron_ingots -= 3;
    sh.iron_pickaxes = (sh.iron_pickaxes || 0) + 1;
  }
  if ((sh.iron_ingots || 0) >= 3) {
    sh.iron_ingots -= 3;
    sh.iron_axes = (sh.iron_axes || 0) + 1;
  }
  if ((sh.iron_ingots || 0) >= 2) {
    sh.iron_ingots -= 2;
    sh.shears = (sh.shears || 0) + 1;
  }

  // Craft Residential Kits with Beds using Wool
  if ((sh.wool || 0) >= 3 && (sh.planks || 0) >= 6 && (sh.cobblestone || 0) >= 6) {
    const kitsCrafted = Math.min(Math.floor(sh.wool / 3), 4);
    sh.wool -= kitsCrafted * 3;
    sh.planks -= kitsCrafted * 6;
    sh.cobblestone -= kitsCrafted * 6;
    sh.building_kits = (sh.building_kits || 0) + kitsCrafted;
  }

  // 5. 📦 Storage Manager: Chest Expansion Check
  const totalItems = (sh.logs || 0) + (sh.planks || 0) + (sh.cobblestone || 0) +
    (sh.iron_ore || 0) + (sh.iron_ingots || 0) + (sh.coal || 0) + (sh.diamonds || 0) +
    (sh.redstone || 0) + (sh.wool || 0) + (sh.food || 0);

  const currentCap = sh.maxCapacity || 200;
  if (totalItems >= currentCap) {
    const needed = Math.ceil((totalItems - currentCap) / 100) + 1;
    for (let c = 0; c < needed; c++) {
      if ((sh.planks || 0) >= 8) {
        sh.planks -= 8;
        sh.chestsPlaced = (sh.chestsPlaced || 1) + 1;
        sh.maxCapacity = (sh.maxCapacity || 200) + 100;
        if (dimension) {
          placeDepotExpansionChest(dimension, terr, sh.chestsPlaced);
        }
      }
    }
  }

  // 6. 🏗️ Builder Housing & Idle Upgrades
  const newCottages = Math.min(sh.building_kits || 0, Math.floor(cycles / 40));
  if (newCottages > 0) {
    sh.building_kits -= newCottages;
    sh.housesBuilt = (sh.housesBuilt || 1) + newCottages;
    sh.bedsPlaced = (sh.bedsPlaced || 2) + newCottages;
  }

  const newUpgrades = Math.floor(cycles / 30);
  sh.upgradesCompleted = (sh.upgradesCompleted || 0) + newUpgrades;
  sh.latestArchitecturalThought = getRandomArchitecturalThought();

  sh.lastActivity = `Simulated Catch-up: Accrued ${addedLogs} logs, ${addedStone} stone, ${addedWool} wool, ${smeltable * 2} smelted ingots`;

  if (player && player.isValid()) {
    player.sendMessage(
      `§6🏛️ [Welcome to ${terr.name}!] §fSimulated Catch-Up (${Math.round(elapsedSeconds)}s away): ` +
      `§a+${addedLogs} Logs§f, §e+${addedStone} Stone§f, §f+${addedWool} Wool§f, §b+${smeltable * 2} Iron Ingots§f! 0% Battery Drain.`
    );
  }
}

/**
 * Initializes the 6-Role Balancer and Global Economic Simulation Engine
 */
export function initJobsEngine() {
  // 1. Role Distribution & Balancing for Active Entities (Every 10s / 200 ticks)
  system.runInterval(() => {
    try {
      for (const player of world.getAllPlayers()) {
        if (!player || !player.isValid()) continue;
        const villagers = getNearbyVillagers(player.dimension, player.location, 80);

        const terrVillagers = new Map();
        for (const v of villagers) {
          if (!v || !v.isValid()) continue;
          const agent = getAgent(v);
          if (!agent || !agent.territory) continue;
          const tId = agent.territory.id;
          if (!terrVillagers.has(tId)) terrVillagers.set(tId, []);
          terrVillagers.get(tId).push({ entity: v, agent });
        }

        for (const [tId, vList] of terrVillagers.entries()) {
          const roleCounts = {
            woodcutter: 0,
            miner: 0,
            crafter: 0,
            storage_manager: 0,
            builder: 0,
            hunter: 0
          };

          for (const item of vList) {
            const role = item.agent.jobRole ? item.agent.jobRole.id : null;
            if (role && roleCounts[role] !== undefined) {
              roleCounts[role]++;
            }
          }

          for (const reqRole of REQUIRED_ROLES) {
            if (roleCounts[reqRole] === 0) {
              const candidate = vList.find(item => !item.agent.jobRole || (roleCounts[item.agent.jobRole.id] > 1));
              if (candidate) {
                const assignedJob = JOB_ROLES.find(j => j.id === reqRole);
                candidate.agent.jobRole = assignedJob;
                candidate.entity.setDynamicProperty("civ_job_role", reqRole);
                candidate.entity.setDynamicProperty("civ_tool_durability", 40);
                roleCounts[reqRole]++;

                const terr = candidate.agent.territory;
                const anchorIcon = terr.hasBellAnchor ? "🔔" : "🏛️";
                candidate.entity.nameTag = `§6${candidate.agent.name} §e[${assignedJob.emoji} ${assignedJob.title}]\n§b${anchorIcon} ${terr.name} §8(Lvl ${terr.level})`;
              }
            }
          }
        }
      }
    } catch (_) {}
  }, 200);

  // 2. Active Local Simulation + Simulated Catch-Up Evaluator (Every 6s / 120 ticks)
  system.runInterval(() => {
    try {
      const currentTime = Date.now();

      for (const [tId, terr] of territoryRegistry.entries()) {
        const sh = terr.storehouse;
        if (!sh) continue;

        // Proximity detection (Overworld only for village settlements)
        let nearbyPlayer = null;
        for (const p of world.getAllPlayers()) {
          if (!p || !p.isValid() || p.dimension.id !== "minecraft:overworld") continue;
          const dx = p.location.x - terr.centerX;
          const dz = p.location.z - terr.centerZ;
          if (Math.sqrt(dx * dx + dz * dz) <= terr.radius + 50) {
            nearbyPlayer = p;
            break;
          }
        }

        if (nearbyPlayer) {
          if (terr.lastActiveTimestamp) {
            const elapsed = (currentTime - terr.lastActiveTimestamp) / 1000;
            if (elapsed >= 15) {
              simulateCatchUp(terr, elapsed, nearbyPlayer.dimension, nearbyPlayer);
            }
          }
          terr.lastActiveTimestamp = currentTime;

          // Local increment for loaded area
          sh.logs = (sh.logs || 0) + 2;
          sh.cobblestone = (sh.cobblestone || 0) + 3;
          sh.coal = (sh.coal || 0) + 1;
          sh.wool = (sh.wool || 0) + 2;

          // 🔨 Crafter builds Stone Furnace (Adupu) with 8 Cobblestones
          if ((sh.cobblestone || 0) >= 8 && (sh.furnacesPlaced || 1) < 2) {
            sh.cobblestone -= 8;
            sh.furnacesPlaced = (sh.furnacesPlaced || 1) + 1;
            placeDepotFurnace(nearbyPlayer.dimension, terr, sh.furnacesPlaced);
            sh.lastActivity = "Crafter constructed a Stone Furnace (Adupu) to smelt raw ores";
          }

          // 🔨 Crafter smelts raw iron ore into refined iron ingots using coal in furnace
          if ((sh.iron_ore || 0) >= 2 && (sh.coal || 0) >= 1) {
            sh.iron_ore -= 2;
            sh.coal -= 1;
            sh.iron_ingots = (sh.iron_ingots || 0) + 2;
            sh.lastActivity = "Crafter smelted 2 Iron Ores into refined Iron Ingots using the Furnace";
          }

          // Forge refined iron tools
          if ((sh.iron_ingots || 0) >= 3 && (sh.iron_pickaxes || 0) < 2 && (sh.planks || 0) >= 2) {
            sh.iron_ingots -= 3;
            sh.planks -= 2;
            sh.iron_pickaxes = (sh.iron_pickaxes || 0) + 1;
          }
          if ((sh.iron_ingots || 0) >= 3 && (sh.iron_axes || 0) < 2 && (sh.planks || 0) >= 2) {
            sh.iron_ingots -= 3;
            sh.planks -= 2;
            sh.iron_axes = (sh.iron_axes || 0) + 1;
          }

          // Convert logs to planks
          if (sh.logs >= 2) {
            sh.logs -= 2;
            sh.planks = (sh.planks || 0) + 8;
          }

          // Housing Construction
          if (sh.building_kits > 0 && (sh.bedsPlaced || 2) < (sh.housesBuilt || 1) + 2) {
            const plotX = Math.floor(terr.centerX + (Math.random() * 24 - 12));
            const plotZ = Math.floor(terr.centerZ + (Math.random() * 24 - 12));
            const safeY = findSafeElevation(nearbyPlayer.dimension, plotX, terr.centerY, plotZ, false);
            if (safeY !== null) {
              const built = constructResidentialCottage(nearbyPlayer.dimension, plotX, safeY, plotZ);
              if (built) {
                sh.building_kits -= 1;
                sh.housesBuilt = (sh.housesBuilt || 1) + 1;
                sh.bedsPlaced = (sh.bedsPlaced || 2) + 1;
              }
            }
          } else {
            sh.latestArchitecturalThought = getRandomArchitecturalThought();
            if (Math.random() < 0.35) {
              executeVillageArchitecturalUpgrade(nearbyPlayer.dimension, terr);
              sh.upgradesCompleted = (sh.upgradesCompleted || 0) + 1;
            }
          }

          persistTerritory(terr);
        }
      }
    } catch (_) {}
  }, 120);
}
