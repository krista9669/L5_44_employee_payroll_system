# Lab 5: Static Code Analysis

## Overview
This project demonstrates static code analysis of a Python employee payroll system using Pylint, Bandit, and Flake8. The objective is to improve code quality, security, readability, and maintainability by identifying and fixing common programming issues.

## Tools Used
- **Pylint** — Checks code quality, programming practices, and potential errors.
- **Bandit** — Detects common security vulnerabilities in Python code.
- **Flake8** — Checks Python style and coding-standard violations.

## Project Structure
```text
L5_44_employee_payroll_system/
├── employee_payroll_system.py
├── pylint_report.txt
├── bandit_report.txt
├── flake8_report.txt
├── issues.md
├── reflection.md
├── payroll_sheet.txt
├── README.md
└── .gitignore
```

## Issues Addressed
- Replaced mutable default arguments with safer initialization.
- Removed unsafe use of `eval()`.
- Replaced MD5 hashing with SHA-256.
- Used the `secrets` module for secure token generation.
- Removed unsafe shell command execution.
- Improved exception handling and input validation.
- Removed unused imports and variables.
- Added docstrings and improved naming conventions.
- Improved file handling by specifying UTF-8 encoding and using a context manager.

## Static Analysis Results

| Tool | Result |
|---|---|
| Pylint | 10.00/10 |
| Bandit | No issues identified |
| Flake8 | No violations reported |

## How to Run

Create and activate a virtual environment, then install the tools:

```bash
python -m venv venv
pip install pylint bandit flake8
```

Run the program:

```bash
python employee_payroll_system.py
```

Run the static analysis tools:

```bash
pylint employee_payroll_system.py > pylint_report.txt 2>&1
bandit -r employee_payroll_system.py > bandit_report.txt 2>&1
flake8 employee_payroll_system.py > flake8_report.txt 2>&1
```

## Documentation
- `issues.md` — Documents the identified issues and their fixes.
- `reflection.md` — Contains reflections on static code analysis.
- The three report files contain the outputs from the analysis tools.

## Conclusion
Static code analysis helped improve the employee payroll system's code quality, maintainability, and security. The updated code achieved a Pylint score of 10/10, with no issues reported by Bandit and no violations reported by Flake8 in the final analysis.