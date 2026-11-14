package com.bedrockmod.ben10

import android.os.Bundle
import android.os.Environment
import android.text.Editable
import android.text.TextWatcher
import android.view.HapticFeedbackConstants
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.chip.Chip
import com.google.android.material.chip.ChipGroup
import com.google.android.material.progressindicator.LinearProgressIndicator

class MainActivity : AppCompatActivity() {

    private lateinit var tvMinecraftStatus: TextView
    private lateinit var btnQuickLaunchMc: Button
    private lateinit var mainProgressBar: LinearProgressIndicator
    private lateinit var etSearch: EditText
    private lateinit var btnClearSearch: TextView
    private lateinit var chipGroupCategories: ChipGroup
    private lateinit var chipFavorites: Chip
    private lateinit var tvResultCount: TextView
    private lateinit var btnSortMode: TextView
    private lateinit var rvMods: RecyclerView
    private lateinit var tvEmptyState: TextView
    private lateinit var tvBottomInfo: TextView
    private lateinit var btnQuickGuide: Button
    private lateinit var btnClearCache: Button

    private lateinit var modAdapter: ModAdapter
    private lateinit var favoritesManager: FavoritesManager
    private var selectedCategory: ModCategory = ModCategory.ALL
    private var currentSortIndex: Int = 0

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
        updateFavoritesChipCount()
    }

    override fun onResume() {
        super.onResume()
        updateMinecraftStatus()
        updateFavoritesChipCount()
    }

    private fun initViews() {
        tvMinecraftStatus = findViewById(R.id.tvMinecraftStatus)
        btnQuickLaunchMc = findViewById(R.id.btnQuickLaunchMc)
        mainProgressBar = findViewById(R.id.mainProgressBar)
        etSearch = findViewById(R.id.etSearch)
        btnClearSearch = findViewById(R.id.btnClearSearch)
        chipGroupCategories = findViewById(R.id.chipGroupCategories)
        chipFavorites = findViewById(R.id.chipFavorites)
        tvResultCount = findViewById(R.id.tvResultCount)
        btnSortMode = findViewById(R.id.btnSortMode)
        rvMods = findViewById(R.id.rvMods)
        tvEmptyState = findViewById(R.id.tvEmptyState)
        tvBottomInfo = findViewById(R.id.tvBottomInfo)
        btnQuickGuide = findViewById(R.id.btnQuickGuide)
        btnClearCache = findViewById(R.id.btnClearCache)
    }

    private fun setupRecyclerView() {
        val modList = ModRepository.getModList()
        modAdapter = ModAdapter(
            allMods = modList,
            favoritesManager = favoritesManager,
            onModClick = { mod ->
                handleModInstall(mod)
            },
            onDetailsClick = { mod ->
                showModDetailsDialog(mod)
            },
            onFavoriteToggled = { _, _ ->
                updateFavoritesChipCount()
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
                R.id.chipCiv -> ModCategory.CIVILIZATION
                R.id.chipVehicles -> ModCategory.VEHICLES
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

    private fun updateFavoritesChipCount() {
        val count = favoritesManager.getFavoriteCount(ModRepository.getModList())
        chipFavorites.text = "⭐ Starred ($count)"
    }

    private fun applyCurrentFilters() {
        val query = etSearch.text?.toString().orEmpty()
        modAdapter.applyFilter(query, selectedCategory)
        val count = modAdapter.getDisplayedCount()
        tvEmptyState.visibility = if (count == 0) View.VISIBLE else View.GONE
        tvResultCount.text = "Showing $count of ${ModRepository.getModList().size} Mods Available"
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
            tvMinecraftStatus.text = "🟢 Minecraft Bedrock Installed"
            tvMinecraftStatus.setTextColor(0xFF34D399.toInt())
            btnQuickLaunchMc.text = "🎮 Open MC"
        } else {
            tvMinecraftStatus.text = "⚠️ Minecraft PE Not Found (Tap to Get)"
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
            .append("   • Available Addons: 14 High-Speed Mods\n")
            .append("   • Battery Profile: Cosmic Dark OLED Optimized\n\n")
            .append("⚡ Performance Engine:\n")
            .append("   • Script Runtime: 100% Offline QuickJS\n")
            .append("   • Experimental Requirement: Pure Beta APIs")
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
            .setNeutralButton("Close", null)
            .show()
    }

    private fun handleModInstall(mod: ModItem) {
        mainProgressBar.visibility = View.VISIBLE
        modAdapter.setImporting(mod.id)
        tvBottomInfo.text = "⏳ Extracting & launching ${mod.title}..."

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

    private fun setupCacheCleaner() {
        val guideListener = View.OnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            showSetupGuideDialog()
        }

        tvBottomInfo.setOnClickListener(guideListener)
        btnQuickGuide.setOnClickListener(guideListener)

        btnClearCache.setOnClickListener {
            it.performHapticFeedback(HapticFeedbackConstants.VIRTUAL_KEY)
            val freed = ModInstaller.clearModCache(this)
            val mb = freed / (1024.0 * 1024.0)
            if (freed > 0) {
                Toast.makeText(this, String.format("🧹 Cleared %.1f MB of cached mod files!", mb), Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "🧹 Cache is already clean!", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun showSetupGuideDialog() {
        AlertDialog.Builder(this)
            .setTitle("💡 Minecraft Bedrock Setup Guide")
            .setMessage("1. Tap any mod card to export and launch Minecraft automatically.\n\n2. In Minecraft World Settings:\n   • Go to Behavior Packs -> Activate the Mod\n   • Go to Resource Packs -> Activate the Mod\n\n3. Under 'Experiments' Settings:\n   • Turn ON 'Beta APIs' (Required for modern GameTest AI scripts)\n   *(Note: 'Holiday Creator Features' was removed by Mojang in modern Bedrock versions)*\n\n4. Experience smooth 60 FPS gameplay!")
            .setPositiveButton("🎮 Got it!", null)
            .show()
    }
}
