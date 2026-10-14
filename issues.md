# Lab 5: Static Code Analysis — Issues and Fixes

## Objective

To identify and fix code quality, security, and style issues in the employee payroll system using Pylint, Bandit, and Flake8.

## Issues Identified and Fixed

| Issue | Type | Original Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Code quality / Bug | 15 | Using `[]` as a default argument can cause a list to be shared between function calls. | Replaced the mutable default with `None` and initialized a new list inside the function. |
| Insecure use of `eval()` | Security — Medium | 42 | `eval()` can execute arbitrary expressions and potentially malicious code. | Removed `eval()` and used direct, validated arithmetic instead. |
| Weak MD5 hash | Security — High | 47 | MD5 is not appropriate for security-sensitive hashing. | Replaced MD5 with SHA-256 using `hashlib.sha256()`. |
| Insecure random token generation | Security — Low | 51 | `random.randint()` is not designed for security-sensitive tokens. | Replaced it with `secrets.randbelow()` to generate a cryptographically secure token. |
| Shell command execution | Security — High | 58 | `os.system()` can introduce command-injection risks when shell commands include untrusted input. | Removed shell-based execution and used safer Python functionality. |
| Bare exception handler | Code quality / Security | 26 | A bare `except` catches broad exceptions and can hide unexpected failures. | Removed the broad exception handling and used explicit validation. |
| Mutable and unused variables | Code quality | 31, 41 | Variables were assigned but not used, making the code harder to maintain. | Removed unnecessary variables. |
| Comparison with `None` | Style / Code quality | 32 | Using `== None` is discouraged in Python. | Changed the check to an explicit `is None` comparison. |
| Missing function docstrings | Maintainability | Multiple | Functions lacked documentation explaining their purpose. | Added descriptive docstrings to the functions. |
| Missing file encoding and context manager | Code quality | 55 | File operations did not specify an encoding or reliably manage the file resource. | Used `with open(..., encoding="utf-8")` for safe file handling. |
| Unused import | Style | 6 | The `math` module was imported but never used. | Removed the unused import. |
| Naming and formatting issues | Style | 15, 19, 73 | The original function name did not follow snake_case, a string could use an f-string, and the file lacked a final newline. | Renamed the function to `process_salary`, improved string formatting, and added the final newline. |

## Verification Results

After modifying the code, all three static analysis tools were executed again.

| Tool | Final Result |
|---|---|
| Pylint | 10.00/10 |
| Bandit | No issues identified; zero high, medium, or low severity findings |
| Flake8 | No reported violations |

## Conclusion

Static code analysis helped identify security vulnerabilities, potential bugs, maintainability problems, and style violations. Addressing these issues improved the readability, consistency, and security of the employee payroll system. Running the tools again verified that the reported issues had been resolved.