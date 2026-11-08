package com.bedrockmod.ben10

import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.core.content.FileProvider
import java.io.File
import java.io.FileOutputStream
import java.io.InputStream

object ModInstaller {

    private const val MINECRAFT_PACKAGE = "com.mojang.minecraftpe"

    const val ASSET_OMNI_EVOLUTION = "Omni-Evolution-Beta.mcaddon"
    const val ASSET_OMNI_BOUND = "Omni_Bound_v1.5.2.mcaddon"
    const val ASSET_ONE_PIECE = "OnePiece_Bedrock_Edition_v76.mcaddon"
    const val ASSET_TENSURA = "Tensura_Reincarnated_Requiem_v4.mcaddon"
    const val ASSET_DRAGON_EVOLUTION = "Dragon_Evolution_v1.5.0.mcaddon"
    const val ASSET_ACTUAL_GUNS = "Actual_Guns_2.mcaddon"
    const val ASSET_QUIRKBORN = "Quirkborn_v1.515.3.mcaddon"
    const val ASSET_IRON_MAN = "Iron_Man_Addon.mcaddon"
    const val ASSET_SPIDER_MAN = "Spider_Man_Addon.mcaddon"
    const val ASSET_MARVEL_PROJECT = "Marvel_Project_v3.0.1.mcaddon"

    fun installMod(
        context: Context,
        assetFileName: String,
        modTitle: String,
        onComplete: (Boolean, String) -> Unit
    ) {
        Thread {
            try {
                // 1. Prepare target file in cache directory
                val targetFile = File(context.cacheDir, assetFileName)
                if (targetFile.exists()) {
                    targetFile.delete()
                }

                // 2. Extract mcaddon from assets to cache
                val inputStream: InputStream = context.assets.open(assetFileName)
                val outputStream = FileOutputStream(targetFile)
                val buffer = ByteArray(16384)
                var bytesRead: Int
                while (inputStream.read(buffer).also { bytesRead = it } != -1) {
                    outputStream.write(buffer, 0, bytesRead)
                }
                outputStream.flush()
                outputStream.close()
                inputStream.close()

                // 3. Generate secure content URI using FileProvider (Bypasses Android 14/15/16+ Scoped Storage)
                val contentUri: Uri = FileProvider.getUriForFile(
                    context,
                    "${context.packageName}.provider",
                    targetFile
                )

                // 4. Create ACTION_VIEW Intent targeting Minecraft PE
                val intent = Intent(Intent.ACTION_VIEW).apply {
                    setDataAndType(contentUri, "application/octet-stream")
                    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                }

                // Try opening with Minecraft directly if installed
                val packageManager = context.packageManager
                val mcIntent = Intent(intent).setPackage(MINECRAFT_PACKAGE)

                if (mcIntent.resolveActivity(packageManager) != null) {
                    context.startActivity(mcIntent)
                    onComplete(true, "Launching Minecraft... Importing $modTitle!")
                } else if (intent.resolveActivity(packageManager) != null) {
                    // Fallback to open with chooser
                    val chooser = Intent.createChooser(intent, "Open with Minecraft").apply {
                        addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    }
                    context.startActivity(chooser)
                    onComplete(true, "Select Minecraft from the list to import $modTitle!")
                } else {
                    // Minecraft is not installed
                    val playStoreIntent = Intent(
                        Intent.ACTION_VIEW,
                        Uri.parse("market://details?id=$MINECRAFT_PACKAGE")
                    ).apply { addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) }

                    if (playStoreIntent.resolveActivity(packageManager) != null) {
                        context.startActivity(playStoreIntent)
                    }
                    onComplete(false, "Minecraft Bedrock not found. Please install Minecraft PE!")
                }

            } catch (e: Exception) {
                e.printStackTrace()
                onComplete(false, "Failed to export mod: ${e.localizedMessage}")
            }
        }.start()
    }
}
