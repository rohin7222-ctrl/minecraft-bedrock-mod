/**
 * ============================================================================
 * MONSTER_BANISHER.JS - ZERO-CPU EVENT-DRIVEN MONSTER PURGE (44+ SPECIES)
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { MONSTER_TYPE_IDS } from "./config.js";

export function purgeMonster(entity) {
  if (!entity || !entity.isValid()) return;
  if (MONSTER_TYPE_IDS.has(entity.typeId)) {
    try { entity.remove(); } catch (_) {}
  }
}

export function initMonsterBanisher() {
  world.afterEvents.entitySpawn.subscribe((event) => {
    purgeMonster(event.entity);
  });

  const DIMENSIONS = ["overworld", "nether", "the_end"];
  let sweepDimIndex = 0;
  system.runInterval(() => {
    try {
      const dimName = DIMENSIONS[sweepDimIndex % DIMENSIONS.length];
      sweepDimIndex++;
      const dim = world.getDimension(dimName);
      if (!dim) return;

      for (const monsterId of MONSTER_TYPE_IDS) {
        try {
          const entities = dim.getEntities({ type: monsterId });
          for (const ent of entities) {
            if (ent && ent.isValid()) ent.remove();
          }
        } catch (_) {}
      }
    } catch (_) {}
  }, 200);
}
