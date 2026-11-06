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

    private lateinit var btnInstall: Button
    private lateinit var progressBar: ProgressBar
    private lateinit var tvStatus: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btnInstall = findViewById(R.id.btnInstall)
        progressBar = findViewById(R.id.progressBar)
        tvStatus = findViewById(R.id.tvStatus)

        // Check and prompt for permissions on startup
        if (!PermissionHelper.hasPermissions(this)) {
            PermissionHelper.requestPermissions(this)
        }

        btnInstall.setOnClickListener {
            handleInstallMod()
        }
    }

    private fun handleInstallMod() {
        if (!PermissionHelper.hasPermissions(this)) {
            PermissionHelper.requestPermissions(this)
            Toast.makeText(this, "Please allow permissions to import the mod!", Toast.LENGTH_SHORT).show()
            return
        }

        btnInstall.isEnabled = false
        progressBar.visibility = View.VISIBLE
        tvStatus.text = getString(R.string.status_importing)

        ModInstaller.installMod(this) { success, message ->
            runOnUiThread {
                btnInstall.isEnabled = true
                progressBar.visibility = View.GONE
                tvStatus.text = if (success) "Status: Import Launched!" else "Status: Error"
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        }
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
                Toast.makeText(this, "Permission granted! Tap BEN 10 MOD to install.", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Permission is required to import into Minecraft.", Toast.LENGTH_LONG).show()
            }
        }
    }
}
