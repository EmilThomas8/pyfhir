"""
pyfhir.validation.result

Stores validation results.
"""

from __future__ import annotations

from typing import Iterator

from .error import ValidationError


class ValidationResult:
    """
    Holds validation errors.
    """

    def __init__(self):

        self._errors: list[ValidationError] = []

    @property
    def valid(self) -> bool:
        return len(self._errors) == 0

    @property
    def errors(self) -> list[ValidationError]:
        return self._errors

    def add(
        self,
        error: ValidationError,
    ) -> None:

        self._errors.append(error)

    def extend(
        self,
        errors: list[ValidationError],
    ) -> None:

        self._errors.extend(errors)

    def clear(self) -> None:

        self._errors.clear()

    def __len__(self):

        return len(self._errors)

    def __iter__(
        self,
    ) -> Iterator[ValidationError]:

        return iter(self._errors)

    def __bool__(self):

        return self.valid

    def __str__(self):

        if self.valid:
            return "Validation successful."

        return "\n".join(
            str(error)
            for error in self._errors
        )

    def to_dict(self):

        return {
            "valid": self.valid,
            "errors": [
                error.to_dict()
                for error in self._errors
            ],
        }