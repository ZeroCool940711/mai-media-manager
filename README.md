# Mai Media Manager

A short summary of the project

## Getting Started

Clone this repository:

```
$ git clone https://github.com/ZeroCool940711/mai-media-manager.git
```

To set up your local development environment, please use a fresh virtual environment (`python -m venv .venv`), then run:

    pip install -r requirements.txt -r requirements-dev.txt
    pip install -e .

The first command will install all requirements for the application and to execute tests.
With the second command, you'll get an editable installation of the module, so that imports work properly.

You can now import functions and classes from the module with `import mai_media_manager` for development or run the `main.py` in order to run the UI.

```
# Run the main file using python
$ python main.py

# or with Flet using hot reloading. Better for development.
$ flet run main.py -d -r
```

**Note**: You MUST run the `main.py` at least once without hot reloading (`-d -r` arguments) for the `db` folder to be created properly, otherwise you will encounter errors since the db will be corrupted since hot reloading kicks in as soon as any new file is created and the db can't be created properly.

### Testing

We use `pytest` as test framework. To execute the tests, please run

    pytest tests

To run the tests with coverage information, please use

    pytest tests --cov=src --cov-report=html --cov-report=term

and have a look at the `htmlcov` folder, after the tests are done.

### Distribution Package

To build a distribution package (wheel), please use

    python setup.py bdist_wheel

You can find the build artifacts in the `dist` folder.

### Contributions

Before contributing, please set up the pre-commit hooks to reduce errors and ensure consistency

    pip install -U pre-commit
    pre-commit install

If you run into any issues, you can remove the hooks again with `pre-commit uninstall`.

## Contact

You can find us in our [Discord server](https://discord.gg/FxjzYDSbE8) to talk about any of our projects.

## License

© Alejandro M Gil Elias
