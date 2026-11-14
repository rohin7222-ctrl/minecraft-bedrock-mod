package com.bedrockmod.ben10

import android.content.Context
import android.content.SharedPreferences

class FavoritesManager(context: Context) {

    private val prefs: SharedPreferences =
        context.getSharedPreferences("bedrock_mod_hub_favorites", Context.MODE_PRIVATE)

    fun isFavorite(modId: String): Boolean {
        return prefs.getBoolean("fav_$modId", false)
    }

    fun toggleFavorite(modId: String): Boolean {
        val current = isFavorite(modId)
        val newState = !current
        prefs.edit().putBoolean("fav_$modId", newState).apply()
        return newState
    }

    fun getFavoriteCount(allMods: List<ModItem>): Int {
        var count = 0
        for (mod in allMods) {
            if (isFavorite(mod.id)) {
                count++
            }
        }
        return count
    }
}
