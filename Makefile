.PHONY: default
default: test coverage coveragehtml mypy

.PHONY: test
test:
	PYTHONPATH=. pytest tests

.PHONY: coverage
coverage:
	coverage run -m pytest tests

.PHONY: coveragehtml
coveragehtml:
	coverage html

.PHONY: mypy
mypy:
	mypy list2tuple

.PHONY: clean
clean:
	rm -rf htmlcov .coverage
