/**
 * ============================================================================
 * UI_TERMINAL.JS - MOBILE RESILIENT FORM RUNNER & COGNITIVE TERMINAL
 * ============================================================================
 */

import { world, system } from "@minecraft/server";
import { ActionFormData, ModalFormData } from "@minecraft/server-ui";
import { getAgent, saveAgent, calculateVillageLevel, persistTerritory, createDefaultStorehouse } from "./territory_manager.js";
import { getWorldRealTime } from "./world_clock.js";
import { getPlayerHeldItemName } from "./terrain_utils.js";

export async function safeShowForm(player, form, maxRetries = 3) {
  if (!player || !player.isValid()) return { canceled: true };
  for (let i = 0; i < maxRetries; i++) {
    try {
      const response = await form.show(player);
      if (response && response.cancelationReason === "UserBusy") {
        await new Promise((resolve) => system.runTimeout(resolve, 6));
        continue;
      }
      return response;
    } catch (_) {
      await new Promise((resolve) => system.runTimeout(resolve, 6));
    }
  }
  return { canceled: true };
}

export function generateTopicDialogue(villager, player, topicKey) {
  const agent = getAgent(villager);
  const wt = getWorldRealTime();
  const words = Object.keys(agent.vocabulary);
  const wordsCount = words.length;
  const totalCivConcepts = agent.territory.conceptsMastered ? agent.territory.conceptsMastered.size : wordsCount;
  const levelInfo = calculateVillageLevel(totalCivConcepts);
  const sh = agent.territory.storehouse || createDefaultStorehouse();

  let heldItemFlavor = "";
  const heldItem = getPlayerHeldItemName(player);
  if (heldItem) {
    if (heldItem.includes("emerald")) {
      heldItemFlavor = " I notice radiant emeralds in your hand—the noble currency of honest exchange!";
    } else if (heldItem.includes("book")) {
      heldItemFlavor = " You hold a tome of wisdom; preserving knowledge is the bedrock of civilized minds!";
    } else if (heldItem.includes("bread") || heldItem.includes("wheat") || heldItem.includes("carrot")) {
      heldItemFlavor = " Bountiful harvests in your hand nourish our entire commonwealth!";
    } else if (heldItem.includes("sword") || heldItem.includes("bow")) {
      heldItemFlavor = " A defensive armament! While monsters are banished from our World, courage safeguards our peace!";
    } else if (heldItem.includes("bell")) {
      heldItemFlavor = " You hold our civic Bell! Placing it will dynamically re-anchor our territory center!";
    } else if (heldItem.includes("clock")) {
      heldItemFlavor = " A synchronized chronometer! It mirrors our top-left World Time clock!";
    }
  }

  switch (topicKey) {
    case "job_info":
      if (agent.jobRole.id === "woodcutter") {
        return (
          `"As a ${agent.jobRole.title}, I harvest timber from our territory's woodlands and transport fresh logs directly to the Crafter! ` +
          `Our central storehouse currently reserves §a${sh.logs} logs§f. When my axe wears down, our Storage Manager supplies a brand-new forged axe!"` +
          heldItemFlavor
        );
      } else if (agent.jobRole.id === "miner") {
        return (
          `"I delve beneath the surface as our ${agent.jobRole.title}, quarrying stone, coal, iron, and precious gems for our community! ` +
          `We have mined §a${sh.cobblestone} cobblestone§f, §e${sh.iron_ore} iron ore§f, and §b${sh.diamonds} diamonds§f. All resources are delivered straight to the Crafter!"` +
          heldItemFlavor
        );
      } else if (agent.jobRole.id === "crafter") {
        return (
          `"Welcome to the workshop! As ${agent.jobRole.title}, I shape raw logs into planks and forge sturdy axes for Woodcutters and pickaxes for Miners. ` +
          `I also assemble architectural kits with cozy beds for our Builder. Everything we craft flows directly into our communal storehouse!"` +
          heldItemFlavor
        );
      } else if (agent.jobRole.id === "storage_manager") {
        return (
          `"I oversee the central depot of ${agent.territory.name}! I keep our axes, pickaxes, and building kits in perfect balance. ` +
          `Whenever a Miner or Woodcutter's tool breaks, I supply a fresh one immediately. And whenever our Builder needs materials for new houses, I authorize the release!"` +
          heldItemFlavor
        );
      } else if (agent.jobRole.id === "builder") {
        return (
          `"I am ${agent.name}, ${agent.jobRole.title}! My mission is expanding our town's architecture. ` +
          `We have erected §a${sh.housesBuilt} complete residential cottages§f and installed §b${sh.bedsPlaced} beds§f! Whenever a new citizen joins our community, I immediately construct a new house with a warm bed for them!"` +
          heldItemFlavor
        );
      }
      break;

    case "storehouse_ledger":
      return (
        `"🏛️ §6Communal Storehouse Ledger for ${agent.territory.name}:§f\n\n` +
        `• 🪵 Timber Logs: §a${sh.logs}§f | Planks: §a${sh.planks}§f\n` +
        `• 🪨 Cobblestone: §a${sh.cobblestone}§f | Iron Ore: §e${sh.iron_ore}§f\n` +
        `• 💎 Diamonds: §b${sh.diamonds}§f | Coal: §8${sh.coal}§f\n` +
        `• 🪓 Ready Axes: §a${sh.axes}§f | ⛏️ Ready Pickaxes: §a${sh.pickaxes}§f\n` +
        `• 📦 Building Kits: §e${sh.building_kits}§f | 🛏️ Total Beds: §b${sh.bedsPlaced}§f\n` +
        `• 🏡 Completed Cottages: §6${sh.housesBuilt} Houses§f\n` +
        `• 🔄 Recent Civic Flow: §7${sh.lastActivity}§f"`
      );

    case "territory":
      return (
        `"I am a proud, sworn citizen of §b${agent.territory.name}§f, serving as ${agent.jobRole.title}, ${player.name}! ` +
        `Our community stands at §e${levelInfo.badge}§f with an active boundary of §a${agent.territory.radius} blocks§f! ` +
        `${agent.territory.hasBellAnchor ? "Our civic perimeter is dynamically anchored to our town Bell! " : ""}` +
        `Our 5 Guilds work in perfect economic harmony, cultivating wisdom and peace!"` +
        heldItemFlavor
      );

    case "levels":
      return (
        `"Our civilization evolves as our collective minds expand, ${player.name}! ` +
        `With ${totalCivConcepts} concepts cataloged across our guilds, ${agent.territory.name} is currently a §e${levelInfo.name} (Level ${levelInfo.level})§f. ` +
        `Our boundary expanded to ${agent.territory.radius} blocks! ` +
        `${totalCivConcepts < 100 ? `Discovering ${levelInfo.nextTarget - totalCivConcepts} more concepts will unlock our next civilization level expansion!` : "We have attained the highest Imperial Golden Age of wisdom!"}"` +
        heldItemFlavor
      );

    case "mountain":
      return (
        `"Our settlement stands proud upon the high peaks, ${player.name}! ` +
        `Our Alpine Safe-Return AI actively protects every citizen and worker. If anyone slips down a steep cliff, falls into a ravine, ` +
        `or steps into hazardous powdered snow, they are gently lifted back up to our mountain plateau near our civic Bell. Zero workers are ever lost!"` +
        heldItemFlavor
      );

    case "science":
      return (
        `"Greetings, ${player.name}! In the research halls of ${agent.territory.name}, empirical observation is paramount. ` +
        `Recently, our inquiries unlocked the principle of '§e${words[0] || "photosynthesis"}§f' (${agent.vocabulary[words[0]] || "fundamental scientific law"}). As a ${agent.personality.trait}, I find this discovery elevates our homeland!"` +
        heldItemFlavor
      );

    case "peace":
      return (
        `"Peace is the crown jewel of ${agent.territory.name}, ${player.name}. With all 44+ hostile monster species permanently removed from our World, ` +
        `we dwell in profound safety. We chop, mine, craft, and build without fear of darkness. ` +
        `Our community values ethics, mutual aid, and peaceful cooperation above all else."` +
        heldItemFlavor
      );

    default:
      return (
        `"A thoughtful reflection, ${player.name}. In our peaceful World civilization, every inquiry deepens our collective understanding. ` +
        `As a dedicated ${agent.jobRole.title}, my current mood is §a${agent.mood.mood} ${agent.mood.icon}§f, and our alliance rating stands at ⭐ ${agent.friendship}/100."` +
        heldItemFlavor
      );
  }
}

