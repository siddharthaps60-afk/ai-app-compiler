def repair(config, validation):

    if validation["valid"]:
        return config

    if "Missing UI schema" in validation["errors"]:
        config["ui_schema"] = {
            "pages": ["Dashboard"]
        }

    if "Missing API schema" in validation["errors"]:
        config["api_schema"] = {
            "endpoints": []
        }

    if "Missing DB schema" in validation["errors"]:
        config["db_schema"] = {
            "tables": []
        }

    return config
