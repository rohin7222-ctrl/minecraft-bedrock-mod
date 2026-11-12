/**
 * ============================================================================
 * ARCHITECT_BUILDER.JS - PHYSICAL BUILDING, ARCHITECTURAL UPGRADES & CHEST PLACEMENT
 * ============================================================================
 */

import { ARCHITECTURAL_DESIGNS } from "./config.js";

/**
 * Returns a contemplation thought for the Builder AI when idle or planning.
 */
export function getRandomArchitecturalThought() {
  const idx = Math.floor(Math.random() * ARCHITECTURAL_DESIGNS.length);
  return ARCHITECTURAL_DESIGNS[idx];
}

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

    // 6. Roof (Cover)
    for (let x = -2; x <= 2; x++) {
      for (let z = -2; z <= 2; z++) {
        dimension.runCommandAsync(`setblock ${bx + x} ${by + 3} ${bz + z} oak_planks replace`);
      }
    }

    // 7. Interior Furnishings: ACTUAL BED & CEILING LANTERN
    dimension.runCommandAsync(`setblock ${bx + 1} ${by} ${bz + 1} bed 2 replace`);
    dimension.runCommandAsync(`setblock ${bx} ${by + 2} ${bz} lantern replace`);

    return true;
  } catch (_) {
    return false;
  }
}

/**
 * Executes a subtle architectural upgrade in the village (Lamp post, Stone path, or Planter).
 */
export function executeVillageArchitecturalUpgrade(dimension, terr) {
  try {
    const angle = Math.random() * Math.PI * 2;
    const dist = 5 + Math.random() * 15;
    const ux = Math.floor(terr.centerX + Math.cos(angle) * dist);
    const uz = Math.floor(terr.centerZ + Math.sin(angle) * dist);
    const uy = terr.centerY;

    const upgradeType = Math.floor(Math.random() * 3);
    if (upgradeType === 0) {
      // Lantern Post: Oak fence + Lantern on top
      dimension.runCommandAsync(`setblock ${ux} ${uy} ${uz} oak_fence replace`);
      dimension.runCommandAsync(`setblock ${ux} ${uy + 1} ${uz} lantern replace`);
    } else if (upgradeType === 1) {
      // Paved Pathway accent: 3-block Stone Bricks
      dimension.runCommandAsync(`setblock ${ux} ${uy - 1} ${uz} stone_bricks replace`);
      dimension.runCommandAsync(`setblock ${ux + 1} ${uy - 1} ${uz} stone_bricks replace`);
      dimension.runCommandAsync(`setblock ${ux} ${uy - 1} ${uz + 1} stone_bricks replace`);
    } else {
      // Architectural Masonry Column: Chiseled stone brick pedestal
      dimension.runCommandAsync(`setblock ${ux} ${uy - 1} ${uz} chiseled_stone_bricks replace`);
      dimension.runCommandAsync(`setblock ${ux} ${uy} ${uz} smooth_stone_slab replace`);
    }
    return true;
  } catch (_) {
    return false;
  }
}

/**
 * Physically places a new storage chest at the village depot when storehouse is full.
 */
export function placeDepotExpansionChest(dimension, terr, chestCount = 1) {
  try {
    const cx = Math.floor(terr.centerX + (chestCount % 4) * 2 - 3);
    const cz = Math.floor(terr.centerZ + Math.floor(chestCount / 4) * 2 - 3);
    const cy = terr.centerY;

    dimension.runCommandAsync(`setblock ${cx} ${cy - 1} ${cz} stone_bricks replace`);
    dimension.runCommandAsync(`setblock ${cx} ${cy} ${cz} chest replace`);
    return true;
  } catch (_) {
    return false;
  }
}

