PWD=$(shell pwd)

install:
	python setup.py install && pip install -r requirements.txt

lint:
	pep8 .

test:
	PYTHONPATH=$(PWD) py.test -v --color=yes --durations=20

.PHONY: install lint test
