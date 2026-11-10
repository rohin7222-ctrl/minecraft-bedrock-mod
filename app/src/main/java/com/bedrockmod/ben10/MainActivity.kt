package com.bedrockmod.ben10

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.chip.ChipGroup
import com.google.android.material.progressindicator.LinearProgressIndicator

class MainActivity : AppCompatActivity() {

    private lateinit var tvMinecraftStatus: TextView
    private lateinit var btnQuickLaunchMc: Button
    private lateinit var mainProgressBar: LinearProgressIndicator
    private lateinit var etSearch: EditText
    private lateinit var btnClearSearch: TextView
    private lateinit var chipGroupCategories: ChipGroup
    private lateinit var rvMods: RecyclerView
    private lateinit var tvEmptyState: TextView
    private lateinit var tvBottomInfo: TextView
    private lateinit var btnClearCache: Button

    private lateinit var modAdapter: ModAdapter
    private var selectedCategory: ModCategory = ModCategory.ALL

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        initViews()
        setupRecyclerView()
        setupSearchAndFilters()
        setupMinecraftStatus()
        setupCacheCleaner()
    }

    override fun onResume() {
        super.onResume()
        updateMinecraftStatus()
    }

    private fun initViews() {
        tvMinecraftStatus = findViewById(R.id.tvMinecraftStatus)
        btnQuickLaunchMc = findViewById(R.id.btnQuickLaunchMc)
        mainProgressBar = findViewById(R.id.mainProgressBar)
        etSearch = findViewById(R.id.etSearch)
        btnClearSearch = findViewById(R.id.btnClearSearch)
        chipGroupCategories = findViewById(R.id.chipGroupCategories)
        rvMods = findViewById(R.id.rvMods)
        tvEmptyState = findViewById(R.id.tvEmptyState)
        tvBottomInfo = findViewById(R.id.tvBottomInfo)
        btnClearCache = findViewById(R.id.btnClearCache)
    }

    private fun setupRecyclerView() {
        val modList = ModRepository.getModList()
        modAdapter = ModAdapter(modList) { mod ->
            handleModInstall(mod)
        }

        rvMods.apply {
            layoutManager = LinearLayoutManager(this@MainActivity)
            adapter = modAdapter
            setHasFixedSize(true)
        }
    }

    private fun setupSearchAndFilters() {
        // Live search text watcher
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
            etSearch.text.clear()
        }

        // Category Filter Chips
        chipGroupCategories.setOnCheckedChangeListener { _, checkedId ->
            selectedCategory = when (checkedId) {
                R.id.chipBen10 -> ModCategory.BEN10
                R.id.chipAnime -> ModCategory.ANIME
                R.id.chipSuperhero -> ModCategory.SUPERHERO
                R.id.chipAction -> ModCategory.ACTION
                else -> ModCategory.ALL
            }
            applyCurrentFilters()
        }
    }

    private fun applyCurrentFilters() {
        val query = etSearch.text?.toString().orEmpty()
        modAdapter.applyFilter(query, selectedCategory)
        tvEmptyState.visibility = if (modAdapter.getDisplayedCount() == 0) View.VISIBLE else View.GONE
    }

    private fun setupMinecraftStatus() {
        updateMinecraftStatus()

        val launchAction = View.OnClickListener {
            val launched = ModInstaller.launchMinecraft(this)
            if (!launched) {
                Toast.makeText(this, "Minecraft PE not detected. Opening Google Play...", Toast.LENGTH_SHORT).show()
            }
        }

        btnQuickLaunchMc.setOnClickListener(launchAction)
        tvMinecraftStatus.setOnClickListener(launchAction)
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
        tvBottomInfo.setOnClickListener {
            androidx.appcompat.app.AlertDialog.Builder(this)
                .setTitle("💡 Minecraft Bedrock Setup Guide")
                .setMessage("1. Tap any mod to export and launch Minecraft.\n2. In Minecraft World Settings:\n   • Activate Behavior Pack\n   • Activate Resource Pack\n3. Under 'Experiments', turn ON:\n   • Beta APIs\n4. Enjoy the mods in 60 FPS!")
                .setPositiveButton("🎮 Got it!", null)
                .show()
        }

        btnClearCache.setOnClickListener {
            val freed = ModInstaller.clearModCache(this)
            val mb = freed / (1024.0 * 1024.0)
            if (freed > 0) {
                Toast.makeText(this, String.format("🧹 Cleared %.1f MB of cached mod files!", mb), Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "🧹 Cache is already clean!", Toast.LENGTH_SHORT).show()
            }
        }
    }
}
