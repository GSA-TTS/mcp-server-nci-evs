"""Enum list handling utilities for API parameters."""

from enum import Enum
from typing import Any, Type, TypeVar

E = TypeVar("E", bound=Enum)


def to_enum_list_value(
    value: E | list[E] | None,
    enum_class: Type[E],
    param_name: str,
) -> str | None:
    """Convert enum value(s) to comma-separated string for URL parameters.
    
    This function handles conversion of single enum values or lists of enum values
    to comma-separated strings suitable for API URL parameters. It also validates
    that the provided values are valid members of the specified enum class.
    
    Args:
        value: The enum value(s) to convert. Can be:
            - A single enum value
            - A list of enum values
            - None (returns None)
        enum_class: The enum class to validate against.
        param_name: The parameter name (used in error messages).
    
    Returns:
        Comma-separated string of enum values, or None if value is None.
    
    Raises:
        TypeError: If value is not an instance or list of instances of enum_class.
        ValueError: If value is an empty list.
    
    Examples:
        >>> from evs_server.models import NCITProperty
        >>> to_enum_list_value(NCITProperty.SEMANTIC_TYPE, NCITProperty, "property")
        'P106'
        >>> to_enum_list_value([NCITProperty.SEMANTIC_TYPE, NCITProperty.CONTRIBUTING_SOURCE], NCITProperty, "property")
        'P106,P322'
        >>> to_enum_list_value(None, NCITProperty, "property")
        None
    """
    if value is None:
        return None
    
    # Handle list of enums
    if isinstance(value, list):
        if not value:
            raise ValueError(f"Parameter '{param_name}' cannot be an empty list")
        
        # Validate all items are correct enum type
        for idx, item in enumerate(value):
            if not isinstance(item, enum_class):
                raise TypeError(
                    f"Parameter '{param_name}' item at index {idx} must be of type {enum_class.__name__}, "
                    f"got {type(item).__name__}"
                )
        
        # Convert to comma-separated string
        return ",".join(item.value for item in value)
    
    # Handle single enum
    if not isinstance(value, enum_class):
        raise TypeError(
            f"Parameter '{param_name}' must be of type {enum_class.__name__} or list[{enum_class.__name__}], "
            f"got {type(value).__name__}"
        )
    
    return value.value


def validate_enum_for_terminology(
    value: Any,
    terminology: str,
    ncit_enum: Type[E] | None,
    ncim_enum: Type[E] | None,
    param_name: str,
) -> None:
    """Validate that enum value matches the terminology being used.
    
    This function ensures that terminology-specific enum values are only used
    with their corresponding terminology. For example, NCITProperty values
    can only be used when terminology='ncit', and NCIMProperty values can
    only be used when terminology='ncim'.
    
    Args:
        value: The value to validate (enum or list of enums).
        terminology: The terminology being used ('ncit', 'ncim', etc.).
        ncit_enum: The NCIT-specific enum class, or None if not applicable.
        ncim_enum: The NCIM-specific enum class, or None if not applicable.
        param_name: The parameter name (used in error messages).
    
    Raises:
        ValueError: If an NCIT enum is used with non-NCIT terminology, or
                   if an NCIM enum is used with non-NCIM terminology.
    
    Examples:
        >>> from evs_server.models import NCITProperty, NCIMProperty
        >>> validate_enum_for_terminology(
        ...     NCITProperty.SEMANTIC_TYPE,
        ...     "ncit",
        ...     NCITProperty,
        ...     NCIMProperty,
        ...     "property"
        ... )  # OK - no exception
        >>> validate_enum_for_terminology(
        ...     NCITProperty.SEMANTIC_TYPE,
        ...     "ncim",
        ...     NCITProperty,
        ...     NCIMProperty,
        ...     "property"
        ... )  # Raises ValueError
    """
    if value is None:
        return
    
    # Get the enum type(s) from the value
    values_to_check = value if isinstance(value, list) else [value]
    
    for v in values_to_check:
        if not isinstance(v, Enum):
            continue
        
        enum_type = type(v)
        
        # Check NCIT-specific enum
        if ncit_enum and enum_type == ncit_enum:
            if terminology.lower() != "ncit":
                raise ValueError(
                    f"Parameter '{param_name}' with {ncit_enum.__name__} values can ONLY be used "
                    f"when terminology='ncit'. Current terminology is '{terminology}'."
                )
        
        # Check NCIM-specific enum
        if ncim_enum and enum_type == ncim_enum:
            if terminology.lower() != "ncim":
                raise ValueError(
                    f"Parameter '{param_name}' with {ncim_enum.__name__} values can ONLY be used "
                    f"when terminology='ncim'. Current terminology is '{terminology}'."
                )
