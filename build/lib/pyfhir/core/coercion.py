"""
Automatic type coercion for FHIR fields.
"""

from .types import PrimitiveType


def coerce_value(field_type, value, many=False):
    """
    Convert a raw value into the expected FHIR type.
    """

    if value is None:
        return None

    if many and isinstance(value, list):
        return [
            coerce_value(field_type, item, many=False)
            for item in value
        ]

    # Already correct type
    if isinstance(value, field_type):
        return value

    # Primitive types
    if issubclass(field_type, PrimitiveType):
        return field_type(value)

    # Nested FHIR models
    from .model import FHIRModel

    if issubclass(field_type, FHIRModel):

        if isinstance(value, dict):
            return field_type.from_dict(value)

    return value