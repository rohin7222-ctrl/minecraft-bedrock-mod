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
    private lateinit var btnInstallOnePiece: Button
    private lateinit var btnInstallTensura: Button
    private lateinit var progressBar: ProgressBar
    private lateinit var tvStatus: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnInstallOmni = findViewById(R.id.btnInstallOmni)
        btnInstallOnePiece = findViewById(R.id.btnInstallOnePiece)
        btnInstallTensura = findViewById(R.id.btnInstallTensura)
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
        btnInstallOnePiece.isEnabled = enabled
        btnInstallTensura.isEnabled = enabled
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
