# Makefile for Pydantic v1/v2 test project

VENV := .venv
PYTHON := python3

.PHONY: venv install activate run tests clean

venv:
	$(PYTHON) -m virtualenv $(VENV)
	$(VENV)/bin/pip install -U pip

install: venv
	$(VENV)/bin/pip install -e .

activate:
	@echo "Run the following command to activate the venv:"
	@echo "source $(VENV)/bin/activate"

run:
	$(VENV)/bin/python -m pytest

test: run

clean:
	rm -rf $(VENV) .pytest_cache __pycache__ */__pycache__