package com.bedrockmod.ben10

import android.content.Context
import android.content.SharedPreferences

object HiddenModManager {

    private const val PREFS_NAME = "bedrock_mod_hub_hidden"
    private const val KEY_HIDDEN_SET = "hidden_mod_ids"

    private fun getPrefs(context: Context): SharedPreferences {
        return context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)
    }

    fun isModHidden(context: Context, modId: String): Boolean {
        val set = getPrefs(context).getStringSet(KEY_HIDDEN_SET, emptySet()) ?: emptySet()
        return set.contains(modId)
    }

    fun hideMod(context: Context, modId: String) {
        val currentSet = HashSet(getPrefs(context).getStringSet(KEY_HIDDEN_SET, emptySet()) ?: emptySet())
        currentSet.add(modId)
        getPrefs(context).edit().putStringSet(KEY_HIDDEN_SET, currentSet).apply()
    }

    fun restoreMod(context: Context, modId: String) {
        val currentSet = HashSet(getPrefs(context).getStringSet(KEY_HIDDEN_SET, emptySet()) ?: emptySet())
        currentSet.remove(modId)
        getPrefs(context).edit().putStringSet(KEY_HIDDEN_SET, currentSet).apply()
    }

    fun restoreAllHiddenMods(context: Context): Int {
        val count = getHiddenCount(context)
        getPrefs(context).edit().remove(KEY_HIDDEN_SET).apply()
        return count
    }

    fun getHiddenCount(context: Context): Int {
        return (getPrefs(context).getStringSet(KEY_HIDDEN_SET, emptySet()) ?: emptySet()).size
    }
}
