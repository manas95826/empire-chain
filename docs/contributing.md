# Contributing to Empire Chain

We love your input! We want to make contributing to Empire Chain as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Local Development Setup

```bash
# Clone the repository
git clone https://github.com/manas95826/empire-chain.git
cd empire-chain

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest
```

## Code Style

We use `black` for Python code formatting and `flake8` for linting:

```bash
# Install formatting tools
pip install black flake8

# Format code
black .

# Run linter
flake8
```

## Documentation

We use MkDocs with the Material theme for documentation:

```bash
# Install documentation dependencies
pip install mkdocs-material mkdocs-mermaid2-plugin

# Serve documentation locally
mkdocs serve

# Build documentation
mkdocs build
```

## Pull Request Process

1. Update the README.md with details of changes to the interface
2. Update the documentation with any new features or changes
3. The PR will be merged once you have the sign-off of at least one maintainer

## Any Contributions You Make Will Be Under the MIT License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](LICENSE) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report Bugs Using GitHub's Issue Tracker

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/manas95826/empire-chain/issues/new).

## Write Bug Reports With Detail, Background, and Sample Code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## License

By contributing, you agree that your contributions will be licensed under its MIT License. 