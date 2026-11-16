import asyncio
import sys
import subprocess
from Terminal_colors import GREEN, RED, RESET

PORT = ""
BAUD = 112500

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

def get_arduinoboard():
    try:
        global PORT
        arduino= subprocess.run(["arduino-cli", "board", "list"], capture_output=True, text=True)
        arr = arduino.stdout.split('\n')
        if arr[0] == "No boards found.":
            raise
        for cmd in arr:
            if "Arduino" in cmd:
                print(f"{GREEN}Arduino boad found!{RESET}")
                PORT = cmd.split(' ')[0]
                return
        raise
    except Exception:
        print(f"{RED}No board found. please plug in Arduino board!{RESET}")



class Serial:
    def __init__(self, port: str, baud: int):
        self.ser = aioserial.AioSerial(port=port, baudrate=baud)
        self.ser_lock = asyncio.Lock()
        print(f"///initializing serial and binding to {port} with {baud}///")

    def sendcmd(self):
        pass
    def readcmd(self) -> str:
        return ""

get_arduinoboard()
board: Serial = Serial(PORT, BAUD)