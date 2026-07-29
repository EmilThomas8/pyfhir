"""
Automatic type coercion for FHIR fields.
"""

from .types import PrimitiveType
from .model import FHIRModel


def coerce_value(field_type, value):
    """
    Convert a raw value into the expected FHIR type.
    """

    if value is None:
        return None

    # Already correct type
    if isinstance(value, field_type):
        return value

    # Primitive types
    if issubclass(field_type, PrimitiveType):
        return field_type(value)

    # Nested FHIR models
    if issubclass(field_type, FHIRModel):

        if isinstance(value, dict):
            return field_type.from_dict(value)

    return value