start:
	python3 main.py

install:
	pip install -r requirements.txt

activate:
	source venv/bin/activate

deactivate:
	deactivate

venv:
	python3 -m venv venv
