"""
FHIR primitive types.
"""

from abc import ABC
import re


class PrimitiveType(ABC):
    """
    Base class for all FHIR primitive types.
    """

    python_type = object

    def __init__(self, value):

        self.validate(value)

        self.value = value

    def validate(self, value):
        pass

    def to_dict(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.value!r})"
        )

    def __eq__(self, other):
        if isinstance(other, PrimitiveType):
            return self.value == other.value
        return self.value == other

class FHIRString(PrimitiveType):

    python_type = str

    def validate(self, value):

        if not isinstance(value, str):
            raise TypeError(
                "FHIRString requires str."
            )

class FHIRBoolean(PrimitiveType):

    python_type = bool

    def validate(self, value):

        if not isinstance(value, bool):
            raise TypeError(
                "FHIRBoolean requires bool."
            )

class FHIRInteger(PrimitiveType):

    python_type = int

    MIN = -(2 ** 31)
    MAX = (2 ** 31) - 1

    def validate(self, value):

        if not isinstance(value, int):
            raise TypeError(
                "FHIRInteger requires int."
            )

        if value < self.MIN or value > self.MAX:
            raise ValueError(
                "FHIR integer out of range."
            )

from decimal import Decimal


class FHIRDecimal(PrimitiveType):

    python_type = Decimal

    def validate(self, value):

        if not isinstance(
            value,
            (Decimal, int, float, str),
        ):
            raise TypeError(
                "Invalid decimal."
            )

        self.value = Decimal(str(value))

class FHIRDate(PrimitiveType):

    DATE_PATTERN = re.compile(
        r"^\d{4}(-\d{2})?(-\d{2})?$"
    )

    def validate(self, value):

        if not isinstance(value, str):
            raise TypeError(
                "Date must be string."
            )

        if not self.DATE_PATTERN.match(value):
            raise ValueError(
                "Invalid FHIR date."
            )


class FHIRId(PrimitiveType):

    ID_PATTERN = re.compile(
        r"^[A-Za-z0-9\-\.]{1,64}$"
    )

    def validate(self, value):

        if not isinstance(value, str):
            raise TypeError(
                "FHIR id must be string."
            )

        if not self.ID_PATTERN.match(value):
            raise ValueError(
                "Invalid FHIR id."
            )