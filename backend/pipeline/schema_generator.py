def generate_schemas(design):

    return {
        "db_schema":{
            "tables":[
                {
                    "name":"users",
                    "columns":[
                        {"name":"id","type":"uuid"},
                        {"name":"email","type":"string"}
                    ]
                }
            ]
        },

        "api_schema":{
            "endpoints":[
                {
                    "path":"/login",
                    "method":"POST"
                }
            ]
        },

        "ui_schema":{
            "pages":[
                "Login",
                "Dashboard"
            ]
        }
    }
