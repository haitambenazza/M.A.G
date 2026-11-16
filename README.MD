# Mouse-Controlled Robotic Arm

A Python project for controlling a three-axis robotic arm from a computer mouse. The planned interface uses Pygame to display the arm's movement and communicates with an Arduino over a serial (UART) connection.

> **Status:** Work in progress. The serial communication and arm-control logic are not yet fully implemented.

## Requirements

- Python 3
- An Arduino connected over USB
- `make`
- `arduino-cli` for Arduino tooling

Python dependencies are listed in [`requirements.txt`](requirements.txt).

## Setup

Create and activate a virtual environment from the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install `arduino-cli` and the Python dependencies:

```bash
make build
```

If `arduino-cli` is not installed when you run the application, it will also prompt to install it using [`setup.sh`](setup.sh).

## Usage

Connect the Arduino, then start the application with:

```bash
make run
```

The Makefile provides:

| Command | Description |
| --- | --- |
| `make build` | Install `arduino-cli` and Python dependencies |
| `make run` | Start the Python application (`python3 main.py`) |

## Hardware and communication

The computer communicates with the Arduino through an asynchronous serial UART connection (`aioserial`). On startup, `serial_manager.py` verifies `arduino-cli` is available, automatically detects the connected Arduino's serial port via `arduino-cli board list`, and binds to it at a baud rate of `112500`. Verify that your Arduino firmware uses the same baud rate.

## Project layout

| File | Purpose |
| --- | --- |
| [`main.py`](main.py) | Application entry point |
| [`serial_manager.py`](serial_manager.py) | Dependency checks, Arduino port detection, and async serial wrapper |
| [`Terminal_colors.py`](Terminal_colors.py) | ANSI color constants for terminal output |
| [`setup.sh`](setup.sh) | Installer script for `arduino-cli` |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`Makefile`](Makefile) | Build and run commands |
