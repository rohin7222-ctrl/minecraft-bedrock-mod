# Ben 10 Bedrock Addon Builder
# Modular Pipeline Runner (Clean & under 10 lines)
import subprocess
import sys

if __name__ == "__main__":
    print("Building Ben 10 Bedrock Addon...")
    result = subprocess.run([sys.executable, "build_addon.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    sys.exit(result.returncode)

