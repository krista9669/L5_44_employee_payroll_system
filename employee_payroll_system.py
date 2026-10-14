"""Employee payroll computation and salary disbursement module."""

import hashlib
import logging
import secrets

PAYROLL_RECORDS = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)


def process_salary(
    emp_id: str,
    bonus: float,
    transaction_logs: list[str] | None = None,
) -> bool:
    """Add a valid bonus to an employee's salary and record the transaction."""
    if transaction_logs is None:
        transaction_logs = []

    if emp_id not in PAYROLL_RECORDS or bonus < 0:
        return False

    PAYROLL_RECORDS[emp_id]["base_salary"] += bonus
    transaction_logs.append(
        f"Credited bonus {bonus:.2f} to employee id {emp_id}"
    )
    logging.info("%s", transaction_logs[-1])
    return True


def deduct_penalty(emp_id: str, penalty: float) -> bool:
    """Deduct a valid penalty from an employee's salary."""
    if emp_id not in PAYROLL_RECORDS or penalty < 0:
        return False

    PAYROLL_RECORDS[emp_id]["base_salary"] -= penalty
    logging.info(
        "Deducted penalty %.2f from employee id %s",
        penalty,
        emp_id,
    )
    return True


def check_bonus_eligibility(
    emp_id: str,
    min_base: float = 4000.0,
) -> bool:
    """Check whether an employee meets the minimum salary threshold."""
    employee = PAYROLL_RECORDS.get(emp_id)

    if employee is None:
        return False

    return employee["base_salary"] >= min_base


def compute_net_salary(
    emp_id: str,
    deduction_rate: float = 0.15,
) -> float:
    """Calculate net salary after applying a validated deduction rate."""
    if emp_id not in PAYROLL_RECORDS:
        raise ValueError(f"Unknown employee ID: {emp_id}")

    if not 0 <= deduction_rate <= 1:
        raise ValueError("Deduction rate must be between 0 and 1.")

    base_salary = PAYROLL_RECORDS[emp_id]["base_salary"]
    return base_salary * (1 - deduction_rate)


def generate_employee_hash(emp_id: str) -> str:
    """Return a SHA-256 digest of an employee identifier."""
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_payroll_token() -> str:
    """Generate a cryptographically secure four-digit token."""
    return f"{secrets.randbelow(9000) + 1000:04d}"


def export_payroll_sheet(
    filename: str = "payroll_sheet.txt",
) -> None:
    """Export payroll records to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as payroll_file:
        payroll_file.write(str(PAYROLL_RECORDS))

    logging.info("Payroll summary exported to: %s", filename)


def main() -> None:
    """Run a demonstration of payroll operations."""
    process_salary("EMP101", 350)
    deduct_penalty("EMP102", 100)

    print(
        "Is EMP101 eligible:",
        check_bonus_eligibility("EMP101"),
    )
    print(
        "Net salary:",
        compute_net_salary("EMP101"),
    )
    print(
        "Employee Hash:",
        generate_employee_hash("EMP101"),
    )
    print("Payroll Token:", generate_payroll_token())

    export_payroll_sheet()


if __name__ == "__main__":
    main()
