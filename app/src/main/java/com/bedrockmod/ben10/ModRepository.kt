package com.bedrockmod.ben10

object ModRepository {

    fun getModList(): List<ModItem> {
        return listOf(
            ModItem(
                id = "mythos",
                title = "MYTHOS: ASCENSION RPG",
                category = ModCategory.MYTHOS,
                badge = "🔮 CLASSES • MANA • DUNGEONS • BOSSES",
                desc = "MYTHOS: Ascension v7.16.0 Masterpiece! The ultimate fantasy RPG addon for Bedrock: 6 Ascendant Classes, Mana & Skill trees, epic Dungeons, Boss Phases (Dawn Sovereign, Void Warden, Blood Emperor), Omega Fortress, and Aegis Mythic Armor!",
                sizeText = "💾 12.4 MB",
                iconEmoji = "🔮",
                assetFileName = ModInstaller.ASSET_MYTHOS,
                buttonBgRes = R.drawable.btn_mythos_arcane,
                buttonText = "🔮 IMPORT MYTHOS ASCENSION 🔮",
                guideInfo = "🔮 Mythos: Ascension In-Game Guide:\n• Choose your Ascendant Class at the Prime Codex altar.\n• Mana & Skills: Unlock active spellcasts, elemental bursts, and passive talent trees.\n• Dungeons & Raids: Locate Omega Fortress and conquer multi-phase world bosses (Void Warden, Blood Emperor, Dawn Sovereign).\n• Aegis Relics: Forge Mythic Aegis Armor and ascend to Godhood!"
            ),
            ModItem(
                id = "ultrareal_texture_pack",
                title = "ULTRAREAL 100X HD v3.0 (ULTRA PRO)",
                category = ModCategory.MYTHOS,
                badge = "🎨 ZERO EXPERIMENTS • 100X MOBS • BIOME FOGS",
                desc = "UltraReal 100x v3.0 Ultra Pro Edition! 100% Zero Experimental Toggles required (pure vanilla resource pack). Features 100x Realistic Mobs, 360 seamless sky, crystal caustic waters, HD rain & crystalline snow, 8 custom biome fogs, natural isotropic block rotations, and 60 FPS locked!",
                sizeText = "💾 3.8 MB",
                iconEmoji = "🎨",
                assetFileName = ModInstaller.ASSET_ULTRAREAL,
                buttonBgRes = R.drawable.btn_ultrareal_hd,
                buttonText = "🎨 IMPORT ULTRAREAL TEXTURE PACK 🎨",
                guideInfo = "🎨 UltraReal v3.0 In-Game Guide:\n• 1. 100% Zero Experiments: Works in pure vanilla Minecraft Bedrock with ALL experimental toggles turned OFF!\n• 2. Activate under Global Resources or World Resource Packs.\n• 3. Features: 100x HD Mobs, 360 seamless sky dome, crystal clear waters with caustics, HD rain & snow, 8 biome fogs, and natural non-repeating isotropic terrain.\n• 4. Locked 60 FPS performance on all mobile devices!"
            ),
            ModItem(
                id = "wheel_of_adaptation",
                title = "WHEEL OF ADAPTATION (MAHORAGA)",
                category = ModCategory.ANIME,
                badge = "☸️ MAHORAGA • DHARMA WHEEL • ADAPTATION",
                desc = "Official Lore-Accurate Wheel of Adaptation (魔虚羅) from Jujutsu Kaisen! Summon the Eight-Handled Sword Divergent Sila Divine General Mahoraga's Dharma Wheel. Adapts to every phenomenon, physical & elemental attacks, and wields the Sword of Extermination!",
                sizeText = "💾 1.0 MB",
                iconEmoji = "☸️",
                assetFileName = ModInstaller.ASSET_WHEEL_OF_ADAPTATION,
                buttonBgRes = R.drawable.btn_dragon_amber,
                buttonText = "☸️ IMPORT WHEEL OF ADAPTATION ☸️",
                guideInfo = "☸️ Wheel of Adaptation In-Game Guide:\n• 1. Craft/Equip the Dharma Wheel on your head or offhand to begin adaptation.\n• 2. Adaptation Mechanism: When taking damage from any source (fire, melee, magic, arrows, poison, void), the wheel spins and progressively increases resistance until 100% immune!\n• 3. Sword of Extermination: Unleash positive energy blade that one-shots cursed spirits and undead mobs.\n• 4. Mode Switcher: Sneak + use to cycle between Defense, Attack, and Barehand combat modes.\n• 5. Mahoraga Armor: Equip Mahoraga armor pieces for massive physical buffs and continuous regeneration!"
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
                id = "aplok_guns",
                title = "APLOK GUNS 3D (v1.8.8)",
                category = ModCategory.ACTION,
                badge = "🔫 3D FIREARMS • RELOAD ANIMATIONS • SCOPES",
                desc = "Official Aplok Guns Public Beta Addon! Hyper-realistic 3D firearms, smooth first-person tactical reload animations, realistic muzzle flash, scopes & sights, custom ammo crafting, and recoil physics!",
                sizeText = "💾 13.2 MB",
                iconEmoji = "🔫",
                assetFileName = ModInstaller.ASSET_APLOK_GUNS,
                buttonBgRes = R.drawable.btn_actualguns_red,
                buttonText = "🔫 IMPORT APLOK GUNS 🔫",
                guideInfo = "🔫 Aplok Guns In-Game Guide:\n• 1. Craft weapons and ammunition at the custom Gun Workbench.\n• 2. Reload: Hold matching ammo magazine in your inventory and sneak/crouch to execute realistic reload animations.\n• 3. Aim Down Sights (ADS): Sneak to aim with holographic sights, red dot, or sniper scopes.\n• 4. Tactical Attachments: Suppressors, extended magazines, and flashlights can be attached.\n• 5. Enable 'Beta APIs' experimental toggle in world settings for full functionality."
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
