all: test mypy ruff

PHONY: test
test:
	uv run pytest

PHONY: coverage
coverage:
	uv run pytest --cov src/ofxstatement
.PHONY: ruff
ruff:
	uv run ruff format src tests

.PHONY: mypy
mypy:
	uv run mypy src tests