export function generateCustomQueryDialogue(villager, player, rawPrompt) {
  const agent = getAgent(villager);
  const prompt = (rawPrompt || "").toLowerCase().trim();
  const wt = getWorldRealTime();
  const words = Object.keys(agent.vocabulary);
  const randomWord = words.length > 0 ? words[Math.floor(Math.random() * words.length)] : "civilization";
  const meaning = agent.vocabulary[randomWord] || "";

  if (prompt.includes("job") || prompt.includes("work") || prompt.includes("wood") || prompt.includes("mine") || prompt.includes("craft") || prompt.includes("build") || prompt.includes("store")) {
    return generateTopicDialogue(villager, player, "job_info");
  }
  if (prompt.includes("ledger") || prompt.includes("inventory") || prompt.includes("chest") || prompt.includes("resource") || prompt.includes("supply")) {
    return generateTopicDialogue(villager, player, "storehouse_ledger");
  }
  if (prompt.includes("level") || prompt.includes("expand") || prompt.includes("city") || prompt.includes("town") || prompt.includes("upgrade")) {
    return generateTopicDialogue(villager, player, "levels");
  }
  if (prompt.includes("mountain") || prompt.includes("cliff") || prompt.includes("fall") || prompt.includes("ravine") || prompt.includes("high") || prompt.includes("snow")) {
    return generateTopicDialogue(villager, player, "mountain");
  }
  if (prompt.includes("territory") || prompt.includes("village") || prompt.includes("border") || prompt.includes("homeland") || prompt.includes("bell") || prompt.includes("where")) {
    return generateTopicDialogue(villager, player, "territory");
  }
  if (prompt.includes("hello") || prompt.includes("hi") || prompt.includes("greetings") || prompt.includes("vanakkam")) {
    return `"Warm greetings, ${player.name}! I am ${agent.name}, ${agent.jobRole.title} of §b${agent.territory.name}§f. It is currently ${wt.timeFormatted} (${wt.periodOfDay}) World Time. How may our guild assist you?"`;
  }

  return (
    `"An intriguing inquiry, ${player.name}. In our peaceful World territory of §b${agent.territory.name}§f, ` +
    `understanding '${randomWord}' (${meaning}) sheds light upon your words. As our 5 Guilds build and learn together, we shall explore this further!"`
  );
}

