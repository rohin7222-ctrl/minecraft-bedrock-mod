package com.bedrockmod.ben10

import android.content.pm.PackageManager
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ProgressBar
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var btnInstallOmni: Button
    private lateinit var btnInstallOmniBound: Button
    private lateinit var btnInstallOnePiece: Button
    private lateinit var btnInstallTensura: Button
    private lateinit var btnInstallDragonEvo: Button
    private lateinit var btnInstallActualGuns: Button
    private lateinit var btnInstallQuirkborn: Button
    private lateinit var btnInstallIronMan: Button
    private lateinit var btnInstallSpiderMan: Button
    private lateinit var btnInstallMarvel: Button
    private lateinit var btnInstallDragonBall: Button
    private lateinit var btnInstallAoT: Button
    private lateinit var btnInstallSoloLeveling: Button
    private lateinit var progressBar: ProgressBar
    private lateinit var tvStatus: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnInstallOmni = findViewById(R.id.btnInstallOmni)
        btnInstallOmniBound = findViewById(R.id.btnInstallOmniBound)
        btnInstallOnePiece = findViewById(R.id.btnInstallOnePiece)
        btnInstallTensura = findViewById(R.id.btnInstallTensura)
        btnInstallDragonEvo = findViewById(R.id.btnInstallDragonEvo)
        btnInstallActualGuns = findViewById(R.id.btnInstallActualGuns)
        btnInstallQuirkborn = findViewById(R.id.btnInstallQuirkborn)
        btnInstallIronMan = findViewById(R.id.btnInstallIronMan)
        btnInstallSpiderMan = findViewById(R.id.btnInstallSpiderMan)
        btnInstallMarvel = findViewById(R.id.btnInstallMarvel)
        btnInstallDragonBall = findViewById(R.id.btnInstallDragonBall)
        btnInstallAoT = findViewById(R.id.btnInstallAoT)
        btnInstallSoloLeveling = findViewById(R.id.btnInstallSoloLeveling)
        progressBar = findViewById(R.id.progressBar)
        tvStatus = findViewById(R.id.tvStatus)

        // Check and prompt for permissions on startup
        if (!PermissionHelper.hasPermissions(this)) {
            PermissionHelper.requestPermissions(this)
        }

        btnInstallOmni.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_OMNI_EVOLUTION,
                getString(R.string.mod_omni_title)
            )
        }

        btnInstallOmniBound.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_OMNI_BOUND,
                getString(R.string.mod_omnibound_title)
            )
        }

        btnInstallOnePiece.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_ONE_PIECE,
                getString(R.string.mod_onepiece_title)
            )
        }

        btnInstallTensura.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_TENSURA,
                getString(R.string.mod_tensura_title)
            )
        }

        btnInstallDragonEvo.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_DRAGON_EVOLUTION,
                getString(R.string.mod_dragonevo_title)
            )
        }

        btnInstallActualGuns.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_ACTUAL_GUNS,
                getString(R.string.mod_actualguns_title)
            )
        }

        btnInstallQuirkborn.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_QUIRKBORN,
                getString(R.string.mod_quirkborn_title)
            )
        }

        btnInstallIronMan.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_IRON_MAN,
                getString(R.string.mod_ironman_title)
            )
        }

        btnInstallSpiderMan.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_SPIDER_MAN,
                getString(R.string.mod_spiderman_title)
            )
        }

        btnInstallMarvel.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_MARVEL_PROJECT,
                getString(R.string.mod_marvel_title)
            )
        }

        btnInstallDragonBall.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_DRAGON_BALL_SPARK,
                getString(R.string.mod_dragonball_title)
            )
        }

        btnInstallAoT.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_ATTACK_ON_TITAN,
                getString(R.string.mod_aot_title)
            )
        }

        btnInstallSoloLeveling.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_SOLO_LEVELING,
                getString(R.string.mod_sololeveling_title)
            )
        }
    }

    private fun handleInstallMod(assetFileName: String, modTitle: String) {
        if (!PermissionHelper.hasPermissions(this)) {
            PermissionHelper.requestPermissions(this)
            Toast.makeText(this, "Please allow permissions to import the mod!", Toast.LENGTH_SHORT).show()
            return
        }

        setButtonsEnabled(false)
        progressBar.visibility = View.VISIBLE
        tvStatus.text = "● Status: Exporting $modTitle..."

        ModInstaller.installMod(this, assetFileName, modTitle) { success, message ->
            runOnUiThread {
                setButtonsEnabled(true)
                progressBar.visibility = View.GONE
                tvStatus.text = if (success) "● Status: Minecraft Launched ($modTitle)" else "● Status: Error"
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        }
    }

    private fun setButtonsEnabled(enabled: Boolean) {
        btnInstallOmni.isEnabled = enabled
        btnInstallOmniBound.isEnabled = enabled
        btnInstallOnePiece.isEnabled = enabled
        btnInstallTensura.isEnabled = enabled
        btnInstallDragonEvo.isEnabled = enabled
        btnInstallActualGuns.isEnabled = enabled
        btnInstallQuirkborn.isEnabled = enabled
        btnInstallIronMan.isEnabled = enabled
        btnInstallSpiderMan.isEnabled = enabled
        btnInstallMarvel.isEnabled = enabled
        btnInstallDragonBall.isEnabled = enabled
        btnInstallAoT.isEnabled = enabled
        btnInstallSoloLeveling.isEnabled = enabled
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults)
        if (requestCode == PermissionHelper.REQUEST_CODE_STORAGE) {
            val allGranted = grantResults.isNotEmpty() && grantResults.all { it == PackageManager.PERMISSION_GRANTED }
            if (allGranted) {
                Toast.makeText(this, "Permission granted! Tap any mod to install.", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Permission is required to import into Minecraft.", Toast.LENGTH_LONG).show()
            }
        }
    }
}
