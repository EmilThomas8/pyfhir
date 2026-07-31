"""
FHIR Field Definition
"""

from __future__ import annotations


class FHIRField:

    __is_fhir_field__ = True

    def __init__(
        self,
        field_type,
        *,
        required=False,
        many=False,
        minimum=0,
        maximum=1,
        enum=None,
        default=None,
    ):

        self.field_type = field_type

        self.required = required

        self.many = many

        self.minimum = minimum

        self.maximum = maximum

        self.enum = enum

        self.default = default

    def get_default(self):
        return self.default

    def __repr__(self):

        return (
            f"FHIRField("
            f"type={self.field_type.__name__}, "
            f"required={self.required}, "
            f"many={self.many})"
        )