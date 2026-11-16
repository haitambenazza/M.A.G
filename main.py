# from serial_manager import board
from shutil import which
import subprocess
import sys
from Terminal_colors import RED, RESET, GREEN
from pathlib import Path


def check_dependacy():
    try:
        if which("arduino-cli") is None:
            dep = input(f"{RED}arduino-cli was not found!{RESET} would you like to install it? (y/n)")
            if dep == 'y':
                script = Path(__file__).parent / "setup.sh"
                script.chmod(0o755)
                subprocess.run([str(script)], cwd=script.parent)
            else:
                print("abort...")
                sys.exit(1)
        print(f"{GREEN}arduino-cli was found{RESET}")
    except:
        sys.exit(f"{RED}encountered an error{RESET}")

if __name__ == "__main__":
    check_dependacy()