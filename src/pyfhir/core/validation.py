class ValidationError:

    def __init__(self, path, message, code):

        self.path = path
        self.message = message
        self.code = code


class ValidationResult:

    def __init__(self):

        self.errors = []

    def add(self, error):

        self.errors.append(error)

    @property
    def valid(self):

        return len(self.errors) == 0

    def __bool__(self):

        return self.valid

    def __iter__(self):

        return iter(self.errors)

    def __len__(self):

        return len(self.errors)

    def _validate_model(
        self,
        model,
        result,
        path,
    ):

        for name, field in model.__fields__.items():

            value = getattr(model, name)

            if field.required:

                if value is None:

                    result.add(

                        ValidationError(
                            path=f"{path}.{name}",
                            message="Required field missing",
                            code="required",
                        )

                    )