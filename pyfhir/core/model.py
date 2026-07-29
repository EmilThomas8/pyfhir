from .coercion import coerce_value
from .model import FHIRModelMeta
from .types import PrimitiveType


class FHIRModel(metaclass=FHIRModelMeta):

    __fields__ = {}

    def __init__(self, **kwargs):

        # Reject unknown fields
        unknown = set(kwargs) - set(self.__fields__)
        if unknown:
            raise TypeError(
                f"{self.__class__.__name__} got unexpected field(s): "
                f"{', '.join(sorted(unknown))}"
            )

        # Populate fields
        for name, field in self.__fields__.items():

            value = kwargs.get(name, field.get_default())

            value = coerce_value(
                field.field_type,
                value,
                many=field.many
            )

            setattr(self, name, value)

        self.validate()

    @classmethod
    def from_dict(cls, data):

        if data is None:
            return None

        if not isinstance(data, dict):
            raise TypeError(
                f"{cls.__name__}.from_dict() expects dict."
            )

        return cls(**data)

    def to_dict(self):

        result = {}

        for name, field in self.__fields__.items():

            value = getattr(self, name)

            if value is None:
                continue

            if field.many:

                result[name] = [
                    item.to_dict()
                    if hasattr(item, "to_dict")
                    else item.value
                    if isinstance(item, PrimitiveType)
                    else item
                    for item in value
                ]

            else:

                if hasattr(value, "to_dict"):
                    result[name] = value.to_dict()

                elif isinstance(value, PrimitiveType):
                    result[name] = value.value

                else:
                    result[name] = value

        return result

    def validate(self):

        for name, field in self.__fields__.items():

            value = getattr(self, name)

            if value is None:
                continue

            expected = field.field_type

            if field.many:

                if not isinstance(value, list):
                    raise TypeError(
                        f"{name} must be a list."
                    )

                for item in value:
                    self._validate_item(name, item, expected)

            else:

                self._validate_item(name, value, expected)

    @staticmethod
    def _validate_item(name, value, expected):

        if isinstance(expected, type):

            if not isinstance(value, expected):
                raise TypeError(
                    f"Field '{name}' expects "
                    f"{expected.__name__}, "
                    f"got {type(value).__name__}."
                )

    def copy(self):
        return self.__class__.from_dict(
            self.to_dict()
        )

    def __repr__(self):

        values = []

        for name in self.__fields__:

            value = getattr(self, name)

            if value is not None:
                values.append(
                    f"{name}={value!r}"
                )

        return (
            f"{self.__class__.__name__}"
            f"({', '.join(values)})"
        )