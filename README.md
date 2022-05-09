# Python Best Practices Cookiecutter

Best practices [cookiecutter](https://github.com/audreyr/cookiecutter) template as described in this [blogpost](https://sourcery.ai/blog/python-best-practices/).

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Deployment ready with [Docker](https://docker.com/)
- Continuous Integration with [GitHub Actions](https://github.com/features/actions)
- Dependency management with [Poetry](https://python-poetry.org/)
- Code coverage with [Codecov](https://codecov.io)

## Quickstart 
```sh
# Install pipx if poetry and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install poetry using pipx
pipx install poetry

# Use cookiecutter to create project from this template
pipx run cookiecutter gh:rasa/python-best-practices-cookiecutter

# Enter project directory
cd {project_module}

# Initialise git repo
git init

# Install dependencies
poetry install

# Setup pre-commit and pre-push hooks
poetry run pre-commit install -t pre-commit
poetry run pre-commit install -t pre-push
```
