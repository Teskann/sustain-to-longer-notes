clean: install
	rm -rf build dist .eggs *.egg-info
	echo Successfuly installed ! Try it running "sustain -h"

tests: requirements
	echo Running tests ...
	python -m pytest

requirements:
	echo Installing requirements ...
	pip install -r requirements.txt

install: tests
	python setup.py install