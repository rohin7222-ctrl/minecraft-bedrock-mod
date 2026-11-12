/**
 * ============================================================================
 * JOBS_ENGINE.JS - 5 AUTONOMOUS JOB AIS & SUPPLY CHAIN PIPELINE
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { JOB_ROLES } from "./config.js";
import { getAgent, persistTerritory } from "./territory_manager.js";
import { findSafeElevation } from "./terrain_utils.js";

/**
 * Physically constructs a complete 5x5 residential cottage with a bed, door, windows, and lantern!
 */
export function constructResidentialCottage(dimension, bx, by, bz) {
  try {
    // 1. Foundation Floor (5x5 Stone Bricks)
    for (let x = -2; x <= 2; x++) {
      for (let z = -2; z <= 2; z++) {
        dimension.runCommandAsync(`setblock ${bx + x} ${by - 1} ${bz + z} stone_bricks replace`);
      }
    }

    // 2. Clear interior air (3x3 interior, height 3)
    for (let x = -1; x <= 1; x++) {
      for (let z = -1; z <= 1; z++) {
        for (let y = 0; y <= 2; y++) {
          dimension.runCommandAsync(`setblock ${bx + x} ${by + y} ${bz + z} air replace`);
        }
      }
    }

    // 3. Walls & Corner Posts (Height 3)
    for (let y = 0; y <= 2; y++) {
      // Corner logs
      dimension.runCommandAsync(`setblock ${bx - 2} ${by + y} ${bz - 2} oak_log replace`);
      dimension.runCommandAsync(`setblock ${bx + 2} ${by + y} ${bz - 2} oak_log replace`);
      dimension.runCommandAsync(`setblock ${bx - 2} ${by + y} ${bz + 2} oak_log replace`);
      dimension.runCommandAsync(`setblock ${bx + 2} ${by + y} ${bz + 2} oak_log replace`);

      // Walls (Planks)
      for (let i = -1; i <= 1; i++) {
        dimension.runCommandAsync(`setblock ${bx + i} ${by + y} ${bz - 2} oak_planks replace`);
        dimension.runCommandAsync(`setblock ${bx + i} ${by + y} ${bz + 2} oak_planks replace`);
        dimension.runCommandAsync(`setblock ${bx - 2} ${by + y} ${bz + i} oak_planks replace`);
        dimension.runCommandAsync(`setblock ${bx + 2} ${by + y} ${bz + i} oak_planks replace`);
      }
    }

    // 4. Windows (Glass Panes on sides)
    dimension.runCommandAsync(`setblock ${bx - 2} ${by + 1} ${bz} glass_pane replace`);
    dimension.runCommandAsync(`setblock ${bx + 2} ${by + 1} ${bz} glass_pane replace`);

    // 5. Front Doorway
    dimension.runCommandAsync(`setblock ${bx} ${by} ${bz - 2} oak_door 0 replace`);
    dimension.runCommandAsync(`setblock ${bx} ${by + 1} ${bz - 2} oak_door 8 replace`);

    // 6. Roof (Stone Bricks / Planks Cover)
    for (let x = -2; x <= 2; x++) {
      for (let z = -2; z <= 2; z++) {
        dimension.runCommandAsync(`setblock ${bx + x} ${by + 3} ${bz + z} oak_planks replace`);
      }
    }

    // 7. Interior Furnishings: BED & LANTERN
    dimension.runCommandAsync(`setblock ${bx + 1} ${by} ${bz + 1} bed 2 replace`);
    dimension.runCommandAsync(`setblock ${bx} ${by + 2} ${bz} lantern replace`);

    return true;
  } catch (_) {
    return false;
  }
}

/**
 * Initializes the Autonomous Role Balancer and the Economic Supply Chain Runner
 */
