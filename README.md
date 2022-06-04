# Modern Python Setup - Packages

### `pytest`

Use `pytest` for writing tests.

Installation:

Add to the `pyproject.toml` of your project.

Useful info:

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
