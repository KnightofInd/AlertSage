# Contributing Guide

!!! info "Coming Soon"
Detailed contribution guidelines are being developed.

## Quick Start

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Run tests: `pytest tests/ -v`
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/AlertSage.git
cd AlertSage
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Code Style

- Follow PEP 8
- Use type hints
- Add docstrings
- Write tests for new features

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_cli.py -v

# With coverage
pytest tests/ --cov=src/triage
```

## Documentation

```bash
# Preview docs locally
mkdocs serve

# Build docs
mkdocs build
```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers

---

See [Development Guide](development.md) for more details.