export function initJobsEngine() {
  // Guaranteed Village Job Distribution (Every 10 seconds / 200 ticks)
  system.runInterval(() => {
    try {
      for (const player of world.getAllPlayers()) {
        const villagers = player.dimension.getEntities({
          type: "minecraft:villager",
          location: player.location,
          maxDistance: 64
        });

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
            builder: 0
          };

          for (const item of vList) {
            const role = item.agent.jobRole ? item.agent.jobRole.id : null;
            if (role && roleCounts[role] !== undefined) {
              roleCounts[role]++;
            }
          }

          const requiredRoles = ["woodcutter", "miner", "crafter", "storage_manager", "builder"];
          for (const reqRole of requiredRoles) {
            if (roleCounts[reqRole] === 0) {
              const candidate = vList.find(item => !item.agent.jobRole || (roleCounts[item.agent.jobRole.id] > 1));
              if (candidate) {
                const assignedJob = JOB_ROLES.find(j => j.id === reqRole);
                candidate.agent.jobRole = assignedJob;
                candidate.entity.setDynamicProperty("civ_job_role", reqRole);
                candidate.entity.setDynamicProperty("civ_tool_durability", 35);
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

  // Economic Supply Chain Pipeline Runner (Every 6 seconds / 120 ticks)
  system.runInterval(() => {
    try {
      for (const player of world.getAllPlayers()) {
        const villagers = player.dimension.getEntities({
          type: "minecraft:villager",
          location: player.location,
          maxDistance: 64
        });

        for (const villager of villagers) {
          if (!villager || !villager.isValid()) continue;
          const agent = getAgent(villager);
          if (!agent || !agent.territory || !agent.jobRole) continue;

          const terr = agent.territory;
          const sh = terr.storehouse;
          if (!sh) continue;

          let toolUses = villager.getDynamicProperty("civ_tool_durability");
          if (toolUses === undefined) toolUses = 35;

          // A. 🪓 WOODCUTTER
          if (agent.jobRole.id === "woodcutter") {
            if (toolUses > 0) {
              sh.logs += 2;
              toolUses -= 1;
              villager.setDynamicProperty("civ_tool_durability", toolUses);
              sh.lastActivity = `${agent.name} delivered 2 Timber Logs to Crafter`;
            } else {
              if (sh.axes > 0) {
                sh.axes -= 1;
                toolUses = 35;
                villager.setDynamicProperty("civ_tool_durability", toolUses);
                sh.lastActivity = `Storage Manager supplied a fresh Axe to Woodcutter ${agent.name}`;
              }
            }
          }

          // B. ⛏️ MINER
          else if (agent.jobRole.id === "miner") {
            if (toolUses > 0) {
              sh.cobblestone += 3;
              if (Math.random() < 0.6) sh.coal += 1;
              if (Math.random() < 0.4) sh.iron_ore += 1;
              if (Math.random() < 0.1) sh.diamonds += 1;
              toolUses -= 1;
              villager.setDynamicProperty("civ_tool_durability", toolUses);
              sh.lastActivity = `${agent.name} extracted cobblestone and ores for Crafter`;
            } else {
              if (sh.pickaxes > 0) {
                sh.pickaxes -= 1;
                toolUses = 35;
                villager.setDynamicProperty("civ_tool_durability", toolUses);
                sh.lastActivity = `Storage Manager supplied a fresh Pickaxe to Miner ${agent.name}`;
              }
            }
          }

          // C. 🔨 CRAFTER
          else if (agent.jobRole.id === "crafter") {
            if (sh.logs >= 2) {
              sh.logs -= 2;
              sh.planks += 8;
            }

            if (sh.axes < 4 && sh.planks >= 3 && sh.cobblestone >= 3) {
              sh.planks -= 3;
              sh.cobblestone -= 3;
              sh.axes += 1;
              sh.lastActivity = `${agent.name} crafted a sturdy Axe for Storage Manager`;
            }

            if (sh.pickaxes < 4 && sh.planks >= 3 && sh.cobblestone >= 3) {
              sh.planks -= 3;
              sh.cobblestone -= 3;
              sh.pickaxes += 1;
              sh.lastActivity = `${agent.name} crafted a sharp Pickaxe for Storage Manager`;
            }

            if (sh.building_kits < 3 && sh.planks >= 8 && sh.cobblestone >= 8) {
              sh.planks -= 8;
              sh.cobblestone -= 8;
              sh.building_kits += 1;
              sh.lastActivity = `${agent.name} assembled an Architectural Kit with a Bed for Builder`;
            }
          }

          // D. 🏗️ BUILDER
          else if (agent.jobRole.id === "builder") {
            const totalPop = villagers.length;
            if (sh.building_kits > 0 && totalPop > (sh.bedsPlaced || 0)) {
              const plotX = Math.floor(terr.centerX + (Math.random() * 20 - 10));
              const plotZ = Math.floor(terr.centerZ + (Math.random() * 20 - 10));
              const groundY = findSafeElevation(villager.dimension, plotX, terr.centerY, plotZ);

              const built = constructResidentialCottage(villager.dimension, plotX, groundY, plotZ);
              if (built) {
                sh.building_kits -= 1;
                sh.housesBuilt = (sh.housesBuilt || 1) + 1;
                sh.bedsPlaced = (sh.bedsPlaced || 2) + 1;
                sh.lastActivity = `Builder ${agent.name} completed Cottage #${sh.housesBuilt} with a cozy bed`;

                for (const p of world.getAllPlayers()) {
                  const pDist = Math.sqrt((p.location.x - plotX)**2 + (p.location.z - plotZ)**2);
                  if (pDist <= terr.radius + 20) {
                    p.sendMessage(`§a🏗️ [${agent.name} - ${terr.name}]§f Completed Cottage #${sh.housesBuilt} equipped with a Bed at [${plotX}, ${groundY}, ${plotZ}] for our expanding population!`);
                  }
                }
              }
            }
          }

          persistTerritory(terr);
        }
      }
    } catch (_) {}
  }, 120);
}
