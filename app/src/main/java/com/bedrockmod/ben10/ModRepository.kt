package com.bedrockmod.ben10

object ModRepository {

    fun getModList(): List<ModItem> {
        return listOf(
            ModItem(
                id = "civilization",
                title = "CIVILIZATION: AUTONOMOUS AI CITIZENS",
                category = ModCategory.CIVILIZATION,
                badge = "👑 7 AUTONOMOUS AIS • 4 RELIGIONS • FULL ARMOR",
                desc = "Part 5 Living World Masterpiece v1.0.86! Villagers think and survive like real players: 4 Faith Pantheons, Sacred Altar Worship, Full Armor Suits (Iron->Diamond->Netherite), Redstone Piston Automations, Spawn-Proofing Sanctuary, and instant in-game !civ chat shortcuts! 100% offline 60 FPS locked!",
                sizeText = "💾 0.5 MB",
                iconEmoji = "🏛️",
                assetFileName = ModInstaller.ASSET_CIVILIZATION,
                buttonBgRes = R.drawable.btn_civilization_emerald,
                buttonText = "🏛️ IMPORT CIVILIZATION ADDON 🏛️",
                guideInfo = "🎮 Civilization In-Game Guide:\n• Chat Commands: Type '!civ' for Civilization Codex, '!religion' for Faith & Altar Codex, '!help' for guide.\n• 4 Faiths: Sol (Sun/Health), Deep Bedrock (Haste/Shield), Emerald Grove (Crops/Satiation), Redstone Spark (Speed/Repairs).\n• Combat & Armor: Villagers equip Iron -> Diamond -> Netherite based on XP.\n• Experiments: Turn ON 'Beta APIs'."
            ),
            ModItem(
                id = "ultrareal_texture_pack",
                title = "ULTRAREAL 100X HD TEXTURE PACK",
                category = ModCategory.CIVILIZATION,
                badge = "🎨 100X REALISTIC MOBS • 360 SKY • CAUSTIC WATER",
                desc = "UltraReal 100x v2.0 HD Texture Pack! 100x Realistic Mobs, 11 sun-shadowed trees, 360 dynamic sky, caustic water, 3D ores, and 110+ HD items. Includes 64x Low-End Mobile 60 FPS mode and Ultra 128x mode. Tap to automatically open and import directly into Minecraft PE!",
                sizeText = "💾 3.7 MB",
                iconEmoji = "🎨",
                assetFileName = ModInstaller.ASSET_ULTRAREAL,
                buttonBgRes = R.drawable.btn_civilization_emerald,
                buttonText = "🎨 IMPORT ULTRAREAL TEXTURE PACK 🎨",
                guideInfo = "🎨 UltraReal HD In-Game Guide:\n• Activate under Global Resources or World Resource Packs.\n• Features 100x HD Mobs, 360 dynamic skybox, caustic waters, and 3D ore blocks.\n• Locked 60 FPS mobile optimization with zero frame drops."
            ),
            ModItem(
                id = "world_vehicles",
                title = "WORLD ALL VEHICLES 2026",
                category = ModCategory.VEHICLES,
                badge = "🏎️ 40 REAL VEHICLES • SUPERCARS • JETS • SUBS",
                desc = "Ultimate 2026 Real-World Vehicle Addon! 40 Driveable, Flyable, Submersible vehicles: Bugatti Tourbillon, Ferrari F80, Koenigsegg Jesko, F-22 Raptor Jet, Apache Heli, Boeing 787, Cybertruck, Ninja H2R, Luxury Superyacht, Nuclear Sub, and SpaceX Starship! 60 FPS mobile optimized, zero experiment toggles needed!",
                sizeText = "💾 1.0 MB",
                iconEmoji = "🏎️",
                assetFileName = ModInstaller.ASSET_WORLD_VEHICLES,
                buttonBgRes = R.drawable.btn_vehicles_nitro,
                buttonText = "🏎️ IMPORT ALL VEHICLES ADDON 🏎️",
                guideInfo = "🏎️ World Vehicles In-Game Guide:\n• 40 driveable, flyable, and submersible vehicles!\n• Creative Spawn Eggs or commands: '/summon world:bugatti_tourbillon', '/summon world:f22_raptor_jet', '/summon world:m1a2_abrams_tank'.\n• Zero experiment toggles required - drive immediately!"
            ),
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
                buttonText = "🧬 IMPORT OMNI EVOLUTION 🧬",
                guideInfo = "🧬 Omni Evolution Guide:\n• Craft the Omnitrix or find it in a fallen meteor!\n• Sneak/crouch to rotate aliens, jump to select.\n• Battle Vilgax, transform into Alien X, Heatblast, Diamondhead, and XLR8."
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
                buttonText = "🛸 IMPORT OMNI BOUND 🛸",
                guideInfo = "🛸 Omni-Bound Guide:\n• Fast quick-switch alien selection wheel.\n• Ultimate alien forms with custom superpowers and energy meters.\n• Battle alien invasion drones."
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
                buttonText = "🗡️ IMPORT SOLO LEVELING 🗡️",
                guideInfo = "🗡️ Solo Leveling Guide:\n• Defeat dungeon bosses to level up stats (STR, AGI, INT).\n• Stand over fallen enemies and activate 'Arise' to extract loyal Shadow Soldiers!\n• Daily penalty zone quests and Red Gate portals."
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
                buttonText = "🏴‍☠️ IMPORT ONE PIECE MOD 🏴‍☠️",
                guideInfo = "🏴‍☠️ One Piece Guide:\n• Find Devil Fruits in pirate treasure chests.\n• Awaken Armament, Observation, and Conqueror's Haki.\n• Dual-wield legendary katanas and fight Sea Kings."
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
                buttonText = "🔮 IMPORT TENSURA MOD 🔮",
                guideInfo = "🔮 Tensura Guide:\n• Great Sage HUD communicates with you in real-time.\n• Devour mobs using Predator skill to gain their attributes.\n• Awaken Demon Lord magicules transformation."
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
                buttonText = "🐉 IMPORT DRAGON EVOLUTION 🐉",
                guideInfo = "🐉 Dragon Evolution Guide:\n• Train ki energy to awaken Super Saiyan 1, 2, 3, God, and Blue.\n• Fire Kamehameha, Spirit Bomb, and Final Flash blasts.\n• Travel to custom Dragon dimensions and collect Dragon Balls."
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
                buttonText = "🔫 IMPORT ACTUAL GUNS 2 🔫",
                guideInfo = "🔫 Actual Guns 2 Guide:\n• Craft weapons at the Custom Weapon Bench.\n• Reload ammo by holding magazine in offhand and sneaking.\n• Aim down sights (ADS) with sniper scopes and holographic reticles."
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
                buttonText = "⚡ IMPORT QUIRKBORN MOD ⚡",
                guideInfo = "⚡ Quirkborn Guide:\n• Test your DNA to awaken a random Quirk.\n• Train Quirk mastery by battling villains.\n• Craft hero support items and battle multi-quirk Nomus."
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
                buttonText = "🤖 IMPORT IRON MAN MOD 🤖",
                guideInfo = "🤖 Iron Man Guide:\n• Build the Stark Armor Station.\n• Equip Arc Reactor in chest slot to power flight and weapons.\n• Double jump to engage supersonic flight."
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
                buttonText = "🕷️ IMPORT SPIDER-MAN MOD 🕷️",
                guideInfo = "🕷️ Spider-Man Guide:\n• Equip web shooters to swing across buildings and lasso enemies.\n• Walk directly against vertical walls to climb them.\n• Spider-Sense warning flashes when mobs target you."
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
                buttonText = "⭐ IMPORT MARVEL PROJECT ⭐",
                guideInfo = "⭐ Marvel Project Guide:\n• Summon Thor's Mjolnir and call down thunder.\n• Throw Captain America's Vibranium shield which ricochets.\n• Collect all 6 Infinity Stones to snap enemies out of existence."
            )
        )
    }
}
