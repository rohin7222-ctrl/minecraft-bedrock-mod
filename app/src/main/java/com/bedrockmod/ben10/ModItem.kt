package com.bedrockmod.ben10

enum class ModCategory(val displayName: String) {
    ALL("🌟 All"),
    FAVORITES("⭐ Starred"),
    CUSTOM("✨ My Mods"),
    MYTHOS("🔮 Mythos & HD"),
    BEN10("👽 Ben 10"),
    ANIME("🎌 Anime"),
    SUPERHERO("🦸 Superheroes"),
    ACTION("⚔️ Action & Guns")
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
    val buttonText: String,
    val guideInfo: String = "",
    val isCustom: Boolean = false,
    val customFilePath: String? = null
)
