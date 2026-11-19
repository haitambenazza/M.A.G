build:
	chmod +x setup.sh
	./setup.sh
	pip3 install -r requirements.txt

run:
	python3 main.py