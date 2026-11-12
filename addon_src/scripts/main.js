/**
 * ============================================================================
 * MAIN.JS - CIVILIZATION AI MASTERPIECE ENTRYPOINT (PART 5 MODULAR ARCHITECTURE)
 * ============================================================================
 * Features:
 * - 5 Autonomous Job AIs (Woodcutter, Miner, Crafter, Storage Manager, Builder)
 * - Autonomous Residential Cottage & Bed Construction on population growth
 * - Dynamic Bell-Linked Territory with Village Level Progression (L1-L5)
 * - Mountain Slope Safety & Freezing Rescue AI
 * - World Real-Time Top-Left HUD Synchronization
 * - 0% CPU Event-Driven Monster Banisher across Overworld, Nether, and The End
 * - Resilient Mobile UI Terminal with Quick Topic Hub & Storehouse Ledger
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { initTerritoryManager } from "./territory_manager.js";
import { initJobsEngine } from "./jobs_engine.js";
import { initAlpineAI } from "./alpine_mountain_ai.js";
import { initWorldClock } from "./world_clock.js";
import { initMonsterBanisher } from "./monster_banisher.js";
import { openAgentTerminal } from "./ui_terminal.js";

// Sneak-interaction listener for opening villager terminal
world.beforeEvents.playerInteractWithEntity.subscribe((event) => {
  const { player, target } = event;
  if (!player || !target || !target.isValid()) return;
  if (target.typeId !== "minecraft:villager" && target.typeId !== "minecraft:villager_v2") return;

  if (player.isSneaking) {
    event.cancel = true;
    system.run(() => {
      openAgentTerminal(player, target).catch((err) => {
        console.warn(`[Civilization UI] Interaction error: ${err}`);
      });
    });
  }
});

// Deferred subsystem orchestrator
system.run(() => {
  try {
    initMonsterBanisher();
    initWorldClock();
    initTerritoryManager();
    initJobsEngine();
    initAlpineAI();
    console.warn("[Civilization AI] Part 5 Masterpiece Engine running. All 6 Autonomous Job AIs & Simulated Catch-Up Engine active.");
  } catch (err) {
    console.warn(`[Civilization AI] Engine bootstrap error: ${err}`);
  }
});

