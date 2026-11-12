/**
 * ============================================================================
 * TERRAIN_UTILS.JS - BEDROCK 1.20/1.21 COMPATIBLE TERRAIN & ELEVATION SCANNER
 * ============================================================================
 */

export function isSolidGround(block) {
  if (!block || block.isAir || block.isLiquid) return false;
  const id = block.typeId;
  if (
    id.includes("air") || id.includes("water") || id.includes("lava") ||
    id.includes("grass") || id.includes("flower") || id.includes("sapling") ||
    id.includes("torch") || id.includes("carpet") || id.includes("sign") ||
    id.includes("fire") || id.includes("pressure_plate") || id.includes("button") ||
    id.includes("redstone") || id.includes("rail") || id.includes("tripwire") ||
    id.includes("leaves") || id.includes("vine") || id.includes("sweet_berry") ||
    id.includes("powder_snow")
  ) {
    return false;
  }
  return true;
}

export function isAirOrPassable(block) {
  if (!block || block.isAir) return true;
  if (block.isLiquid) return false;
  const id = block.typeId;
  if (
    id.includes("grass") || id.includes("flower") || id.includes("torch") ||
    id.includes("carpet") || id.includes("sign") || id.includes("pressure_plate") ||
    id.includes("button") || id.includes("redstone")
  ) {
    return true;
  }
  return false;
}

export function findSafeElevation(dimension, x, startY, z) {
  const intX = Math.floor(x);
  const intZ = Math.floor(z);
  const baseY = Math.floor(startY);

  for (let dy = 8; dy >= -8; dy--) {
    const testY = baseY + dy;
    try {
      const gBlock = dimension.getBlock({ x: intX, y: testY, z: intZ });
      const feetBlock = dimension.getBlock({ x: intX, y: testY + 1, z: intZ });
      const headBlock = dimension.getBlock({ x: intX, y: testY + 2, z: intZ });

      if (isSolidGround(gBlock) && isAirOrPassable(feetBlock) && isAirOrPassable(headBlock)) {
        return testY + 1;
      }
    } catch (_) {}
  }
  return startY;
}

export function getPlayerHeldItemName(player) {
  try {
    const equippable = player.getComponent("minecraft:equippable");
    if (!equippable) return null;
    const mainhand = equippable.getEquipment("Mainhand");
    return mainhand ? mainhand.typeId : null;
  } catch (_) {
    return null;
  }
}
