"""Field helpers for FHIR models."""

from typing import Any, Optional


class FHIRField:
    """Descriptor-like holder used by `FHIRModelMeta` to collect fields.

    Attributes:
        field_type: The Python/type or FHIR model class for the field.
        many: Whether the field holds a list of values.
        default: The default value for the field when not provided.
        name: Set by the metaclass to the attribute name.
    """

    __is_fhir_field__ = True

    def __init__(self, field_type: Any, many: bool = False, default: Optional[Any] = None):
        self.field_type = field_type
        self.many = many
        self.default = default
        self.name: Optional[str] = None

    def __repr__(self) -> str:
        return (
            f"FHIRField(name={self.name!r}, field_type={self.field_type!r}, many={self.many})"
        )