export async function openAgentTerminal(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const wordsCount = Object.keys(agent.vocabulary).length;
  const totalCivConcepts = agent.territory.conceptsMastered ? agent.territory.conceptsMastered.size : wordsCount;
  const levelInfo = calculateVillageLevel(totalCivConcepts);
  const wt = getWorldRealTime();
  const sh = agent.territory.storehouse || createDefaultStorehouse();

  const loc = villager.location;
  const dx = loc.x - agent.territory.centerX;
  const dz = loc.z - agent.territory.centerZ;
  const dist = Math.round(Math.sqrt(dx * dx + dz * dz));

  const form = new ActionFormData()
    .title(`🏛️ ${agent.name} [${agent.jobRole.emoji} ${agent.jobRole.title}]`)
    .body(
      `§e"Welcome, ${player.name}! World Real Time: §6${wt.timeFormatted}§e"\n\n` +
      `§f• Assigned Civic Profession: §6${agent.jobRole.emoji} ${agent.jobRole.title}\n` +
      `§f• Homeland Realm: §b${agent.territory.name}\n` +
      `§f• Civilization Level: §e${levelInfo.badge}\n` +
      `§f• Border Radius: §a${agent.territory.radius} Blocks §7(Expanded by Knowledge)\n` +
      `§f• Civic Anchor: §b${agent.territory.hasBellAnchor ? "🔔 Bell Center" : "🏛️ Town Origin"} §7[${agent.territory.centerX}, ${agent.territory.centerY}, ${agent.territory.centerZ}]\n` +
      `§f• Housing Status: §a${sh.housesBuilt} Cottages Built §7| §b${sh.bedsPlaced} Beds Available\n` +
      `§f• Storehouse Stock: §a${sh.logs} Logs§f, §e${sh.cobblestone} Stones§f, §b${sh.diamonds} Diamonds§f, §6${sh.axes} Axes§f, §6${sh.pickaxes} Pickaxes\n` +
      `§f• Mountain Guard: §aAlpine Safe-Return AI Active\n` +
      `§f• Alliance Rating: §e⭐ ${agent.friendship}/100\n\n` +
      `§7Choose an Action below for instant mobile gameplay:`
    )
    .button(`💬 Converse (${agent.jobRole.title})`, "textures/ui/chat_icon")
    .button("📦 Communal Storehouse Ledger", "textures/ui/inventory_icon")
    .button("🏛️ Homeland Territory & Level Charter", "textures/ui/village_hero_effect")
    .button("📜 View Learned Concepts (" + totalCivConcepts + " Words)", "textures/ui/book_enchanted")
    .button("⏰ Check World Real-Time Clock", "textures/ui/clock")
    .button("🎁 Present Gift to " + agent.name, "textures/ui/emerald")
    .button("🤝 Open Default Vanilla Trading", "textures/ui/trade_icon");

  const response = await safeShowForm(player, form);
  if (response.canceled) return;

  switch (response.selection) {
    case 0:
      openQuickConversationHub(player, villager);
      break;
    case 1:
      openStorehouseLedgerView(player, villager);
      break;
    case 2:
      openTerritoryDetails(player, villager);
      break;
    case 3:
      openMemoryBankView(player, villager);
      break;
    case 4:
      openClockDetails(player, villager);
      break;
    case 5:
      handleGiftGiving(player, villager);
      break;
    case 6:
      player.sendMessage(`§7[Tip] Stand up (release Sneak) and tap ${agent.name} to trade items normally!`);
      break;
  }
}

