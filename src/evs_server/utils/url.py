"""URL parameter conversion utilities."""

from enum import Enum
from typing import Any


def to_url_value(value: Any) -> str:
    """Convert a value to its URL parameter string representation.
    
    This function handles conversion of enum values to their string values
    for use in URL parameters and query strings.
    
    Args:
        value: The value to convert. Can be an Enum, string, or other type.
    
    Returns:
        String representation suitable for URL parameters.
        - For Enum types: returns the enum's value
        - For other types: returns str(value)
    
    Examples:
        >>> from evs_server.models import Terminology, Include
        >>> to_url_value(Terminology.NCIT)
        'ncit'
        >>> to_url_value(Include.SUMMARY)
        'summary'
        >>> to_url_value("already_a_string")
        'already_a_string'
    """
    if isinstance(value, Enum):
        return value.value
    return str(value)
