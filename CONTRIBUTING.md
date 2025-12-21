# Contributing to AlertSage

Thank you for your interest in contributing to AlertSage! This document provides guidelines and instructions for contributing.

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant logs or screenshots

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- Use a clear and descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes** following the coding standards below

3. **Add tests** for any new functionality

4. **Run the test suite** to ensure all tests pass:
   ```bash
   pytest tests/ -v
   ```

5. **Update documentation** as needed

6. **Commit your changes** with clear, descriptive commit messages:
   ```bash
   git commit -m "Add feature: description of changes"
   ```

7. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```

8. **Open a Pull Request** with a clear title and description

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AlertSage.git
   cd AlertSage
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install in editable mode with dev dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

4. Verify installation:
   ```bash
   pytest tests/ -v
   ```

## Coding Standards

- **Style**: Follow PEP 8 guidelines
- **Type Hints**: Add type hints to function signatures
- **Docstrings**: Include docstrings for all public functions and classes
- **Comments**: Add comments for complex logic
- **Testing**: Write tests for new features and bug fixes

### Code Formatting

We recommend using `black` for code formatting:

```bash
black src/ tests/
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_cli.py -v

# With coverage report
pytest tests/ --cov=src/triage --cov-report=html
```

### Documentation

If your changes affect user-facing functionality:

1. Update relevant documentation in `docs/`
2. Update the README.md if needed
3. Test documentation locally:
   ```bash
   mkdocs serve
   ```

## Project Structure

```
AlertSage/
├── src/triage/          # Main package code
├── tests/               # Test files
├── docs/                # Documentation
├── generator/           # Dataset generation scripts
├── notebooks/           # Jupyter notebooks
├── models/              # Saved model artifacts
└── data/                # Data files (gitignored)
```

## Commit Message Guidelines

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests when relevant

Examples:
- `Fix bug in preprocessing pipeline (#123)`
- `Add support for custom thresholds`
- `Update documentation for CLI usage`

## Questions?

Feel free to open an issue for questions or reach out via [GitHub Discussions](https://github.com/texasbe2trill/AlertSage/discussions).

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