export async function openStorehouseLedgerView(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const sh = agent.territory.storehouse || createDefaultStorehouse();

  const form = new ActionFormData()
    .title(`📦 ${agent.territory.name} Storehouse`)
    .body(
      `§6Executive Communal Inventory & Supply Chain:\n\n` +
      `§f• 🪵 Timber Logs: §a${sh.logs}§f (Collected by Woodcutters)\n` +
      `• 🪚 Processed Planks: §a${sh.planks}§f (Crafted by Crafters)\n` +
      `• 🪨 Cobblestone: §a${sh.cobblestone}§f (Mined by Miners)\n` +
      `• ⛏️ Iron Ore: §e${sh.iron_ore}§f | Coal: §8${sh.coal}§f | Diamonds: §b${sh.diamonds}§f\n` +
      `• 🪓 Ready Woodcutter Axes: §a${sh.axes}§f\n` +
      `• ⛏️ Ready Miner Pickaxes: §a${sh.pickaxes}§f\n` +
      `• 📦 Architectural Building Kits: §e${sh.building_kits}§f\n` +
      `• 🏡 Completed Cottages: §6${sh.housesBuilt} Houses Built§f\n` +
      `• 🛏️ Total Placed Beds: §b${sh.bedsPlaced} Beds Installed§f\n\n` +
      `§7Last Supply Activity: ${sh.lastActivity}\n` +
      `All 5 Guilds actively supply and draw from this communal depot!`
    )
    .button("🪵 Donate 8 Wood Logs to Depot")
    .button("🪨 Donate 8 Cobblestone to Depot")
    .button("⬅️ Return to Terminal");

  const res = await safeShowForm(player, form);
  if (res.canceled) return;

  if (res.selection === 0) {
    sh.logs += 8;
    persistTerritory(agent.territory);
    player.sendMessage(`§a[Storehouse] Donated 8 Wood Logs to ${agent.territory.name}! Crafters will process these into building kits.`);
    openStorehouseLedgerView(player, villager);
  } else if (res.selection === 1) {
    sh.cobblestone += 8;
    persistTerritory(agent.territory);
    player.sendMessage(`§a[Storehouse] Donated 8 Cobblestone to ${agent.territory.name}! Miners and Crafters salute your contribution.`);
    openStorehouseLedgerView(player, villager);
  } else {
    openAgentTerminal(player, villager);
  }
}

export async function openQuickConversationHub(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const wt = getWorldRealTime();

  const form = new ActionFormData()
    .title(`💬 Converse with ${agent.name}`)
    .body(
      `§6Role: §e${agent.jobRole.emoji} ${agent.jobRole.title} §7of §b${agent.territory.name}\n` +
      `§7World Real Time: §e${wt.timeFormatted} §7| Period: §a${wt.periodEmoji} ${wt.periodOfDay}`
    )
    .button(`💼 Inquire about My Profession (${agent.jobRole.title})`, "textures/ui/anvil_icon")
    .button("📦 Check Communal Storehouse & Supplies", "textures/ui/inventory_icon")
    .button("🏛️ Ask about Territory & Border Expansion", "textures/ui/village_hero_effect")
    .button("🏔️ Inquire about Mountain Safety AI", "textures/items/amethyst_shard")
    .button("🔬 Ask about Science & Nature", "textures/items/potion_bottle_splash_heal")
    .button("🕊️ Discuss World Peace & Safety", "textures/items/emerald")
    .button("🌾 Talk about Farming & Crops", "textures/items/wheat")
    .button("🔨 Inquire about Craft & Metallurgy", "textures/items/iron_ingot")
    .button("💡 \"What did you learn today?\"", "textures/items/book_enchanted")
    .button("📜 Philosophical Wisdom & Life", "textures/items/paper")
    .button("⏰ Inquire about World Time", "textures/items/clock_item")
    .button("🎁 Quick Gift: Emerald (+15 Friendship)", "textures/items/emerald")
    .button("✍️ Custom Question (Open Keyboard)", "textures/ui/editIcon")
    .button("⬅️ Return to Main Terminal", "textures/ui/cancel");

  const res = await safeShowForm(player, form);
  if (res.canceled) return;

  const topics = [
    "job_info",
    "storehouse_ledger",
    "territory",
    "mountain",
    "science",
    "peace",
    "agriculture",
    "craft",
    "recent_word",
    "philosophy",
    "clock"
  ];

  if (res.selection >= 0 && res.selection <= 10) {
    const topicKey = topics[res.selection];
    const dialogue = generateTopicDialogue(villager, player, topicKey);
    showDialogueResponseModal(player, villager, dialogue);
  } else if (res.selection === 11) {
    handleGiftGiving(player, villager);
  } else if (res.selection === 12) {
    openCustomTypingModal(player, villager);
  } else {
    openAgentTerminal(player, villager);
  }
}

