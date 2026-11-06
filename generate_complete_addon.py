# Ben 10 Bedrock Addon Builder Runner
import os
import subprocess
import sys

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    runner = os.path.join(script_dir, "ben10_bedrock_addon", "python", "generate_complete_addon.py")
    sys.exit(subprocess.run([sys.executable, runner]).returncode)
