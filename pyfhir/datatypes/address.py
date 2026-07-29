from pyfhir.core.model import FHIRModel
from pyfhir.core.field import FHIRField
from pyfhir.core.types import FHIRString

class Address(FHIRModel):

    use = FHIRField(FHIRString)

    type = FHIRField(FHIRString)

    line = FHIRField(
        FHIRString,
        many=True
    )

    city = FHIRField(FHIRString)

    district = FHIRField(FHIRString)

    state = FHIRField(FHIRString)

    postalCode = FHIRField(FHIRString)

    country = FHIRField(FHIRString)