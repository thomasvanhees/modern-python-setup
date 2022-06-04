# Modern Python Setup - Packages

### `pipx`

### `poetry`

### `pre-commit`

Useful info:

- For a list of built-in pre-commit hooks and how to configure them see: https://github.com/pre-commit/pre-commit-hooks/blob/main/README.md.

Commands:

- `pre-commit install`
- `pre-commit run --all-files`
- `pre-commit autoupdate`
- `pre-commit gc`: Garbage collect all virtual environments.

### `pytest`

Use `pytest` for writing tests.

Installation:

Add to the `pyproject.toml` of your project.

Useful info:

- The how-to has some nifty guides: https://docs.pytest.org/en/7.1.x/how-to/index.html#.
- Markers can be used to add attributes to tests, see: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark.
For instance we can distinguish unit and integration tests.
Select markers during a run using the `-m` command, for example: `pytest tests/ -vvv -m unit_test`.

### `pytest-cov`

Use `pytest-cov` for adding coverage checks to `pytest`.

Installation:

Add to the `pyproject.toml` of your project.

Useful commands:

- `pytest --cov=mpspkg tests/`: add coverage to the tests you are running.
- `pytest --cov=mpspkg tests/ --cov-fail-under 90`: fail the run if coverage is below a certain percentage.

Note:

All the extra flags can be added to `addopts` in the `pytest` settings of `pyproject.toml`.
