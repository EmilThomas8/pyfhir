import unittest

import pyfhir


class TestImport(unittest.TestCase):

    def test_version(self):
        self.assertEqual(pyfhir.__version__, "0.1.0")

    def test_title(self):
        self.assertEqual(pyfhir.__title__, "pyfhir")


if __name__ == "__main__":
    unittest.main()