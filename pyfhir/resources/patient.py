from pyfhir.resources import Resource
from pyfhir.core.field import FHIRField

from pyfhir.core.types import (
    FHIRBoolean,
    FHIRDate,
    FHIRCode,
    FHIRId,
)

from pyfhir.datatypes import (
    Identifier,
    HumanName,
    Address,
)


class Patient(Resource):

    resource_type = "Patient"

    id = FHIRField(FHIRId)

    identifier = FHIRField(
        Identifier,
        many=True
    )

    active = FHIRField(FHIRBoolean)

    name = FHIRField(
        HumanName,
        many=True
    )

    gender = FHIRField(FHIRCode)

    birthDate = FHIRField(FHIRDate)

    address = FHIRField(
        Address,
        many=True
    )