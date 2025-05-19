install: 
	pip install --upgrade pip
	pip install -r requirements.txt 

run:
	python cli.py

#test:
	#pytest


lint:
	flake8 cli.py test.py 



