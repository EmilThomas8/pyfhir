"""
Custom exceptions for PyFHIR.
"""


class PyFHIRException(Exception):
    """Base exception for all PyFHIR errors."""


class ValidationError(PyFHIRException):
    """Raised when validation fails."""


class ParseError(PyFHIRException):
    """Raised when parsing fails."""


class SerializationError(PyFHIRException):
    """Raised when serialization fails."""