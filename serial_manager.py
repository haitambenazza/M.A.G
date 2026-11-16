import asyncio
import sys
import subprocess
from Terminal_colors import GREEN, RED, RESET
from shutil import which
from pathlib import Path



try:
    import aioserial
except ImportError:
    sys.exit(f"{RED}aioserial was not found, try running make or make build{RESET}")

try:
    command = subprocess.run(["command", "-v","arduino-cli"], text=True, capture_output=True)
    if not len(command.stdout):
        print("arduino-cli is ")
except:
    pass

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

def get_arduinoboard():
    try:
        print("getting the port of the arduino...")
        arduino= subprocess.run(["arduino-cli", "board", "list"], capture_output=True, text=True)
        arr = arduino.stdout.split('\n')
        if arr[0] == "No boards found.":
            raise
        for cmd in arr:
            if "Arduino" in cmd:
                print(f"{GREEN}Arduino boad found!{RESET}")
                Serial.PORT = cmd.split(' ')[0]
                return
        raise
    except Exception:
        print(f"{RED}No board found. please plug in Arduino board!{RESET}")



class Serial:
    PORT:str = ""
    BAUD:int = 112500
    def __init__(self):
        check_dependacy()
        get_arduinoboard()
        self.ser = aioserial.AioSerial(port=Serial.PORT, baudrate=Serial.BAUD)
        self.ser_lock = asyncio.Lock()
        print(f"///initializing serial and binding to {GREEN}{self.PORT}{RESET} with {GREEN}{self.BAUD}{RESET}///")

    def sendcmd(self):
        pass
    def readcmd(self) -> str:
        return ""

board: Serial = Serial()