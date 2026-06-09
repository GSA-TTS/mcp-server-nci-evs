# Fix: Variable Name Shadowing Issue in search_concepts

## Problem

When calling `search_concepts` from an MCP client, the following error occurred:
```
Error calling tool 'search_concepts': 'SearchType' object is not callable
```

## Root Cause

The function parameter named `type` was shadowing Python's built-in `type()` function:

```python
async def search_concepts(
    term: str,
    terminology: Terminology = Terminology.NCIT,
    type: SearchType = SearchType.CONTAINS,  # <-- This shadows built-in type()
    ...
):
```

Later in the function, we attempted to call `type()` to get the enum class:

```python
# This fails because 'type' now refers to SearchType.CONTAINS, not the built-in
enum_class = type(property)  # Tries to call SearchType.CONTAINS(property)
```

## Solution

Replaced all uses of `type(value)` with `value.__class__` to get the enum class:

```python
# Before (fails when 'type' parameter shadows built-in)
if isinstance(property, list):
    enum_class = type(property[0]) if property else NCITProperty
else:
    enum_class = type(property)

# After (works regardless of variable shadowing)
if isinstance(property, list):
    enum_class = property[0].__class__ if property else NCITProperty
else:
    enum_class = property.__class__
```

## Changes Made

Updated four parameter handling blocks in `search_concepts.py`:
1. `property` parameter (lines ~188-194)
2. `definitionSource` parameter (lines ~206-211)
3. `synonymSource` parameter (lines ~223-228)
4. `synonymTermType` parameter (lines ~241-246)

## Why __class__ Works

- `value.__class__` is an attribute access, not a function call
- It returns the same class object as `type(value)` would
- It's not affected by variable name shadowing
- It's a common Python idiom for getting an object's class

## Testing

Verified the fix with:
- Existing validation tests still pass
- Manual test of `__class__` with shadowed `type` variable
- No remaining `type()` function calls in the affected code

## Prevention

To avoid this issue in the future:
1. Avoid using built-in names as parameter names (type, id, list, dict, etc.)
2. Use `__class__` instead of `type()` when working in scopes with many variables
3. Consider renaming the `type` parameter to `search_type` for clarity
