from pyfhir.core.field import FHIRField
from pyfhir.core.model import FHIRModel
from pyfhir.core.types import FHIRString


class HumanName(FHIRModel):

    use = FHIRField(FHIRString)

    family = FHIRField(FHIRString)

    given = FHIRField(
        FHIRString,
        many=True
    )

    prefix = FHIRField(
        FHIRString,
        many=True
    )

    suffix = FHIRField(
        FHIRString,
        many=True
    )