export async function showDialogueResponseModal(player, villager, speechText) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  player.sendMessage(`§6[${agent.name} - ${agent.jobRole.title}]: §f${speechText}`);

  const form = new ActionFormData()
    .title(`🗣️ ${agent.name} Speaks`)
    .body(
      `§6${agent.name} §e[${agent.jobRole.emoji} ${agent.jobRole.title}] §7of §b${agent.territory.name} §7says:\n\n` +
      `§f${speechText}\n\n` +
      `§7Mood: §a${agent.mood.mood} ${agent.mood.icon} §7| Friendship: §e⭐ ${agent.friendship}/100`
    )
    .button("🔄 Ask Another Quick Question", "textures/ui/chat_icon")
    .button("📦 View Storehouse Inventory", "textures/ui/inventory_icon")
    .button("🏛️ Territory Details", "textures/ui/village_hero_effect")
    .button("🎁 Give Gift (+15 Friendship)", "textures/items/emerald")
    .button("⬅️ Return to Terminal", "textures/ui/cancel");

  const res = await safeShowForm(player, form);
  if (res.canceled) return;

  if (res.selection === 0) {
    openQuickConversationHub(player, villager);
  } else if (res.selection === 1) {
    openStorehouseLedgerView(player, villager);
  } else if (res.selection === 2) {
    openTerritoryDetails(player, villager);
  } else if (res.selection === 3) {
    handleGiftGiving(player, villager);
  } else {
    openAgentTerminal(player, villager);
  }
}

export async function openTerritoryDetails(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const loc = villager.location;
  const dx = loc.x - agent.territory.centerX;
  const dz = loc.z - agent.territory.centerZ;
  const dist = Math.round(Math.sqrt(dx * dx + dz * dz));
  const wordsCount = Object.keys(agent.vocabulary).length;
  const totalCivConcepts = agent.territory.conceptsMastered ? agent.territory.conceptsMastered.size : wordsCount;
  const levelInfo = calculateVillageLevel(totalCivConcepts);
  const sh = agent.territory.storehouse || createDefaultStorehouse();

  let direction = "Center Point";
  if (Math.abs(dx) > 4 || Math.abs(dz) > 4) {
    const angle = Math.atan2(-dz, -dx) * (180 / Math.PI);
    if (angle >= -22.5 && angle < 22.5) direction = "East";
    else if (angle >= 22.5 && angle < 67.5) direction = "North-East";
    else if (angle >= 67.5 && angle < 112.5) direction = "North";
    else if (angle >= 112.5 && angle < 157.5) direction = "North-West";
    else if (angle >= 157.5 || angle < -157.5) direction = "West";
    else if (angle >= -157.5 && angle < -112.5) direction = "South-West";
    else if (angle >= -112.5 && angle < -67.5) direction = "South";
    else direction = "South-East";
  }

  const form = new ActionFormData()
    .title(`🏛️ Territory: ${agent.territory.name}`)
    .body(
      `§6Official Territorial Charter of ${agent.territory.name}:\n\n` +
      `§f• Sovereign Realm: §b${agent.territory.name}\n` +
      `§f• Civilization Level: §e${levelInfo.badge}\n` +
      `§f• Civic Center Anchor: §a${agent.territory.hasBellAnchor ? "🔔 Dynamic Bell Block" : "🏛️ Settlement Origin"} §7[${agent.territory.centerX}, ${agent.territory.centerY}, ${agent.territory.centerZ}]\n` +
      `§f• Dynamic Border Perimeter: §a${agent.territory.radius} Blocks Radius §7(Expands with knowledge)\n` +
      `§f• Current Distance to Center: §e${dist} Blocks §7(Bearing: §b${direction}§7)\n` +
      `§f• Completed Cottages: §6${sh.housesBuilt} Houses Built§f\n` +
      `§f• Total Installed Beds: §b${sh.bedsPlaced} Beds Installed§f\n` +
      `§f• 5 Specialized Guilds: §aActive (Woodcutter, Miner, Crafter, Storage Manager, Builder)\n` +
      `§f• Mountain Guard Protocol: §aAlpine Safe-Return AI Active\n` +
      `§f• Hostile Threat Level: §a0.0% (Zero Monsters World Active)\n\n` +
      `§7Tip: Break and place a Bell anywhere to dynamically re-center your village territory!`
    )
    .button("🔄 Converse with " + agent.name)
    .button("⬅️ Return to Terminal");

  const res = await safeShowForm(player, form);
  if (res.canceled) return;

  if (res.selection === 0) {
    openQuickConversationHub(player, villager);
  } else {
    openAgentTerminal(player, villager);
  }
}

