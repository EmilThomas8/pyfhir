import unittest

from src.pyfhir.resources import Patient
from src.pyfhir.datatypes import HumanName
from src.pyfhir.core.types import FHIRDate


class TestCoercion(unittest.TestCase):

    def test_nested_object(self):

        patient = Patient(
            name=[
                {
                    "family": "Thomas",
                    "given": ["Emil"]
                }
            ]
        )

        self.assertIsInstance(
            patient.name[0],
            HumanName
        )

    def test_primitive(self):

        patient = Patient(
            birthDate="2004-03-21"
        )

        self.assertIsInstance(
            patient.birthDate,
            FHIRDate
        )


if __name__ == "__main__":
    unittest.main()