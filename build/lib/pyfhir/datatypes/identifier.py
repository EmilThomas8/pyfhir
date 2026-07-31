from .base import DataType


class Identifier(DataType):

    def __init__(
        self,
        system=None,
        value=None,
    ):
        self.system = system
        self.value = value

    def to_dict(self):
        data = {}

        if self.system:
            data["system"] = self.system

        if self.value:
            data["value"] = self.value

        return data