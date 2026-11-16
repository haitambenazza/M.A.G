build:
	curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
	pip3 install -r requirements.txt

run:
	python3 main.py