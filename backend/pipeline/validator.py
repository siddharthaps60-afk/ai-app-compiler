def validate(config):

    errors = []

    if "db_schema" not in config:
        errors.append("Missing DB schema")

    if "api_schema" not in config:
        errors.append("Missing API schema")

    if "ui_schema" not in config:
        errors.append("Missing UI schema")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
