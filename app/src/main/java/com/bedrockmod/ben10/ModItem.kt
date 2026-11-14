package com.bedrockmod.ben10

enum class ModCategory(val displayName: String) {
    ALL("🌟 All (14)"),
    CIVILIZATION("🏛️ Civilization & HD (2)"),
    VEHICLES("🏎️ Vehicles (1)"),
    BEN10("👽 Ben 10 (2)"),
    ANIME("🎌 Anime (4)"),
    SUPERHERO("🦸 Superheroes (3)"),
    ACTION("⚔️ Action & Guns (2)")
}

data class ModItem(
    val id: String,
    val title: String,
    val category: ModCategory,
    val badge: String,
    val desc: String,
    val sizeText: String,
    val iconEmoji: String,
    val assetFileName: String,
    val buttonBgRes: Int,
    val buttonText: String
)
