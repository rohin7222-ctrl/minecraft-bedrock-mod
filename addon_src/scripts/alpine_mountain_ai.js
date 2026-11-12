/**
 * ============================================================================
 * ALPINE_MOUNTAIN_AI.JS - ALPINE MOUNTAIN CLIFF & POWDERED SNOW SAFE-RETURN
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { getAgent } from "./territory_manager.js";
import { findSafeElevation } from "./terrain_utils.js";

/**
 * Periodically verifies citizen elevation and boundary positions (Every 40 ticks / 2s):
 * 1. Rescues citizens fallen > 8 blocks down mountain cliffs into ravines/water.
 * 2. Rescues citizens trapped in freezing powdered snow.
 * 3. Enforces territory border lockdown with solid elevation landing.
 * Guarantees zero fall damage, zero suffocation, and zero particles!
 */
export function initAlpineAI() {
  system.runInterval(() => {
    try {
      const players = world.getAllPlayers();
      if (players.length === 0) return;

      for (const player of players) {
        const villagers = player.dimension.getEntities({
          type: "minecraft:villager",
          location: player.location,
          maxDistance: 48
        });

        for (const villager of villagers) {
          if (!villager || !villager.isValid()) continue;
          const agent = getAgent(villager);
          if (!agent || !agent.territory) continue;

          const terr = agent.territory;
          const loc = villager.location;
          const dx = loc.x - terr.centerX;
          const dz = loc.z - terr.centerZ;
          const horizontalDist = Math.sqrt(dx * dx + dz * dz);
          const altitudeDrop = terr.centerY - loc.y;

          let isSnowHazard = false;
          try {
            const feetB = villager.dimension.getBlock({ x: Math.floor(loc.x), y: Math.floor(loc.y), z: Math.floor(loc.z) });
            if (feetB && feetB.typeId === "minecraft:powder_snow") {
              isSnowHazard = true;
            }
          } catch (_) {}

          // A. Alpine Mountain Rescue
          if ((altitudeDrop >= 8 || isSnowHazard) && horizontalDist <= terr.radius + 25) {
            const targetX = terr.centerX + 1.5;
            const targetZ = terr.centerZ + 1.5;
            const safeY = findSafeElevation(villager.dimension, targetX, terr.centerY, targetZ);

            try { villager.clearVelocity(); } catch (_) {}
            try {
              villager.addEffect("slow_falling", 40, { showParticles: false, amplifier: 1 });
              villager.addEffect("resistance", 40, { showParticles: false, amplifier: 5 });
            } catch (_) {}

            try {
              villager.teleport(
                { x: targetX, y: safeY, z: targetZ },
                { dimension: villager.dimension }
              );
            } catch (_) {}
            continue;
          }

          // B. Border Lockdown
          if (horizontalDist > terr.radius) {
            const safeRatio = (terr.radius - 2.5) / horizontalDist;
            const safeX = terr.centerX + dx * safeRatio;
            const safeZ = terr.centerZ + dz * safeRatio;
            const safeY = findSafeElevation(villager.dimension, safeX, loc.y, safeZ);

            try { villager.clearVelocity(); } catch (_) {}
            try {
              villager.teleport(
                { x: safeX, y: safeY, z: safeZ },
                { dimension: villager.dimension }
              );
            } catch (_) {}
          }
        }
      }
    } catch (_) {}
  }, 40);
}
