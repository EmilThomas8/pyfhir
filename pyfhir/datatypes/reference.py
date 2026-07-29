from .base import DataType


class Reference(DataType):

    def __init__(
        self,
        reference=None,
        display=None,
    ):
        self.reference = reference
        self.display = display

    def to_dict(self):
        data = {}

        if self.reference:
            data["reference"] = self.reference

        if self.display:
            data["display"] = self.display

        return data