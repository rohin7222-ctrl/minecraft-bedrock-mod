/**
 * ============================================================================
 * WORLD_CLOCK.JS - WORLD REAL-TIME SYNCHRONIZATION & TOP-LEFT ACTIONBAR HUD
 * ============================================================================
 */

import { world, system } from "@minecraft/server";

export function getWorldRealTime() {
  const now = new Date();
  const utcMs = now.getTime() + (now.getTimezoneOffset() * 60000);
  const worldDate = new Date(utcMs + 19800000); // Standard World Reference Time (+05:30)

  const hours24 = worldDate.getHours();
  const minutes = worldDate.getMinutes();
  const seconds = worldDate.getSeconds();

  let hours12 = hours24 % 12;
  hours12 = hours12 ? hours12 : 12;
  const ampm = hours24 >= 12 ? "PM" : "AM";

  const pad = (n) => (n < 10 ? "0" + n : n);
  const timeFormatted = `${pad(hours12)}:${pad(minutes)}:${pad(seconds)} ${ampm}`;

  const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  const dateFormatted = `${worldDate.getDate()} ${months[worldDate.getMonth()]}`;

  let periodOfDay = "Morning";
  let periodEmoji = "☀️";
  if (hours24 >= 5 && hours24 < 7) {
    periodOfDay = "Dawn";
    periodEmoji = "🌅";
  } else if (hours24 >= 7 && hours24 < 12) {
    periodOfDay = "Morning";
    periodEmoji = "☀️";
  } else if (hours24 >= 12 && hours24 < 14) {
    periodOfDay = "Zenith (Noon)";
    periodEmoji = "🔆";
  } else if (hours24 >= 14 && hours24 < 18) {
    periodOfDay = "Afternoon";
    periodEmoji = "🌤️";
  } else if (hours24 >= 18 && hours24 < 20) {
    periodOfDay = "Dusk Twilight";
    periodEmoji = "🌇";
  } else if (hours24 >= 20 || hours24 < 1) {
    periodOfDay = "Starlight Night";
    periodEmoji = "🌌";
  } else {
    periodOfDay = "Deep Night";
    periodEmoji = "🌙";
  }

  let minsSince6AM = (hours24 * 60 + minutes + seconds / 60) - 360;
  if (minsSince6AM < 0) minsSince6AM += 1440;
  const targetMcTick = Math.floor(minsSince6AM * (24000 / 1440));

  return {
    hours24,
    minutes,
    seconds,
    ampm,
    timeFormatted,
    dateFormatted,
    periodOfDay,
    periodEmoji,
    targetMcTick
  };
}

let lastSyncedTick = -1;

export function initWorldClock() {
  system.runInterval(() => {
    const wt = getWorldRealTime();

    if (Math.abs(wt.targetMcTick - lastSyncedTick) >= 10) {
      try {
        const overworld = world.getDimension("overworld");
        if (overworld) {
          overworld.setTimeOfDay(wt.targetMcTick);
          lastSyncedTick = wt.targetMcTick;
        }
      } catch (_) {}
    }

    const clockText = `§6⏰ §e${wt.timeFormatted} §7(World Time) §8| §a${wt.periodEmoji} ${wt.periodOfDay} §8| §f${wt.dateFormatted}`;
    for (const player of world.getAllPlayers()) {
      if (!player || !player.isValid()) continue;
      try {
        player.onScreenDisplay.setActionBar(clockText);
      } catch (_) {}
    }
  }, 20);

  system.runTimeout(() => {
    try {
      const overworld = world.getDimension("overworld");
      if (overworld) {
        overworld.runCommandAsync("gamerule dodaylightcycle false");
      }
    } catch (_) {}
  }, 40);
}

