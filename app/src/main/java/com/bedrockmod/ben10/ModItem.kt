package com.bedrockmod.ben10

enum class ModCategory(val displayName: String) {
    ALL("🌟 All (13)"),
    ANIME("🎌 Anime (6)"),
    SUPERHERO("🦸 Superheroes (3)"),
    ACTION("⚔️ Action & Sci-Fi (4)")
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
