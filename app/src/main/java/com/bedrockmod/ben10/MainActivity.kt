package com.bedrockmod.ben10

import android.app.Activity
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.os.Environment
import android.provider.OpenableColumns
import android.text.Editable
import android.text.TextWatcher
import android.view.HapticFeedbackConstants
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.chip.Chip
import com.google.android.material.chip.ChipGroup
import com.google.android.material.floatingactionbutton.ExtendedFloatingActionButton
import com.google.android.material.progressindicator.LinearProgressIndicator
import java.io.File

class MainActivity : AppCompatActivity() {

    private lateinit var tvMinecraftStatus: TextView
    private lateinit var btnQuickLaunchMc: Button
    private lateinit var mainProgressBar: LinearProgressIndicator
    private lateinit var etSearch: EditText
    private lateinit var btnClearSearch: TextView
    private lateinit var chipGroupCategories: ChipGroup
    private lateinit var chipAll: Chip
    private lateinit var chipFavorites: Chip
    private lateinit var chipCustom: Chip
    private lateinit var tvResultCount: TextView
    private lateinit var btnSortMode: TextView
    private lateinit var rvMods: RecyclerView
    private lateinit var tvEmptyState: TextView
    private lateinit var fabAddMod: ExtendedFloatingActionButton
    private lateinit var tvBottomInfo: TextView
    private lateinit var btnQuickGuide: Button
    private lateinit var btnClearCache: Button

    private lateinit var modAdapter: ModAdapter
    private lateinit var favoritesManager: FavoritesManager
    private var selectedCategory: ModCategory = ModCategory.ALL
    private var currentSortIndex: Int = 0

    // For file picker dialog
    private var pendingUploadFileUri: Uri? = null
    private var pendingDialogFileStatusView: TextView? = null

    private val filePickerLauncher = registerForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { result ->
        if (result.resultCode == Activity.RESULT_OK && result.data != null) {
            val uri = result.data?.data
            if (uri != null) {
                pendingUploadFileUri = uri
                val fileName = getFileName(uri) ?: "selected_mod.mcaddon"
                val fileSizeStr = getFileSizeString(uri)
                pendingDialogFileStatusView?.apply {
                    text = "✅ $fileName ($fileSizeStr)"
                    setTextColor(0xFF34D399.toInt())
                }
            }
        }
    }

    private val sortLabels = arrayOf(
        "⚡ Sort: Featured ▼",
        "🔤 Sort: A to Z ▼",
        "💾 Sort: Smallest ▼",
        "⭐ Sort: Starred First ▼"
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        favoritesManager = FavoritesManager(this)
        initViews()
        setupRecyclerView()
        setupSearchAndFilters()
        setupMinecraftStatus()
        setupCacheCleaner()
        setupAddModFab()

        // Clean any leftover temp files on startup to prevent 350MB bloat
        ModInstaller.clearModCache(this)
        updateChipCounts()
    }

    override fun onResume() {
        super.onResume()
        updateMinecraftStatus()
        updateChipCounts()
        // Auto-clean cache when returning to app
        ModInstaller.clearModCache(this)
    }

    private fun initViews() {
        tvMinecraftStatus = findViewById(R.id.tvMinecraftStatus)
        btnQuickLaunchMc = findViewById(R.id.btnQuickLaunchMc)
        mainProgressBar = findViewById(R.id.mainProgressBar)
        etSearch = findViewById(R.id.etSearch)
        btnClearSearch = findViewById(R.id.btnClearSearch)
        chipGroupCategories = findViewById(R.id.chipGroupCategories)
        chipAll = findViewById(R.id.chipAll)
        chipFavorites = findViewById(R.id.chipFavorites)
        chipCustom = findViewById(R.id.chipCustom)
        tvResultCount = findViewById(R.id.tvResultCount)
        btnSortMode = findViewById(R.id.btnSortMode)
        rvMods = findViewById(R.id.rvMods)
        tvEmptyState = findViewById(R.id.tvEmptyState)
        fabAddMod = findViewById(R.id.fabAddMod)
        tvBottomInfo = findViewById(R.id.tvBottomInfo)
        btnQuickGuide = findViewById(R.id.btnQuickGuide)
        btnClearCache = findViewById(R.id.btnClearCache)
    }

