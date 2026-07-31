"""
pyfhir.validation.error

Defines a single validation error.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ValidationError:
    """
    Represents one validation failure.
    """

    path: str
    message: str
    code: str

    def __str__(self) -> str:
        return (
            f"[{self.code}] "
            f"{self.path}: "
            f"{self.message}"
        )

    def to_dict(self) -> dict:
        return {
            "path": self.path,
            "message": self.message,
            "code": self.code,
        }