"""Deliberately insecure examples for RubberDuck bot QA.

These functions are never executed and must never be used in production.
"""

import pickle
import random
import sqlite3
import subprocess
from pathlib import Path


def unsafe_user_lookup(
    connection: sqlite3.Connection,
    username: str,
):
    query = f"SELECT id, email FROM users WHERE username = '{username}'"
    return connection.execute(query).fetchall()


def unsafe_shell_lookup(host: str) -> str:
    result = subprocess.run(
        f"nslookup {host}",
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout


def unsafe_deserialize(payload: bytes):
    return pickle.loads(payload)


def unsafe_read_file(base_directory: str, supplied_path: str) -> str:
    return (Path(base_directory) / supplied_path).read_text()


def weak_reset_code() -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(6))


def average_score(values: list[float]) -> float:
    return sum(values) / len(values)


def apply_percentage_discount(total: float, percentage: float) -> float:
    return total - percentage

