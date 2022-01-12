init_venv:
	python3 -m venv venv

activate:
	source venv/bin/activate

create_package_list:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

run:
	python3 html-parser/main.py