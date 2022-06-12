# Modern Python Setup - Packages

## Inspiration

The Poetry GitHub repository: https://github.com/python-poetry/poetry.

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

#### `pre-commit` hooks

- `pycln`: https://hadialqattan.github.io/pycln/#/
- `flake8`: https://flake8.pycqa.org/en/latest/index.html#quickstart

### `flake8`

Extensions:

- `flake8-annotations`: https://pypi.org/project/flake8-annotations/
- `flake8-broken-line`: https://pypi.org/project/flake8-broken-line/
- `flake8-bugbear`: https://pypi.org/project/flake8-bugbear/
- `flake8-comprehensions`: Helps you write proper comprehensions. See https://pypi.org/project/flake8-comprehensions/.
- `flake8-eradicate`: Helps find commented out (dead) code. See https://pypi.org/project/flake8-eradicate/.
- `flake8-quotes`: Something with quotes. See https://github.com/zheller/flake8-quotes
- `flake8-simplify`: Finds locations where code can be simplified. See https://pypi.org/project/flake8-simplify/.
- `flake8-tidy-imports`: Simplifies imports. Can also ban imports. See https://pypi.org/project/flake8-tidy-imports/.
- `flake8-type-checking`: (NOT IMPLEMENTED YET) Moves imports that are only used for type checking into separate blocks. See https://github.com/snok/flake8-type-checking.
- `flake8-use-fstring`: Forces you to use f-strings. See https://github.com/MichaelKim0407/flake8-use-fstring.
- `pep8-naming`: Stick to PEP8 standards for names. See https://github.com/PyCQA/pep8-naming.
- `pep8-docstrings`: Check the format and content of docstrings. See https://github.com/PyCQA/flake8-docstrings and https://www.pydocstyle.org/en/stable/index.html.


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
