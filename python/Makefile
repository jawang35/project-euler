PWD=$(shell pwd)

install:
	python3 setup.py install && pip3 install -r requirements.txt

lint:
	pep8 .

test:
	PYTHONPATH=$(PWD) py.test -v --color=yes --durations=20

.PHONY: install lint test
