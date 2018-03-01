PWD=$(shell pwd)

install:
	python setup.py install && pip install -r requirements.txt

test:
	pep8 . && PYTHONPATH=$(PWD) py.test -v --color=yes --durations=20 --cov=./ && codecov

run:
	PYTHONPATH=$(PWD) python lib/problem$(problem).py

.PHONY: install test run
