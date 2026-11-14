package com.bedrockmod.ben10

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.progressindicator.LinearProgressIndicator

class ModAdapter(
    private val allMods: List<ModItem>,
    private val onModClick: (ModItem) -> Unit
) : RecyclerView.Adapter<ModAdapter.ModViewHolder>() {

    private val displayedMods = ArrayList<ModItem>(allMods)
    private var currentQuery: String = ""
    private var currentCategory: ModCategory = ModCategory.ALL
    private var activeImportingId: String? = null

    class ModViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvEmoji: TextView = itemView.findViewById(R.id.tvModEmoji)
        val tvTitle: TextView = itemView.findViewById(R.id.tvModTitle)
        val tvBadge: TextView = itemView.findViewById(R.id.tvModBadge)
        val tvSize: TextView = itemView.findViewById(R.id.tvModSize)
        val tvDesc: TextView = itemView.findViewById(R.id.tvModDesc)
        val cardProgress: LinearProgressIndicator = itemView.findViewById(R.id.cardProgress)
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

        // Button background & text
        holder.btnImport.setBackgroundResource(mod.buttonBgRes)
        val isImporting = (activeImportingId == mod.id)
        val isAnyImporting = (activeImportingId != null)

        if (isImporting) {
            holder.cardProgress.visibility = View.VISIBLE
            holder.btnImport.text = "⏳ EXPORTING & LAUNCHING..."
            holder.btnImport.isEnabled = false
        } else {
            holder.cardProgress.visibility = View.GONE
            holder.btnImport.text = mod.buttonText
            holder.btnImport.isEnabled = !isAnyImporting
        }

        // Text color for buttons with bright background
        if (mod.buttonBgRes == R.drawable.btn_dragonball_orange ||
            mod.buttonBgRes == R.drawable.btn_quirkborn_yellow ||
            mod.buttonBgRes == R.drawable.btn_omnibound_lime ||
            mod.buttonBgRes == R.drawable.btn_onepiece_orange ||
            mod.buttonBgRes == R.drawable.btn_omni_blue ||
            mod.buttonBgRes == R.drawable.btn_ben10_v6_neon ||
            mod.buttonBgRes == R.drawable.btn_ben10_omni_nr_neon
        ) {
            holder.btnImport.setTextColor(0xFF050B14.toInt())
        } else {
            holder.btnImport.setTextColor(0xFFFFFFFF.toInt())
        }

        holder.btnImport.setOnClickListener {
            onModClick(mod)
        }
        holder.itemView.setOnClickListener {
            onModClick(mod)
        }
    }

    override fun getItemCount(): Int = displayedMods.size

    fun setImporting(modId: String?) {
        activeImportingId = modId
        notifyDataSetChanged()
    }

    fun applyFilter(query: String, category: ModCategory) {
        currentQuery = query.trim().lowercase()
        currentCategory = category

        displayedMods.clear()
        for (mod in allMods) {
            val matchesCategory = (category == ModCategory.ALL || mod.category == category)
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
        notifyDataSetChanged()
    }

    fun getDisplayedCount(): Int = displayedMods.size
}