export async function openCustomTypingModal(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const form = new ModalFormData()
    .title(`✍️ Custom Thought for ${agent.name}`)
    .textField("Enter any thought, question, or inquiry in English:", "e.g. How are your mining or building operations progressing?");

  const res = await safeShowForm(player, form);
  if (res.canceled || !res.formValues) {
    openQuickConversationHub(player, villager);
    return;
  }

  const input = res.formValues[0];
  if (!input || input.trim() === "") {
    openQuickConversationHub(player, villager);
    return;
  }

  player.sendMessage(`§b[You -> ${agent.name}]: §f"${input}"`);
  const reply = generateCustomQueryDialogue(villager, player, input);
  showDialogueResponseModal(player, villager, reply);
}

export async function openMemoryBankView(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const words = Object.keys(agent.vocabulary);

  let stream = `§6=== AUTONOMOUSLY LEARNED VOCABULARY (${words.length} Words) ===\n\n`;
  for (const w of words) {
    stream += `• §a${w.toUpperCase()}§f: ${agent.vocabulary[w]}\n\n`;
  }

  const form = new ActionFormData()
    .title(`📜 ${agent.name}'s Mind Graph`)
    .body(stream)
    .button("🔄 Converse with " + agent.name)
    .button("⬅️ Return to Terminal");

  const res = await safeShowForm(player, form);
  if (res.canceled) return;

  if (res.selection === 0) {
    openQuickConversationHub(player, villager);
  } else {
    openAgentTerminal(player, villager);
  }
}

export async function openClockDetails(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  const wt = getWorldRealTime();

  const form = new ActionFormData()
    .title(`⏰ World Real-Time Clock`)
    .body(
      `§6🌍 World Standard Real-Time (UTC+05:30):\n\n` +
      `§f• Current Time: §e${wt.timeFormatted}\n` +
      `§f• Date: §a${wt.dateFormatted}\n` +
      `§f• Solar Period: §b${wt.periodEmoji} ${wt.periodOfDay}\n` +
      `§f• Minecraft Daylight: §bSynchronized to World Sun & Moon\n` +
      `§f• On-Screen Clock: §6Running at Top-Left (Unobstructed)\n\n` +
      `§7The clock runs live on your top-left screen without covering touch controls!`
    )
    .button("⬅️ Return to Terminal");

  await safeShowForm(player, form);
  openAgentTerminal(player, villager);
}

export async function handleGiftGiving(player, villager) {
  if (!player || !player.isValid() || !villager || !villager.isValid()) return;
  const agent = getAgent(villager);
  agent.friendship = Math.min(100, agent.friendship + 15);
  saveAgent(villager, agent);

  if (agent.friendship >= 50) {
    try {
      player.runCommandAsync(`give @s emerald 3`);
      player.sendMessage(`§a⭐ High Friendship Blessing! ${agent.name} gifted you 3 Emeralds!`);
    } catch (_) {}
  }

  const responseText = `"Thank you deeply, ${player.name}! On behalf of ${agent.territory.name}'s guilds, our alliance level is now ⭐ ${agent.friendship}/100! May our homeland flourish together!"`;
  showDialogueResponseModal(player, villager, responseText);
}
