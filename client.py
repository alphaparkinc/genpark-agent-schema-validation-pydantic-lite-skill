"""Schema Validation Lite Engine.
100% Python Standard Library.
"""

from typing import Dict, Any, List

class SchemaValidationLite:
    """Validates dictionary inputs against typed schema specifications without requiring Pydantic or jsonschema."""
    def __init__(self):
        pass

    def validate(self, schema: Dict[str, Dict[str, Any]], data: Dict[str, Any]) -> Dict[str, Any]:
        errors: List[str] = []
        for field, rules in schema.items():
            expected_type = rules.get("type")
            required = rules.get("required", True)

            if field not in data:
                if required:
                    errors.append(f"Missing required field: '{field}'")
                continue

            val = data[field]
            type_map = {
                "string": str,
                "integer": int,
                "number": (int, float),
                "boolean": bool,
                "list": list,
                "dict": dict
            }
            if expected_type in type_map and not isinstance(val, type_map[expected_type]):
                errors.append(f"Field '{field}' expected {expected_type}, got {type(val).__name__}")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "validated_fields": list(data.keys())
        }
