def generate_fastapi_app(config):

    code = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Generated App"}
"""

    return code
