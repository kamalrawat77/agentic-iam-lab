class ValidationError(Exception):
    """Raised when tool arguments are invalid."""
    pass


def validate(tool, arguments):

    schema = tool.parameters

    # Check required parameters
    for name, info in schema.items():
        if info["required"] and name not in arguments:
            raise ValidationError(
                f"Missing required parameter: {name}"
            )

    # Check unknown parameters
    for arg in arguments:
        if arg not in schema:
            raise ValidationError(
                f"Unknown parameter: {arg}"
            )

    TYPE_CHECKERS = {
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "string": str,
    }

    for name, value in arguments.items():

      expected = schema[name]["type"]

      if not isinstance(value, TYPE_CHECKERS[expected]):
          raise ValidationError(
              f"{name} must be {expected}"
          )