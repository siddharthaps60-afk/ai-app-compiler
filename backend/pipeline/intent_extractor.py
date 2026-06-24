def extract_intent(prompt):

    return {
        "app_name": "Generated Application",
        "description": prompt,
        "modules": [
            "Authentication",
            "Dashboard",
            "Database"
        ]
    }