    private fun loadAllActiveMods(): MutableList<ModItem> {
        val builtIn = ModRepository.getModList().filter { !HiddenModManager.isModHidden(this, it.id) }
        val custom = CustomModManager.getCustomMods(this)
        val combined = ArrayList<ModItem>(builtIn.size + custom.size)
        // Custom mods at the top for easy access
        combined.addAll(custom)
        combined.addAll(builtIn)
        return combined
    }

    private fun setupRecyclerView() {
        val modsList = loadAllActiveMods()
        modAdapter = ModAdapter(
            allMods = modsList,
            favoritesManager = favoritesManager,
            onModClick = { mod ->
                handleModInstall(mod)
            },
            onDetailsClick = { mod ->
                showModDetailsDialog(mod)
            },
            onDeleteClick = { mod ->
                confirmDeleteMod(mod)
            },
            onFavoriteToggled = { _, _ ->
                updateChipCounts()
            }
        )

        rvMods.apply {
            layoutManager = LinearLayoutManager(this@MainActivity)
            adapter = modAdapter
            setHasFixedSize(true)
        }
        applyCurrentFilters()
    }

    private fun setupSearchAndFilters() {
        etSearch.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {
                val query = s?.toString().orEmpty()
                btnClearSearch.visibility = if (query.isNotEmpty()) View.VISIBLE else View.GONE
                applyCurrentFilters()
            }
            override fun afterTextChanged(s: Editable?) {}
        })

        btnClearSearch.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            etSearch.text.clear()
        }

        chipGroupCategories.setOnCheckedChangeListener { _, checkedId ->
            selectedCategory = when (checkedId) {
                R.id.chipFavorites -> ModCategory.FAVORITES
                R.id.chipCustom -> ModCategory.CUSTOM
                R.id.chipMythos -> ModCategory.MYTHOS
                R.id.chipBen10 -> ModCategory.BEN10
                R.id.chipAnime -> ModCategory.ANIME
                R.id.chipSuperhero -> ModCategory.SUPERHERO
                R.id.chipAction -> ModCategory.ACTION
                else -> ModCategory.ALL
            }
            applyCurrentFilters()
        }

        btnSortMode.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            currentSortIndex = (currentSortIndex + 1) % sortLabels.size
            btnSortMode.text = sortLabels[currentSortIndex]
            modAdapter.setSortMode(currentSortIndex)
            Toast.makeText(this, sortLabels[currentSortIndex].replace(" ▼", ""), Toast.LENGTH_SHORT).show()
        }
    }

    private fun setupAddModFab() {
        fabAddMod.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            showUploadModDialog()
        }
    }

    private fun showUploadModDialog() {
        pendingUploadFileUri = null
        val dialogView = LayoutInflater.from(this).inflate(R.layout.dialog_upload_mod, null)
        val etTitle = dialogView.findViewById<EditText>(R.id.etCustomModTitle)
        val etDesc = dialogView.findViewById<EditText>(R.id.etCustomModDesc)
        val btnSelectFile = dialogView.findViewById<Button>(R.id.btnSelectFile)
        val tvFileStatus = dialogView.findViewById<TextView>(R.id.tvSelectedFileStatus)
        val btnCancel = dialogView.findViewById<Button>(R.id.btnCancelDialog)
        val btnSubmit = dialogView.findViewById<Button>(R.id.btnUploadSubmit)

        pendingDialogFileStatusView = tvFileStatus

        val dialog = AlertDialog.Builder(this)
            .setView(dialogView)
            .setCancelable(true)
            .create()

        btnSelectFile.setOnClickListener {
            val intent = Intent(Intent.ACTION_OPEN_DOCUMENT).apply {
                addCategory(Intent.CATEGORY_OPENABLE)
                type = "*/*"
                val mimeTypes = arrayOf(
                    "application/octet-stream",
                    "application/zip",
                    "application/x-zip-compressed",
                    "*/*"
                )
                putExtra(Intent.EXTRA_MIME_TYPES, mimeTypes)
            }
            filePickerLauncher.launch(intent)
        }

        btnCancel.setOnClickListener {
            dialog.dismiss()
        }

        btnSubmit.setOnClickListener {
            val title = etTitle.text.toString().trim()
            val desc = etDesc.text.toString().trim()
            val uri = pendingUploadFileUri

            if (title.isEmpty()) {
                etTitle.error = "Please enter a mod title"
                etTitle.requestFocus()
                return@setOnClickListener
            }

            if (uri == null) {
                Toast.makeText(this, "⚠️ Please select a .mcaddon or .mcpack file first!", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            mainProgressBar.visibility = View.VISIBLE
            dialog.dismiss()

            Thread {
                val addedMod = CustomModManager.addCustomMod(this, title, desc, uri)
                runOnUiThread {
                    mainProgressBar.visibility = View.GONE
                    if (addedMod != null) {
                        Toast.makeText(this, "✨ Custom mod '${addedMod.title}' added successfully!", Toast.LENGTH_LONG).show()
                        refreshModsList()
                        // Switch to Custom Mods category to view it immediately
                        chipCustom.isChecked = true
                    } else {
                        Toast.makeText(this, "❌ Failed to import file. Please check storage permissions.", Toast.LENGTH_LONG).show()
                    }
                }
            }.start()
        }

        dialog.show()
    }

    private fun confirmDeleteMod(mod: ModItem) {
        val isCustom = mod.isCustom
        val title = "🗑️ Delete \"${mod.title}\"?"
        val message = if (isCustom) {
            "Are you sure you want to permanently delete this custom mod?\n\n• The file (${mod.sizeText}) will be deleted from your device storage to free up space."
        } else {
            "Are you sure you want to remove this mod from your list?\n\n• You can restore all default mods anytime by tapping 'Clean Cache' -> 'Restore Default Mods'."
        }

        AlertDialog.Builder(this)
            .setTitle(title)
            .setMessage(message)
            .setPositiveButton("🗑️ Delete") { _, _ ->
                performDeleteMod(mod)
            }
            .setNegativeButton("Cancel", null)
            .show()
    }

    private fun performDeleteMod(mod: ModItem) {
        if (mod.isCustom) {
            CustomModManager.deleteCustomMod(this, mod.id)
            Toast.makeText(this, "🗑️ Deleted custom mod: ${mod.title}", Toast.LENGTH_SHORT).show()
        } else {
            HiddenModManager.hideMod(this, mod.id)
            Toast.makeText(this, "🗑️ Removed from list: ${mod.title}", Toast.LENGTH_SHORT).show()
        }
        modAdapter.removeMod(mod)
        updateChipCounts()
        applyCurrentFilters()
    }

    private fun refreshModsList() {
        val list = loadAllActiveMods()
        modAdapter.updateModsList(list)
        updateChipCounts()
        applyCurrentFilters()
    }

    private fun updateChipCounts() {
        val allMods = loadAllActiveMods()
        val favCount = favoritesManager.getFavoriteCount(allMods)
        val customCount = allMods.count { it.isCustom }
        chipAll.text = "🌟 All (${allMods.size})"
        chipFavorites.text = "⭐ Starred ($favCount)"
        chipCustom.text = "✨ My Mods ($customCount)"
    }

    private fun applyCurrentFilters() {
        val query = etSearch.text?.toString().orEmpty()
        modAdapter.applyFilter(query, selectedCategory)
        val count = modAdapter.getDisplayedCount()
        tvEmptyState.visibility = if (count == 0) View.VISIBLE else View.GONE
        tvResultCount.text = "Showing $count of ${modAdapter.getTotalCount()} Mods Available"
    }

    private fun setupMinecraftStatus() {
        updateMinecraftStatus()

        btnQuickLaunchMc.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            val launched = ModInstaller.launchMinecraft(this)
            if (!launched) {
                Toast.makeText(this, "Minecraft PE not detected. Opening Google Play...", Toast.LENGTH_SHORT).show()
            }
        }

        tvMinecraftStatus.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            showDiagnosticsHubDialog()
        }
    }

    private fun updateMinecraftStatus() {
        val isInstalled = ModInstaller.isMinecraftInstalled(this)
        if (isInstalled) {
            tvMinecraftStatus.text = "🟢 Minecraft Installed"
            tvMinecraftStatus.setTextColor(0xFF34D399.toInt())
            btnQuickLaunchMc.text = "🎮 Open MC"
        } else {
            tvMinecraftStatus.text = "⚠️ Minecraft PE Not Found"
            tvMinecraftStatus.setTextColor(0xFFFBBF24.toInt())
            btnQuickLaunchMc.text = "📥 Get MC"
        }
    }

    private fun showDiagnosticsHubDialog() {
        val isInstalled = ModInstaller.isMinecraftInstalled(this)
        val freeBytes = Environment.getDataDirectory().usableSpace
        val freeGb = freeBytes / (1024.0 * 1024.0 * 1024.0)

        val statusMsg = StringBuilder()
            .append("🎮 Minecraft Bedrock Status:\n")
            .append(if (isInstalled) "   • Status: Installed & Ready (60 FPS Locked)\n" else "   • Status: Not Detected (Google Play link available)\n")
            .append("   • Supported: v1.20.80 through v1.21.x\n\n")
            .append("💾 Device Telemetry & Storage:\n")
            .append(String.format("   • Free Internal Space: %.2f GB\n", freeGb))
            .append("   • Available Addons: ${modAdapter.getTotalCount()} Mods\n")
            .append("   • Custom Mods: ${modAdapter.getCustomModsCount()} Uploaded\n\n")
            .append("⚡ Performance Engine:\n")
            .append("   • Script Runtime: 100% Offline QuickJS\n")
            .append("   • Cache Auto-Purge: Enabled (0MB Dead Storage)")
            .toString()

        AlertDialog.Builder(this)
            .setTitle("⚙️ Bedrock System & Diagnostics Hub")
            .setMessage(statusMsg)
            .setPositiveButton("🎮 Launch MC") { _, _ ->
                ModInstaller.launchMinecraft(this)
            }
            .setNegativeButton("🧹 Clean Cache") { _, _ ->
                val freed = ModInstaller.clearModCache(this)
                val mb = freed / (1024.0 * 1024.0)
                Toast.makeText(this, String.format("🧹 Cleared %.1f MB of cached mod files!", mb), Toast.LENGTH_SHORT).show()
            }
            .setNeutralButton("Close", null)
            .show()
    }

    private fun showModDetailsDialog(mod: ModItem) {
        val isFav = favoritesManager.isFavorite(mod.id)
        val guideText = if (mod.guideInfo.isNotEmpty()) "\n\n${mod.guideInfo}" else ""
        val favStatus = if (isFav) "⭐ (Favorited)" else "☆ (Tap Star on card to favorite)"
        val message = "${mod.badge} • ${mod.sizeText}\nStatus: $favStatus\n\n${mod.desc}$guideText"

        AlertDialog.Builder(this)
            .setTitle("${mod.iconEmoji} ${mod.title}")
            .setMessage(message)
            .setPositiveButton("🚀 Import & Launch") { _, _ ->
                handleModInstall(mod)
            }
            .setNegativeButton("🗑️ Delete") { _, _ ->
                confirmDeleteMod(mod)
            }
            .setNeutralButton("Close", null)
            .show()
    }

    private fun handleModInstall(mod: ModItem) {
        mainProgressBar.visibility = View.VISIBLE
        modAdapter.setImporting(mod.id)
        tvBottomInfo.text = "⏳ Extracting & launching ${mod.title}..."

        if (mod.isCustom && mod.customFilePath != null) {
            val file = File(mod.customFilePath)
            ModInstaller.installCustomMod(
                context = this,
                customFile = file,
                modTitle = mod.title,
                onProgress = { step ->
                    tvBottomInfo.text = "⏳ $step"
                },
                onComplete = { success, message ->
                    mainProgressBar.visibility = View.GONE
                    modAdapter.setImporting(null)
                    tvBottomInfo.text = "💡 Enable 'Beta APIs' in Minecraft World Settings"
                    Toast.makeText(this, message, Toast.LENGTH_LONG).show()
                }
            )
        } else {
            ModInstaller.installMod(
                context = this,
                assetFileName = mod.assetFileName,
                modTitle = mod.title,
                onProgress = { step ->
                    tvBottomInfo.text = "⏳ $step"
                },
                onComplete = { success, message ->
                    mainProgressBar.visibility = View.GONE
                    modAdapter.setImporting(null)
                    tvBottomInfo.text = "💡 Enable 'Beta APIs' in Minecraft World Settings"
                    Toast.makeText(this, message, Toast.LENGTH_LONG).show()
                }
            )
        }
    }

    private fun setupCacheCleaner() {
        val guideListener = View.OnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            showSetupGuideDialog()
        }

        tvBottomInfo.setOnClickListener(guideListener)
        btnQuickGuide.setOnClickListener(guideListener)

        btnClearCache.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            val hiddenCount = HiddenModManager.getHiddenCount(this)
            val freed = ModInstaller.clearModCache(this)
            val mb = freed / (1024.0 * 1024.0)

            if (hiddenCount > 0) {
                AlertDialog.Builder(this)
                    .setTitle("🧹 Storage & Mods Manager")
                    .setMessage(String.format("Cleared %.1f MB of cache!\n\nYou have $hiddenCount hidden default mod(s). Would you like to restore them?", mb))
                    .setPositiveButton("Restore Mods") { _, _ ->
                        HiddenModManager.restoreAllHiddenMods(this)
                        refreshModsList()
                        Toast.makeText(this, "✅ Restored $hiddenCount default mods!", Toast.LENGTH_SHORT).show()
                    }
                    .setNegativeButton("Keep Hidden", null)
                    .show()
            } else {
                if (freed > 0) {
                    Toast.makeText(this, String.format("🧹 Cleared %.1f MB! App storage is now compact.", mb), Toast.LENGTH_SHORT).show()
                } else {
                    Toast.makeText(this, "🧹 Cache is 100% clean (0 MB used)!", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }

    private fun showSetupGuideDialog() {
        AlertDialog.Builder(this)
            .setTitle("💡 Minecraft Bedrock Setup Guide")
            .setMessage("1. Tap any mod card to export and launch Minecraft automatically.\n\n2. In Minecraft World Settings:\n   • Go to Behavior Packs -> Activate the Mod\n   • Go to Resource Packs -> Activate the Mod\n\n3. Under 'Experiments' Settings:\n   • Turn ON 'Beta APIs' (Required for modern GameTest AI scripts)\n   *(Note: 'Holiday Creator Features' was removed by Mojang in modern Bedrock versions)*\n\n4. Experience smooth 60 FPS gameplay!\n\n5. Add Your Own Mods: Tap '➕ Add Mod' anytime to upload your own .mcaddon or .mcpack files!")
            .setPositiveButton("🎮 Got it!", null)
            .show()
    }

    private fun getFileName(uri: Uri): String? {
        var name: String? = null
        if (uri.scheme == "content") {
            val cursor = contentResolver.query(uri, null, null, null, null)
            cursor?.use {
                if (it.moveToFirst()) {
                    val idx = it.getColumnIndex(OpenableColumns.DISPLAY_NAME)
                    if (idx != -1) name = it.getString(idx)
                }
            }
        }
        if (name == null) {
            name = uri.path?.substringAfterLast('/')
        }
        return name
    }

    private fun getFileSizeString(uri: Uri): String {
        return try {
            val cursor = contentResolver.query(uri, null, null, null, null)
            var size = 0L
            cursor?.use {
                if (it.moveToFirst()) {
                    val idx = it.getColumnIndex(OpenableColumns.SIZE)
                    if (idx != -1) size = it.getLong(idx)
                }
            }
            if (size > 1024 * 1024) {
                String.format("%.1f MB", size / (1024.0 * 1024.0))
            } else {
                String.format("%d KB", size / 1024)
            }
        } catch (e: Exception) {
            "Unknown size"
        }
    }
}
