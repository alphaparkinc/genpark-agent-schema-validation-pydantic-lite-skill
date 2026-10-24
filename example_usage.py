from client import SchemaValidationLite

validator = SchemaValidationLite()
contract = {
    "agent_name": {"type": "string", "required": True},
    "max_iterations": {"type": "integer", "required": True},
    "verbose": {"type": "boolean", "required": False}
}

good_payload = {"agent_name": "researcher", "max_iterations": 5}
bad_payload = {"agent_name": 12345}

print("=== Schema Validation Telemetry ===")
print("Good Payload:", validator.validate(contract, good_payload))
print("Bad Payload:", validator.validate(contract, bad_payload))
