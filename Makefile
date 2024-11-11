.PHONY: run install check clean runner
.DEFAULT_GOAL:=runner


run:install
	cd app; poetry run python run.py

install:pyproject.toml
	poetry install

check:
	poetry run ruff check .

clean:
	rm -rf `find . -type d -name __pycache__`

runner: check run clean