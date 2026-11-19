#!/bin/sh

curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
sudo apt install pipx
pipx ensurepath
pipx install platformio