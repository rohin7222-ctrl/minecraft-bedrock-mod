package com.bedrockmod.ben10

import android.content.Context
import android.net.Uri
import android.provider.OpenableColumns
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.io.FileOutputStream
import java.util.UUID

object CustomModManager {

    private const val JSON_FILE_NAME = "custom_mods.json"
    private const val CUSTOM_MODS_DIR = "custom_mods"

    fun getCustomMods(context: Context): List<ModItem> {
        val list = mutableListOf<ModItem>()
        try {
            val jsonFile = File(context.filesDir, JSON_FILE_NAME)
            if (!jsonFile.exists()) return emptyList()

            val content = jsonFile.readText()
            val array = JSONArray(content)

            for (i in 0 until array.length()) {
                val obj = array.getJSONObject(i)
                val id = obj.getString("id")
                val title = obj.getString("title")
                val desc = obj.optString("desc", "")
                val sizeText = obj.optString("sizeText", "💾 Custom")
                val filePath = obj.getString("filePath")
                val file = File(filePath)

                if (file.exists()) {
                    list.add(
                        ModItem(
                            id = id,
                            title = title,
                            category = ModCategory.CUSTOM,
                            badge = "✨ CUSTOM USER ADDON",
                            desc = desc,
                            sizeText = sizeText,
                            iconEmoji = "📦",
                            assetFileName = file.name,
                            buttonBgRes = R.drawable.btn_mod_custom,
                            buttonText = "📥 IMPORT CUSTOM MOD",
                            guideInfo = "📦 Custom Addon Guide:\n• 1. Tap 'Import' to launch Minecraft Bedrock and install this custom addon.\n• 2. Enable under World Settings (Resource & Behavior Packs).\n• 3. Enable 'Beta APIs' if this addon uses custom GameTest scripts.",
                            isCustom = true,
                            customFilePath = file.absolutePath
                        )
                    )
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return list
    }

    fun addCustomMod(context: Context, title: String, desc: String, uri: Uri): ModItem? {
        return try {
            val dir = File(context.filesDir, CUSTOM_MODS_DIR)
            if (!dir.exists()) {
                dir.mkdirs()
            }

            // Get original file name and extension
            var originalName = getFileNameFromUri(context, uri) ?: "custom_addon_${System.currentTimeMillis()}.mcaddon"
            if (!originalName.endsWith(".mcaddon", ignoreCase = true) &&
                !originalName.endsWith(".mcpack", ignoreCase = true) &&
                !originalName.endsWith(".zip", ignoreCase = true)
            ) {
                originalName += ".mcaddon"
            }

            val safeFileName = "${System.currentTimeMillis()}_${originalName.replace(Regex("[^a-zA-Z0-9._-]"), "_")}"
            val targetFile = File(dir, safeFileName)

            // Copy file from Uri to private storage
            context.contentResolver.openInputStream(uri)?.use { input ->
                FileOutputStream(targetFile).use { output ->
                    input.copyTo(output)
                }
            }

            val sizeBytes = targetFile.length()
            val sizeMb = sizeBytes / (1024.0 * 1024.0)
            val sizeText = if (sizeMb >= 1.0) {
                String.format("💾 %.1f MB", sizeMb)
            } else {
                String.format("💾 %d KB", sizeBytes / 1024)
            }

            val newId = "custom_${UUID.randomUUID().toString().take(8)}"
            val modItem = ModItem(
                id = newId,
                title = title,
                category = ModCategory.CUSTOM,
                badge = "✨ CUSTOM USER ADDON",
                desc = desc,
                sizeText = sizeText,
                iconEmoji = "📦",
                assetFileName = targetFile.name,
                buttonBgRes = R.drawable.btn_mod_custom,
                buttonText = "📥 IMPORT CUSTOM MOD",
                guideInfo = "📦 Custom Addon Guide:\n• 1. Tap 'Import' to launch Minecraft Bedrock and install this custom addon.\n• 2. Enable under World Settings (Resource & Behavior Packs).\n• 3. Enable 'Beta APIs' if this addon uses custom GameTest scripts.",
                isCustom = true,
                customFilePath = targetFile.absolutePath
            )

            // Save to JSON
            val existingMods = getCustomModJsonArray(context)
            val newObj = JSONObject().apply {
                put("id", newId)
                put("title", title)
                put("desc", desc)
                put("sizeText", sizeText)
                put("filePath", targetFile.absolutePath)
            }
            existingMods.put(newObj)
            saveCustomModJsonArray(context, existingMods)

            modItem
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    fun deleteCustomMod(context: Context, modId: String): Boolean {
        return try {
            val array = getCustomModJsonArray(context)
            val newArray = JSONArray()
            var deletedFile = false

            for (i in 0 until array.length()) {
                val obj = array.getJSONObject(i)
                if (obj.getString("id") == modId) {
                    val path = obj.optString("filePath")
                    if (path.isNotEmpty()) {
                        val file = File(path)
                        if (file.exists()) {
                            file.delete()
                        }
                    }
                    deletedFile = true
                } else {
                    newArray.put(obj)
                }
            }
            saveCustomModJsonArray(context, newArray)
            deletedFile
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }

    private fun getCustomModJsonArray(context: Context): JSONArray {
        val jsonFile = File(context.filesDir, JSON_FILE_NAME)
        if (!jsonFile.exists()) return JSONArray()
        return try {
            JSONArray(jsonFile.readText())
        } catch (e: Exception) {
            JSONArray()
        }
    }

    private fun saveCustomModJsonArray(context: Context, array: JSONArray) {
        val jsonFile = File(context.filesDir, JSON_FILE_NAME)
        jsonFile.writeText(array.toString(2))
    }

    private fun getFileNameFromUri(context: Context, uri: Uri): String? {
        var name: String? = null
        if (uri.scheme == "content") {
            val cursor = context.contentResolver.query(uri, null, null, null, null)
            cursor?.use {
                if (it.moveToFirst()) {
                    val idx = it.getColumnIndex(OpenableColumns.DISPLAY_NAME)
                    if (idx != -1) {
                        name = it.getString(idx)
                    }
                }
            }
        }
        if (name == null) {
            name = uri.path?.substringAfterLast('/')
        }
        return name
    }
}
