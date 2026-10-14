# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis, and why is it important?

Static code analysis examines source code without executing the program. It helps detect potential bugs, security vulnerabilities, maintainability issues, and coding-standard violations early in development. This makes code easier to maintain and reduces the risk of problems reaching production.

### 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint focuses on overall code quality, programming practices, naming conventions, documentation, and potential logical issues. Bandit focuses on common security vulnerabilities, such as unsafe evaluation, weak hashing algorithms, and insecure shell execution. Flake8 checks Python style and common code errors, including unused imports, incorrect formatting, and line-length violations.

### 3. What issues did you identify and fix in your program?

I corrected several issues in the employee payroll system. I replaced a mutable default argument with `None`, removed the unsafe use of `eval()`, replaced MD5 with SHA-256, and used the `secrets` module for token generation. I also removed unsafe shell execution, improved exception handling, removed unused variables and imports, added docstrings, and corrected file handling and naming conventions.

### 4. How did static analysis improve your code, and what did you learn?

Static analysis improved the code's readability, consistency, maintainability, and security. Initially, Pylint rated the program 5.32/10, and Bandit identified five security findings. After fixing the issues, Pylint rated the code 10.00/10, Bandit reported no issues, and Flake8 reported no violations. I learned that these tools complement one another: passing one tool alone is not enough to establish code quality or security, so using all three provides broader coverage.