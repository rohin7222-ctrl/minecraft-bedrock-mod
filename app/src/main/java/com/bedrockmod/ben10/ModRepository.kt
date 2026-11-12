package com.bedrockmod.ben10

object ModRepository {

    fun getModList(): List<ModItem> {
        return listOf(
            ModItem(
                id = "omni_evolution",
                title = "BEN 10: OMNI EVOLUTION",
                category = ModCategory.BEN10,
                badge = "🧬 OMNI EVOLUTION BETA",
                desc = "Official Omni Evolution Beta Addon! Custom evolution dimension, Vilgax boss animations, custom combat controllers, and extra alien variants.",
                sizeText = "💾 1.4 MB",
                iconEmoji = "🧬",
                assetFileName = ModInstaller.ASSET_OMNI_EVOLUTION,
                buttonBgRes = R.drawable.btn_omni_blue,
                buttonText = "🧬 IMPORT OMNI EVOLUTION 🧬"
            ),
            ModItem(
                id = "omni_bound",
                title = "OMNI-BOUND: FASTER SWITCHING",
                category = ModCategory.BEN10,
                badge = "⚡ INSTANT SWITCHING • 50+ ALIENS",
                desc = "High-speed Omni-Bound v1.5.2! Instant quick-switch alien dials, ultimate forms, custom boss raids, drone attacks, and cinematic transformation sequences.",
                sizeText = "💾 18.4 MB",
                iconEmoji = "🛸",
                assetFileName = ModInstaller.ASSET_OMNI_BOUND,
                buttonBgRes = R.drawable.btn_omnibound_lime,
                buttonText = "🛸 IMPORT OMNI BOUND 🛸"
            ),
            ModItem(
                id = "solo_leveling",
                title = "SOLO LEVELING V1.0.6",
                category = ModCategory.ANIME,
                badge = "🗡️ SHADOW MONARCH • DUNGEONS",
                desc = "Arise as the Shadow Monarch! Awaken Jinwoo's Hunter System, complete daily quests, level up stats, clear red gates & dungeons, and extract defeated enemies as loyal Shadow Soldiers!",
                sizeText = "💾 4.2 MB",
                iconEmoji = "🗡️",
                assetFileName = ModInstaller.ASSET_SOLO_LEVELING,
                buttonBgRes = R.drawable.btn_sololeveling_darkpurple,
                buttonText = "🗡️ IMPORT SOLO LEVELING 🗡️"
            ),
            ModItem(
                id = "one_piece",
                title = "ONE PIECE: BEDROCK EDITION",
                category = ModCategory.ANIME,
                badge = "🏴‍☠️ DEVIL FRUITS • HAKI • FACTIONS",
                desc = "Epic anime adventure! Legendary Devil Fruits with special moves, Busoshoku & Kenbunshoku Haki, Marine & Pirate mobs, legendary katanas (Yoru, Enma), and custom 3D bosses!",
                sizeText = "💾 8.7 MB",
                iconEmoji = "🏴‍☠️",
                assetFileName = ModInstaller.ASSET_ONE_PIECE,
                buttonBgRes = R.drawable.btn_onepiece_orange,
                buttonText = "🏴‍☠️ IMPORT ONE PIECE MOD 🏴‍☠️"
            ),
            ModItem(
                id = "tensura",
                title = "TENSURA: REINCARNATED REQUIEM",
                category = ModCategory.ANIME,
                badge = "🔮 SLIME SKILLS • GREAT SAGE",
                desc = "That Time I Got Reincarnated as a Slime! Great Sage mental HUD overlay, Predator skill mimicry, magicules system, Direwolves, Goblins, Charybdis and Demon Lord abilities!",
                sizeText = "💾 9.0 MB",
                iconEmoji = "🔮",
                assetFileName = ModInstaller.ASSET_TENSURA,
                buttonBgRes = R.drawable.btn_tensura_purple,
                buttonText = "🔮 IMPORT TENSURA MOD 🔮"
            ),
            ModItem(
                id = "dragon_evolution",
                title = "DRAGON EVOLUTION V1.5.0",
                category = ModCategory.ANIME,
                badge = "🐉 SAIYAN FORMS • KI BLASTS",
                desc = "Massive Dragon Evolution experience! Transform into Super Saiyan, unleash Kamehameha & Final Flash ki attacks, custom dimensions, and battle epic anime bosses!",
                sizeText = "💾 22.4 MB",
                iconEmoji = "🐉",
                assetFileName = ModInstaller.ASSET_DRAGON_EVOLUTION,
                buttonBgRes = R.drawable.btn_dragon_amber,
                buttonText = "🐉 IMPORT DRAGON EVOLUTION 🐉"
            ),
            ModItem(
                id = "actual_guns",
                title = "ACTUAL GUNS 2 (3D TACTICAL)",
                category = ModCategory.ACTION,
                badge = "🔫 3D FIREARMS • RELOAD ANIMATIONS",
                desc = "Ultra-detailed 3D firearms for Minecraft Bedrock! Custom recoil, first-person reload animations, sniper scopes, shotguns, assault rifles, and tactical combat!",
                sizeText = "💾 9.6 MB",
                iconEmoji = "🔫",
                assetFileName = ModInstaller.ASSET_ACTUAL_GUNS,
                buttonBgRes = R.drawable.btn_actualguns_red,
                buttonText = "🔫 IMPORT ACTUAL GUNS 2 🔫"
            ),
            ModItem(
                id = "quirkborn",
                title = "QUIRKBORN: MY HERO ACADEMIA",
                category = ModCategory.ACTION,
                badge = "⚡ ONE FOR ALL • EXPLOSION",
                desc = "Awaken your Quirk! One For All, Explosion, Decay, Overhaul, Half-Cold Half-Hot, craft hero/villain gear, fight Nomus, and unlock custom super moves!",
                sizeText = "💾 3.5 MB",
                iconEmoji = "⚡",
                assetFileName = ModInstaller.ASSET_QUIRKBORN,
                buttonBgRes = R.drawable.btn_quirkborn_yellow,
                buttonText = "⚡ IMPORT QUIRKBORN MOD ⚡"
            ),
            ModItem(
                id = "civilization",
                title = "CIVILIZATION: AUTONOMOUS AI CITIZENS",
                category = ModCategory.ACTION,
                badge = "🏛️ MOBILE QUICK BUTTONS • REAL TIME • BATTERY OPTIMIZED",
                desc = "Masterpiece Civilization Addon! Synchronized to real-world Tamil Nadu Time (IST) with top-left running clock. Features mobile Quick-Response buttons for 1-tap dialogue, battery and thermal optimization, silent background AI self-learning, zero particles, and 43+ monster banishment!",
                sizeText = "💾 1.6 MB",
                iconEmoji = "🏛️",
                assetFileName = ModInstaller.ASSET_CIVILIZATION,
                buttonBgRes = R.drawable.btn_civilization_emerald,
                buttonText = "🏛️ IMPORT CIVILIZATION ADDON 🏛️"
            ),
            ModItem(
                id = "iron_man",
                title = "IRON MAN: ARMOR WARS",
                category = ModCategory.SUPERHERO,
                badge = "🤖 MARK 1-85 • FLIGHT • REPULSORS",
                desc = "Suit up as Tony Stark! Fly at supersonic speeds with custom animations, fire repulsor blasts & unibeam, equip nano-tech armor, launch micro-missiles, and activate JARVIS HUD!",
                sizeText = "💾 5.7 MB",
                iconEmoji = "🤖",
                assetFileName = ModInstaller.ASSET_IRON_MAN,
                buttonBgRes = R.drawable.btn_ironman_goldred,
                buttonText = "🤖 IMPORT IRON MAN MOD 🤖"
            ),
            ModItem(
                id = "spider_man",
                title = "SPIDER-MAN: WEB OF SHADOWS",
                category = ModCategory.SUPERHERO,
                badge = "🕷️ WEB SLINGING • 20+ SUITS",
                desc = "Become the Friendly Neighborhood Spider-Man! Fluid 3D web swinging through cities, wall climbing, Spider-Sense danger alerts, Symbiote & Iron Spider suits, and battle iconic villains!",
                sizeText = "💾 28.7 MB",
                iconEmoji = "🕷️",
                assetFileName = ModInstaller.ASSET_SPIDER_MAN,
                buttonBgRes = R.drawable.btn_spiderman_redblue,
                buttonText = "🕷️ IMPORT SPIDER-MAN MOD 🕷️"
            ),
            ModItem(
                id = "marvel_project",
                title = "MARVEL PROJECT: AVENGERS",
                category = ModCategory.SUPERHERO,
                badge = "⭐ MJOLNIR • CAP SHIELD • THANOS",
                desc = "The Ultimate Marvel Universe in Bedrock! Summon Mjolnir lightning, throw Cap's vibranium shield, unsheathe adamantium claws, open Doctor Strange portals, and wield the Infinity Gauntlet!",
                sizeText = "💾 30.9 MB",
                iconEmoji = "⭐",
                assetFileName = ModInstaller.ASSET_MARVEL_PROJECT,
                buttonBgRes = R.drawable.btn_marvel_purple,
                buttonText = "⭐ IMPORT MARVEL PROJECT ⭐"
            )
        )
    }
}
