"""
Validation error objects.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationError:

    path: str

    message: str

    code: str | None = None

    severity: str = "error"

    def __str__(self):

        return f"{self.path}: {self.message}"