package com.bedrockmod.ben10

import android.app.Activity
import android.os.Build

object PermissionHelper {
    const val REQUEST_CODE_STORAGE = 1001

    /**
     * FileProvider shares directly from internal app cache (context.cacheDir),
     * which is fully sandboxed and permissionless on all Android versions.
     */
    fun hasPermissions(activity: Activity): Boolean {
        return true
    }

    fun requestPermissions(activity: Activity) {
        // No-op: Internal cache sharing requires no runtime permissions
    }
}
