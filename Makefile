run:
	python3 htmlparser/main.py

init_venv:
	python3 -m venv venv

activate:
	source venv/bin/activate

update_packages:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt