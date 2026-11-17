package com.bedrockmod.ben10

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.progressindicator.LinearProgressIndicator

class ModAdapter(
    private var allMods: MutableList<ModItem>,
    private val favoritesManager: FavoritesManager,
    private val onModClick: (ModItem) -> Unit,
    private val onDetailsClick: (ModItem) -> Unit,
    private val onDeleteClick: (ModItem) -> Unit,
    private val onFavoriteToggled: (ModItem, Boolean) -> Unit
) : RecyclerView.Adapter<ModAdapter.ModViewHolder>() {

    private val displayedMods = ArrayList<ModItem>(allMods)
    private var currentQuery: String = ""
    private var currentCategory: ModCategory = ModCategory.ALL
    private var activeImportingId: String? = null
    private var currentSortMode: Int = 0 // 0: Featured, 1: A-Z, 2: Size, 3: Starred First

    class ModViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvEmoji: TextView = itemView.findViewById(R.id.tvModEmoji)
        val tvTitle: TextView = itemView.findViewById(R.id.tvModTitle)
        val tvBadge: TextView = itemView.findViewById(R.id.tvModBadge)
        val tvSize: TextView = itemView.findViewById(R.id.tvModSize)
        val tvDesc: TextView = itemView.findViewById(R.id.tvModDesc)
        val btnFavorite: TextView = itemView.findViewById(R.id.btnFavorite)
        val cardProgress: LinearProgressIndicator = itemView.findViewById(R.id.cardProgress)
        val btnModDetails: Button = itemView.findViewById(R.id.btnModDetails)
        val btnDeleteMod: Button = itemView.findViewById(R.id.btnDeleteMod)
        val btnImport: Button = itemView.findViewById(R.id.btnImportMod)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ModViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.item_mod_card, parent, false)
        return ModViewHolder(view)
    }

    override fun onBindViewHolder(holder: ModViewHolder, position: Int) {
        val mod = displayedMods[position]

        holder.tvEmoji.text = mod.iconEmoji
        holder.tvTitle.text = mod.title
        holder.tvBadge.text = mod.badge
        holder.tvSize.text = mod.sizeText
        holder.tvDesc.text = mod.desc

        // Category Badge Tinting
        when (mod.category) {
            ModCategory.CUSTOM -> {
                holder.tvBadge.setTextColor(0xFF34D399.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF064E3B.toInt())
            }
            ModCategory.MYTHOS -> {
                holder.tvBadge.setTextColor(0xFFF0ABFC.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF4A044E.toInt())
            }
            ModCategory.BEN10 -> {
                holder.tvBadge.setTextColor(0xFF86EFAC.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF064E3B.toInt())
            }
            ModCategory.ANIME -> {
                holder.tvBadge.setTextColor(0xFFFDBA74.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF431407.toInt())
            }
            ModCategory.SUPERHERO -> {
                holder.tvBadge.setTextColor(0xFFF472B6.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF311042.toInt())
            }
            ModCategory.ACTION -> {
                holder.tvBadge.setTextColor(0xFFA5B4FC.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF1E1B4B.toInt())
            }
            else -> {
                holder.tvBadge.setTextColor(0xFFCBD5E1.toInt())
                holder.tvBadge.background?.mutate()?.setTint(0xFF1E293B.toInt())
            }
        }

        // Favorite Star
        val isFav = favoritesManager.isFavorite(mod.id)
        holder.btnFavorite.text = if (isFav) "⭐" else "☆"
        holder.btnFavorite.setOnClickListener {
            it.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            val newState = favoritesManager.toggleFavorite(mod.id)
            holder.btnFavorite.text = if (newState) "⭐" else "☆"
            onFavoriteToggled(mod, newState)
            if (currentCategory == ModCategory.FAVORITES) {
                applyFilter(currentQuery, currentCategory)
            }
        }

        // Details Guide Button
        holder.btnModDetails.setOnClickListener {
            it.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            onDetailsClick(mod)
        }

        // Delete Button
        holder.btnDeleteMod.setOnClickListener {
            it.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            onDeleteClick(mod)
        }

        // Import Button styling & state
        holder.btnImport.setBackgroundResource(mod.buttonBgRes)
        val isImporting = (activeImportingId == mod.id)
        val isAnyImporting = (activeImportingId != null)

        if (isImporting) {
            holder.cardProgress.visibility = View.VISIBLE
            holder.btnImport.text = "⏳ IMPORTING..."
            holder.btnImport.isEnabled = false
        } else {
            holder.cardProgress.visibility = View.GONE
            // Concise button text that never truncates on screen
            holder.btnImport.text = if (mod.isCustom) "📥 IMPORT CUSTOM" else "${mod.iconEmoji} IMPORT MOD"
            holder.btnImport.isEnabled = !isAnyImporting
        }

        // High-contrast text color for bright button backgrounds
        if (mod.buttonBgRes == R.drawable.btn_dragonball_orange ||
            mod.buttonBgRes == R.drawable.btn_quirkborn_yellow ||
            mod.buttonBgRes == R.drawable.btn_omnibound_lime ||
            mod.buttonBgRes == R.drawable.btn_onepiece_orange ||
            mod.buttonBgRes == R.drawable.btn_omni_blue ||
            mod.buttonBgRes == R.drawable.btn_header_mc ||
            mod.buttonBgRes == R.drawable.btn_mod_custom
        ) {
            holder.btnImport.setTextColor(0xFF042F2E.toInt())
        } else {
            holder.btnImport.setTextColor(0xFFFFFFFF.toInt())
        }

        holder.btnImport.setOnClickListener {
            it.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            onModClick(mod)
        }
        holder.itemView.setOnClickListener {
            it.performHapticFeedback(android.view.HapticFeedbackConstants.VIRTUAL_KEY)
            onDetailsClick(mod)
        }
    }

    override fun getItemCount(): Int = displayedMods.size

    fun setImporting(modId: String?) {
        activeImportingId = modId
        notifyDataSetChanged()
    }

    fun setSortMode(sortMode: Int) {
        currentSortMode = sortMode
        applySort()
        notifyDataSetChanged()
    }

    fun updateModsList(newMods: List<ModItem>) {
        allMods.clear()
        allMods.addAll(newMods)
        applyFilter(currentQuery, currentCategory)
    }

    fun removeMod(mod: ModItem) {
        val indexInDisplayed = displayedMods.indexOfFirst { it.id == mod.id }
        allMods.removeAll { it.id == mod.id }
        if (indexInDisplayed != -1) {
            displayedMods.removeAt(indexInDisplayed)
            notifyItemRemoved(indexInDisplayed)
        } else {
            notifyDataSetChanged()
        }
    }

    fun applyFilter(query: String, category: ModCategory) {
        currentQuery = query.trim().lowercase()
        currentCategory = category

        displayedMods.clear()
        for (mod in allMods) {
            val matchesCategory = when (category) {
                ModCategory.ALL -> true
                ModCategory.FAVORITES -> favoritesManager.isFavorite(mod.id)
                ModCategory.CUSTOM -> mod.isCustom
                else -> mod.category == category
            }
            val matchesQuery = if (currentQuery.isEmpty()) {
                true
            } else {
                mod.title.lowercase().contains(currentQuery) ||
                mod.desc.lowercase().contains(currentQuery) ||
                mod.badge.lowercase().contains(currentQuery)
            }

            if (matchesCategory && matchesQuery) {
                displayedMods.add(mod)
            }
        }
        applySort()
        notifyDataSetChanged()
    }

    private fun applySort() {
        when (currentSortMode) {
            1 -> displayedMods.sortBy { it.title }
            2 -> displayedMods.sortBy { extractSizeMb(it.sizeText) }
            3 -> displayedMods.sortByDescending { favoritesManager.isFavorite(it.id) }
            else -> {
                // Featured: Keep order from allMods
                displayedMods.sortBy { allMods.indexOf(it) }
            }
        }
    }

    private fun extractSizeMb(sizeText: String): Float {
        return try {
            val num = sizeText.replace(Regex("[^0-9.]"), "").toFloat()
            if (sizeText.contains("KB", ignoreCase = true)) num / 1024f else num
        } catch (e: Exception) {
            0f
        }
    }

    fun getDisplayedCount(): Int = displayedMods.size
    fun getTotalCount(): Int = allMods.size
    fun getCustomModsCount(): Int = allMods.count { it.isCustom }
}
