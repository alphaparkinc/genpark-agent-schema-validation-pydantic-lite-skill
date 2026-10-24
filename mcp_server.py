import sys
import json
from client import SchemaValidationLite

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "validate_schema",
                        "description": "Validates dictionary data against structured type definitions.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "schema": {"type": "object"},
                                "data": {"type": "object"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        validator = SchemaValidationLite()
        res = validator.validate(args.get("schema", {}), args.get("data", {}))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    validator = SchemaValidationLite()
    print(json.dumps(validator.validate({"a": {"type": "string"}}, {"a": "ok"}), indent=2))

if __name__ == "__main__":
    main()
