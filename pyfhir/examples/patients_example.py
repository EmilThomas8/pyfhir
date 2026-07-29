from pyfhir import Patient
from pyfhir.datatypes import (
    HumanName,
    Identifier,
    Address,
)

patient = Patient(

    id="001",

    identifier=[
        Identifier(
            system="Hospital",
            value="MRN10001"
        )
    ],

    name=[
        HumanName(
            family="Thomas",
            given=["Emil"]
        )
    ],

    gender="male",

    birth_date="2004-03-21",

    address=[
        Address(
            city="Mangalore",
            country="India"
        )
    ]
)

print(patient.to_json())