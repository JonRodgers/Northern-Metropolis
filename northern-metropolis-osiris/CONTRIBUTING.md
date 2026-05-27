# Contributing to Northern Metropolis OSIRIS

Thank you for your interest in contributing to the Northern Metropolis OSIRIS project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/JonRodgers/Northern-Metropolis.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Install development dependencies: `pip install -e ".[dev]"`

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest`
4. Run linting: `black . && flake8 . && mypy .`
5. Commit your changes: `git commit -am 'Add your feature'`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for all modules, classes, and functions
- Use Black for code formatting
- Use isort for import sorting

## Testing

- Write tests for all new features
- Maintain or improve code coverage
- Run tests before submitting a PR: `pytest --cov=northern_metropolis_osiris`

## Documentation

- Update README.md if adding new features
- Add docstrings to all new code
- Update API documentation if modifying endpoints

## Commit Messages

Use clear, descriptive commit messages:
- `feat: Add new feature`
- `fix: Fix bug in module`
- `docs: Update documentation`
- `test: Add tests for feature`
- `refactor: Refactor code structure`

## Pull Request Process

1. Update documentation and tests
2. Ensure all tests pass
3. Provide a clear description of changes
4. Link related issues
5. Request review from maintainers

## Reporting Issues

- Use GitHub Issues for bug reports
- Provide clear description and reproduction steps
- Include environment details (OS, Python version, etc.)
- Attach relevant logs or screenshots

## Questions?

Open an issue or contact the development team.

Thank you for contributing!
