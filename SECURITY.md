# Security Policy

## Supported Versions

This project is currently in active development. Security updates will be applied to the latest version.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security issues seriously. If you discover a security vulnerability, please follow these steps:

### Please Do Not

- **Do not** open a public GitHub issue for security vulnerabilities
- **Do not** disclose the vulnerability publicly until it has been addressed

### Please Do

1. **Report privately** by opening a security advisory on GitHub:
   - Go to the [Security tab](https://github.com/texasbe2trill/AlertSage/security)
   - Click "Report a vulnerability"
   - Provide detailed information about the vulnerability

2. **Include in your report**:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Any suggested fixes (if available)
   - Your contact information for follow-up questions

### What to Expect

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Assessment**: We will assess the vulnerability and determine its severity
- **Updates**: We will keep you informed of progress toward a fix
- **Credit**: We will credit you for the discovery (unless you prefer to remain anonymous)
- **Timeline**: We aim to address critical vulnerabilities within 7 days and other issues within 30 days

## Security Best Practices

When using AlertSage:

1. **Local LLM Models**: The project uses local LLM models by default. No data is sent to external APIs unless you explicitly configure it.

2. **Sensitive Data**: Do not include real sensitive or confidential incident data in issues, pull requests, or public discussions.

3. **Dependencies**: Keep dependencies up to date. Run `pip install --upgrade -e ".[dev]"` regularly.

4. **Credentials**: Never commit credentials, API keys, or sensitive configuration to the repository.

5. **Production Use**: This is an educational/research project. Do not use in production security operations without thorough evaluation and additional security hardening.

## Known Limitations

- **Synthetic Data Only**: Trained on synthetic data; real-world performance is unvalidated
- **No Authentication**: No built-in authentication or authorization mechanisms
- **Local Execution**: Designed for local research use, not as a public service
- **LLM Safety**: Local LLMs may generate unexpected outputs; always review results

## Scope

### In Scope

- Security vulnerabilities in the codebase
- Dependency vulnerabilities with exploitable impact
- Authentication/authorization bypasses (if applicable)
- Code injection vulnerabilities
- Data leakage issues

### Out of Scope

- Issues in third-party dependencies (report to the maintainers)
- Social engineering attacks
- Physical security
- Issues requiring physical access to the system
- Denial of service on local installations

## Contact

For security-related questions or concerns that don't require immediate attention, you can:

- Open a [GitHub Discussion](https://github.com/texasbe2trill/AlertSage/discussions)
- Review our [Contributing Guidelines](CONTRIBUTING.md)

Thank you for helping keep AlertSage and its users safe!
