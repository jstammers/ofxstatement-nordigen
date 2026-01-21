PYPROJECT := pyproject.toml
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



.PHONY: bump-patch bump-minor bump-major

bump-patch:
	@uv version --bump patch

bump-minor:
	@uv version --bump minor

bump-major:
	@uv version --bump major

