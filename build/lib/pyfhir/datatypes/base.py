"""
Base class for all FHIR datatypes.
"""


class DataType:
    """
    Base datatype.
    """

    def to_dict(self):
        raise NotImplementedError

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.to_dict() == other.to_dict()
        )