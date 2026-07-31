"""
Base FHIR Resource.
"""

import json

from src.pyfhir.core.model import FHIRModel

from .datatypes import Meta


class Resource(FHIRModel):
    """
    Base class for all FHIR resources.
    """

    resource_type = "Resource"

    def __init__(
        self,
        id=None,
        meta=None,
        extension=None,
        **kwargs,
    ):
        self.id = id
        self.meta = meta or Meta()
        self.extension = extension or []
        super().__init__(**kwargs)

    @property
    def resourceType(self):
        return self.resource_type

    def to_dict(self):
        data = super().to_dict()
        data["resourceType"] = self.resourceType

        if self.id:
            data["id"] = self.id

        meta = self.meta.to_dict()

        if meta:
            data["meta"] = meta

        if self.extension:
            data["extension"] = self.extension

        return data

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            indent=4,
            ensure_ascii=False,
        )

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
        )

    @classmethod
    def from_json(cls, text):
        return cls.from_dict(
            json.loads(text)
        )

    def validate(self):
        """
        Validation hook.
        """
        return super().validate()

    def __repr__(self):
        return (
            f"<{self.resourceType}"
            f" id={self.id}>"
        )

    def __eq__(self, other):
        return (
            isinstance(other, Resource)
            and self.to_dict() == other.to_dict()
        )