def generate_design(intent):

    return {
        "entities":[
            "User",
            "Role",
            "Subscription"
        ],
        "roles":intent.get("roles", []),
        "flows":[
            "Authentication",
            "Dashboard",
            "Management"
        ]
    }
