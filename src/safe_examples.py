"""Safe comparison examples for RubberDuck bot false-positive testing."""

import secrets
import sqlite3
import subprocess
from pathlib import Path


def safe_user_lookup(
    connection: sqlite3.Connection,
    username: str,
):
    return connection.execute(
        "SELECT id, email FROM users WHERE username = ?",
        (username,),
    ).fetchall()


def safe_shell_lookup(host: str) -> str:
    if not host.replace(".", "").replace("-", "").isalnum():
        raise ValueError("Invalid hostname")

    result = subprocess.run(
        ["nslookup", host],
        shell=False,
        capture_output=True,
        text=True,
        check=False,
        timeout=5,
    )
    return result.stdout


def safe_read_file(base_directory: str, supplied_path: str) -> str:
    base = Path(base_directory).resolve()
    candidate = (base / supplied_path).resolve()

    if candidate != base and base not in candidate.parents:
        raise ValueError("Path is outside the allowed directory")

    return candidate.read_text()


def strong_reset_token() -> str:
    return secrets.token_urlsafe(32)


def average_score(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def apply_percentage_discount(total: float, percentage: float) -> float:
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")
    return total * (1 - percentage / 100)
