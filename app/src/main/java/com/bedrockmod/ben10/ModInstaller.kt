package com.bedrockmod.ben10

import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Handler
import android.os.Looper
import androidx.core.content.FileProvider
import java.io.File
import java.io.FileOutputStream
import java.io.InputStream

object ModInstaller {

    const val MINECRAFT_PACKAGE = "com.mojang.minecraftpe"
    const val MINECRAFT_TRIAL_PACKAGE = "com.mojang.minecrafttrialpe"

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
    const val ASSET_DRAGON_BALL_SPARK = "Dragon_Ball_Spark.mcaddon"
    const val ASSET_ATTACK_ON_TITAN = "Attack_On_Titan.mcaddon"
    const val ASSET_SOLO_LEVELING = "Solo_Leveling_v1.0.6.mcaddon"
    const val ASSET_DEMON_SLAYER = "Demon_Slayer.mcaddon"
    const val ASSET_BEN10_V6 = "Ben10_Addon_v6.mcaddon"
    const val ASSET_BEN10_OMNI_NR = "Ben10_Omni_NR.mcaddon"
    const val ASSET_BEN10_V7 = "Ben10_Addon_v7.mcaddon"

    private val mainHandler = Handler(Looper.getMainLooper())

    /**
     * Checks whether Minecraft Bedrock Edition (Retail or Trial) is installed on the device.
     */
    fun isMinecraftInstalled(context: Context): Boolean {
        val pm = context.packageManager
        return try {
            pm.getPackageInfo(MINECRAFT_PACKAGE, 0)
            true
        } catch (e: PackageManager.NameNotFoundException) {
            try {
                pm.getPackageInfo(MINECRAFT_TRIAL_PACKAGE, 0)
                true
            } catch (e2: PackageManager.NameNotFoundException) {
                false
            }
        }
    }

    /**
     * Directly launches Minecraft Bedrock if installed, or opens the Google Play Store page.
     */
    fun launchMinecraft(context: Context): Boolean {
        val pm = context.packageManager
        val launchIntent = pm.getLaunchIntentForPackage(MINECRAFT_PACKAGE)
            ?: pm.getLaunchIntentForPackage(MINECRAFT_TRIAL_PACKAGE)

        return if (launchIntent != null) {
            launchIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            context.startActivity(launchIntent)
            true
        } else {
            try {
                val storeIntent = Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse("market://details?id=$MINECRAFT_PACKAGE")
                ).apply { addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) }
                context.startActivity(storeIntent)
            } catch (e: Exception) {
                val webIntent = Intent(
                    Intent.ACTION_VIEW,
                    Uri.parse("https://play.google.com/store/apps/details?id=$MINECRAFT_PACKAGE")
                ).apply { addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) }
                context.startActivity(webIntent)
            }
            false
        }
    }

    /**
     * Clears previously extracted mod files from cache to prevent storage bloat.
     */
    fun clearModCache(context: Context): Long {
        var freedBytes = 0L
        try {
            val cacheFiles = context.cacheDir.listFiles() ?: return 0L
            for (file in cacheFiles) {
                if (file.name.endsWith(".mcaddon", ignoreCase = true) ||
                    file.name.endsWith(".mcpack", ignoreCase = true)
                ) {
                    val size = file.length()
                    if (file.delete()) {
                        freedBytes += size
                    }
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return freedBytes
    }

    /**
     * Extracts the requested .mcaddon from assets into private cache, generates a secure
     * FileProvider content URI, and launches Minecraft Bedrock for automatic import.
     */
    fun installMod(
        context: Context,
        assetFileName: String,
        modTitle: String,
        onProgress: ((String) -> Unit)? = null,
        onComplete: (Boolean, String) -> Unit
    ) {
        Thread {
            try {
                postProgress(onProgress, "Preparing file cache...")
                clearModCache(context)

                val targetFile = File(context.cacheDir, assetFileName)
                if (targetFile.exists()) {
                    targetFile.delete()
                }

                postProgress(onProgress, "Extracting $modTitle...")
                val inputStream: InputStream = context.assets.open(assetFileName)
                val outputStream = FileOutputStream(targetFile)
                val buffer = ByteArray(32768)
                var bytesRead: Int
                while (inputStream.read(buffer).also { bytesRead = it } != -1) {
                    outputStream.write(buffer, 0, bytesRead)
                }
                outputStream.flush()
                outputStream.close()
                inputStream.close()

                postProgress(onProgress, "Granting permissions & launching...")
                val contentUri: Uri = FileProvider.getUriForFile(
                    context,
                    "${context.packageName}.provider",
                    targetFile
                )

                // Explicitly grant read URI permissions to target packages
                try {
                    context.grantUriPermission(
                        MINECRAFT_PACKAGE,
                        contentUri,
                        Intent.FLAG_GRANT_READ_URI_PERMISSION
                    )
                    context.grantUriPermission(
                        MINECRAFT_TRIAL_PACKAGE,
                        contentUri,
                        Intent.FLAG_GRANT_READ_URI_PERMISSION
                    )
                } catch (e: Exception) {
                    e.printStackTrace()
                }

                // Primary intent targeting Minecraft
                val intent = Intent(Intent.ACTION_VIEW).apply {
                    setDataAndType(contentUri, "application/octet-stream")
                    addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
                    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                }

                val packageManager = context.packageManager
                val mcIntent = Intent(intent).setPackage(MINECRAFT_PACKAGE)
                val trialIntent = Intent(intent).setPackage(MINECRAFT_TRIAL_PACKAGE)

                when {
                    mcIntent.resolveActivity(packageManager) != null -> {
                        context.startActivity(mcIntent)
                        postComplete(onComplete, true, "🎮 Launching Minecraft... Importing $modTitle!")
                    }
                    trialIntent.resolveActivity(packageManager) != null -> {
                        context.startActivity(trialIntent)
                        postComplete(onComplete, true, "🎮 Launching Minecraft Trial... Importing $modTitle!")
                    }
                    intent.resolveActivity(packageManager) != null -> {
                        val chooser = Intent.createChooser(intent, "Open with Minecraft").apply {
                            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                        }
                        context.startActivity(chooser)
                        postComplete(onComplete, true, "Select Minecraft from the list to import $modTitle!")
                    }
                    else -> {
                        launchMinecraft(context)
                        postComplete(onComplete, false, "Minecraft Bedrock not found. Please install Minecraft PE!")
                    }
                }

            } catch (e: Exception) {
                e.printStackTrace()
                postComplete(onComplete, false, "Failed to export mod: ${e.localizedMessage}")
            }
        }.start()
    }

    private fun postProgress(callback: ((String) -> Unit)?, message: String) {
        callback?.let {
            mainHandler.post { it(message) }
        }
    }

    private fun postComplete(callback: (Boolean, String) -> Unit, success: Boolean, message: String) {
        mainHandler.post {
            callback(success, message)
        }
    }
}
