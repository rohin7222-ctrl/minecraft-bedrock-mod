package com.bedrockmod.ben10

enum class ModCategory(val displayName: String) {
    ALL("🌟 All (17)"),
    BEN10("👽 Ben 10 (5)"),
    ANIME("🎌 Anime (7)"),
    SUPERHERO("🦸 Superheroes (3)"),
    ACTION("⚔️ Weapons & Quirk (2)")
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

