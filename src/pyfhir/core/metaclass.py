"""
Metaclass for all FHIR models.
"""


class FHIRModelMeta(type):

    def __new__(mcls, name, bases, namespace):

        fields = {}

        # inherit fields from parent classes
        for base in bases:
            if hasattr(base, "__fields__"):
                fields.update(base.__fields__)

        # collect fields from this class
        for key, value in list(namespace.items()):
            if hasattr(value, "__is_fhir_field__"):
                value.name = key
                fields[key] = value

        namespace["__fields__"] = fields

        return super().__new__(
            mcls,
            name,
            bases,
            namespace,
        )