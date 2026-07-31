"""
FHIR Validation Engine
"""

from __future__ import annotations

from src.pyfhir.validation import (
    ValidationError,
    ValidationResult,
)


class FHIRValidator:

    def validate(
        self,
        model,
    ) -> ValidationResult:

        result = ValidationResult()

        self._validate_model(
            model=model,
            result=result,
            path=model.__class__.__name__,
        )

        return result

    def _validate_model(
        self,
        model,
        result,
        path,
    ):

        for name, field in model.__fields__.items():

            value = getattr(model, name)

            # ----------------------------
            # Required
            # ----------------------------

            if field.required:

                if value is None:

                    result.add(

                        ValidationError(
                            path=f"{path}.{name}",
                            message="Required field missing",
                            code="required",
                        )

                    )

                    continue

            if value is None:
                continue

            # ----------------------------
            # Cardinality
            # ----------------------------

            if field.many:

                if len(value) < field.minimum:

                    result.add(

                        ValidationError(
                            path=f"{path}.{name}",
                            message=(
                                f"Minimum cardinality "
                                f"is {field.minimum}"
                            ),
                            code="minimum",
                        )

                    )

                if (
                    field.maximum != "*"
                    and len(value) > field.maximum
                ):

                    result.add(

                        ValidationError(
                            path=f"{path}.{name}",
                            message=(
                                f"Maximum cardinality "
                                f"is {field.maximum}"
                            ),
                            code="maximum",
                        )

                    )

            # ----------------------------
            # Enum
            # ----------------------------

            if field.enum:

                code = getattr(
                    value,
                    "value",
                    value,
                )

                if code not in field.enum:

                    result.add(

                        ValidationError(
                            path=f"{path}.{name}",
                            message=(
                                "Invalid code. "
                                f"Expected "
                                f"{sorted(field.enum)}"
                            ),
                            code="enum",
                        )

                    )

            # ----------------------------
            # Nested model
            # ----------------------------

            if hasattr(
                value,
                "__fields__",
            ):

                self._validate_model(
                    value,
                    result,
                    f"{path}.{name}",
                )

            # ----------------------------
            # Lists
            # ----------------------------

            elif isinstance(
                value,
                list,
            ):

                for index, item in enumerate(value):

                    if hasattr(
                        item,
                        "__fields__",
                    ):

                        self._validate_model(
                            item,
                            result,
                            f"{path}.{name}[{index}]",
                        )