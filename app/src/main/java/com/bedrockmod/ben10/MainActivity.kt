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
    private lateinit var btnInstallBen10V2: Button
    private lateinit var btnInstallOmniBound: Button
    private lateinit var btnInstallOnePiece: Button
    private lateinit var btnInstallNarutoCraft: Button
    private lateinit var btnInstallTensura: Button
    private lateinit var btnInstallDragonEvo: Button
    private lateinit var btnInstallArise: Button
    private lateinit var btnInstallActualGuns: Button
    private lateinit var progressBar: ProgressBar
    private lateinit var tvStatus: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnInstallOmni = findViewById(R.id.btnInstallOmni)
        btnInstallBen10V2 = findViewById(R.id.btnInstallBen10V2)
        btnInstallOmniBound = findViewById(R.id.btnInstallOmniBound)
        btnInstallOnePiece = findViewById(R.id.btnInstallOnePiece)
        btnInstallNarutoCraft = findViewById(R.id.btnInstallNarutoCraft)
        btnInstallTensura = findViewById(R.id.btnInstallTensura)
        btnInstallDragonEvo = findViewById(R.id.btnInstallDragonEvo)
        btnInstallArise = findViewById(R.id.btnInstallArise)
        btnInstallActualGuns = findViewById(R.id.btnInstallActualGuns)
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

        btnInstallBen10V2.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_BEN10_V2,
                getString(R.string.mod_ben10v2_title)
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

        btnInstallNarutoCraft.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_NARUTO_CRAFT,
                getString(R.string.mod_narutocraft_title)
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

        btnInstallArise.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_ARISE,
                getString(R.string.mod_arise_title)
            )
        }

        btnInstallActualGuns.setOnClickListener {
            handleInstallMod(
                ModInstaller.ASSET_ACTUAL_GUNS,
                getString(R.string.mod_actualguns_title)
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
        btnInstallBen10V2.isEnabled = enabled
        btnInstallOmniBound.isEnabled = enabled
        btnInstallOnePiece.isEnabled = enabled
        btnInstallNarutoCraft.isEnabled = enabled
        btnInstallTensura.isEnabled = enabled
        btnInstallDragonEvo.isEnabled = enabled
        btnInstallArise.isEnabled = enabled
        btnInstallActualGuns.isEnabled = enabled
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
