PWD=$(shell pwd)

test:
	PYTHONPATH=$(PWD) py.test -v --color=yes --durations=20

.PHONY: test
