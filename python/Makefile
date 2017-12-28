PWD=$(shell pwd)

install:
	python3 setup.py install && pip3 install -r requirements.txt

test:
	pep8 . && PYTHONPATH=$(PWD) py.test -v --color=yes --durations=20

run:
	PYTHONPATH=$(PWD) python3 lib/problem$(problem).py

.PHONY: install test
